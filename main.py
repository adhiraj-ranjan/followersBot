from time import sleep
import subprocess
import os
os.chdir("Followers script")

while True:
  subprocess.call("python followers.py", shell = True)
  sleep(3750)

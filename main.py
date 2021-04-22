import subproces
from time import sleep

while True:
  subprocess.call("python followers.py", shell=True)
  sleep(4000)

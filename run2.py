import subprocess
import time

cmd = 'obs';
p = subprocess.Popen('exec ' + cmd, stdout=subprocess.PIPE, shell=True)
time.sleep(15)
p.kill()
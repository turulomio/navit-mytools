#!/usr/bin/python3
import datetime
import multiprocessing
import os
import time
import argparse
import sys
import signal
sys.path.append("/usr/share/navit-mytools/")
from libnavitmytools import espeak, bluenmea_make_connection, bluenmea_is_receiving_connections, navit_pid, gpsd_is_receiving_data
def espeak_conditionated(s):
    if datetime.datetime.now()-inicio>datetime.timedelta(minutes=2) and navit_pid()!=None:
        espeak(s)
    print(s)

def step():
    global numloops
    time.sleep(10)
    if navit_pid()==None:
        numloops=numloops+1
    print("{} Bucles sin navit {}/{}".format(datetime.datetime.now()-inicio,numloops,maxloops))

parser=argparse.ArgumentParser("This program launches my gps system. This program ends after 10 minutes if navit is not running. It speaks problems after 2 minutes if navit is running")
parser.add_argument('--phoneip', help='Telephone IP Adress',  default="192.168.43.1")
args=parser.parse_args()

inicio=datetime.datetime.now()
numloops=0
maxloops=60


def kill_subprocess():
    os.system("killall -9 gpsd")    
    os.system("killall -9 socat")

def terminate(signal, frame):
    print('You pressed Ctrl+C!')
    kill_subprocess()
    sys.exit(0)
    
signal.signal(signal.SIGINT, terminate)
signal.signal(signal.SIGTERM, terminate)
soca=None
lastgpsdata=datetime.datetime.now()

while numloops<maxloops:
    if gpsd_is_receiving_data():
        lastgpsdata=datetime.datetime.now()
        step()
        continue
    elif datetime.datetime.now()-lastgpsdata>datetime.timedelta(seconds=30):
        espeak_conditionated("No data in the last 30 seconds")

    if soca==None:
        soca = multiprocessing.Process(target=bluenmea_make_connection, args=(args.phoneip, ))
        soca.start()
        time.sleep(3)
        os.system("chmod 644 /dev/gps")
        os.system("gpsd /dev/gps")
    if soca.is_alive()==False:
        kill_subprocess()
        soca=None
    step()
kill_subprocess()
while True:#Used to mantain the daemon in order to start-stop-daemon work
    time.sleep(3)
import subprocess
import os
import psutil


def config_read(prop):
    try:
        for line in open("/etc/conf.d/nmt-system","r"):
            if line.find(prop)!=-1:
                return line.split('"')[1]
    except:
        print ("config_read {} not found".format(prop))
        return None


def espeak(s, language="en"):
    os.system("espeak -v {} '{}'".format(language, s))

def wifi_is_name(name):
    try:
        w=subprocess.check_output(["nmcli",],stderr=subprocess.STDOUT, timeout=3)
        if w.find(name.encode('UTF-8'))!=-1:
            return True
        return False
    except:
        return False

def navit_pid():
    for proc in psutil.process_iter():
            if proc.name()=="navit":
                return proc.pid
    return 

def bluenmea_connection_pid():
    for proc in psutil.process_iter():
        for cmd in proc.cmdline():
            if cmd.find(",link=/dev/gps")!=-1:
                return proc.pid
    return 


def bluenmea_make_connection(ip):
    try:
        subprocess.check_output(["socat", "TCP:{}:4352".format(ip),"PTY,link=/dev/gps"], stderr=subprocess.STDOUT)
    except:
        pass

def bluenmea_is_receiving_connections(ip):
    result=False
    try:
        b=subprocess.check_output(["nc", ip,"4352","-zv","-w","3"],stderr=subprocess.STDOUT,timeout=4)
        if b.find(b"open")!=-1:
            result=True
    except:
        pass
    return result
    
def bluenmea_is_connected(ip):  
    if bluenmea_connection_pid()==None:
        return False
    else:
        return True

def gpsd_is_receiving_connections(ip="127.0.0.1", port="2947"):
    result=False
    try:
        b=subprocess.check_output(["nc", ip,port,"-zv","-w","3"],stderr=subprocess.STDOUT,timeout=4)
        if b.find(b"open")!=-1:
            result=True
    except:
         pass
    return result


def gpsd_is_receiving_data():
    result=False
    try:
        b=subprocess.check_output(["nmt-geopositioning",],stderr=subprocess.STDOUT,timeout=4)
        if len(b.split(b"|"))==3:
            result=True
    except:
        pass
    return result

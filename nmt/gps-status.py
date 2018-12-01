#!/usr/bin/python3
import argparse
import sys
sys.path.append("/usr/share/navit-mytools/")
from libnavitmytools import wifi_is_name, bluenmea_is_receiving_connections, gpsd_is_receiving_connections, gpsd_is_receiving_data,  bluenmea_is_connected, espeak, config_read

parser=argparse.ArgumentParser("This program checks my gps system")
parser.add_argument('--speak', help='Speaks result', action="store_true",default=False)
parser.add_argument('--phoneip', help='Telephone IP Adress',  default="192.168.43.1")
parser.add_argument('--ssid', help='SSID phone is connected',  default=None)
args=parser.parse_args()

if not args.ssid:
    ssid=config_read("SSID")
else:
    ssid=args.ssid

wifi=wifi_is_name(ssid)
bluenmea=bluenmea_is_receiving_connections(args.phoneip)
bluenmea_up=bluenmea_is_connected(args.phoneip)
gpsd=gpsd_is_receiving_connections()
gpsdata=gpsd_is_receiving_data()
gps_bluenmea=False

print ("Wifi: {}. Phone makes connections: {}. Phone is connected: {} Gpsd: {}. Gps data: {}".format(wifi,bluenmea, bluenmea_up,gpsd,gpsdata))

if args.speak==True:
    if wifi==False:
        espeak("Wifi problem")
    elif  bluenmea==False:
        espeak("Phone does not receive connections")
    elif bluenmea_up==False:
        espeak("Phone connection has fallen")
    elif  gpsd==False:
        espeak("GPS daemon problem")
    elif gpsdata==False:
        espeak("Missing GPS data")
    else:
        espeak("No problem")

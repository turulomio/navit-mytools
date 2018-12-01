#!/usr/bin/python3
import argparse
import datetime
import os    
import subprocess
import sys
import urllib.request

start=datetime.datetime.now()
dir="/tmp/navit-map-point_{}".format(datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))
os.system("mkdir -p '{}'".format(dir))

parser=argparse.ArgumentParser("This program generates a navit binary map from OpenStreetMap. It takes a decimal degrees radius around the latitude and longitude passed by parameter.")
parser.add_argument('-a', '--latitude', help='Latitude in decimal', type=float, default=40.4165)
parser.add_argument('-o', '--longitude', help='Longitude in decimal', type=float, default=-3.70256)
parser.add_argument('-r', '--radius', help='Radius around the point', type=float, default=0.01)
parser.add_argument('-d',  '--output',  help='Output directory', default="/usr/share/navit/maps")
parser.add_argument('-v',  '--verbose',  help='Verbose mode', action='store_true', default=False)
args=parser.parse_args()

#Download from openstreetmap
try:
    a=urllib.request.urlretrieve("http://api.openstreetmap.org/api/0.6/map?bbox={},{},{},{}".format(args.longitude-args.radius, args.latitude-args.radius, args.longitude+args.radius, args.latitude+args.radius), "{}/point.osm".format(dir))
    print ("Downloaded {} ({} bytes)".format(a[0], os.path.getsize("{}/point.osm".format(dir))))
except:
    print ("Error getting the map. Try a smaller radius.")
    sys.exit(127)

#Verbosing
if args.verbose==True:
    err=None
else:
    err=subprocess.STDOUT

#Generate map
os.chdir(dir)
p1 = subprocess.Popen(["cat", "point.osm"], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["maptool", "point.bin"], stdin=p1.stdout, stdout=subprocess.PIPE,  stderr=err)
p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
output = p2.communicate()[0]

#Removing old, moving and generating XML
if os.path.exists("{}/point.bin".format(args.output))==True:
    os.system("rm {}/point.bin".format(args.output))
os.system("mv point.bin {}".format(args.output))
f=open("{}/point.xml".format(args.output), "w")
f.write('<map type="binfile" enabled="yes" data="$NAVIT_SHAREDIR/maps/point.bin"/>')
f.close()

#Validating result
if os.path.exists("{}/point.bin".format(args.output))==True:
    print("Generated {}/point.bin ({} bytes) from {},{} coordinates and {} of radius".format(args.output, os.path.getsize("{}/point.bin".format(args.output)),  args.latitude, args.longitude, args.radius))
else:
    print("There was a problem generating point.bin")
print ("It took {}".format(datetime.datetime.now()-start))

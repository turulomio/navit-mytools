#!/usr/bin/python3
import argparse
import datetime
import os    
import subprocess

start=datetime.datetime.now()

class Geoname:
    def __init__(self,continent,country):
        self.continent=continent
        self.country=country
        
    def url(self):
        """Download server url """
        if self.continent==None:
            return "http://planet.openstreetmap.org/planet/planet-latest.osm.bz2"
        if self.country==None:
            return "http://download.geofabrik.de/{}-latest.osm.bz2".format(self.continent.lower())
        return "http://download.geofabrik.de/{}/{}-latest.osm.bz2".format(self.continent.lower(), self.country.lower())
        
    def path(self):
        """FIle in output"""
        if self.continent==None:
            return "{}/planet-latest.osm.bz2".format(args.output)
        if self.country==None:
            return "{}/{}-latest.osm.bz2".format(args.output, self.continent.lower())
        return "{}/{}-latest.osm.bz2".format(args.output, self.country.lower())
        
    def path_tmp(self):
        """Download path in osmdir/tmp"""
        return self.path().replace(args.output, args.output+"/tmp/")
        
    def exists(self):
        """Checks if path exists"""
        if os.path.exists(self.path()):
            return True
        return False
        
        
    

#Parse args
parser=argparse.ArgumentParser("This program downloads OSM map of a named region. Region names can be found in http://download.geofabrik.de")
parser.add_argument('-C', '--continent', help='Name of a continent', default=None)
parser.add_argument('-c', '--country', help='Name of a country', default=None)
parser.add_argument('-d', '--delete', help='Delete old file', action="store_true",default=False)
parser.add_argument('-o', '--output', help='Directory output',  default="/usr/local/share/osm")
args=parser.parse_args()

#Create osm dir
subprocess.call(["mkdir", "-p", "{}/tmp".format(args.output)])

#Create object
geo=Geoname(args.continent,  args.country)

#Download
os.chdir("{}/tmp".format(args.output))
retrieved=subprocess.call(["wget","-N", geo.url()]) #Returns int

#Renames old
if args.delete==False and geo.exists() and retrieved==0:
    subprocess.call(["mv", geo.path(), geo.path()+".old"])#Rename file to old
    print ("Old file renamed")
    
#Move files and delete tmp
if retrieved==0:
    subprocess.call(["mv", geo.path_tmp(), geo.path()]) #Move from tmp to output dir
else:
    print ("File was not moved to {} due to an error".format(args.output))
subprocess.call(["rm", "-Rf", "{}/tmp".format(args.output)]) #Delete tmp dir
        


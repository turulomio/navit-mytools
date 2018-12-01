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

    def name(self):
        """Resume name from continent and country"""
        if self.continent==None:
            return "planet"
        if self.country==None:
            return self.continent.lower()
        return self.country.lower()


    def path_map(self):
        """FIle in math"""
        return "{}/{}-latest.osm.bz2".format(args.maps, self.name())
        
    def path_bin(self):
        """FIle map.bin in output"""
        return "{}/{}.bin".format(args.output, self.name())

    def exists_bin(self):
        """Checks if path exists"""
        if os.path.exists(self.path_bin()):
            return True
        return False
        
        
    

#Parse args
parser=argparse.ArgumentParser("This program gets OSM map of a named region. Region names can be found in http://download.geofabrik.de")
parser.add_argument('-C', '--continent', help='Name of a continent', default=None)
parser.add_argument('-c', '--country', help='Name of a country', default=None)
parser.add_argument('-d', '--delete', help='Delete old file', action="store_true",default=False)
parser.add_argument('-o', '--output', help='Directory output',  default="/usr/share/navit/maps")
parser.add_argument('-m', '--maps', help='Maps directory',  default="/usr/local/share/osm")
parser.add_argument('-v',  '--verbose',  help='Verbose mode', action='store_true', default=False)
args=parser.parse_args()

#Create dirs
tmpdir="{}/navit-map-geoname_{}".format(args.output,  datetime.datetime.now().strftime("%Y%m%d_%H%M%S"))
subprocess.call(["mkdir", "-p", args.output])
subprocess.call(["mkdir", "-p", tmpdir])

#Create object
geo=Geoname(args.continent,  args.country)

#Verbosing
if args.verbose==True:
    err=None
else:
    err=subprocess.STDOUT
    

    
#Generate map
os.chdir(tmpdir)
p1 = subprocess.Popen(["bzcat", geo.path_map()], stdout=subprocess.PIPE)
p2 = subprocess.Popen(["maptool", geo.name()+".bin"], stdin=p1.stdout, stdout=subprocess.PIPE,  stderr=err)
p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
output = p2.communicate()[0]


#Renames old
if args.delete==False and geo.exists_bin():
    subprocess.call(["mv", geo.path_bin(), geo.path_bin()+".old"])#Rename file to old
    print ("Old file renamed")
  
#Move to maps from tmp
subprocess.call(["mv", "{}/{}.bin".format(tmpdir, geo.name()), geo.path_bin()])

#Generating xml
f=open("{}/{}.xml".format(args.output, geo.name()), "w")
f.write('<map type="binfile" enabled="yes" data="$NAVIT_SHAREDIR/maps/{}.bin"/>'.format(geo.name()))
f.close()

#Validating result
if os.path.exists(geo.path_bin())==True:
    print("Generated {} ({} bytes)".format(geo.path_bin(), os.path.getsize(geo.path_bin())))
    subprocess.call(["rm", "-Rf", tmpdir])
else:
    print("There was a problem generating {}. Leaving temporal directory.".format(geo.path_bin()))
print ("It took {}".format(datetime.datetime.now()-start))



#chmod 644 *
#cd $mipwd

#!/usr/bin/python2
import sys, gps

position=[0,0,0]

session = gps.gps()
session.stream(gps.WATCH_ENABLE|gps.WATCH_NEWSTYLE)
for report in session:
    #print (report)
    position[0]=float(session.fix.latitude)
    position[1]=float(session.fix.longitude)
    position[2]=float(session.fix.altitude)
    if str(position[2])!="nan":
        print ("{0}|{1}|{2}".format(position[0],position[1],position[2]))
        sys.exit(0)
    #print(session.fix.latitude, report, session)
    

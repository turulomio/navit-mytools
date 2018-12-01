#!/bin/bash
# $1 gtk|internal|sdl|qt
# $2 es,en,fr,...


cp /usr/share/navit/navit.xml.dist /usr/share/navit/navit.xml
#cp /usr/portage/distfiles/svn-src/navit/navit/navit/xpm/gui_sound_32.xpm /usr/portage/distfiles/svn-src/navit/navit/navit/xpm/gui_sound_off_32.xpm /usr/share/navit/xpm/


sed -i -e 's:tracking="1" orientation="-1":tracking="1" orientation="-1" autozoom_active="1":' /usr/share/navit/navit.xml
sed -i -e 's:<vehicle name="Local GPS":<vehicle name="Local GPS" follow="1":' /usr/share/navit/navit.xml
sed -i -e "s:echo 'Fix the speech tag in navit.xml to let navit say\:' '%s':espeak -s 170 -v $2 '%s':" /usr/share/navit/navit.xml
sed -i -e 's:<log enabled="no" type="gpx":<log enabled="yes" type="gpx":' /usr/share/navit/navit.xml
sed -i -e 's:<osd enabled="no" type="compass"/>: \
<osd enabled="yes" type="compass" x="0" y="0" w="150" h="210" font_size="600" text_color="#FFFFFF"/> \
<osd enabled="yes" type="gps_status" x="0" y="210" h="60" w="150" font_size="600" text_color="#FFFFFF" h="60" w="150"/> \
<osd enabled="yes" type="text" label="${vehicle.position_sats_used} / ${vehicle.position_qual}" text_color="#FFFFFF" font_size="600" x="0" y="270" w="150" h="60"/> \
<osd enabled="yes" type="speed_cam" w="700" h="70" x="-1000" y="60" text_color="#FFFFFF" font_size="1200" label="Radar ${speed_limit} a ${distance}" /> \
<osd enabled="yes" type="text" label="${vehicle.position_time_iso8601[local;%X]}" x="0" y="330" w="150" h="60" text_color="#FFFFFF" font_size="500" /> \
<osd type="navigation_status" x="150" y="0" w="120" h="120" icon_src="%s_wh_64_64.png" enable_expression="navigation.nav_status==-1 || navigation.nav_status==1 || navigation.nav_status==2" /> \
<osd enabled="yes" type="navigation_next_turn" x="0" y="-250" w="150" h="130" /> \
<osd enabled="yes" type="text" label="${navigation.item[1].length[named]}" x="0" y="-120" w="150" h="60" font_size="600" text_color="#FFFFFF"/> \
<osd enabled="yes" type="scale" x="-270" y="-120" w="300" h="60" font_size="250"/> \
<osd enabled="yes" type="text" label="${vehicle.position_coord_geo[pos_deg]}" font_size="600"  text_color="#FFFFFF" x="-1000" y="0" w="700" h="60"/> \
<osd enabled="yes" type="text" label="Alt. ${vehicle.position_height} m" font_size="600" text_color="#FFFFFF" x="-300" y="0" w="300" h="60"/> \
<osd enabled="yes" type="text" label="H.Lleg. ${navigation.item.destination_time[arrival]}"  font_size="600" x="-300" y="60" w="300" h="60"/> \
<osd enabled="yes" type="text" label="T.Rest. ${navigation.item.destination_time[remaining]}"  font_size="600" x="-300" y="120" w="300" h="60"/> \
<osd enabled="yes" type="text" label="Dist. ${navigation.item.destination_length[named]}"  font_size="600" x="-300" y="180" w="300" h="60"/> \
<osd enabled="yes" type="text" label="${vehicle.position_speed}"  font_size="600" text_color="#FFFFFF" x="-300" y="240" w="300" h="60"/> \
<osd enabled="yes" type="text" label="Lim. ${tracking.item.route_speed}" text_color="#FFFFFF" font_size="600" x="-300" y="300" w="300" h="60"/> \
<osd enabled="yes" type="text" label="${navigation.item.street_name} (${navigation.item.street_name_systematic})" x="0" y="-60" w="100%" font_size="600" h="60"/> \
<osd enabled="yes" type="button" command="pitch=pitch==0?20\:0; say(\&quot; Visualización cambiada \&quot;)" x="-65" y="310" w="1" h="1" use_overlay="1" accesskey="\&\#118;" src="zoom_out.svg" /> \
<osd enabled="yes" type="button" command="announcer_toggle();say(\&quot; Sonido activado \&quot;)" x="-65" y="310" w="1" h="1" use_overlay="1" accesskey="\&\#115;" src="zoom_out.svg" /> \
<osd enabled="yes" type="button" x="-68" y="235" w="1" h="1" use_overlay="1" accesskey="\&\#97;" command="autozoom_active=1; gui.fullscreen=1;follow=1; pitch=80;  orientation=-1; say(\&quot; Modo automático activado \&quot;)" src="zoom_out.svg" /> \
<osd enabled="yes" type="button" x="-170" y="-180" command="autozoom_active=0; orientation=0; follow=3000; pitch=0; zoom_in()" accesskey="\&\#45;" use_overlay="1" src="zoom_in.png"/> \
<osd enabled="yes" type="button" x="-110" y="-180" command="autozoom_active=0; orientation=0; follow=3000; pitch=0;  zoom_out()" accesskey="\&\#43;" use_overlay="1" src="zoom_out.png"/> \
<osd enabled="yes" type="button" x="-150" y="-150" w="1" h="1" command="autozoom_active=0; orientation=0; follow=3000; pitch=0;  zoom_to_route()" src="zoom_out.png"  accesskey="\&\#122;" use_overlay="1"/> \
<osd enabled="yes" type="button" x="-150" y="-150" w="1" h="1" command="spawn(\&quot;sudo\&quot;,\&quot;reboot\&quot;)" src="zoom_out.png"  accesskey="\&\#114;" use_overlay="1"/> \
<osd enabled="yes" type="button" x="-150" y="-150" w="1" h="1" command="spawn(\&quot;nmt-navit-reboot\&quot;)" src="zoom_out.png"  accesskey="\&\#32;" use_overlay="1"/> \
<osd enabled="yes" type="button" x="-150" y="-150" w="1" h="1" command="spawn(\&quot;sudo\&quot;,\&quot;halt\&quot;)" src="zoom_out.png"  accesskey="\&\#104;" use_overlay="1"/> \
<osd enabled="yes" type="button" x="500" y="500" w="1" h="1"  command="layout_name=layout.nightlayout?layout.nightlayout\:layout.daylayout" accesskey="\&\#110;" use_overlay="1" src="zoom_in.png" /> \
<osd enabled="yes" type="button" x="48"  y="48" w="1" h="1" command="gui.fullscreen=!gui.fullscreen"  accesskey="\&\#102;" use_overlay="1" src="toggle_fullscreen.svg" /> \
<osd enabled="yes" type="button" x="48"  y="48" w="1" h="1" command="gui.quit()"  accesskey="\&\#113;" use_overlay="1" src="toggle_fullscreen.svg" /> \
:' /usr/share/navit/navit.xml



echo "Teclas: v visualizacion, n modo noche, s sonido, a modo automatico, z zoom to route, f fullscreen, q quit, + y - zoom, h halt, r reboot <space> navit reboott"




case $1 in
    gtk)
	sed -i -e 's:<gui type="internal" enabled="yes">:<gui type="internal" enabled="no">:' /usr/share/navit/navit.xml
	sed -i -e 's:<gui type="gtk" enabled="no":<gui type="gtk" enabled="yes" fullscreen="0" statusbar="0":' /usr/share/navit/navit.xml
	;;
    gtki) 
	;;
    qt)
	sed -i -e 's:<graphics type="gtk_drawing_area"/>:<graphics type="qt_qpainter"/>:' /usr/share/navit/navit.xml
	sed -i -e 's:<gui type="gtk" enabled="no":<gui type="qml" enabled="yes" fullscreen="0":' /usr/share/navit/navit.xml

	;;
    internal)
#	sed -i -e 's:<osd enabled="no" :<osd enabled="yes" :' /usr/share/navit/navit.xml
        sed -i -e 's:<gui type="internal" enabled="yes">:<gui type="internal" fullscreen="1" menubar="0" toolbar="0" statusbar="0" font_size="250" pitch="60">:' /usr/share/navit/navit.xml
	;;
    dist)
	cp /usr/share/navit/navit.xml.dist /usr/share/navit/navit.xml
	;;

esac
#<osd enabled="yes" type="button" x="-65" y="260" w="40" h="40"  use_overlay="1" command="zoom_to_route()"  src="toggle_fullscreen.svg" accesskey="\&\#109;"/> \

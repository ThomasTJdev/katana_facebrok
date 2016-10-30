# This module requires katana framework 
# https://github.com/PowerScript/KatanaFramework

"""
ARCH requirements:
* apache (httpd)
* mariadb
* php56

yaourt -S apache mariadb php56 php56-apache

sudo nano /etc/php56/php.ini
	extension=mssql.so
	extension=mysql.so
	extension=mysqli.so
	extension=pdo_mysql.so
	
sudo nano /etc/mysql/my.cnf 
	skip-networking
	
nano /etc/httpd/conf/httpd.conf
	#LoadModule mpm_event_module modules/mod_mpm_event.so
	LoadModule mpm_prefork_module modules/mod_mpm_prefork.so
	LoadModule php56_module modules/libphp56.so
	AddHandler php56-script php
	Include conf/extra/php7_module.conf

iptables -A INPUT -p tcp -m tcp --dport 80 -j ACCEPT	
iptables -A INPUT -p tcp --destination-port 80 -j DROP

Always in spanish? Change lang.php es to en ($lang="en";})

"""

# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #
# Katana Core import				  #
from core.KATANAFRAMEWORK import *	#
# :-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-:-: #

# LIBRARIES
from core.Function import status_cmd
# END LIBRARIES 

# INFORMATION MODULE
def init():
	init.Author			    ="RedToor - Minor changes: TTJ, ThomasTJ 2016"
	init.Version			="1.0"
	init.Description		="facebrok project Launcher."
	init.CodeName		    ="set/facebrok"
	init.DateCreation	    ="23/08/2015"	  
	init.LastModification   ="24/03/2016"
	init.References		    =None
	init.License			=KTF_LINCENSE
	init.var				={}

	# DEFAULT OPTIONS MODULE
	init.options = {
		# NAME	VALUE				     RQ     DESCRIPTION
		'u_sql':["root" 					    ,True,'User Mysql'],
		'p_sql':["" 						    ,True,'Pass Mysql'],
		'systemd':["systemctl"                  ,True,'service/systemctl'],
		'html_dir':["/srv/http/croak/"          ,True,'www dir   ']		
	}
	return init
# END INFORMATION MODULE

# CODE MODULE	############################################################################################
def main(run):

	printAlert(0,"Installing facebrok project in local server")
	printAlert(0,"Coping files to server			"+status_cmd("cp -R files/facebrok/* "+init.var['html_dir']))
	printAlert(0,"Giving privileges to files		"+status_cmd("chmod -R 777 "+init.var['html_dir']))
	if init.var['systemd'] == "systemctl":
		printAlert(0,"Starting Apache Server		"+status_cmd("systemctl start httpd"))
		printAlert(0,"Starting Mysql Server			"+status_cmd("systemctl start mariadb"))
	else:
		printAlert(0,"Starting Apache Server	   "+status_cmd("service apache2 start"))
		printAlert(0,"Starting Mysql Server		   "+status_cmd("service mysql start"))
	printAlert(0,"Installing facebrok			   "+status_cmd('cd tmp;wget -b -nv --post-data "server=127.0.0.1&user='+init.var['u_sql']+'&pass='+init.var['p_sql']+'&data=facebrok&userp=fbrok&passp=fbrok" 127.0.0.1/croak/install/startgame.php'))
	Space()
	printAlert(7,"Control Panel in http://127.0.0.1/croak/ With: user[fbrok] pass[fbrok]")
	raw_input(printAlert(8,"Press [ENTER] key for Stop facebrok"))
	printAlert(0,"Stoping Process")
	printAlert(0,"Removing files					"+status_cmd("rm -R "+init.var['html_dir']+"*"))
	if init.var['systemd'] == "systemctl":
		printAlert(0,"Stoping Apache				"+status_cmd("systemctl stop httpd"))
		printAlert(0,"Stoping Mysql					"+status_cmd("systemctl stop mariadb"))
	else:
		printAlert(0,"Stoping Apache				"+status_cmd("service apache2 stop"))
		printAlert(0,"Stoping Mysql					"+status_cmd("service mysql stop"))
# END CODE MODULE ############################################################################################

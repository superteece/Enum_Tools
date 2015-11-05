#!/bin/bash

echo `mkdir configs`
echo `mkdir app_info`
echo `mkdir services`
echo `mkdir user_info`


#Get system info
echo `cat /etc/*-release > release_info.txt`
echo ""
echo "Release info for this system has been saved in release_info.txt"

#Dump .conf files into individual text files
echo "Dumping interesting .conf files"
echo `cat /etc/syslog.conf > configs/syslog.txt`
echo `cat /etc/chttp.conf > configs/chttp.txt`
echo `cat /etc/lighttpd.conf > configs/lighttpd.txt`
echo `cat /etc/cups/cupsd.conf > configs/cupsd.txt`
echo `cat /etc/inetd.conf > configs/inetd.txt`
echo `cat /etc/apache2/apache2.conf > configs/apache2.txt`
echo `cat /etc/my.conf > configs/my.conf.txt`
echo `cat /etc/httpd/conf/httpd.conf > configs/httpd_conf.txt`
echo `cat /opt/lampp/etc/httpd.conf > configs/lampp_httpd_conf.txt`
echo "Output complete"
echo ""

#Gather and dump info revealing applications installed on the system
echo "Gathering application info"
echo `ls -alh /usr/bin/ > app_info/usr-bin_contents.txt`
echo `ls -alh /sbin/ > app_info/sbin_contents.txt`
echo `dpkg -l > app_info/dpkg_history.txt`
echo `rpm -qa > app_info/rpm_history.txt` #For redhat variants
echo `ls -alh /var/cache/apt/archives > app_info/apt_history.txt`
echo `ls -alh /var/cache/yum/ > app_info/yum_history.txt` #For redhat variants
echo "Output complete"
echo ""
#Gather and dump info about running services
echo "Gathering services info"
echo `echo "Output from ps aux" >> services/user_lvl.txt`
echo `ps aux >> services/user_lvl.txt`
echo `echo "===============BREAK===============" >> services/user_lvl.txt`
echo `echo "Output from ps -ef" >> services/user_lvl.txt`
echo `ps -ef >> services/user_lvl.txt`
echo `echo "===============BREAK===============" >> services/user_lvl.txt`
#echo `top >> services/user_lvl.txt`
echo `echo "Contents from cat /etc/services" >> services/user_lvl.txt`
echo `cat /etc/services >> services/user_lvl.txt`
echo `echo "===============BREAK===============" >> services/user_lvl.txt`
echo "Output complete"
echo ""

#Enum user info
echo "Gathering and dumping information about users"
echo `id > user_info/curent_user_info.txt`
echo `who > user_info/users_logged_in_now.txt`
echo `w > user_info/users_running_processes.txt`
echo `last > user_info/last_logged_in_users.txt`
#echo `cat /etc/passwd | cut -d: > user_info/list_of_users.txt`    # List of users
echo `grep -v -E "^#" /etc/passwd | awk -F: '$3 == 0 { print $1}' > user_info/list_of_superusers.txt`   # List of super users
echo `awk -F: '($3 == "0") {print}' /etc/passwd >> user_info/list_of_superusers.txt`   # List of super users
echo `cat /etc/sudoers > user_info/list_of_sudoers.txt`
echo `sudo -l >> user_info/list_of_sudoers.txt`
echo "Output complete"
echo ""

# Creating IBM Cloud CE Automatically 

- create 1 virtual server, running Centos 7 
	- download here: http://isoredirect.centos.org/centos/7/isos/x86_64/CentOS-7-x86_64-Minimal-1708.iso)
	- recommended virtual hardware: 2 vCPUs + 8 GB RAM + 100 GB vDISK 

- login virtual server
  - execute: curl -l https://raw.githubusercontent.com/jmbarros/minicloud-auto/master/jumper.py | python

  - edit: "inventory" file and change the password

  - execute: python install_minicloud.py
  
  that's it!
#!/usr/bin/python 

import os
####################################################
def cmd ( cmdx ):
   " run"
   os.system(cmdx)
   return;

def move ( ori, dest ):
   " coping file "
   pw = "mv " + ori + " " + dest
   os.system(pw)
   return;

def copy ( ori, dest ):
   " coping file "
   cpw = "cp -r " + ori + " " + dest
   os.system(cpw)
   return;

def python ( py ):
  "run py script"
  ps = "/usr/bin/python ./" + py
  os.system(ps)
  return;
####################################################
copy("/root/minicloud-auto/post_boot.service", "/etc/systemd/system/post_boot.service")
cmd("/usr/bin/systemctl enable post_boot.service")
cmd("/sbin/reboot")
#!/usr/bin/python 

import os

def cmd ( cmdx ):
   " run"
   os.system(cmdx)
   return;

def python ( py ):
  "run py script"
  ps = "/usr/bin/python " + py
  os.system(ps)
  return;

####################################################
#python("/root/minicloud-auto/to_execute.py")
python("/root/minicloud-auto/update_inventory.py")
python("/root/minicloud-auto/install.py")
cmd("/usr/bin/systemctl disable post_boot.service")
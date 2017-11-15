#!/usr/bin/python 

import os

def yum_install ( pkg ):
   "install via yum"
   install = "yum install -y  " + pkg
   os.system(install)
   return;

def play_book ( pb ):
   "run playbook"
   book = "ansible-playbook " + pb
   os.system(book)
   return;

def pip ( pp ):
   "run playbook"
   pcom = "pip install " + pp
   os.system(pcom)
   return;

def install_galaxy ( galaxy ):
   "install galaxy repo"
   ig = "ansible-galaxy install " + galaxy
   os.system(ig)
   return;

def git ( url ):
   " using git"
   gt = "git clone " + url
   os.system(gt)
   return;

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
 ############
yum_install("epel-release")
yum_install("python-setuptools")
cmd("easy_install pip")
yum_install("ansible")
yum_install("git")
git("https://github.com/jmbarros/minicloud-auto.git")
play_book("~/minicloud-auto/jumper.yml")
copy("~/minicloud-auto/inventory", "~/inventory")
copy("~/minicloud-auto/install_minicloud.py", "~/install_minicloud.py")
install_galaxy("jmbarros.minicloud")

#! /usr/bin/env python

import pysnmp
import paramiko

# dir(pysnmp) can find attributes named '__version__ and '__name__' '

def show_lib_version(lib):
    
    lib_version = str(lib.__version__)
    lib_name = lib.__name__
 
    print "The version of %s is %s" % (lib_name, lib.__version__)


show_lib_version(pysnmp)
show_lib_version(paramiko)

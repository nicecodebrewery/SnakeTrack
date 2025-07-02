import argparse
import configparser
from datetime import datetime
import grp,pwd
from fnmatch import fnmatch
import hashlib
from math import ceil
import os
import re
import sys
import zlib

from src.core import *
argparser = argparse.ArgumentParser(description="None")
argsubparser = argparser.add_subparsers(title="Commands",dest="command")
argsubparser.required = True

def main():
    if(len(sys.argv) == 1):
        print("No commands. Okay I'll do nothing.")
        return
    match sys.argv[1]:
        case 'init' : cmd_init(sys.argv[2:])
        case 'dog-file' :cmd_dog_file(sys.argv[2:])
        case _ : print("Bad command")
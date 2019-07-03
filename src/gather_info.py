#!/usr/local/bin/python3.6

import psutil
import time
import os
import sys
import mysql.connector

def print_methods (obj):
    print ([method for method in dir(obj) if callable(getattr(obj, method))])

try:
    mydb = mysql.connector.connect(
    host="localhost",
    user="gweiss",
    passwd=os.environ['MYSQL_PW'],
    database="sys_watch3"
    )
except:
    print("Couldn't connect to the database.")
    sys.exit(1)


while True:
    cpu_load = psutil.cpu_percent()
    print ("CPU load: {}%".format(cpu_load))

    mem = psutil.virtual_memory()
    print ("Memory available: {} GB".format(round(mem.available/1000000000, 1)))

    running_processes_count = len(psutil.pids())
    print ("Running processes: {}".format(running_processes_count))

    print ("")
    time.sleep(1)

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
    passwd="gweiss", #os.environ['MYSQL_PW'],
    database="sys_watch"
    )
except:
    print("Couldn't connect to the database.")
    sys.exit(1)

comp_id = 0
mycursor = mydb.cursor()

while True:
    cpu_load = psutil.cpu_percent()
    print ("CPU load: {}%".format(cpu_load))

    mem = round(psutil.virtual_memory().available/1000000000, 1)
    print ("Memory available: {} GB".format(mem))

    running_processes_count = len(psutil.pids())
    print ("Running processes: {}".format(running_processes_count))

    sql = "INSERT INTO events (computer_id, cpu_load, available_memory, running_processes) VALUES ({}, {}, {}, {})".format(comp_id, cpu_load, mem, running_processes_count)
    mycursor.execute(sql)
    mydb.commit()

    print ("")
    time.sleep(1)

#!/usr/bin/python3
#read the file
#extract ip address and error success logs
#convert the output to csv file
import re

with open("server.log", "r") as server:
    print(server.read())

    for line in server:
        the_parttern = re.search(pattern, line)
        print(the_parttern.group())
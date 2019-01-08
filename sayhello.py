#!/usr/bin/env python3
#this script reads from STDIN 
# it greets the person whose name gets passed in
import sys
name = sys.stdin.read()
print("Hello " + name + "!")
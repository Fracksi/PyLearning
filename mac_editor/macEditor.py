#!/usr/bin/env python

import subprocess

subprocess.call("ip link set eth0 down", shell=True)
subprocess.call("ip link set eth0 address 00:11:22:33:44:66", shell=True)
subprocess.call("ip link set eth0 up", shell=True)

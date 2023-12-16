#!/usr/bin/env python

import subprocess

# Variables

userInterface = "eth0"
newMacAddress = "00:11:22:33:44:66"

# Print output overview
print("[+] Changing MAC Address for " + userInterface + " to " + newMacAddress)

# Make system calls
subprocess.call("ip link set " + userInterface + " down", shell=True)
subprocess.call("ip link set " + userInterface + " address " + newMacAddress, shell=True)
subprocess.call("ip link set " + userInterface + " up", shell=True)

# Checks
subprocess.call("ip addr", shell=True)

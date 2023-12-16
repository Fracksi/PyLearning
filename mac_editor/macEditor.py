#!/usr/bin/env python

import subprocess

# Variables
userInterface = input("Please enter interface to change: ")
newMacAddress = input("Enter the new MAC: ")

# Print output overview
print("[+] Changing MAC Address for " + userInterface + " to " + newMacAddress)

# Make system calls
subprocess.call("ip link set " + userInterface + " down", shell=True)
subprocess.call("ip link set " + userInterface + " address " + newMacAddress, shell=True)
subprocess.call("ip link set " + userInterface + " up", shell=True)

# Checks
subprocess.call("ip addr", shell=True)

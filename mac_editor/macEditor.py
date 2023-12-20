#!/usr/bin/env python

import subprocess

def main():

  # Variables
  userInterface = input("Please enter interface to change: ")
  newMacAddress = input("Enter the new MAC: ")

  # Print output overview
  print("[+] Changing MAC Address for " + userInterface + " to " + newMacAddress)

  # Make system calls
  subprocess.call(["ip", "link", "set", userInterface, "down"])
  subprocess.call(["ip", "link", "set", userInterface, "address", newMacAddress])
  subprocess.call(["ip", "link", "set", userInterface, "up"])

  # Checks
  subprocess.call(["ip", "addr"])

# Technically more proper
if __name__ == '__main__':
  main()

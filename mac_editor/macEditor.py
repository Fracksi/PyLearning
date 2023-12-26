#!/usr/bin/env python

import subprocess
import optparse


def macSwitcharoo(userInterface, newMacAddr):
  # Print output overview
  print("[+] Changing MAC Address for " + userInterface + " to " + newMacAddr)

  # Make system calls
  subprocess.call(["ip", "link", "set", userInterface, "down"])
  subprocess.call(["ip", "link", "set", userInterface, "address", newMacAddr])
  subprocess.call(["ip", "link", "set", userInterface, "up"])

  # Checks
  subprocess.call(["ip", "addr"])


def main():

  # Loads child for OptionsParser and assigns basic inline flags
  parser = optparse.OptionParser()
  parser.add_option("-i", "--interface", dest="userInterface", help="Interface where the MAC is changed.")
  parser.add_option("-m", "--mac", dest="newMacAddr", help="New MAC being assigned.")

  # Method that returns the options from the args
  (options, arguments) = parser.parse_args()

  macSwitcharoo(options.userInterface,options.newMacAddr)


# Technically more proper since this isn't imported.
if __name__ == '__main__':
  main()


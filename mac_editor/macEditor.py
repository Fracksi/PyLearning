#!/usr/bin/env python


import subprocess
import optparse
import re


def argumentGrabbing():
  # Loads child for OptionsParser and assigns basic inline flags
  parser = optparse.OptionParser()
  parser.add_option("-i", "--interface", dest="userInterface", help="Interface where the MAC is changed.")
  parser.add_option("-m", "--mac", dest="newMacAddr", help="New MAC being assigned.")

  # Method that returns the options from the args
  (options, arguments) = parser.parse_args()

  #Basic error handling if -i or -m aren't provided.
  if not options.userInterface:
    parser.error("[-] IP Interface not included, use --help for more info.")
  elif not options.newMacAddr:
    parser.error("[-] New MAC not included, use --help for more info.")
  return options


def getCurrentMac(userInterface):
  # Prints the ip addr show for the userinterface
  rsltchk = subprocess.check_output(["ip","addr","show", userInterface])

  # Thanking IBM for their regex while I still pick up the flow
  # Snatches (unfortunately) all the MACs (for now). ifconfig has only the one but some low package installs
  # -- I've made include ip suite over ifconfig now. No respect for the OGs.
  macRegexSearch = re.search(r"((?:[0-9a-fA-F]{2}\:){5}[0-9a-fA-F]{2})", str(rsltchk))

  #Sends back the first MAC found
  if macRegexSearch:
    return macRegexSearch.group(0)
  else:
    print("[-] MAC could not be read.")


def macSwitcharoo(userInterface, newMacAddr):
  # Print output overview
  print("[+] Changing MAC Address for " + userInterface + " to " + newMacAddr)

  # Make system calls
  subprocess.call(["ip", "link", "set", userInterface, "down"])
  subprocess.call(["ip", "link", "set", userInterface, "address", newMacAddr])
  subprocess.call(["ip", "link", "set", userInterface, "up"])


def main():
  # Grabs what to send from function above, basic error handling.
  options = argumentGrabbing()

  # Grabs current MAC and prints it, passes stampedMac as a string in case print() doesn't approve of combo
  stampedMac = getCurrentMac(options.userInterface)
  print("[$] Current MAC is: " + str(stampedMac))

  # Sticks the info the script wants into the function to change MAC
  macSwitcharoo(options.userInterface,options.newMacAddr)

  # Comment placeholder
  stampedMac = getCurrentMac(options.userInterface)
  if stampedMac == options.newMacAddr:
    print("[+] MAC Address changed to: " + stampedMac)
  else:
    print("[-] MAC Address was not changed.")

# Technically more proper since this isn't imported.
if __name__ == '__main__':
  main()


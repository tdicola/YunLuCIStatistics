#!/bin/python
# Collectd-exec plugin script to gather data from the Yun console.
# Copyright 2014 Tony DiCola (tony@tonydicola.com) 
# Released under an MIT license (http://opensource.org/licenses/MIT)

import os
import socket
import sys
import time

# Global configuration.
CONNECT_RETRY_SECONDS = 30.0	# How long to wait (in seconds) before attempting to connect to a closed console.
CONSOLE_PORT = 6571				# TCP port to connect to for accessing the console.  Default is 6571.

# Read hostname and interval environment variables set by collectd exec plugin.
hostname = os.environ.get('COLLECTD_HOSTNAME', 'localhost')
interval = os.environ.get('COLLECTD_INTERVAL', 30)

# Connect to Yun console.
# No timeout is used since collectd prefers the app run indefinitely.
console_soc = None
while console_soc is None:
	try:
		console_soc = socket.create_connection(('localhost', CONSOLE_PORT))
	except socket.error:
		# Ignore connection errors.  Wait a little while and try again.
		time.sleep(CONNECT_RETRY_SECONDS)

# Connected, now grab a file-like object to talk to the socket.
console = console_soc.makefile()

# Loop reading lines from the console forever (or until the socket closes).
# Note if the socket closes and the program stops, collectd exec will just run the program again.
for line in console:
	# Parse lines which have a semicolon into a name and value.
	values = line.split(':', 1)
	# Ignore lines which aren't parseable.
	if len(values) != 2:
		continue
	# Ignore lines with no name.
	name = values[0]
	if name is None:
		continue
	# Ignore lines which don't have a numeric value.
	value = None
	try:
		value = float(values[1])
	except ValueError:
		continue
	# Output value for collectd exec plugin.
	print 'PUTVAL "{0}/exec-{1}/gauge" {2}:{3}'.format(hostname, name, int(time.time()), value)
	sys.stdout.flush()
	# Give up processing time to not bog down the CPU.
	time.sleep(0)

#!/usr/bin/env python

import paramiko
import time

## Example Deploy Script
## This file uses paramiko to login to a box. Note that this is a skeleton file and you will need to do a bunch to complete the assignment.
def deploy(key, server, prefix):
	print "Connecting to box"
	ssh = paramiko.SSHClient()
	#k = paramiko.RSAKey.from_private_key_file("/Users/neerjadoshi/msan/BusinessStrategies/MSAN-603-Sprint/sprint.pem")

	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(server, username = 'ec2-user', key_filename = key )

	ssh.exec_command('sudo yum install git -y')
	#ssh.exec_command("rm -rf MSAN-603-Sprint; rm -rf Output; mkdir ~/Output; git clone https://github.com/neerjad/MSAN-603-Sprint.git; echo '1 * * * * python /home/ec2-user/MSAN-603-Sprint/hello_world.py' >  ~/.crontab; crontab ~/.crontab")
	ssh.exec_command('rm -rf MSAN-603-Sprint; rm -rf Output; mkdir ~/Output; git clone https://github.com/neerjad/MSAN-603-Sprint.git; crontab -l | echo "*/5 * * * * python /home/ec2-user/MSAN-603-Sprint/hello_world.py" | crontab -')

	print "Pull from Github successful"
	time.sleep(10)






	print "Script fully executed ... exiting" 
	ssh.close()
	## EOF ##


deploy('sprint.pem', 'ec2-54-186-173-133.us-west-2.compute.amazonaws.com', 'prefix')
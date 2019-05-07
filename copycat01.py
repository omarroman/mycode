#!/usr/bin/env python3
import shutil
import os
os.chdir('/home/student/mycode/')
# The following line will create the file if it does not already exist
shutil.copy('5g_research/sdn_network.txt', '5g_research/sdn_network.txt.copy')
# The following line will create the directory if it does not already exist
shutil.copytree('5g_research/', '5g_research_backup/')


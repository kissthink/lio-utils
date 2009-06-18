#!/usr/bin/python

import os
import subprocess as sub
import string
from optparse import OptionParser

tcm_root = "/sys/kernel/config/target/core"

def rd_createvirtdev(path, params):
	
#	print "Calling rd_createvirtdev: path " + path
	cfs_path = tcm_root + "/" + path + "/"
#	print "Calling rd_createvirtdev: params " + str(params)
	rd_pages = params[0]

	rd_params = "rd_pages=" + rd_pages
	print "rd_params: " + rd_params

	control_opt = "echo " + rd_params.rstrip() + " > " + cfs_path + "/control"
	print "control_opt: " + control_opt
	ret = os.system(control_opt)
	if ret:
		print "RAMDISK: createvirtdev failed for control_opt with " + rd_params
		return -1

	enable_opt = "echo 1 > " +  cfs_path + "enable"	
	print "Calling enable_opt " + enable_opt
	ret = os.system(enable_opt)
	if ret:
		print "RAMDISK: createvirtdev failed for enable_opt with " + rd_params
		return -1

	return

def rd_freevirtdev():
	return

def rd_get_params(path):
	
	info_file = path + "/info"
	p = os.open(info_file, 0)
	value = os.read(p, 1024)
	off = value.index('PAGE_SIZE: ')
	off += 11 # Skip over "PAGE_SIZE: "
	rd_pages_tmp = value[off:]
	rd_pages = rd_pages_tmp.split('*')
	params = "rd_pages=" + rd_pages[0]
	os.close(p)

	return params
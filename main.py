# -*- coding: utf-8 -*-

def dispatch():
	import runpy
	import sys
	import os
	
	from android.permissions import request_permissions, Permission
	request_permissions([Permission.READ_EXTERNAL_STORAGE])
	
	from jnius import autoclass
	Environment = autoclass('android.os.Environment')
	sdcard_path = Environment.getExternalStorageDirectory().getAbsolutePath()
	entrypoint = sdcard_path + '/kivy/startup/main.py'
	
	entrypoint_path = os.path.dirname(entrypoint)
	sys.path.append(os.path.realpath(entrypoint_path))
	runpy.run_path(
		entrypoint,
		run_name='__main__')

if __name__ == '__main__':
	dispatch()

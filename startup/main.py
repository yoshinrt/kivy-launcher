# -*- coding: utf-8 -*-

def run_entrypoint(entrypoint):
	import runpy
	import sys
	import os
	entrypoint_path = os.path.dirname(entrypoint)
	sys.path.append(os.path.realpath(entrypoint_path))
	runpy.run_path(
		entrypoint,
		run_name="__main__")


def run_launcher(tb=None):
	from launcher.app import Launcher
	Launcher().run()


def dispatch():
	import os
	
	from jnius import autoclass
	Environment = autoclass('android.os.Environment')
	sdcard_path = Environment.getExternalStorageDirectory().getAbsolutePath() + '/'
	
	from kivy.resources import resource_add_path
	resource_add_path(sdcard_path + 'kivy/resource')

	# desktop launch
	entrypoint = os.environ.get("KIVYLAUNCHER_ENTRYPOINT")
	if entrypoint is not None:
		return run_entrypoint(entrypoint)

	# try android
	activity = autoclass("org.kivy.android.PythonActivity").mActivity
	intent = activity.getIntent()
	entrypoint = intent.getStringExtra("entrypoint")
	
	if entrypoint is not None:
		orientation = intent.getStringExtra("orientation")
		
		if orientation == "portrait":
			# SCREEN_ORIENTATION_PORTRAIT
			activity.setRequestedOrientation(0x1)
		elif orientation == "landscape":
			# SCREEN_ORIENTATION_LANDSCAPE
			activity.setRequestedOrientation(0x0)
		elif orientation == "sensor":
			# SCREEN_ORIENTATION_SENSOR
			activity.setRequestedOrientation(0x4)
	else:
		entrypoint = intent.getDataString()
		if entrypoint is not None:
			import urllib.parse
			import re
			
			entrypoint = re.sub('\?.*', '', entrypoint)
			entrypoint = urllib.parse.unquote(entrypoint)
			entrypoint = re.sub('.*file://', '', entrypoint)
			entrypoint = entrypoint.replace('content://com.android.externalstorage.documents/document/primary:', sdcard_path)
	
	if entrypoint is not None:
		return run_entrypoint(entrypoint)
	
	run_launcher()


if __name__ == "__main__":
	try:
		dispatch()
	except Exception:
		import traceback
		import show_msg
		show_msg.ShowMsgApp(msg = traceback.format_exc()).run()

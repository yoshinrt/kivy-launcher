# -*- coding: utf-8 -*-
from kivy.utils import platform

def check_manage_all_files_permission():
	if platform != 'android': return True # Return True for PC environments etc. for convenience
	
	from jnius import autoclass
	
	# Determine if the version is Android 11 (API 30) or higher
	Build = autoclass('android.os.Build$VERSION')
	if Build.SDK_INT >= 30:
		Environment = autoclass('android.os.Environment')
		# Check if permission is granted
		return Environment.isExternalStorageManager()
	
	# For API 29 and below, check the standard WRITE_EXTERNAL_STORAGE permission
	PythonActivity = autoclass('org.kivy.android.PythonActivity')
	ContextCompat = autoclass('androidx.core.content.ContextCompat')
	PermissionChecker = autoclass('androidx.core.content.PermissionChecker')
	
	context = PythonActivity.mActivity
	permission = "android.permission.WRITE_EXTERNAL_STORAGE"
	
	# Check permission status (0 is PERMISSION_GRANTED)
	result = ContextCompat.checkSelfPermission(context, permission)
	return result == 0

def open_manage_all_files_setting():
	if platform != 'android':
		return

	from jnius import autoclass, cast
	
	PythonActivity = autoclass('org.kivy.android.PythonActivity')
	Intent = autoclass('android.content.Intent')
	Uri = autoclass('android.net.Uri')
	Settings = autoclass('android.provider.Settings')
	
	activity = PythonActivity.mActivity
	
	# 1. Specify the Action directly as a string (this is the most reliable way)
	# MANAGE_APP_ALL_FILES_ACCESS_PERMISSION is a constant added in API 30
	ACTION = "android.settings.MANAGE_APP_ALL_FILES_ACCESS_PERMISSION"
	
	try:
		# Attempt to open the specific settings screen for this app
		package_name = activity.getPackageName()
		uri = Uri.parse(f"package:{package_name}")
		intent = Intent(ACTION)
		intent.setData(uri)
		activity.startActivity(intent)
		
	except Exception as e:
		print(f"Individual setting failed: {e}")
		try:
			# If it fails, open the general management screen listing all apps (fallback)
			# Do not use setData here
			fallback_action = "android.settings.MANAGE_ALL_FILES_ACCESS_PERMISSION"
			intent = Intent(fallback_action)
			activity.startActivity(intent)
		except Exception as e2:
			print(f"Fallback failed: {e2}")

def ensure_storage_permission():
	if not check_manage_all_files_permission():
		open_manage_all_files_setting()

def dispatch():
	import runpy
	import sys
	import os.path
	
	from jnius import autoclass
	Environment = autoclass('android.os.Environment')
	sdcard_path = Environment.getExternalStorageDirectory().getAbsolutePath()
	entrypoint = sdcard_path + '/kivy/startup/main.py'
	
	entrypoint_path = os.path.dirname(entrypoint)
	sys.path.append(os.path.realpath(entrypoint_path))
	
	ensure_storage_permission()
	
	runpy.run_path(entrypoint, run_name='__main__')

if __name__ == '__main__':
	dispatch()

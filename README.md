# Direct Kivy Launcher

This fork allows you to launch a python script directly from the home screen.

The following has been changed from the original Kivy Launcher.

- Direct Kivy Launcher can be launched by implicit intents (*.py).
  - You can run a python script directly from a filer or home screen shortcut.
- When the Direct Kivy Launcher is launched, it will run `{SDCARD}/kivy/startup/main.py`.
  - You can change the behavior of the starting Direct Kivy Launcher without building the apk.

## Instructions

`{SDCARD}` is your device's sdcard path, e.g. `/sdcard`

1. Install the apk
1. Place all `startup/` files of this repository under `{SDCARD}/kivy/startup/`, or place your initial script as `{SDCARD}/kivy/startup/main.py`.
1. If you open the python script from a filer etc., it will be executed by Direct Kivy Launcher.
    - When using `startup/`, you can also start the original launcher by starting Direct Kivy Launcher.

The following description is the original README.md. There is a description that does not apply to this fork.

-----
# Kivy Launcher

(work in progress, not yet published on Google Play)

This is a reboot of the previously pygame/kivy launcher, implemented in Java in Python for android. It was barely maintainable, and with the rewrite of the new Python for android, it was lost.

This version aimed to provide a replacement for the launcher, but works also on desktop, on Python 2 or 3.

Anybody can clone the repo, add the dependencies we would not provide by default, and recompile it.

![kivy-launcher](https://user-images.githubusercontent.com/37904/37256979-0611d5be-2563-11e8-98a6-485e656b0f4b.png)

## How it works

Follow the guide the same as before:

https://kivy.org/docs/guide/packaging-android.html#packaging-your-application-for-the-kivy-launcher

Then just start the launcher, you should see your application listed, then press play.

## `android.txt` specification

- `title`: Title of the application
- `author`: Author of the application
- `orientation`: Default orientation, one of "landscape", "portrait", "sensor"

## Works

- Provide a simple UI to discover and start another app
- Start another main.py as a `__name__ == '__main__'`
- Reduce to the minimum the overhead of the launcher to launch another app
- Support landscape / portrait / sensor

## Ideas

- Act as a server to just launch any Kivy-based app from desktop to mobile
- Ability to configure multiple paths to look for applications
- Different ordering: by name, last updated, size
- Add tiny icon to show what application orientation is
- Allow to change multiple configuration token / environemnt (like different density/dpi to simulate other screens)
- Support for application without "android.txt"

PyNit
======================
Python for Nitrogen :)

script for manually changing your wallpaper from the obmenu. this script works
too for dual monitors.

![image](https://raw.githubusercontent.com/frodo4fingers/PyNit/master/PyNit.png)
wallpaper from [hdwallpapers.cat](https://hdwallpapers.cat/winding_valley_road_b_w_black_and_white_hd-wallpaper-1666507/)

**see [>>>>> wiki <<<<<](https://github.com/frodo4fingers/PyNit/wiki)**
what you need to do
----------------------
- download [PIL - the Python Imaging Library](https://github.com/python-pillow/Pillow)
- download [natsorted](https://pypi.python.org/pypi/natsort) ...but that is optional
- download PyNit
- save in folder
    + make executable and ln -s to /usr/bin/
- change paths for nitrogen, wallpaper, menu.xml (maybe you symlink them into the program folder)
- manually create a menu in obmenu named Backgrounds or Wallpaper
    + be sure you named the keyword in script after your menu in obmenu
- you will need to run PyNit.py by hand once to scan your wallpapers (bind it in the obmenu)
- run backup once - just to be sure


options
----------------------
+ w/o any option it will check for wallpapers on the wallpaper path and list them ready to use in your ObMenu
```python
PyNit.py
```

+ to alter your nitrogen configs and eventually change the wallpaper this is what is behind every wallpaper entry in ObMenu
```python
Pynit.py -a picture.jpg
```

+ to clear every wallpaper entry from your ObMenu. Make sure to use this option if you're about to delete or rename wallpapers!
```python
PyNit.py -C
```

+ to backup all nitrogen configs and menu.xml with a time stamp
```python
PyNit.py -B
```

+ to randomly change your wallpaper w/o much fuzzing around. set the intervall between with seconds and run second time to stop it
```python
PyNit.py -r -s 15
```

+ slightly more fancy and costly is a Transistion between two wallpapers. to give PyNit the number of steps use t but note that the more steps you choose the longer it takes and the cpu usage will rise. s is again the time between two wallpapers. you need to specify z in script (easier) for your screen resolution if not all of your wallpapers are the same size. run second time to stop it and note if you stop the script right in the transition the two overlaying pictures will stay :)
```python
PyNit.py -T -t 10 -s 15 -z 1920 1080
```

TODO
----------------------
- won't work with spaces in filenames for now

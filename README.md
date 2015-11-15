PyNit
======================
Python for Nitrogen :)
script for manually changing your wallpaper from the obmenu. since it changes 
all configs in the nitrogen folder (except for nitrogen.cfg) this script works 
too for dual monitors

![image](https://raw.githubusercontent.com/frodo4fingers/PyNit/master/PyNit.png)
wallpaper from [hdwallpapers.cat](https://hdwallpapers.cat/winding_valley_road_b_w_black_and_white_hd-wallpaper-1666507/)

**see [wiki](https://github.com/frodo4fingers/PyNit/wiki)**
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
```python
PyNit.py             --> will read your wallpapers and create entries in menu.xml
PyNit.py -a          --> [a]lter the cfgs in nitrogen with given picture
PyNit.py -c          --> will [c]lear wallpaper entries from obmenu
PyNit.py -B          --> will [B]ackup the menu.xml and all nitrogen configs from given paths with a time stamp
PyNit.py -r -s       --> will [r]andomly choose the wallpaper at given time step in seconds. run second time to stop.
PyNit.py -T -t -s -z --> will create a [T]ransition between two consecutive wallpapers with given count of s[t]eps, then rest for a few [s]econds. due to the overlay process a resolution or picture si[z]e must be given if not 1920x1080 (default). run second time to stop.
```


TO DO
----------------------
- won't work with spaces in filenames for now

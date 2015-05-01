#!/usr/bin/python
"""
@ frodo4fingers
@ january 2015
"""

import os, sys, time, datetime, random
from PIL import Image

def check4wallpapers(path_wall):
    """
        this function will read the wallpapers from given directory containing 
        such
    """

    wallpapers = []

    for pic in os.listdir(path_wall):

        if not os.path.isdir(path_wall + pic):

            wallpapers.append(pic)

    return wallpapers

    """END OF CHECK4WALLPAPERS"""

def clear_xml(path_menuxml, wallpapers):
    """
        delete all wallpaper entries from dropdown menu 'Backgrounds' maybe 
        not that efficient but clean (Backgrounds... see "key" in def main)
    """

    xml = open(path_menuxml)

    raw_list = []
    for line in xml:
        raw_list.append(line)
    xml.close()
    ## mark the whole xml structure around the embedded wallpaper
    ## replace it later, otherwise the indizes would change during the process
    for i in range(len(raw_list)):
        for item in wallpapers:
            if item in raw_list[i]:
                raw_list[i-2] = 'NOTINURXML\n'
                raw_list[i-1] = 'NOTINURXML\n'
                raw_list[i-0] = 'NOTINURXML\n'
                raw_list[i+1] = 'NOTINURXML\n'
                raw_list[i+2] = 'NOTINURXML\n'

    ## now write everything except marked lines
    with open(path_menuxml + '.tmp', 'w') as out:
        for item in raw_list:
            if not 'NOTINURXML' in item:
                out.write(str(item))
        out.close()

    os.rename(path_menuxml + '.tmp', path_menuxml)
    os.system('openbox --reconfigure')

    """END OF CLEAR_XML"""

def write_xml(key, path_menuxml, wallpapers):
    """
        here the new wallpaper names will be written to the xml file.
        therefore an entry must be made once in obmenu by hand.. named 
        'Backgrounds' by default.
        
        !!!please consider the "key" value in def main!!! and have a look in 
        your xml structure!!!
    """

    xml = open(path_menuxml)

    raw_list = []
    for line in xml:
        raw_list.append(line)
    xml.close()
    ## search for the given key to get position
    for i in range(len(raw_list)):
        if key in raw_list[i]:
            key_index = i
        pass

    for pic in wallpapers:
        """
        use former position to receive the actual position to start with
        ..in my menu.xml i want to start AFTER (see key in def main)
        
        <execute>PyNit.py -C</execute> ONE </action> TWO </item> 
        THREE <separator/> --------> therefore a +4!!!!!!!!
        """
        ## write a line/entry for every wallpaper for obmenu
        raw_list.insert(key_index + 4, '\t'*4 + '<item label="' + pic[:-4] + '">\n' + '\t'*5 + '<action name="Execute">\n ' + '\t'*6 + '<execute>PyNit.py -a ' + pic + '</execute>\n ' + '\t'*5 + '</action>\n ' + '\t'*4 + '</item>\n')

    with open(path_menuxml + '.tmp', 'w') as out:

        for item in raw_list:
            out.write(str(item))
        out.close()

    os.rename(path_menuxml + '.tmp', path_menuxml)
    os.system('openbox --reconfigure')

    """END OF WRITE_XML"""

def alter_cfg(path_nitro, path_wall, wallpaper):
    """
        this function will change the entries in the cfg files in the nitrogen 
        directory
    """

    for config in os.listdir(path_nitro):

        ## check for original nitrogen config and make sure there isn't a 
        ## folder containing stuff
        if not config == 'nitrogen.cfg' and not os.path.isdir(path_nitro + config):

            with open(path_nitro + config, 'r') as inf:
                with open(path_nitro + config + '.tmp', 'w') as out:

                    for line in inf:

                        if 'file=' in line:

                            newLine = 'file=' + path_wall + wallpaper + '\n'

                            out.write(newLine)

                        else:
                            out.write(line)

                    out.close()
                inf.close()
            os.rename(path_nitro + config + '.tmp', path_nitro + config)
    os.system('nitrogen --restore')

    """END OF ALTER_CFG"""

def backup(path_nitro, path_menuxml):
    """
        function to copy/backup the config files or xml file before it will be 
        changed.
    """
    ## create timestamp
    ts = time.time()

    ## make it human readable
    ## %Year %month %day %Hour %Minute... you might add %Second
    stamp = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M')
    
    os.system('cp '+ path_menuxml +' '+ path_menuxml[:-4] + stamp + '.bak')
    
    for config in os.listdir(path_nitro):
        
        if not config == 'nitrogen.cfg' and not os.path.isdir(path_nitro + config) and not config.endswith('.bak'):

            os.system('cp '+ path_nitro + config +' '+ path_nitro + config[:-4] + stamp +'.bak')

    """END OF BACKUP"""

def randomize(path_nitro, path_wall, wallpapers, step):
    """
        switch wallpaper randomly every now and then
    """
    
    key = checkRun(path_wall)
    if key == True:

        while True:
            ## pick a random wallpaper from list
            random_pic = random.choice(wallpapers)
            ## make the change
            alter_cfg(path_nitro, path_wall, random_pic)
            ## rest STEP seconds
            time.sleep(step)

    """END OF RANDOMIZE"""

def checkRun(path_wall):
    """
        check if randomize or switch is running
    """
    ## if its running
    if os.path.isfile(path_wall + '.run'):
        try:
            ## remove the randomize key
            os.system('rm ' + path_wall + '.run')
            ## remove the .PyNit_trash folder
            os.system('rm -r ' + path_wall + '.PyNit_trash')
        except:
            pass
        ## then turn it off
        os.system('killall PyNit.py')
        key = False

    else:
        ## else turn it on
        os.system('touch ' + path_wall + '.run')
        key = True

    return key

    """END OF CHECKRUN"""

def shuffle(wallpapers):
    """
        shuffle the wallpaper list and return it
    """
    
    return random.shuffle(wallpapers)

    """END OF SHUFFLE"""


def resize(size, image):
    """
        resize a given image to desired size
    """
    ## size of picture that doesnt fit the desired size
    wrong_sized = image.size

    new_width = int(wrong_sized[0]*size[0]/wrong_sized[0])
    new_height = int(wrong_sized[1]*size[1]/wrong_sized[1])

    return image.resize((new_width, new_height), Image.ANTIALIAS)

    """END OF RESIZE"""

def transition(path_wall, wallpapers, size, step, trans_step):
    """
        overlay two following images from the wallpapers list, save them and 
        write the new overlay to the next list
    """

    key = checkRun(path_wall)
    if key == True:

        ## for a clean picture folder, all unvisible images will be stored in here
        path_trans = path_wall + '.PyNit_trash/'
        if not os.path.isdir(path_trans):
            os.mkdir(path_trans)

        ## shuffle the wallpaper list in place
        random.shuffle(wallpapers)

        for i in range(len(wallpapers)-1):

            old_pic = wallpapers[i]
            new_pic = wallpapers[i+1]
            background = Image.open(path_wall + old_pic)
            overlay = Image.open(path_wall + new_pic)

            ## check if both pictures have desired size
            ## a dummy is prdoduced there will be no harm done to your pictures
            if background.size != size:
                background = resize(size, background)
                background.save(path_trans + 'dummy_background.jpg','JPEG')
                background = Image.open(path_trans + 'dummy_background.jpg')

            if overlay.size != size:
                overlay = resize(size, overlay)
                overlay.save(path_trans + 'dummy_overlay.jpg','JPEG')
                overlay = Image.open(path_trans + 'dummy_overlay.jpg')

            background = background.convert('RGBA')
            overlay = overlay.convert('RGBA')

            new_img_lst = []

            for k in range(0, trans_step, 1):
                new_img = Image.blend(background, overlay, (k/trans_step))
                new_img.save(path_trans + 'new' + str(k) + '.jpg','JPEG')
                new_img_lst.append('new' + str(k) + '.jpg')

            for transit_pic in new_img_lst:
                ## just a reminder: "-a" uses the wallpaper path
                os.system('PyNit.py -a ' + '.PyNit_trash/' + transit_pic)

            ## end loop with 100% of the new pic
            os.system('PyNit.py -a ' + new_pic)
            ## rest STEP seconds
            time.sleep(step)

            if i == len(wallpapers)-1:
                ## if end of shuffled list is reached shuffle again
                random.shuffle(wallpapers)
            else:
                continue

    """END OF TRANSITION"""

def main(argv):
    """
        Well. That's the main function..
    """
    import argparse
    parser = argparse.ArgumentParser(description = 'Wallpaper management for obmenu')

    parser.add_argument('-a', '--alter',
        dest = 'alter_cfg',
        help = 'change wallpaper in configuration file of nitrogen')

    parser.add_argument('-C', '--clear',
        dest = 'clear',
        help = 'clear the menu.xml from all wallpapers',
        default = False,
        action = 'store_true')

    parser.add_argument('-B', '--backup',
        dest = 'backup',
        help = 'save the configs or xml',
        default = False,
        action = 'store_true')

    parser.add_argument('-r', '--random',
        dest = 'random',
        help = 'run randomly through the wallpapers',
        default = False,
        action = 'store_true')

    parser.add_argument('-s', '--step',
        dest = 'step',
        help = 'seconds between two wallpapers',
        type = int,
        default = 15)
    
    parser.add_argument('-T', '--transition',
        dest = 'transition',
        help = 'transition between two wallpapers',
        action = 'store_true')

    parser.add_argument('-t', '--trans_step',
        dest = 'trans_step',
        help = 'number of overlaying steps',
        type = int,
        default = 10)

    parser.add_argument('-z', '--size',
        dest = 'size',
        help = 'maximum monitor/desired resolution',
        default = (1920,1080))

    args = parser.parse_args()

    ###########################################################################
    ### paths for configs and wallpapers
    path_menuxml = '/home/frodo/.config/openbox/menu.xml'
    path_nitro = '/home/frodo/.config/nitrogen/'
    path_wall = '/home/frodo/Pictures/'
    ###
    ###########################################################################
    
    ###########################################################################
    ### keyword for search in menu.xml so PyNit knows where to put stuff
    key = 'PyNit.py -C'
    ###
    ###########################################################################

    if args.alter_cfg:
        ## call to change configs so wallpaper will change
        alter_cfg(path_nitro, path_wall, args.alter_cfg)

    elif args.clear:
        ## read wallpapers so ...
        wallpapers = check4wallpapers(path_wall)
        ## ...they can be deleted from the xml
        clear_xml(path_menuxml, wallpapers)

    elif args.backup:
        ## backup ALL configs from nitrogen and the menu.xml
        ## feel free to change the backup plan and call the function between..
        ## ..wallpaper changing processes
        backup(path_nitro, path_menuxml)

    elif args.random:
        ## get wallpapers
        wallpapers = check4wallpapers(path_wall)
        ## start random mode
        randomize(path_nitro, path_wall, wallpapers, args.step)

    elif args.transition:
        ## get wallpapers
        wallpapers = check4wallpapers(path_wall)
        ## make switch
        transition(path_wall, wallpapers, args.size, args.step, args.trans_step)
    
    else:
        ## read them...
        wallpapers = check4wallpapers(path_wall)
        ## ...delete them...
        clear_xml(path_menuxml, wallpapers)
        ## ...write them
        write_xml(key, path_menuxml, wallpapers)

    """END OF MAIN"""


if __name__ == '__main__':
    main(sys.argv[1:])
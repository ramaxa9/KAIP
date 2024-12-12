#####################################################################
### Please set the paths accordingly. In case you don't have all  ###
### the listed folders, just keep that line commented out.        ###
#####################################################################
### Path to your config folder you want to backup
import os
import platform
import sys

config_folder='~/klipper_config'

### Path to your Klipper folder, by default that is '~/klipper'
klipper_folder='~/klipper'

### Path to your Moonraker folder, by default that is '~/moonraker'
moonraker_folder='~/moonraker'

### Path to your Mainsail folder, by default that is '~/mainsail'
mainsail_folder='~/mainsail'

### Path to your Fluidd folder, by default that is '~/fluidd'
fluidd_folder='~/fluidd'

## Distro package manager
package_manager = {
    'arch': 'sudo pacman -S',
    'debian': 'sudo apt install',
}

distro_dependency = {
    'arch': 'git nginx ',
}

def distro_select():
    if platform.system() == "Windows":
        print("Windows not supported!")
        return
    else:
        try:
            selected = package_manager[platform.system()]
        except 'Not supported!':
            if selected:
                return selected
            else:
                print("Distro not supported!")
                return

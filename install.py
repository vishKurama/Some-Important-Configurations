# install script
import os as process
import subprocess as os
from distutils.spawn import find_executable

home = process.path.expanduser("~")

VIMRC = open(home + "/.vimrc", "w+")
with open(".vimrc") as Tv :
    cpy = True
    for line in Tv :
        if "plug#end" in line :
            cpy = False
            VIMRC.write(line)
        elif cpy is True:
            VIMRC.write(line)
VIMRC.close()
Tv.close()

# find the distro and install vim in it
if find_executable("vim") is None :
    print ("Installing Vim")
    distroName =  process.popen("lsb_release -a").read()
    if "Fedora" in distroName :
        os.call(["sudo", "dnf", "install", "vim"])
    elif "Ubuntu" in distroName :
        os.call(["sudo", "apt", "install", "vim"])
    elif "Arch" in distroName :
        os.call(["sudo", "pacman", "-S", "vim"])
    elif "Antergos" in distroName :
        os.call(["sudo", "pacman", "-S", "vim"])
    print ("Finished Installing!!")

home = home + "/.vim"

# create .vim directory, if not available
if not process.path.isdir(home) :
    print ("Creating .vim")
    os.call(["mkdir", home])

# now copy all the files in .vim directory, to set up the working environment
print ("Copying the plugins and configurations!!")
os.call("cp -r * ~/.vim", shell = True)

# install all the required plugins
print ("Vim Plug Is Installing the Plugins, Please Wait....")
os.call('vim -c ":PlugInstall" -c ":qa"', shell = True, stderr = True)

# setting up the vimrc
home = process.path.expanduser("~")
print ("Copying VIMRC!!")
os.call(["cp", "-rf", ".vimrc", home])
print ("Copying VIMRC finished!!")
print ("Plugins Installed.... Enjoy VIM!!")

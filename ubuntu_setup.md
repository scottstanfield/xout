##
## Jetblue script for Ubuntu 18
##
 
# either run as root or as user with sudo permissions
sudo su -
apt-get update -y && apt-get -y dist-upgrade && apt-get upgrade -y          # accept local files if askedk     kjkk       kj
reboot now
 
# ssh back in and set timezone
sudo su -
date
timedatectl set-timezone America/New_York
date
 
# setup scratch jetblue account
adduser --gecos "" jetblue
usermod -a -G sudo jetblue
sudo - jetblue
 
##
## user: jetblue from now on
##
 
# Confirm Python 3 (3.6.5) installed
python3 -V     
 
# pip/pipenv will need this location in the path
echo "PATH=$HOME/.local/bin:$PATH" > .bash_profile
source .bashrc
 
# install pip and pipenv
sudo apt-get -y install python3-pip python3-dev
pip3 install --user pipenv  # don't use sudo here
 
##
## repo
##
 
git clone https://github.com/scottstanfield/xout
cd xout
pipenv install tqdm docopt
pipenv shell
python xout.py # to test
 
##
## copy the sample file into this folder and call it b6.txt
##
./test.sh
 
## add steps here for azure copy


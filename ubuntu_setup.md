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
python xout.py
 
## install az cli
## https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-apt?view=azure-cli-latest 

AZ_REPO=$(lsb_release -cs)
echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $AZ_REPO main" | \
    sudo tee /etc/apt/sources.list.d/azure-cli.list
curl -L https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
sudo apt-get install apt-transport-https
sudo apt-get update && sudo apt-get install azure-cli

# install azcopy
wget -O azcopy.tar.gz https://aka.ms/downloadazcopylinux64
tar -xf azcopy.tar.gz
sudo ./install.sh



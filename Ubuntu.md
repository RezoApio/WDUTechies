
# Installing Ubuntu Memo

## Installing Old Machines 

###Moving from 16.04 LTS to 18.04 LTS
Starts by installing 16.04 LTS 64bits as 18.04 LiveCD stalls
Then we upgrade distro
```shell
#Just make sure we are up-to-date
sudo apt update 
sudo apt upgrade
sudo apt dist-upgrade
sudo apt autoremove

#Install Updater the Ubuntu Way
sudo apt install update-manager-core

#Let's go
sudo do-release-upgrade -d
#-d is only needed because moving path will be present after July 2018 

```

## Installing Main Laptop

###Creating Directories
```shell
mkdir ~/Containers
mkdir ~/Repositories
mkdir ~/

```

###Adding Hubic support to synch folders
```shell
sudo apt-get install gdebi # Adding deb package Manager
wget http://mir7.ovh.net/ovh-applications/hubic/hubiC-Linux/2.1.0/hubiC-Linux-2.1.0.53-linux.deb

```

## New Item

```shell


```


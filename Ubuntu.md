
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
mkdir ~/Downloads/Installer
mkdir ~/Documents/Hubic

```
###Adding git & Techies Repo
```shell
sudo apt install git
cd ~/Repositories
git clone https://github.com/RezoApio/WDUTechies.git
```

###Adding Hubic support to synch folders
```shell
sudo apt install gdebi-core # Adding deb package Manager
cd ~/Downloads/Installer
wget http://mir7.ovh.net/ovh-applications/hubic/hubiC-Linux/2.1.0/hubiC-Linux-2.1.0.53-linux.deb
sudo gdebi hubiC-Linux-2.1.0.53-linux.deb
hubic login william.dupre@gmail.com /home/william/Documents/Hubic
hubic synchronize

```

### Installing Visual Studio Code

```shell
firefox https://code.visualstudio.com/download
#Save .deb to ~/Downloads/Installer
sudo gdebi code_1.25.1-1531323788_amd64.deb
#Extension for Markdown Preview & Markdown Linting
code --install-extension shd101wyy.markdown-preview-enhanced
code --install-extension davidanson.vscode-markdownlint
code --install-extension ms-python.python
#Installing python3 pip to install linter
sudo apt install python3-pip
/usr/bin/python3 -m pip install -U pylint

#Make VSCode default editor
sudo update-alternatives --set editor /usr/bin/code

```


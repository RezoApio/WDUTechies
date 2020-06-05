
# Installing Ubuntu Memo

## Installing Main Laptop

### Creating Directories

```shell
mkdir ~/Containers
mkdir ~/Repositories
mkdir ~/Downloads/Installer
mkdir ~/Documents/Mega
mkdir ~/WineInstall
```

### Creating a new ssh key-pair

```shell
ssh-keygen -t rsa -b 4096 -C "william.dupre@gmail.com"
```



### Adding git & Techies Repo

Add the new ssh key to git account

```shell
sudo apt install git
cd ~/Repositories
git clone git@github.com:RezoApio/WDUTechies.git
```

### Git Password Caching

```shell
git config --global credential.helper cache
git config --global credential.helper 'cache --timeout=86400'
#This is One Day time out

```

### Adding Mega to get sync

```shell
sudo apt install gdebi-core # Adding deb package Manager
cd ~/Downloads/Installer
#get megasync-xUbuntu_19.10_amd64.deb from mega.nz website
sudo gdebi megasync-xUbuntu_19.10_amd64.deb
```

Then run Mega from gnome and enjoy synch

### Installing DVD burner

```shell
sudo apt install brasero
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

### Installing Pixma MG5650

```shell
firefox "https://www.canon-europe.com/support/consumer_products/products/fax__multifunctionals/inkjet/pixma_mg_series/pixma_mg5650.aspx?type=drivers&language=EN&os=Linux%20(64-bit)"
#Save Scangear and IJ Printer .deb to Installer
#scangearmp2-3.00-1-deb.tar.gz & cnijfilter2-5.00-1-deb.tar.gz currently

tar -xvf cnijfilter2-5.00-1-deb.tar.gz
cd cnijfilter2-5.00-1-deb/
sudo ./install.sh
#Follow the instruction it should detect the printer (may need to search twice)

sudo apt install libpango1.0-0
#needed package for scangear
tar -xvf scangearmp2-3.00-1-deb.tar.gz
cd scangearmp2-3.00-1-deb/
sudo ./install.sh

```

### Adding Rolf Bensch PPA for xsane
sudo add-apt-repository ppa:rolfbensch/sane-git
sudo apt update
sudo apt install xsane


### Installing Keepass2

```shell
sudo add-apt-repository ppa:jtaylor/keepass
sudo apt update && sudo apt install keepass2
```

### Pdf Mix Tool to join pdf

```shell
sudo snap install pdfmixtool
#Warning the first run takes quite some time
```

### Installing a Spigot Minecraft Server

```shell
sudo apt install git openjdk-8-jre-headless
mkdir ~/Repositories/Spigot
cd ~/Repositories/Spigot
wget -O BuildTools.jar https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar
git config --global --unset core.autocrlf
java -jar BuildTools.jar
java -jar BuildTools.jar --rev 1.13

echo "cd ~/Repositories/Spigot" >~/RunMinecreftServer.sh
echo "java -Xms1G -Xmx1G -XX:+UseConcMarkSweepGC -jar spigot-1.13.jar" >>~/RunMinecreftServer.sh
chmod a+x ~/RunMinecreftServer.sh
~/RunMinecreftServer.sh
#Server will stop as EULA is not accepted
sed -i '/^eula/s/false/true/' eula.txt
#Will accept the eula
~/RunMinecreftServer.sh
```

### Removing a user from Ubuntu Gnome Login Menu

```shell
cd /var/lib/AccountsService/users
#edit file for user and set SystemAccount=true
```


### Nvidia Drivers: the easy way

```shell
ubuntu-drivers devices
sudo ubuntu-drivers autoinstall
```

### Gaming is forever

https://wiki.winehq.org/Ubuntu

sudo dpkg --add-architecture i386
cd ~/Downloads
wget -nc https://dl.winehq.org/wine-builds/winehq.key
sudo apt-key add winehq.key
sudo apt-add-repository 'deb https://dl.winehq.org/wine-builds/ubuntu/ eoan main'

sudo apt update
sudo apt install --install-recommends winehq-staging winbind winetricks


WINEPREFIX="/home/william/WineInstall/BNet" winetricks

WINEPREFIX="/home/william/WineInstall/BNet" wine64 ~/Downloads/Installer/Diablo/Battle.net-Setup.exe

```shell
#Steam Package
sudo dpkg --add-architecture i386
sudo apt update
sudo apt install wget gdebi-core libgl1-mesa-dri:i386 libgl1-mesa-glx:i386

cd ~/Downloads/Installer
wget http://media.steampowered.com/client/installer/steam.deb

sudo gdebi steam.deb


wget -qO- https://dl.winehq.org/wine-builds/winehq.key | sudo apt-key add -
sudo apt-add-repository 'deb http://dl.winehq.org/wine-builds/ubuntu/ bionic main'
sudo apt-get install --install-recommends winehq-stable


WINEPREFIX="/home/william/WineInstall/WOW" winecfg

WINEPREFIX="/home/william/WineInstall/WOW" wine /home/william/Downloads/Installer/WOW-NOSTALGEEK/WoW.exe -opengl
WINEPREFIX="/home/william/WineInstall/WOW" wine /home/william/Downloads/Installer/WOW-NOSTALGEEK/world_of_warcraft_wow_cartographe_1_07.exe -opengl

echo '#!/usr/bin/env xdg-open' > ~/Desktop/WoW.desktop
echo "[Desktop Entry]" >> ~/Desktop/WoW.desktop
echo "Version=1.0" >> ~/Desktop/WoW.desktop
echo "Type=Application" >> ~/Desktop/WoW.desktop
echo "Terminal=false" >> ~/Desktop/WoW.desktop
echo 'Exec=WINEPREFIX="/home/william/RunWoW.sh' >> ~/Desktop/WoW.desktop
echo "Name=WoW" >> ~/Desktop/WoW.desktop
echo "Comment=NostalGeek Vanilla" >> ~/Desktop/WoW.desktop
echo "Icon=/home/william/Downloads/Installer/WOW-NOSTALGEEK/WoW-icon.png" >> ~/Desktop/WoW.desktop
```

### Installing Docker CE (Community Edition)

```shell
#from https://www.itzgeek.com/how-tos/linux/ubuntu-how-tos/how-to-install-docker-on-ubuntu-18-04-lts-bionic-beaver.html
sudo apt update
sudo apt install -y apt-transport-https software-properties-common ca-certificates curl wget
wget https://download.docker.com/linux/ubuntu/gpg 
sudo apt-key add gpg

echo "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable" | sudo tee /etc/apt/sources.list.d/docker.list
sudo apt update

sudo apt-cache policy docker-ce #just to check version
sudo apt install -y docker-ce
sudo systemctl start docker
sudo systemctl enable docker

sudo usermod -aG docker william
```

```shell
# Install the source repository
echo 'deb https://crawl.develz.org/debian crawl 0.22' | sudo tee -a /etc/apt/sources.list
# Install the DCSS signing key
wget https://crawl.develz.org/debian/pubkey -O - | sudo apt-key add -
# update your package list
sudo apt-get update
# install console version
sudo apt-get install crawl
# install tiles version
sudo apt-get install crawl-tiles
```

### install ssh daemon
```shell
sudo apt update
sudo apt install openssh-server
sudo systemctl status ssh
```

### systemd start service



sudo vi /etc/java-8-openjdk/accessibility.properties
#need to comment the assistive technology module there
java -jar squirrel-sql-4.0.0-standard.jar



sudo apt install openjdk-8-jre





sed -n '/^-- Current Database: `auth`/,/^-- Current Database: `/p' /media/william/Transport/Trinity/TCdump.sql > authdump.sql

sed -n '/^-- Current Database: `characters`/,/^-- Current Database: `/p' /media/william/Transport/Trinity/TCdump.sql > chardump.sql

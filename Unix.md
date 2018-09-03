# Offending TCP Blocker
```shell
netstat -Aan | grep 3141
f100060002134398 tcp4       0      0  127.0.0.1.3141     127.0.0.1.64501    CLOSE_WAIT
f100060002282b98 tcp        0      0  127.0.0.1.64501    127.0.0.1.3141     FIN_WAIT_2
f1000600024cd398 tcp        0      0  *.3141             *.*                LISTEN
f100060001f36398 tcp4       0      0  10.75.1.147.3141   10.75.2.107.4268   ESTABLISHED

rmsock f1000600024cd398 tcpcb
The socket 0x24cd008 is being held by proccess 1675400 (java).

ps -ef|grep 1675400

```

# Allow greater size for vi file under AIX

```shell
export EXINIT="set ll=20000000"
export EXINIT="set ll=20000000 dir=/tmp"
```
# User & Group Manipulation

```bash
groupadd mynewgroup #Create a new group
usermod -a -G examplegroup exampleusername # add exampleusername to the group examplegroup
```

# Copy vs rsync 

```bash
rsync -avhW --no-compress --progress /src/ /dst/
#Here's my reasoning:
# -a is for archive, which preserves ownership, permissions etc.
# -v is for verbose, so I can see what's happening (optional)
# -h is for human-readable, so the transfer rate and file sizes are easier to read (optional)
# -W is for copying whole files only, without delta-xfer algorithm which should reduce CPU load
# --no-compress as there's no lack of bandwidth between local devices
# --progress so I can see the progress of large files (optional) 
```

# Prevent cp to ask for overwrite in script

By default cp is aliased as cp -i and -f is not preventing -i so Jenkins scripts could fail,
you can force to use the not aliased version by running \cp instead of cp.


# Reset password AIX

```bash
passwd <UserName>
chuser unsuccessful_login_count=0 <UserName>
```
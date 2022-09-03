# OverTheWire - Bandit - Solutions

**My solutions to the [Bandit wargame](https://overthewire.org/wargames/bandit/).**
<br /><br />

## Brief

Solved using WSL:
 ```bash
$ uname -rom && lsb_release -d
5.10.102.1-microsoft-standard-WSL2 x86_64 GNU/Linux
Description:    Ubuntu 20.04.4 LTS
 ```

**Connecting:**
```bash
$ ssh banditX@bandit.labs.overthewire.org -p 2220    # X = level number
```
**or**
```bash
$ ssh banditX@localhost   # from within bandit machine. X = level number.
```
<br />

## [Bandit0](https://overthewire.org/wargames/bandit/bandit0.html)
**Level Goal**<br/>
``
The goal of this level is for you to log into the game using SSH.
The host to which you need to connect is
bandit.labs.overthewire.org, on port 2220.
The username is bandit0 and the password is bandit0. Once
logged in, go to the Level 1 page to find out how to beat Level
1.
``

**Solution**
```bash
$ ssh bandit0@bandit.labs.overthewire.org -p 2220
bandit0                                              # bandit0's password .
```
<br />


## [Bandit1](https://overthewire.org/wargames/bandit/bandit1.html)
**Level Goal**<br/>
``
The password for the next level is stored in a file called
readme located in the home directory. Use this password to log
into bandit1 using SSH. Whenever you find a password for a level,
use SSH (on port 2220) to log into that level and continue the game.
``

**Solution**
```bash
$ ssh bandit0@bandit.labs.overthewire.org -p 2220

bandit0@bandit:~$ cat ~/readme
boJ9jbbUNNfktd78OOpsqOltutMc3MY1                     # bandit1's passsword.
```
<br />


## [Bandit2](https://overthewire.org/wargames/bandit/bandit2.html)
**Level Goal**<br/>
``
The password for the next level is stored in a file called -
located in the home directory
``

**Solution**
```bash
$ ssh bandit1@bandit.labs.overthewire.org -p 2220

bandit1@bandit:~$ cat ~/-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9                     # bandit2's passsword.
```
<br />


## [Bandit3](https://overthewire.org/wargames/bandit/bandit3.html)
**Level Goal**<br/>
``
The password for the next level is stored in a file called spaces
in this filename located in the home directory
``

**Solution**
```bash
$ ssh bandit2@bandit.labs.overthewire.org -p 2220

bandit2@bandit:~$ cat ~/'spaces in this filename'
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK                     # bandit3's password.
```
<br />


## [Bandit4](https://overthewire.org/wargames/bandit/bandit4.html)
**Level Goal**<br/>
``
The password for the next level is stored in a hidden file in the
inhere directory.
``

**Solution**
```bash
$ ssh bandit3@bandit.labs.overthewire.org -p 2220

bandit3@bandit:~$ ls -a ~/inhere
.  ..  .hidden
bandit3@bandit:~$ cat ~/inhere/.hidden
pIwrPrtPN36QITSp3EQaw936yaFoFgAB                     # bandit4's password.
```
<br />


## [Bandit5](https://overthewire.org/wargames/bandit/bandit5.html)
**Level Goal**<br/>
``
The password for the next level is stored in the only human-readable
file in the inhere directory. Tip: if your terminal is messed
up, try the "reset" command.
``

**Solution**
```bash
$ ssh bandit4@bandit.labs.overthewire.org -p 2220

bandit4@bandit:~$ file ~/inhere/*
/home/bandit4/inhere/-file00: data
/home/bandit4/inhere/-file01: data
/home/bandit4/inhere/-file02: data
/home/bandit4/inhere/-file03: data
/home/bandit4/inhere/-file04: data
/home/bandit4/inhere/-file05: data
/home/bandit4/inhere/-file06: data
/home/bandit4/inhere/-file07: ASCII text
/home/bandit4/inhere/-file08: data
/home/bandit4/inhere/-file09: data

bandit4@bandit:~$ cat ~/inhere/-file07
koReBOKuIDDepwhWk7jZC0RTdopnAYKh                     # bandit5's password.
```
<br />


## [Bandit6](https://overthewire.org/wargames/bandit/bandit6.html)
**Level Goal**<br/>
``
The password for the next level is stored in a file somewhere under
the inhere directory and has all of the following properties:
``

**Solution**
```bash
$ ssh bandit5@bandit.labs.overthewire.org -p 2220

bandit5@bandit:~$ find ~/inhere -size 1033c
/home/bandit5/inhere/maybehere07/.file2

bandit5@bandit:~$ file ~/inhere/maybehere07/.file2
/home/bandit5/inhere/maybehere07/.file2: ASCII text, with very long lines

bandit5@bandit:~$ cat ~/inhere/maybehere07/.file2 | grep . 
DXjZPULLxYr17uwoI01bNLQbtFemEgo7                     # bandit6's password.
```
<br />


## [Bandit7](https://overthewire.org/wargames/bandit/bandit7.html)
**Level Goal**<br/>
``
The password for the next level is stored somewhere on the
server and has all of the following properties:
``

**Solution**
```bash
$ ssh bandit6@bandit.labs.overthewire.org -p 2220

# suppress permisison errors by redirecting stderr to null.
bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c -print 2>/dev/null
/var/lib/dpkg/info/bandit7.password

bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs                     # bandit7's password.
```
<br />


## [Bandit8](https://overthewire.org/wargames/bandit/bandit8.html)
**Level Goal**<br/>
``
The password for the next level is stored in the file data.txt
next to the word millionth
``

**Solution**
```bash
$ ssh bandit7@bandit.labs.overthewire.org -p 2220

bandit7@bandit:~$ cat ~/data.txt | grep millionth
millionth       cvX2JJa4CFALtqS87jk27qwqGhBM9plV     # bandit8's password.
```
<br />


## [Bandit9](https://overthewire.org/wargames/bandit/bandit9.html)
**Level Goal**<br/>
``
The password for the next level is stored in the file data.txt
and is the only line of text that occurs only once
``

**Solution**
```bash
$ ssh bandit8@bandit.labs.overthewire.org -p 2220

bandit8@bandit:~$ sort ~/data.txt | uniq -u
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR                     # bandit9's password.
```
<br />


## [Bandit10](https://overthewire.org/wargames/bandit/bandit10.html)
**Level Goal**<br/>
``
The password for the next level is stored in the file data.txt
in one of the few human-readable strings, preceded by several '='
characters.
``

**Solution**
```
$ ssh bandit9@bandit.labs.overthewire.org -p 2220

# readable strings, preceded by several '=' characters..
bandit9@bandit:~$ strings ~/data.txt | grep -E '==+' 
========== the*2i"4
========== password
Z)========== is
&========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk         # bandit10's password.
```
<br />


## [Bandit11](https://overthewire.org/wargames/bandit/bandit11.html)
**Level Goal**<br/>
``
The password for the next level is stored in the file data.txt,
which contains base64 encoded data
``

**Solution**
```bash
$ ssh bandit10@bandit.labs.overthewire.org -p 2220

bandit10@bandit:~$ base64 -d ~/data.txt 
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR     # bandit11's password.
```
<br />


## [Bandit12](https://overthewire.org/wargames/bandit/bandit12.html)
**Level Goal**<br/>
``
The password for the next level is stored in the file data.txt,
where all lowercase (a-z) and uppercase (A-Z) letters have been
rotated by 13 positions
``

**Solution**
```bash
$ ssh bandit11@bandit.labs.overthewire.org -p 2220

# A little help from python
bandit11@bandit:~$ python -c "print 'a -> ' + chr(ord('a') + 13)"
a -> n

# Hence we deduce the substitution:
# a-z  ->  n-za-m
# A-Z  ->  N-ZA-M
bandit11@bandit:~$ cat ~/data.txt | tr 'a-zA-Z' 'n-za-mN-ZA-M'
The password is 5Te8Y4drgCRfCx8ugdwuEX8KFC6k2EUu     # bandit12's password.
```
<br />


## [Bandit13](https://overthewire.org/wargames/bandit/bandit13.html)
**Level Goal**<br/>
``
The password for the next level is stored in the file data.txt,
which is a hexdump of a file that has been repeatedly compressed.
For this level it may be useful to create a directory under /tmp in
which you can work using mkdir. For example: mkdir /tmp/myname123.
Then copy the datafile using cp, and rename it using mv (read the
manpages!)
``

**Solution**
```bash
$ ssh bandit12@bandit.labs.overthewire.org -p 2220

bandit12@bandit:~$ mkdir /tmp/bt12
bandit12@bandit:~$ cp ~/data.txt /tmp/bt12
bandit12@bandit:~$ cd /tmp/bt12

bandit12@bandit:/tmp/bt12$ xxd -r data.txt > data
bandit12@bandit:/tmp/bt12$ file data
data: gzip compressed data, was "data2.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix

bandit12@bandit:/tmp/bt12$ gzip -dc data | file -
/dev/stdin: bzip2 compressed data, block size = 900k

bandit12@bandit:/tmp/bt12$ gzip -dc data | bzip2 -dc | file -
/dev/stdin: gzip compressed data, was "data4.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix

bandit12@bandit:/tmp/bt12$ gzip -dc data | bzip2 -dc | gzip -dc | file -
/dev/stdin: POSIX tar archive (GNU)

bandit12@bandit:/tmp/bt12$ gzip -dc data | bzip2 -dc | gzip -dc | tar -xO | file -
/dev/stdin: POSIX tar archive (GNU)

bandit12@bandit:/tmp/bt12$ gzip -dc data | bzip2 -dc | gzip -dc | tar -xO | tar -xO | file -
/dev/stdin: bzip2 compressed data, block size = 900k

bandit12@bandit:/tmp/bt12$ gzip -dc data | bzip2 -dc | gzip -dc | tar -xO | tar -xO | bzip2 -dc | file -
/dev/stdin: POSIX tar archive (GNU)

bandit12@bandit:/tmp/bt12$ gzip -dc data | bzip2 -dc | gzip -dc | tar -xO | tar -xO | bzip2 -dc | tar -xO | file -
/dev/stdin: gzip compressed data, was "data9.bin", last modified: Thu May  7 18:14:30 2020, max compression, from Unix

bandit12@bandit:/tmp/bt12$ gzip -dc data | bzip2 -dc | gzip -dc | tar -xO | tar -xO | bzip2 -dc | tar -xO | gzip -dc | file -
/dev/stdin: ASCII text

bandit12@bandit:/tmp/bt12$ gzip -dc data | bzip2 -dc | gzip -dc | tar -xO | tar -xO | bzip2 -dc | tar -xO | gzip -dc 
The password is 8ZjyCRiBWFYkneahHwxCv3wb2a1ORpYL     # bandit13's password.

bandit12@bandit:~$ rm -rf /tmp/bt12
```
<br />


## [Bandit14](https://overthewire.org/wargames/bandit/bandit14.html)
**Level Goal**<br/>
``
The password for the next level is stored in
/etc/bandit_pass/bandit14 and can only be read by user
bandit14. For this level, you don't get the next password, but you
get a private SSH key that can be used to log into the next level.
Note: localhost is a hostname that refers to the machine
you are working on
``

**Solution**
```bash
$ ssh bandit13@bandit.labs.overthewire.org -p 2220

bandit13@bandit:~$ ls
sshkey.private

bandit13@bandit:~$ ssh -i sshkey.private bandit14@localhost

bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e                     # bandit14's password.
```
<br />


## [Bandit15](https://overthewire.org/wargames/bandit/bandit15.html)
**Level Goal**<br/>
``
The password for the next level can be retrieved by submitting the
password of the current level to port 30000 on localhost.
``

**Solution**
```bash
$ ssh bandit14@bandit.labs.overthewire.org -p 2220

# nc can be replaced by telnet
bandit14@bandit:~$ nc localhost 30000
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e                     # submitted bandit14's password.
Correct!
BfMYroe26WYalil77FoDi9qh59eK5xNr                     # bandit15's password.
```
<br />


## [Bandit16](https://overthewire.org/wargames/bandit/bandit16.html)
**Level Goal**<br/>
``
The password for the next level can be retrieved by submitting the
password of the current level to port 30001 on localhost using
SSL encryption.
``

**Solution**
```bash
$ ssh bandit15@bandit.labs.overthewire.org -p 2220

bandit15@bandit:~$ openssl s_client -connect localhost:30001
# blah blah..
BfMYroe26WYalil77FoDi9qh59eK5xNr                     # submitted bandit15's password.
Correct!
cluFn7wTiGryunymYOu4RcffSxQluehd                     # bandit16's password.
```
<br />


## [Bandit17](https://overthewire.org/wargames/bandit/bandit17.html)
**Level Goal**<br/>
``
The credentials for the next level can be retrieved by submitting the
password of the current level to a port on localhost in the range
31000 to 32000. First find out which of these ports have a server
listening on them. Then find out which of those speak SSL and which
don't. There is only 1 server that will give the next credentials, the
others will simply send back to you whatever you send to it.
``

**Solution**
```bash
$ ssh bandit16@bandit.labs.overthewire.org -p 2220

# use -sV for version detection and --version-intensity 1 is enough for ssl.
bandit16@bandit:~$ nmap -p 31000-32000 -sV --version-intensity 1 localhost

Starting Nmap 7.40 ( https://nmap.org ) at 2022-08-07 21:13 CEST
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00032s latency).
Not shown: 996 closed ports
PORT      STATE    SERVICE     VERSION
31046/tcp open     unknown
31518/tcp filtered unknown
31691/tcp open     unknown
31790/tcp open     ssl/unknown     # <--- our target.
31960/tcp open     unknown
# blah blah..

bandit16@bandit:~$ openssl s_client -connect localhost:31790
# blah blah..
cluFn7wTiGryunymYOu4RcffSxQluehd
Correct!
# [RSA KEY], copied to clipboard, pasted on host.

$ chmod 600 sshkey.private   # owner access only.
```
<br />


## [Bandit18](https://overthewire.org/wargames/bandit/bandit18.html)
**Level Goal**<br/>
``
There are 2 files in the homedirectory: passwords.old and
passwords.new. The password for the next level is in
passwords.new and is the only line that has been changed between
passwords.old and passwords.new
``

**Solution**
```bash
$ ssh bandit17@bandit.labs.overthewire.org -p 2220

bandit17@bandit:~$ diff passwords.old passwords.new | grep '>'
> kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd                   # bandit18's password.
```
<br />


## [Bandit19](https://overthewire.org/wargames/bandit/bandit19.html)
**Level Goal**<br/>
``
The password for the next level is stored in a file readme in
the homedirectory. Unfortunately, someone has modified .bashrc
to log you out when you log in with SSH.
``

**Solution**
```bash
# ssh with inline command because of auto logout by .bashrc.
$ ssh bandit18@bandit.labs.overthewire.org -p 2220 'cat readme'

bandit18@bandit.labs.overthewire.org s password:
IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x                     # bandit19's password.
```
<br />


## [Bandit20](https://overthewire.org/wargames/bandit/bandit20.html)
**Level Goal**<br/>
``
To gain access to the next level, you should use the setuid binary
in the homedirectory. Execute it without arguments to find out how
to use it. The password for this level can be found in the usual
place (/etc/bandit_pass), after you have used the setuid binary.
``

**Solution**
```bash
$ ssh bandit19@bandit.labs.overthewire.org -p 2220

# Can't access as bandit19
bandit19@bandit:~$ cat /etc/bandit_pass/bandit20
cat: /etc/bandit_pass/bandit20: Permission denied

# bandit20 is owner, with read access.
bandit19@bandit:~$ stat -c "%U %u %A" /etc/bandit_pass/bandit20
bandit20 11020 -r--------

# find bandit20-do's usage.
bandit19@bandit:~$ ./bandit20-do
Run a command as another user.
  Example: ./bandit20-do id

# Get the password
bandit19@bandit:~$ ./bandit20-do cat /etc/bandit_pass/bandit20
GbKksEFF4yrVs6il55v6gwY5aVje5f0j                     # bandit20's password.
```
<br />


## [Bandit21](https://overthewire.org/wargames/bandit/bandit21.html)
**Level Goal**<br/>
``
There is a setuid binary in the homedirectory that does the
following: it makes a connection to localhost on the port you
specify as a commandline argument. It then reads a line of text from
the connection and compares it to the password in the previous level
(bandit20). If the password is correct, it will transmit the
password for the next level (bandit21).
``

**Solution**
```bash
$ ssh bandit20@bandit.labs.overthewire.org -p 2220

# find suconnect's usage.
bandit20@bandit:~$ ./suconnect
Usage: ./suconnect <portnumber>
This program will connect to the given port on localhost using TCP. If it receives the correct password from the other side, the next password is transmitted back.

# create first window
bandit20@bandit:~$ tmux new -s "A"
bandit20@bandit:~$ nc -lvp 1234
listening on [any] 1234 ...

# ctrl+b, d to detach. create another window:
bandit20@bandit:~$ tmux new -s "B"
bandit20@bandit:~$ ./suconnect 1234

# ctrl+b, s, choose 'A' window & paste bandit 20 password:
bandit20@bandit:~$ nc -lvp 1234
listening on [any] 1234 ...
connect to [127.0.0.1] from localhost [127.0.0.1] 58114
GbKksEFF4yrVs6il55v6gwY5aVje5f0j                     # bandit20's pasted password.
gE269g2h3mw3pwgrj0Ha9Uoqen1c9DGr                     # bandit21's password.

# ctrl+b, s, choose 'B' window:
bandit20@bandit:~$ ./suconnect 1234
Read: GbKksEFF4yrVs6il55v6gwY5aVje5f0j
Password matches, sending next password

# killing tmux:
bandit20@bandit:~$ tmux ls
A: 1 windows (created Thu Aug 11 23:02:31 2022) [120x29]
B: 1 windows (created Thu Aug 11 23:03:19 2022) [120x29]
bandit20@bandit:~$ tmux kill-server
bandit20@bandit:~$ tmux ls
no server running on /tmp/tmux-11020/default
```
<br />


## [Bandit22](https://overthewire.org/wargames/bandit/bandit22.html)
**Level Goal**<br/>
``
A program is running automatically at regular intervals from
cron, the time-based job scheduler. Look in /etc/cron.d/ for
the configuration and see what command is being executed.
``

**Solution**
```bash
$ ssh bandit21@bandit.labs.overthewire.org -p 2220

bandit21@bandit:~$ file /etc/cron.d/*
/etc/cron.d/cronjob_bandit15_root: ASCII text
/etc/cron.d/cronjob_bandit17_root: ASCII text
/etc/cron.d/cronjob_bandit22:      ASCII text
/etc/cron.d/cronjob_bandit23:      ASCII text
/etc/cron.d/cronjob_bandit24:      ASCII text
/etc/cron.d/cronjob_bandit25_root: ASCII text

bandit21@bandit:~$ cat /etc/cron.d/cronjob_bandit22
@reboot bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null
* * * * * bandit22 /usr/bin/cronjob_bandit22.sh &> /dev/null

bandit21@bandit:~$ cat /usr/bin/cronjob_bandit22.sh
#!/bin/bash
chmod 644 /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
cat /etc/bandit_pass/bandit22 > /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv

bandit21@bandit:~$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
Yk7owGAcWjwMVRwrTesJEwB7WVOiILLI                     # bandit22's password.
```
<br />


## [Bandit23](https://overthewire.org/wargames/bandit/bandit23.html)
**Level Goal**<br/>
``
A program is running automatically at regular intervals from
cron, the time-based job scheduler. Look in /etc/cron.d/ for
the configuration and see what command is being executed.
``

**Solution**
```bash
$ ssh bandit22@bandit.labs.overthewire.org -p 2220

bandit22@bandit:~$ file /etc/cron.d/*
/etc/cron.d/cronjob_bandit15_root: ASCII text
/etc/cron.d/cronjob_bandit17_root: ASCII text
/etc/cron.d/cronjob_bandit22:      ASCII text
/etc/cron.d/cronjob_bandit23:      ASCII text
/etc/cron.d/cronjob_bandit24:      ASCII text
/etc/cron.d/cronjob_bandit25_root: ASCII text

bandit22@bandit:~$ cat /etc/cron.d/cronjob_bandit23
@reboot bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null
* * * * * bandit23 /usr/bin/cronjob_bandit23.sh  &> /dev/null

bandit22@bandit:~$ cat /usr/bin/cronjob_bandit23.sh
#!/bin/bash
myname=$(whoami)
mytarget=$(echo I am user $myname | md5sum | cut -d ' ' -f 1)
echo "Copying passwordfile /etc/bandit_pass/$myname to /tmp/$mytarget"
cat /etc/bandit_pass/$myname > /tmp/$mytarget

# The following line was automatically suggested by github copilot before I even tried to understand the script above. What a time to be alive.
bandit22@bandit:~$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349

# Anyway, executing /usr/bin/cronjob_bandit23.sh will yield the same result:
bandit22@bandit:~$ /usr/bin/cronjob_bandit23.sh
Copying passwordfile /etc/bandit_pass/bandit22 to /tmp/8169b67bd894ddbb4412f91573b38db3

# so we just have to read the generated file:
bandit22@bandit:~$ cat /tmp/8ca319486bfbbc3663ea0fbe81326349
jc1udXuA1tiHqjIsL8yaapX5XIAI6i0n                     # bandit23's password.
```
<br />


## [Bandit24](https://overthewire.org/wargames/bandit/bandit24.html)
**Level Goal**<br/>
``
A program is running automatically at regular intervals from
cron, the time-based job scheduler. Look in /etc/cron.d/ for
the configuration and see what command is being executed.
``

**Solution**
```bash
$ ssh bandit23@bandit.labs.overthewire.org -p 2220

bandit23@bandit:~$ file /etc/cron.d/*
/etc/cron.d/cronjob_bandit15_root: ASCII text
/etc/cron.d/cronjob_bandit17_root: ASCII text
/etc/cron.d/cronjob_bandit22:      ASCII text
/etc/cron.d/cronjob_bandit23:      ASCII text
/etc/cron.d/cronjob_bandit24:      ASCII text
/etc/cron.d/cronjob_bandit25_root: ASCII text

bandit23@bandit:~$ cat /etc/cron.d/cronjob_bandit24
@reboot bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null
* * * * * bandit24 /usr/bin/cronjob_bandit24.sh &> /dev/null

bandit23@bandit:~$ cat bandit24 /usr/bin/cronjob_bandit24.sh
cat: bandit24: No such file or directory
#!/bin/bash
myname=$(whoami)
cd /var/spool/$myname
echo "Executing and deleting all scripts in /var/spool/$myname:"
for i in * .*;
do
    if [ "$i" != "." -a "$i" != ".." ];
    then
        echo "Handling $i"
        owner="$(stat --format "%U" ./$i)"
        if [ "${owner}" = "bandit23" ]; then
            timeout -s 9 60 ./$i
        fi
        rm -f ./$i
    fi
done

# we need to create our own script and copy it to /var/spool/bandit24.
bandit23@bandit:~$ mkdir /tmp/12082022
bandit23@bandit:~$ cd /tmp/12082022
bandit23@bandit:/tmp/12082022$ touch password
bandit23@bandit:/tmp/12082022$ chmod 666 password     # rw for all
bandit23@bandit:/tmp/12082022$ vim script.sh
```

```bash
#!/bin/bash
cat /etc/bandit_pass/bandit24 > /tmp/12082022/password
```

```bash
bandit23@bandit:/tmp/12082022$ chmod 777 script.sh    # rwx for all
bandit23@bandit:/tmp/12082022$ cp script.sh /var/spool/bandit24/

# script will be executed after 60 seconds..
bandit23@bandit:/tmp/12082022$ cat password
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ                     # bandit24's password.

bandit23@bandit:~$ rm -rf /tmp/12082022
```
<br />


## [Bandit25](https://overthewire.org/wargames/bandit/bandit25.html)
**Level Goal**<br/>
``
A daemon is listening on port 30002 and will give you the password for
bandit25 if given the password for bandit24 and a secret numeric 4-digit pincode.
There is no way to retrieve the pincode except by going through all of the 10000
combinations, called brute-forcing.
``

**Solution**
```bash
$ ssh bandit24@bandit.labs.overthewire.org -p 2220

bandit24@bandit:~$ mkdir /tmp/13082022
bandit24@bandit:~$ cd /tmp/13082022
bandit24@bandit:/tmp/13082022$ vim script.sh
```

```bash
#!/bin/bash

# generate input file
for i in {0..9999}
do
    echo $i | awk '{printf "UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ %04d\n", $0}' >> input.txt
done

# nc the file
nc localhost 30002 < input.txt | grep -v -e "Wrong"
```

```bash
bandit24@bandit:/tmp/13082022$ chmod +x ./script.sh
bandit24@bandit:/tmp/13082022$ ./script.sh
I am the pincode checker for user bandit25. Please enter the password for user bandit24 and the secret pincode on a single line, separated by a space.
Correct!
The password of user bandit25 is uNG9O58gUE7snukf3bvZ0rxhtnjzSGzG

Exiting.

bandit24@bandit:~$ rm -rf /tmp/13082022
```
<br />


## [Bandit26](https://overthewire.org/wargames/bandit/bandit26.html)
**Level Goal**<br/>
``
Logging in to bandit26 from bandit25 should be fairly easy...
The shell for user bandit26 is not /bin/bash, but something else.
Find out what it is, how it works and how to break out of it.
``

**Solution**
```bash
$ ssh bandit25@bandit.labs.overthewire.org -p 2220

# List available shells
bandit25@bandit:~$ cat /etc/shells
# /etc/shells: valid login shells
/bin/sh
/bin/dash
/bin/bash
/bin/rbash
/usr/bin/screen
/usr/bin/tmux
/usr/bin/showtext

# # find bandit25's login shell.
bandit25@bandit:~$ cat /etc/passwd | grep bandit26
bandit26:x:11026:11026:bandit level 26:/home/bandit26:/usr/bin/showtext

bandit25@bandit:~$ cat /usr/bin/showtext
#!/bin/sh
export TERM=linux
more ~/text.txt
exit 0
```

Upon ssh bandit26, the connection is closed, not before printing bandit26 logo from text.txt by `more`. We will resize terminal to smaller screen and then:

```bash
bandit25@bandit:~$ ls
bandit26.sshkey

bandit25@bandit:~$ ssh -i bandit26.sshkey bandit26@localhost
```

Now that the connection is not closed yet, we will press `v` to enter `vi`. Then, in command mode, we will type `:r /etc/bandit_pass/bandit26` followed by enter. We will receive bandit26's password: `5czgV9L3Xx8JPOyRbXh6lQbmIOWvPT6Z`.
<br />


## [Bandit27](https://overthewire.org/wargames/bandit/bandit27.html)
**Level Goal**<br/>
``
Good job getting a shell! Now hurry and grab the password for bandit27!
``

**Solution**
```bash
# login to bandit25 first
$ ssh bandit25@bandit.labs.overthewire.org -p 2220

# similar to bandit20, will want to invoke /home/bandit27-do cat /etc/bandit_pass/bandit27
# Enter vi by doing the same trick as in bandit 26.
$ ssh -i bandit26.sshkey bandit26@localhost   # with small terminal, press v to enter vi.

# After entering vi, resize to normal and set the default bash within command mode.
:set shell=/bin/bash 
:shell    # open default shell.

# list bandit26's files
bandit26@bandit:~$ ls
bandit27-do  text.txt

bandit26@bandit:~$ ./bandit27-do cat /etc/bandit_pass/bandit27
3ba3118a22e93127a4ed485be72ef5ea                     # bandit27's password.
```
<br />


## [Bandit28](https://overthewire.org/wargames/bandit/bandit28.html)
**Level Goal**<br/>
``
There is a git repository at ssh://[bandit27-git@localhost]/home/bandit27-git/repo. The password for the user bandit27-git is the same as for the user bandit27.
``

**Solution**
```bash
$ ssh bandit27@bandit.labs.overthewire.org -p 2220

# clone the repo.
bandit27@bandit:~$ mkdir /tmp/13082022
bandit27@bandit:~$ cd /tmp/13082022
bandit27@bandit:/tmp/13082022$ git clone ssh://bandit27-git@localhost/home/bandit27-git/repo
```
```
Cloning into 'repo'...
...
bandit27-git@localhost's password:
remote: Counting objects: 3, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0)
Receiving objects: 100% (3/3), done.
```
```bash
# read bandit28's password.
bandit27@bandit:/tmp/13082022$ ls repo
README
bandit27@bandit:/tmp/13082022$ cat repo/README
The password to the next level is: 0ef186ac70e04ea33b4c1853d2526fa2

bandit27@bandit:~$ rm -rf /tmp/13082022
```
<br />


## [Bandit29](https://overthewire.org/wargames/bandit/bandit29.html)
**Level Goal**<br/>
``
There is a git repository at ssh://[bandit28-git@localhost]/home/bandit28-git/repo. The password for the user bandit28-git is the same as for the user bandit28.
``

**Solution**
```bash
$ ssh bandit28@bandit.labs.overthewire.org -p 2220

bandit28@bandit:~$ mkdir /tmp/13082022
bandit28@bandit:~$ cd /tmp/13082022
bandit28@bandit:/tmp/13082022$ git clone ssh://bandit28-git@localhost/home/bandit28-git/repo
```
```
Cloning into 'repo'...
...
bandit28-git@localhost's password:
remote: Counting objects: 9, done.
remote: Compressing objects: 100% (6/6), done.
remote: Total 9 (delta 2), reused 0 (delta 0)
Receiving objects: 100% (9/9), done.
Resolving deltas: 100% (2/2), done.
```
```bash
bandit28@bandit:/tmp/13082022$ cd repo
bandit28@bandit:/tmp/13082022/repo$ git log
```
```
commit edd935d60906b33f0619605abd1689808ccdd5ee
Author: Morla Porla <morla@overthewire.org>
Date:   Thu May 7 20:14:49 2020 +0200

    fix info leak

commit c086d11a00c0648d095d04c089786efef5e01264
Author: Morla Porla <morla@overthewire.org>
Date:   Thu May 7 20:14:49 2020 +0200

    add missing data

commit de2ebe2d5fd1598cd547f4d56247e053be3fdc38
Author: Ben Dover <noone@overthewire.org>
Date:   Thu May 7 20:14:49 2020 +0200

    initial commit of README.md
```
```bash
bandit28@bandit:/tmp/13082022/repo$ git checkout c086d11a00c0648d095d04c089786efef5e01264
Previous HEAD position was de2ebe2... initial commit of README.md
HEAD is now at c086d11... add missing data

bandit28@bandit:/tmp/13082022/repo$ cat README.md
# Bandit Notes
Some notes for level29 of bandit.

## credentials

- username: bandit29
- password: bbc96594b4e001778eee9975372716b2         # bandit29's password.

bandit27@bandit:~$ rm -rf /tmp/13082022
```
<br />


## [Bandit30](https://overthewire.org/wargames/bandit/bandit30.html)
**Level Goal**<br/>
``
There is a git repository at ssh://[bandit29-git@localhost]/home/bandit29-git/repo. The password for the user bandit29-git is the same as for the user bandit29.
``

**Solution**
```bash
$ ssh bandit29@bandit.labs.overthewire.org -p 2220

bandit29@bandit:~$ mkdir /tmp/13082022 && cd /tmp/13082022
bandit29@bandit:/tmp/13082022$ git clone ssh://bandit29-git@localhost/home/bandit29-git/repo
```
```
Cloning into 'repo'...
...
bandit29-git@localhost's password:
remote: Counting objects: 16, done.
remote: Compressing objects: 100% (11/11), done.
remote: Total 16 (delta 2), reused 0 (delta 0)
Receiving objects: 100% (16/16), done.
Resolving deltas: 100% (2/2), done.
```
```bash
bandit29@bandit:/tmp/13082022$ cd repo
bandit29@bandit:/tmp/13082022/repo$ ls
README.md
bandit29@bandit:/tmp/13082022/repo$ cat README.md
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: <no passwords in production!>

# list remote branches
bandit29@bandit:/tmp/13082022/repo$ git branch -r
  origin/HEAD -> origin/master
  origin/dev
  origin/master
  origin/sploits-dev

bandit29@bandit:/tmp/13082022/repo$ git checkout origin/dev
Note: checking out 'origin/dev'.
...

bandit29@bandit:/tmp/13082022/repo$ ls
code  README.md
bandit29@bandit:/tmp/13082022/repo$ cat README.md
# Bandit Notes
Some notes for bandit30 of bandit.

## credentials

- username: bandit30
- password: 5b90576bedb2cc04c86a9e924ce42faf                  # bandit30's password.

bandit29@bandit:/tmp$ cd ~/
bandit29@bandit:~$ rm -rf /tmp/13082022
```
<br />


## [Bandit31](https://overthewire.org/wargames/bandit/bandit31.html)
**Level Goal**<br/>
``
There is a git repository at ssh://[bandit30-git@localhost]/home/bandit30-git/repo. The password for the user bandit30-git is the same as for the user bandit30.
``

**Solution**
```bash
$ ssh bandit30@bandit.labs.overthewire.org -p 2220

bandit30@bandit:~$ mkdir /tmp/13082022 && cd /tmp/13082022
bandit30@bandit:/tmp/13082022$ git clone ssh://bandit30-git@localhost/home/bandit30-git/repo && cd repo
Cloning into 'repo'...

bandit30@bandit:/tmp/13082022/repo$ git tag
secret

bandit30@bandit:/tmp/13082022/repo$ git show secret
47e603bb428404d265f59c42920d81e5                  # bandit31's password.

bandit30@bandit:/tmp/13082022/repo$ cd ~/ && rm -rf /tmp/13082022
```
<br />


## [Bandit32](https://overthewire.org/wargames/bandit/bandit32.html)
**Level Goal**<br/>
``
There is a git repository at ssh://[bandit31-git@localhost]/home/bandit31-git/repo. The password for the user bandit31-git is the same as for the user bandit31.
``

**Solution**
```bash
$ ssh bandit31@bandit.labs.overthewire.org -p 2220

bandit31@bandit:~$ mkdir /tmp/13082022 && cd /tmp/13082022
bandit31@bandit:/tmp/13082022$ ssh://bandit31-git@localhost/home/bandit31-git/repo && cd repo
-bash: ssh://bandit31-git@localhost/home/bandit31-git/repo: No such file or directory
bandit31@bandit:/tmp/13082022$ git clone ssh://bandit31-git@localhost/home/bandit31-git/repo && cd repo
Cloning into 'repo'...

bandit31@bandit:/tmp/13082022/repo$ ls
README.md
bandit31@bandit:/tmp/13082022/repo$ cat README.md
This time your task is to push a file to the remote repository.

Details:
    File name: key.txt
    Content: 'May I come in?'
    Branch: master

bandit31@bandit:/tmp/13082022/repo$ echo 'May I come in?' > key.txt

bandit31@bandit:/tmp/13082022/repo$ git add key.txt

The following paths are ignored by one of your .gitignore files:
key.txt
Use -f if you really want to add them.

bandit31@bandit:/tmp/13082022/repo$ git add -f key.txt

bandit31@bandit:/tmp/13082022/repo$ git commit -m "key"
[master 2b2ff3c] key
 1 file changed, 1 insertion(+)
 create mode 100644 key.txt

bandit31@bandit:/tmp/13082022/repo$ git push
...
remote: ### Attempting to validate files... ####
remote:
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote:
remote: Well done! Here is the password for the next level:
remote: 56a9bf19c63d650ce78e6ec0354ee45e             # bandit32's password.
remote:
remote: .oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.oOo.
remote:
...

bandit31@bandit:/tmp/13082022/repo$ cd ~/ && rm -rf /tmp/13082022
```
<br />


## [Bandit33](https://overthewire.org/wargames/bandit/bandit33.html)

``
After all this git stuff its time for another escape. Good luck!
``

**Solution**
```bash
# login with bandit31 first
$ ssh bandit31@bandit.labs.overthewire.org -p 2220

bandit31@bandit:~$ cat /etc/passwd | grep bandit32
bandit32:x:11032:11032:bandit level 32:/home/bandit32:/home/bandit32/uppershell

# login to bandit32
$ ssh bandit32@bandit.labs.overthewire.org -p 2220

...
WELCOME TO THE UPPERCASE SHELL

# Login Shell name
>> $SHELL
WELCOME TO THE UPPERCASE SHELL

# We have a clue here that sh is executing first. Meaning $0 = sh and $1+ will be our arguments.
>> ls
sh: 1: LS: not found

>> $USER
sh: 1: bandit32: not found 

# Escaping the uppershell. This will execute `sh $0` = `sh sh`.
>> $0
$ ls
uppershell

$ cat /etc/bandit_pass/bandit33
c9c3199ddf4121b10cf581a98d51caee             # bandit33's password.
```
<br />


## [Bandit34](https://overthewire.org/wargames/bandit/bandit34.html)

``
At this moment, level 34 does not exist yet.
``

**Solution**
```
# login with bandit31 first
$ ssh bandit33@bandit.labs.overthewire.org -p 2220

bandit33@bandit:~$ ls
README.txt
bandit33@bandit:~$ cat README.txt
Congratulations on solving the last level of this game!

At this moment, there are no more levels to play in this game. However, we are constantly working
on new levels and will most likely expand this game with more levels soon.
Keep an eye out for an announcement on our usual communication channels!
In the meantime, you could play some of our other wargames.

If you have an idea for an awesome new level, please let us know!
```
<br />




# OverTheWire - Bandit - Solutions

**My solutions to the [Bandit wargame](https://overthewire.org/wargames/bandit/).**


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

### [bandit0](https://overthewire.org/wargames/bandit/bandit0.html)
```bash
# bandit0 = password.
```


### [bandit1](https://overthewire.org/wargames/bandit/bandit1.html)
```bash
$ ssh bandit0@bandit.labs.overthewire.org -p 2220

bandit0@bandit:~$ cat ~/readme
boJ9jbbUNNfktd78OOpsqOltutMc3MY1                     # bandit1's passsword.
```


### [bandit2](https://overthewire.org/wargames/bandit/bandit2.html)
```bash
$ ssh bandit1@bandit.labs.overthewire.org -p 2220

bandit1@bandit:~$ cat ~/-
CV1DtqXWVFXTvM2F0k09SHz0YwRINYA9                     # bandit2's passsword.
```


### [bandit3](https://overthewire.org/wargames/bandit/bandit3.html)
```bash
$ ssh bandit2@bandit.labs.overthewire.org -p 2220

bandit2@bandit:~$ cat ~/'spaces in this filename'
UmHadQclWmgdLOKQ3YNgjWxGoRMb5luK                     # bandit3's password.
```


### [bandit4](https://overthewire.org/wargames/bandit/bandit4.html)
```bash
$ ssh bandit3@bandit.labs.overthewire.org -p 2220

bandit3@bandit:~$ ls -a ~/inhere
.  ..  .hidden
bandit3@bandit:~$ cat ~/inhere/.hidden
pIwrPrtPN36QITSp3EQaw936yaFoFgAB                     # bandit4's password.
```


### [bandit5](https://overthewire.org/wargames/bandit/bandit5.html)
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


### [bandit6](https://overthewire.org/wargames/bandit/bandit6.html)
```bash
$ ssh bandit5@bandit.labs.overthewire.org -p 2220

bandit5@bandit:~$ find ~/inhere -size 1033c
/home/bandit5/inhere/maybehere07/.file2

bandit5@bandit:~$ file ~/inhere/maybehere07/.file2
/home/bandit5/inhere/maybehere07/.file2: ASCII text, with very long lines

bandit5@bandit:~$ cat ~/inhere/maybehere07/.file2 | grep . 
DXjZPULLxYr17uwoI01bNLQbtFemEgo7                     # bandit6's password.
```


### [bandit7](https://overthewire.org/wargames/bandit/bandit7.html)
```bash
$ ssh bandit6@bandit.labs.overthewire.org -p 2220

# suppress permisison errors by redirecting stderr to null.
bandit6@bandit:~$ find / -user bandit7 -group bandit6 -size 33c -print 2>/dev/null
/var/lib/dpkg/info/bandit7.password

bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password
HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs                     # bandit7's password.
```


### [bandit8](https://overthewire.org/wargames/bandit/bandit8.html)
```bash
$ ssh bandit7@bandit.labs.overthewire.org -p 2220

bandit7@bandit:~$ cat ~/data.txt | grep millionth
millionth       cvX2JJa4CFALtqS87jk27qwqGhBM9plV     # bandit8's password.
```


### [bandit9](https://overthewire.org/wargames/bandit/bandit9.html)
```bash
$ ssh bandit8@bandit.labs.overthewire.org -p 2220

bandit8@bandit:~$ sort ~/data.txt | uniq -u
UsvVyFSfZZWbi6wgC7dAFyFuR6jQQUhR                     # bandit9's password.
```


### [bandit10](https://overthewire.org/wargames/bandit/bandit10.html)
```
$ ssh bandit9@bandit.labs.overthewire.org -p 2220

# readable strings, preceded by several '=' characters..
bandit9@bandit:~$ strings ~/data.txt | grep -E '==+' 
========== the*2i"4
========== password
Z)========== is
&========== truKLdjsbJ5g7yyJ2X2R0o3a5HQJFuLk         # bandit10's password.
```


### [bandit11](https://overthewire.org/wargames/bandit/bandit11.html)
```bash
$ ssh bandit10@bandit.labs.overthewire.org -p 2220

bandit10@bandit:~$ base64 -d ~/data.txt 
The password is IFukwKGsFW8MOq3IRFqrxE1hxTNEbUPR     # bandit11's password.
```


### [bandit12](https://overthewire.org/wargames/bandit/bandit12.html)
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


### [bandit13](https://overthewire.org/wargames/bandit/bandit13.html)
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
```


### [bandit14](https://overthewire.org/wargames/bandit/bandit14.html)
```bash
$ ssh bandit13@bandit.labs.overthewire.org -p 2220
bandit13@bandit:~$ ls
sshkey.private

bandit13@bandit:~$ ssh -i sshkey.private bandit14@localhost

bandit14@bandit:~$ cat /etc/bandit_pass/bandit14
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e                     # bandit14's password.
```


### [bandit15](https://overthewire.org/wargames/bandit/bandit15.html)
```bash
$ ssh bandit14@bandit.labs.overthewire.org -p 2220

# nc can be replaced by telnet
bandit14@bandit:~$ nc localhost 30000
4wcYUJFw0k0XLShlDzztnTBHiqxU3b3e                     # submitted bandit14's password.
Correct!
BfMYroe26WYalil77FoDi9qh59eK5xNr                     # bandit15's password.
```


### [bandit16](https://overthewire.org/wargames/bandit/bandit16.html)
```bash
$ ssh bandit15@bandit.labs.overthewire.org -p 2220

bandit15@bandit:~$ openssl s_client -connect localhost:30001
# blah blah..
BfMYroe26WYalil77FoDi9qh59eK5xNr                     # submitted bandit15's password.
Correct!
cluFn7wTiGryunymYOu4RcffSxQluehd                     # bandit16's password.
```


### [bandit17](https://overthewire.org/wargames/bandit/bandit17.html)
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


### [bandit18](https://overthewire.org/wargames/bandit/bandit18.html)
```bash
$ ssh -i sshkey.private bandit17@bandit.labs.overthewire.org -p 2220

bandit17@bandit:~$ diff passwords.old passwords.new | grep '>'
> kfBf3eYk5BPBRzwjqutbbfE887SVc5Yd                   # bandit18's password.
```


### [bandit19](https://overthewire.org/wargames/bandit/bandit19.html)
```bash
# ssh with inline command because of auto logout by .bashrc.
$ ssh bandit18@bandit.labs.overthewire.org -p 2220 'cat readme'

bandit18@bandit.labs.overthewire.org s password:
IueksS7Ubh8G3DCwVzrTd8rAVOwq3M5x                     # bandit19's password.
```


### [bandit20](https://overthewire.org/wargames/bandit/bandit20.html)
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


### [bandit21](https://overthewire.org/wargames/bandit/bandit21.html)
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


### [bandit22](https://overthewire.org/wargames/bandit/bandit22.html)
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


### [bandit23](https://overthewire.org/wargames/bandit/bandit23.html)
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


### [bandit24](https://overthewire.org/wargames/bandit/bandit24.html)
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
#!/bin/bash
cat /etc/bandit_pass/bandit24 > /tmp/12082022/password

bandit23@bandit:/tmp/12082022$ chmod 777 script.sh    # rwx for all
bandit23@bandit:/tmp/12082022$ cp script.sh /var/spool/bandit24/

# script will be executed after 60 seconds..
bandit23@bandit:/tmp/12082022$ cat password
UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ                     # bandit24's password.
``` 


### [bandit25](https://overthewire.org/wargames/bandit/bandit25.html)
```bash
$ ssh bandit24@bandit.labs.overthewire.org -p 2220

# TBD
```
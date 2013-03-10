pyOwnCloud
==========

ownCloud CLI client written in python, more info about owncloud: www.owncloud.org

Requirements:
	* the ocsync C library from ownCloud. If you install Mirall, you get it for free on linux.
	if you don't want to install mirall, you can install the 'ocsync' binary package from the owncloud repo's.
	* Python > 2.6
	* an ownCloud server to sync with. (presumably you already have one of these)


usage: just run csync.py -h, and it will give you help.

usage: csync.py [-h] [-v] [-c [CONFIG]] [-u [USER]] [-p [PASS]] [-d [DST]]
                [src] [url]

Synchronize files across machines using ownCloud DAV server

positional arguments:
  src                   local Directory to sync with
  url                   url to sync to.

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -c [CONFIG], --config [CONFIG]
                        username on server.
  -u [USER], --user [USER]
                        username on server.
  -p [PASS], --pass [PASS]
                        password on server. you can also store this in
                        environment variable OCPASS
  -d [DST], --dst [DST]
                        fodler on server.

I only support the 'ownCloud' section of the ownCloud config file.
I support the following keys in the cfg  file:
	user: The username on the ownCloud server
	url: the url of the ownCloud Server
	pass: the password on the ownCloud server
	sslFingerprint: a valid SSL fingerprint for the server.
	src: local directory to sync against.
	dst: folder on the server to sync against.
complete example:
[ownCloud]
user=awesomeSauce
pass=PasswordThisIsSuperSuperSecretReallyISwearLOL
url=url=https://www.example.org/owncloud/
sslFingerprint=
src=/home/awesomeSauce/ownCloud
dst=clientsync

Password options:
  *) You can specify on the cmd line: -p (not very safe)
  *) in the envifonment variable: OCPASS
  *) in the owncloud.cfg file as pass = <password>
  the choice is yours, if you put it in the cfg file, be careful to 
  make sure nobody but you can read the file. (0400/0600 file perms)

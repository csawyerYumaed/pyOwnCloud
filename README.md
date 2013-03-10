pyOwnCloud
==========

ownCloud CLI client written in python, more info about owncloud: www.owncloud.org

Requirements:
	* the ocsync C library from ownCloud. If you install Mirall, you get it for free on linux.
	if you don't want to install mirall, you can install the 'ocsync' binary package from the owncloud repo's.
	* Python > 2.6
	* an ownCloud server to sync with. (presumably you already have one of these)


usage: just run csync.py -h, and it will give you help.

    usage: csync.py [-h] [-v] [-c [CONFIG]] [-u [USER]] [--ssl [SSLFINGERPRINT]]
                [-p [PASS]] [--dry-run] [-s [SRC]] [-d [DST]] [--url [URL]]

    Synchronize files across machines using ownCloud DAV server

    optional arguments:
	    -h, --help            show this help message and exit
      -v, --version
      -c [CONFIG], --config [CONFIG]
                            username on server.
      -u [USER], --user [USER]
                            username on server.
      --ssl [SSLFINGERPRINT]
                            SSL fingerprint on server to accept.
      -p [PASS], --pass [PASS]
                        password on server. you can also store this in
                        environment variable OCPASS
      --dry-run             Dry Run, do not actually execute command.
      -s [SRC], --src [SRC]
                        local Directory to sync with
      -d [DST], --dst [DST]
                        fodler on server.
      --url [URL]           url to sync to.

    I support the ownCloud config file, which is located here:
      $HOME/.local/share/data/ownCloud/owncloud.cfg
    I only support the 'ownCloud' section of the config.
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

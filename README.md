pyOwnCloud
==========

ownCloud CLI client written in python, more info about owncloud: www.owncloud.org

This code is now in production use, and has been tested against a variety of Linux machines,
other platforms should work, but are currently untested. This code is in no way currently endorsed or
supported by ownCloud, all bugs should be reported here and not there.

Support/Discussion:
-------------------

* Use github for issues/patches/etc: https://github.com/csawyerYumaed/pyOwnCloud
* For discussion use: http://lists.cknow.org/listinfo.cgi/pyowncloud-cknow.org (pyowncloud <@> lists.cknow.org)

Requirements:
-------------
* The ocsync C library from ownCloud. If you install Mirall, you get it for free on Linux.
	If you don't want to install mirall, you can install the 'ocsync' binary package from the owncloud repo's.
        So far we have successfully tested against 0.70.4 and 0.70.5 of the libocsync library.
* Python > 2.6 < 3 (patches welcome)
* An ownCloud server to sync with. (Presumably you already have one of these.)

Installation:
-------------
* standard python setup.py script.
* It will create a new command called oclient, and you can call that :)

    python setup.py install

usage: just run oclient -h, and it will give you help.
    
    usage: oclient [-h] [-v] [-c [CONFIG]] [-u [USER]] [--ssl [SSLFINGERPRINT]]
                   [-p [PASS]] [--dry-run] [--debug] [-s [SRC]] [-d [DST]]
                   [--url [URL]] [--use-keyring]
    
    Synchronize files across machines using ownCloud DAV server.
    
    optional arguments:
    -h, --help            Show this help message and exit
    -v, --version         Show program's version number and exit
    -c [CONFIG], --config [CONFIG]
                          Configuration to use.
    -u [USER], --user [USER]
                          Username on server.
    --ssl [SSLFINGERPRINT]
                          SSL fingerprint on server to accept.
    -p [PASS], --pass [PASS]
                          Password on server. You can also store this in
                          environment variable OCPASS.
    --dry-run             Dry Run, do not actually execute command.
    --debug               Print a bunch of debug info.
    -s [SRC], --src [SRC]
                          Local Directory to sync with.
    -d [DST], --dst [DST]
                          Folder on server.
    --url [URL]           URL to sync to.
    --use-keyring         use keyring if available to store password safely.

    
    oclient supports the ownCloud config file, which is located here:
        $HOME/.local/share/data/ownCloud/owncloud.cfg
    oclient only supports the 'ownCloud' section of the config.
    oclient supports the following keys in the cfg  file:
    	user: username on the ownCloud server
    	pass: password on the ownCloud server
    	url: url of the ownCloud server
    	sslfingerprint: valid SSL fingerprint for the server
    	src: local directory to sync against
    	dst: folder on the server to sync against
    
    complete example:
    [ownCloud]
    user=awesomeSauce
    pass=PasswordThisIsSuperSuperSecretReallyISwearLOL
    url=https://www.example.org/owncloud/
    sslfingerprint=
    src=/home/awesomeSauce/ownCloud
    dst=clientsync
    
    Password options:
     *) You can specify on the cmd line: -p (not very safe)
     *) In the environment variable: OCPASS
     *) In the owncloud.cfg file as pass = <password>
     *) Do none of the above, and it will prompt you for the password.
     *) Use keyring to store passwords in a keyring. (needs Python Keyring Lib to be installed)
     
     The choice is yours, if you put it in the cfg file, be careful to
     make sure nobody but you can read the file. (0400/0600 file perms).

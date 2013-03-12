pyOwnCloud
==========

ownCloud CLI client written in python, more info about owncloud: www.owncloud.org

This code is in no way currently endorsed or supported by ownCloud, all bugs should be reported here
and not there.

Requirements:
* The ocsync C library from ownCloud. If you install Mirall, you get it for free on Linux.  
	If you don't want to install mirall, you can install the 'ocsync' binary package from the owncloud repo's.  
        So far we have only successfully tested against 0.70.4 of the libocsync library.
* Python > 2.6 < 3 (patches welcome)
* An ownCloud server to sync with. (Presumably you already have one of these.)

usage: just run csync.py -h, and it will give you help.

    usage: csync.py [-h] [-v] [-c [CONFIG]] [-u [USER]] [--ssl [SSLFINGERPRINT]]
                [-p [PASS]] [--dry-run] [--debug] [-s [SRC]] [-d [DST]] [--url [URL]]
    
    Synchronize files across machines using ownCloud DAV server.
    
    optional arguments:
    -h, --help            show this help message and exit
    -v, --version         show program's version number and exit
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
    url=https://www.example.org/owncloud/
    sslFingerprint=
    src=/home/awesomeSauce/ownCloud
    dst=clientsync
    
    Password options:
     *) You can specify on the cmd line: -p (not very safe)
     *) In the envifonment variable: OCPASS
     *) In the owncloud.cfg file as pass = <password>
     The choice is yours, if you put it in the cfg file, be careful to 
     make sure nobody but you can read the file. (0400/0600 file perms).

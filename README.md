pyOwnCloud
==========

IMPORTANT UPDATE
=================
It's come to my attention that owncloud requires X running to auto-sync, they have 'owncloudcmd' that will sync once and exit. To get around that, here are some solutions:

 That's kind of awful.  You can run X behind the scenes with 
xvfb (installable on most all distro's). something like: xvfb-run 
<path to owncloud>

if you wanted pyOwncloud to run, you will need to rebind to the latest owncloud libs. If I remember  right, it's CFFI bindings that I used.  Since we don't run it here anymore, I'm not really in a place to mess with the bindings anymore.

Another option, would be to run something like https://pypi.python.org/pypi/watchdog, and have it monitor the FS for events in the dir(s) yuo care about and then have it run owncloudcmd for you.  That would have it only run on change(s).
Actually.. if you wanted to update pyOwncloud to do that, I'd happily merge that and give you admin rights.

Most of this above was from an email exchange with someone, but I think it's worth mentioning here, since apparently the owncloud docs don't talk about it very well.

End update
========================================



ownCloud CLI client written in python, more info about owncloud: www.owncloud.org

This code is now in production use, and has been tested against a variety of Linux machines,
other platforms should work, but are currently untested. This code is in no way currently endorsed or
supported by ownCloud, all bugs should be reported here and not there.

Support/Discussion:
-------------------

* Use github for issues/patches/etc: https://github.com/csawyerYumaed/pyOwnCloud

Requirements:
-------------
* The ocsync C library from ownCloud < 0.91.0. If you install Mirall/owncloud-client, you get it for free on Linux.
	If you don't want to install mirall, you have to install the 'ocsync' binary package,
	usually named 'libocsync0' and the owncloud plugin, usually named 'libocsync-plugin-owncloud'.
	Installing the plugin should also install 'libocsync0' as a dependency.

When running Debian (jessy) or Ubuntu raring, you can install it right from the archives.
For other distributions you can get them through https://build.opensuse.org/package/show/isv:ownCloud:devel/ocsync .
* Python > 2.6 < 3 (patches welcome)
* An ownCloud server to sync with. (Presumably you already have one of these.)
* argparse for python (included with python > 2.6)

Installation:
-------------
* standard python setup.py script.
* It will create a new command called oclient, and you can call that :)

    python setup.py install

usage: just run oclient -h, and it will give you help.
    
    usage: oclient [-h] [-v] [-c [CONFIG]] [-u [USER]] [--ssl [SSLFINGERPRINT]]
                   [-p [PASS]]
                   [--dry-run] [--debug] [--verbosity-ocsync VERBOSITY_OCSYNC]
                   [-s [SRC]] [-d [DST]]
                   [--url [URL]] [--use-keyring]
                   [--downloadlimit [DOWNLOADLIMIT]]
                   [--uploadlimit [UPLOADLIMIT]]
                   [--progress]
    
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
    --verbosity-ocsync VERBOSITY_OCSYNC
                          Verbosity for libocsync. (0=NOLOG,11=Everything)

    -s [SRC], --src [SRC]
                          Local Directory to sync with.
    -d [DST], --dst [DST]
                          Folder on server.
    --url [URL]           URL to sync to.
    --use-keyring         use keyring if available to store password safely.
    --downloadlimit [DOWNLOADLIMIT]
                          Download limit in KB/s.
    --uploadlimit [UPLOADLIMIT]
                          Upload limit in KB/s.

    --progress            Show progress while syncing.

    oclient supports the ownCloud config file, which is located here:
        $HOME/.local/share/data/ownCloud/owncloud.cfg
    oclient only supports the 'ownCloud' section of the config.
    oclient support for download/upload limits requires libocsync version >= 0.81.0
      these versions also support 'BWLimit' section of the config.
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
     *) Use keyring to store passwords in a keyring. (needs Python Keyring Lib to be installed)
     *) Do none of the above, and it will prompt you for the password.
     
     The choice is yours, if you put it in the cfg file, be careful to
     make sure nobody but you can read the file. (0400/0600 file perms).

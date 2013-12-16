#!/usr/bin/env python2
"""Generates ctype python files for the missing versions
need python modules:
* ctypeslib
* GitPython

run it with one argument where a git clone of ocsync exists:
git://git.csync.org/users/owncloud/csync
"""

from git import Repo
from distutils.version import StrictVersion
from subprocess import call
import os
import sys

from csync.csynclib import specific_parts

#the known versions
known_versions=[ i[0] for i in specific_parts ]

#Add files that are needed to compile .h files
open('csync_version.h','a')
open('config.h','a')

#open the git repo
repo = Repo(sys.argv[1])

for tag in repo.tags:
    #only match tags, that are version tags and are higher than 0.70.0
    if not tag.name.startswith('v'):
        continue
    version = tag.name[1:]
    try:
        if StrictVersion(version) < StrictVersion('0.70.0'):
            continue
    except ValueError:
        continue

    #only new versions interessting us
    if version in known_versions:
        continue

    print version

    # get the csync.h at the version
    with open("csync"+version+".h",'w') as f:
        f.write(repo.commit(tag).tree['src/csync.h'].data_stream.read())

    #create python file out of the header file
    safe_name = tag.name.replace('.',"_")

    call(["h2xml","csync"+version+".h","-I", os.getcwd(), "-o", "csync"+version+".xml", "-q"])
    call(["xml2py", "csync"+version+".xml", "-o", safe_name+".py", "-k", "efst", "-l", "libocsync.so.0"])

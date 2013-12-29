from . import pre
from distutils.version import StrictVersion
import sys
__version__ = pre.csync_version(0)

#load version specific parts

specific_parts = (
		('0.70.0','v0_70_5'),
		('0.70.90','v0_70_90'),
		('0.80.1','v0_80_1'),
		('0.91.0','v0_91_0'),
		('0.91.2','v0_91_2'),
		)

ov = StrictVersion(__version__)
oldname = None

for v,name in specific_parts:
	if StrictVersion(v) >= ov:
		print v,ov,oldname
		mod = __import__(__name__+"."+oldname, globals(), locals(), [oldname])
		break
	oldname = name
else:
	mod = __import__(__name__+"."+name, globals(), locals(), [name])

me = sys.modules[__name__]
__all__= []
for n,v in mod.__dict__.items():
	if not n.startswith('__'):
		setattr(me,n,v)
		__all__.append(n)

from . import log
#from . import post
from .pre import *
from .log import *
#from .post import *

__all__ += pre.__all__

# vim: noet:ts=4:sw=4:sts=4

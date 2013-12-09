from . import pre
from distutils.version import StrictVersion
import imp, sys
__version__ = pre.csync_version(0)

#load version specific parts

default = '0.91.0'
specific_parts = (
		('0.70.0','v0_70_0'),
		('0.90.9','v0_90_0'),
		)

ov = StrictVersion(__version__)

for v,name in specific_parts:
	if StrictVersion(v) > ov:
		fp, pathname, description = imp.find_module(name, __path__)
		mod = imp.load_module(name, fp, pathname, description)
		break
else:
	fp, pathname, description = imp.find_module(name, __path__)
	mod = imp.load_module(name, fp, pathname, description)

me = sys.modules[__name__]
__all__= []
for n,v in mod.__dict__.items():
	if not n.startswith('__'):
		setattr(me,n,v)
		__all__.append(n)

from . import post

from .pre import *
from .post import *

__all__ += post.__all__
__all__ += pre.__all__

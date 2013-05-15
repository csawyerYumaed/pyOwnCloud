import subprocess
import json
import os
import pkg_resources
import locale

encoding = locale.getdefaultlocale()[1]

verfile = pkg_resources.resource_filename(__name__, 'version.dat')

class ver(object):
	def __init__(self, verfile='version.dat'):
		self.verfile = verfile
		self.loadVersion()
		self.setup()
	def setup(self):
		"""sublass this to do something useful for yourself"""
		pass
	@property
	def asFloat(self):
		return self.version['float']
	@property
	def asString(self):
		return self.version['string']
	@property
	def asHead(self):
		return self.version['head']
	def makeString(self):
		s = str(self.asFloat)
		#s = s.replace('.','_')
		return s
	def makeNpackd(self):
		s = "%.2f" % (self.asFloat)
		return s
	def makeFloat(self, s):
		s = str(s)
		s = s.replace('_', '.')
		f = float(s)
		return f
	def bumpVersion(self, amt=.1):
		newVersion = self.asFloat + amt
		self.setVersion(newVersion)
	def setVersion(self, ver):
		ver = str(ver)
		self.version['float'] = self.makeFloat(ver)
		self.version['string'] = self.makeString()
		self.asNpackd = self.makeNpackd()
		self.saveVersion()
	def loadVersion(self):
		try:
			#ver = open(self.verfile,'r').read()
			ver = json.load(open(self.verfile,'r'))
		except IOError:
			ver = {'float': 0.0, 'string': '0.0' }
		self.version = ver
		#self.asFloat = self.makeFloat(ver['version'])
		#self.asString = self.makeString()
		self.asNpackd = self.makeNpackd()
		return ver
	def saveVersion(self):
		json.dump(self.version,open(self.verfile,'w'))
		#open(self.verfile,'w').write(str(self.asFloat))
		return self.verfile

class hgVersion(ver):
	def getHeadVersion(self):
		"""if hg is around, return the current version and save it
		otherwise return the saved copy, or 00 if not already saved.
		"""
		cmd = "hg heads".split()
		try:
			out = subprocess.check_output(cmd)
		except:
			out = '\n'
		out = out.split('\n',1)
		if 'changeset' in out[0]:
			out = out[0].split()
			ver = out[1]
			self.version['head'] = ver
			self.saveVersion()
		else:
			if head in self.version:
				ver = self.version['head']
			else:
				ver = '00'
		return ver
	def setup(self):
		self.getHeadVersion()
	@property
	def asHead(self):
		return self.getHeadVersion()

class gitVersion(ver):
	def getHeadVersion(self):
		"""if git is around, return the current version and save it.
		otherwise return the saved copy, or 00 if not already saved.
		"""
		gitdir = os.path.join(os.path.dirname(os.path.abspath(self.verfile)),'..','.git')
		if not os.path.exists(gitdir):
			if 'head' in self.version:
				return self.version['head']
			return '00'
		cmd = 'git rev-parse --verify HEAD'.split()
		try:
			out = subprocess.check_output(cmd)
		except:
			out = '\n'
		out = out.decode(encoding).split('\n',1)
		if len(out[0]) > 1:
			ver = out[0]
			self.version['head'] = ver
			self.saveVersion()
		else:
			if self.version.has_key('head'):
				ver = self.version['head']
			else:
				ver = '00'
		return ver
	def setup(self):
		self.getHeadVersion()
	@property
	def asHead(self):
		return self.getHeadVersion()

#BASE_DIR = os.path.abspath(os.path.dirname(__file__))
#if os.path.exists(os.path.join(BASE_DIR, 'devel')):
#    version = gitVersion(os.path.join(BASE_DIR, 'version.dat'))
#else:
#    version = ver(os.path.join(BASE_DIR, 'version.dat'))

version = gitVersion(verfile)

if __name__ == '__main__':
	print('Testing version.')
	v = hgVersion()
	print('dict:', v.version)
	print('string:', v.asString)
	print('float:', v.asFloat)
	print('hghead', v.asHead)

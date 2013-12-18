from distribute_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages
import csync.version as ver
setup(
	name = "pyOwnCloud",
	version = ver.version.asString,
	packages = find_packages(),
	package_data = {
		'csync': [ 'version.dat'],
	},
	entry_points = {
		'console_scripts': [
			'oclient = csync.csync:main',
		],
	},
	extras_require = {
		'keyring':  ["keyring"],
	},
	author = 'pyOwnCloud Team',
	author_email = 'pyowncloud@lists.cknow.org',
	license = 'GPLv2',
	url = "https://github.com/csawyerYumaed/pyOwnCloud",
		download_url = "https://github.com/csawyerYumaed/pyOwnCloud/tag/"+ver.version.asString,
	description = 'ownCloud CLI client- connect your ownCloud with python.',
	long_description = open('README.md').read(),
	classifiers = [
		"Development Status :: 3 - Alpha",
		"Environment :: Console",
		"Topic :: Communications :: File Sharing",
		"Intended Audience :: End Users/Desktop",
		"Programming Language :: Python",
		"License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
	]

)

# vim: noet:ts=4:sw=4:sts=4

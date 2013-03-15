from distribute_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages
import version as ver
setup(
    name = "pyOwnCloud",
    version = ver.version.asFloat,
    packages = find_packages(),
	entry_points = {
		'console_scripts': [
            'csync = csync.csync:main',
        ],
)

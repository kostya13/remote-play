from distutils.core import setup

setup(name='remoteplay',
      version='1.0',
      description='Play files from remote server',
      author='Konstantin Ilyashenko',
      author_email='kx13@ya.ru',
      packages=['remoteplay'],
      install_requires=['requests'],
      entry_points={
	'console_scripts': [
	    'remoteplay=remoteplay:remoteplay.main']}
     )

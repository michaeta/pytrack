import os
import sys

from setuptools import setup

version = '0.0.1.dev1'

install_requires = ['pyechonest']

setup(name='pytrack',
      version=version,
      description='A DJ Command line tool to analyze and build set lists' +
                  ' of audio files',
      long_description='TBA',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Intended Audience :: DJs',
          'License :: OSI Approved :: MIT License',
          'Topic :: Software Development :: Build Tools',
          'Programming Language :: Python :: 2.7',
      ],
      keywords='DJ music audio analysis pyechonest mp3',
      author='Taylor Michael',
      author_email='ot41is@gmail.com',
      url='http://github.com/michaeta/pytrack',
      license='MIT',
      packages=['pytrack'],
      entry_points=dict(console_scripts=['pytrack=pytrack:main']),
      install_requires=install_requires,
      zip_safe=False)

import setuptools

with open('README.md', 'r') as fh:
  long_description = fh.read()

setuptools.setup(
  name='pytranscoder-ffmpeg',
  version='1.0.0',
  python_requires='>=3.6',
  author='Marshall L Smith Jr',
  author_email='marshallsmithjr@gmail.com',
  description='A ffmpeg wrapper to better manage transcode operations',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  extras_require={'with_plexapi': ['plexapi>=3.1.0']},
  url='https://github.com/mlsmithjr/transcoder',
  packages=['pytranscoder'],
  entry_points={"console_scripts": ["pytranscoder=pytranscoder.transcode:main"]},
  classifiers=[
    'Programming Language :: Python :: 3',
    'Environment :: Console',
    'Topic :: Multimedia :: Video :: Conversion',
    'Intended Audience :: Other',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Natural Language :: English',
    'Operating System :: POSIX :: Linux',
  ],
)

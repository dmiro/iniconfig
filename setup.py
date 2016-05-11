from setuptools import setup, find_packages

long_description = ''

try:
  import requests
  r = requests.post(url='http://c.docverter.com/convert',
                    data={'to':'rst','from':'markdown'},
                    files={'input_files[]':open('README.md','rb')})
  if r.ok:
    long_description = r.content
except:
  pass

setup(
    name = 'iniconfig.py',
    version = __import__('iniconfig').__version__,
    author = 'David Miro',
    author_email = 'lite.3engine@gmail.com',
    description = 'A more convenient and practical approach to manage .ini files',
    long_description = long_description,
    license = open('LICENSE').read(),
    url = 'https://github.com/dmiro/iniconfig',
    packages = find_packages(),
    test_suite = 'tests',
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License'
        ]
    )

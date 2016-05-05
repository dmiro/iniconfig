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
    name='iniconfig',
    version=__import__('iniconfig').__version__,
    author = 'David Miro',
    author_email = 'lite.3engine@gmail.com',
    description = 'A more convenient and practical approach to manage .ini files',
    long_description=long_description,
    license=open('LICENSE').read(),
    url='https://github.com/dmiro/iniconfig',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License'
        ]
    )

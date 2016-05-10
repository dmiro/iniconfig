# iniconfig

[![Build Status](https://travis-ci.org/dmiro/iniconfig.svg?branch=master)](https://travis-ci.org/dmiro/iniconfig)

A more convenient and practical approach to manage .ini files. You can link a class property with an .ini file option and delegating your management.

:package: Installation
-----------------------

Install it via `pip`

soon....

Or download zip and then install it by running

`$ [sudo] python setup.py install`


Example
-------

```python
from iniconfig import IniConfig

class Config(IniConfig):

    # file section
    useCsvWizard = IniConfig.iniproperty('file', 'useCsvWizard', True)
    owner = IniConfig.iniproperty('file', 'owner', {'name':'david', 'login':'yeap'})
    files = IniConfig.iniproperty('file', 'files', [])

    # tools section
    searches = IniConfig.iniproperty('tools', 'searches', ['primate', 'wolf', 'rabbit'])
    matchMode = IniConfig.iniproperty('tools', 'matchMode', 0)
    weight = IniConfig.iniproperty('tools', 'weight', False)

    # config section
    restore = IniConfig.iniproperty('config', 'restore', True)


config = Config('demo.ini')#, autocreate=True)

print '\nafter'
print 'file/useCsvWizard:', config.useCsvWizard
print 'file/owner:', config.owner
print 'file/files:', config.files
print 'tools/searches:', config.searches

config.useCsvWizard = False
config.files = ['myfile.py']
config.owner['name'] = 'joan'
config.owner['surname'] = 'miro'
del(config.owner['login'])
del config.searches[2]

print '\nbefore'
print 'file/useCsvWizard:', config.useCsvWizard
print 'file/owner:', config.owner
print 'file/files:', config.files
print 'tools/searches:', config.searches
```

Result

```bash
after
file/useCsvWizard: True
file/owner: {'login': 'yeap', 'name': 'david'}
file/files: []
tools/searches: ['primate', 'wolf', 'rabbit']

before
file/useCsvWizard: False
file/owner: {'surname': 'miro', 'name': 'joan'}
file/files: ['myfile.py']
tools/searches: ['primate', 'wolf']
```

Now the content .ini file is:

```text
[file]
usecsvwizard = False
files = ['myfile.py']
owner = {'surname': 'miro', 'name': 'joan'}

[tools]
searches = ['primate', 'wolf']
```

:yum: How to contribute
-----------------------

Have an idea? Found a bug? [add a new issue](https://github.com/dmiro/iniconfig/issues) or [fork] (https://github.com/dmiro/iniconfig#fork-destination-box) and sendme a pull request. Don't forget to add your name to the Contributors section of this document.

:scroll: License
----------------

Licensed under the MIT, see `LICENSE`

:heart_eyes: Contributors
--------------------------

David Miro <lite.3engine@gmail.com>

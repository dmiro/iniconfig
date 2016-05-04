# iniconfig
A more convenient and practical approach to manage .ini files. You can link a class property with an .ini file option and delegating your management.

Example
-------

```
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

```
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

And the content of the .ini file is this:

```
[file]
usecsvwizard = False
files = ['myfile.py']
owner = {'surname': 'miro', 'name': 'joan'}

[tools]
searches = ['primate', 'wolf']
```

## :yum: How to contribute

Have an idea? Found a bug? [add a new issue](https://github.com/dmiro/iniconfig/issues) or [fork the project] (https://github.com/dmiro/iniconfig#fork-destination-box) and pull a request.

## :scroll: license

MIT

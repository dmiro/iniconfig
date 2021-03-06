# -*- coding: utf-8 -*-
# allow direct execution
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from iniconfig import IniConfig


class Config(IniConfig):

    # file section
    file_useCsvWizard = IniConfig.iniproperty('file', 'useCsvWizard', True)
    file_owner = IniConfig.iniproperty('file', 'owner', {'name':'david'})
    file_address = IniConfig.iniproperty('file', 'address', 'my house')
    file_files = IniConfig.iniproperty('file', 'files', [])

    # tools section
    tools_searches = IniConfig.iniproperty('tools', 'searches', ['primate', 'wolf'])
    tools_matchMode = IniConfig.iniproperty('tools', 'matchMode', 0)
    tools_matchCase = IniConfig.iniproperty('tools', 'matchCase', False)
    tools_weight = IniConfig.iniproperty('tools', 'weight', False)

    # config section
    config_restore = IniConfig.iniproperty('config', 'restore', True)


config = Config(filename='demo.ini')

print('\nbefore')
print('file/useCsvWizard:', config.file_useCsvWizard)
print('file/owner:', config.file_owner)
print('file/files:', config.file_files)
print('file/address:', config.file_address)
print('tools/searches:', config.tools_searches)

config.file_useCsvWizard = False
config.file_files = ['myfile.py']
config.file_owner['surname'] = 'miro'
config.file_address = 'my office'

print(config.file_owner.__class__.__name__)

print('\nafter')
print('file/useCsvWizard:', config.file_useCsvWizard)
print('file/owner:', config.file_owner)
print('file/files:', config.file_files)
print('file/address:', config.file_address)
print('tools/searches:', config.tools_searches)

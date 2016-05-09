# -*- coding: utf-8 -*-

# allow direct execution
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from iniconfig import IniConfig
    import unittest
    import unittest.mock as mock
except:
    from iniconfig import IniConfig
    import unittest
    import mock


class Conf(IniConfig):

    optBool = IniConfig.iniproperty(section='section', option='option1', default=False)
    optFloat = IniConfig.iniproperty(section='section', option='option2', default=40.5)
    optInt = IniConfig.iniproperty(section='section', option='option3', default=0)
    optList = IniConfig.iniproperty(section='section', option='option4', default=[])
    optDict = IniConfig.iniproperty(section='section', option='option5', default={'one':1, 'two':2})


class Test(unittest.TestCase):

    def setUp(self):
       pass

    @mock.patch('__builtin__.open', spec=file)
    def test_load_inifile(self, mock_method):

        file_metadata = ['[section]',
                         'option3 = 10',
                         "option5 = {'three': '3', 'four': '4'}"]

        def side_effect():
            if file_metadata:
                return file_metadata.pop(0)

        mock_method.return_value.__enter__ = lambda s: s       # with clausule
        mock_method.return_value.__exit__ = mock.MagicMock()   # compatibility
        mock_method.return_value.readline.side_effect = side_effect

        conf = Conf('conf.ini')

        mock_method.assert_called_once_with('conf.ini')
        self.assertFalse(conf.optBool)
        self.assertEqual(conf.optFloat, 40.5)
        self.assertEqual(conf.optInt, 10)
        self.assertEqual(conf.optList, [])
        self.assertEqual(conf.optDict, {'three': '3', 'four': '4'})

    @mock.patch('__builtin__.open', spec=file)
    def test_inifile_not_exist_return_default_values(self, mock_method):

        mock_method.side_effect = IOError()

        conf = Conf('conf.ini')

        mock_method.assert_called_once_with('conf.ini')
        self.assertFalse(conf.optBool)
        self.assertEqual(conf.optFloat, 40.5)
        self.assertEqual(conf.optInt, 0)
        self.assertEqual(conf.optList, [])
        self.assertEqual(conf.optDict, {'one':1, 'two':2})

    @mock.patch('__builtin__.open', spec=file)
    def test_load_inifile_and_set_props(self, mock_method):

        file_metadata = ['[section]',
                         'option3 = 10',
                         "option5 = {'three': '3', 'four': '4'}"]

        def side_effect():
            if file_metadata:
                return file_metadata.pop(0)

        mock_file = mock_method.return_value
        mock_file.__enter__ = lambda s: s       # with clausule
        mock_file.__exit__ = mock.MagicMock()   # compatibility
        mock_file.readline.side_effect = side_effect
        conf = Conf('conf.ini')

        conf.optInt = 20
        conf.optList = ['twenty']
        del(conf.optDict['three'])

        self.assertTrue(mock_method.called)
        self.assertEqual(conf.optInt, 20)
        expected = [mock.call('[section]\n'),
                    mock.call('option3 = 20\n'),
                    mock.call("option5 = {'three': '3', 'four': '4'}\n"),
                    mock.call('\n'),
                    mock.call('[section]\n'),
                    mock.call('option3 = 20\n'),
                    mock.call("option5 = {'three': '3', 'four': '4'}\n"),
                    mock.call("option4 = ['twenty']\n"),
                    mock.call('\n'),
                    mock.call('[section]\n'),
                    mock.call('option3 = 20\n'),
                    mock.call("option5 = {'four': '4'}\n"),
                    mock.call("option4 = ['twenty']\n"),
                    mock.call('\n')]
        self.assertEqual(mock_file.write.call_args_list, expected)
        self.assertEqual(mock_file.write.call_count, 14)

if __name__ == '__main__':
    unittest.main()

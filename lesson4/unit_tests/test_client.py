import unittest
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..'))
from client import *
import time


try:
    # python 3.4+ should use builtin unittest.mock not mock package
    from unittest.mock import patch
except ImportError:
    from mock import patch


class TestClient(unittest.TestCase):
    def test_create_message(self):
        correct_message = {
            ACTION: PRESENCE,
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: 'Guest'
            }
        }
        message_created = create_presence()
        self.assertEqual(type(message_created), type(correct_message))
        self.assertEqual(message_created[ACTION], correct_message[ACTION])
        self.assertAlmostEqual(message_created[TIME], correct_message[TIME], 3)
        self.assertEqual(message_created[USER], correct_message[USER])

    def test_create_message_with_account_name(self):
        self.assertEqual(create_presence('Kostia')[USER][ACCOUNT_NAME], 'Kostia')

    def test_main_incorrect_port(self):
        test_args = ["client.py", "localhost", "incorrect_port"]
        with patch.object(sys, 'argv', test_args):
            with unittest.mock.patch('builtins.print') as mocked_print:
                with self.assertRaises(SystemExit):
                    main()
                self.assertEqual(mocked_print.mock_calls, [unittest.mock.call('В качестве порта может быть указано только число в диапазоне от 1024 до 65535.')])


if __name__ == "__main__":
    unittest.main()

import unittest

from lesson3.server import *
import time


class TestClient(unittest.TestCase):
    def test_message_response(self):
        correct_message = {
            ACTION: PRESENCE,
            TIME: time.time(),
            USER: {
                ACCOUNT_NAME: 'Guest'
            }
        }
        self.assertEqual(process_client_message(correct_message), {RESPONSE: 200})

    def test_message_response_incorrect(self):
        incorrect_message = {}
        self.assertEqual(process_client_message(incorrect_message), {RESPONDEFAULT_IP_ADDRESSSE: 400, ERROR: 'Bad Request'})


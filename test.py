from lambda_function import lambda_handler
import unittest

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_linear(self):
        event = {
            "queryStringParameters": {
                "environment": 'test',
                "integrationIDs": [
                    ['669f586074915'],
                    ['669f58853d1f4'],
                    ['669f58d9c5804']
                ]
            }
        }

        self.assertEqual(lambda_handler(event, None), 'All good')


    def test_multiples(self):
        event = {
            "queryStringParameters": {
                "environment": 'test',
                "integrationIDs": [
                    ['669f586074915'],
                    ['669f58853d1f4','669f58853d1f4'],
                    ['669f58d9c5804']
                ]
            }
        }

        self.assertEqual(lambda_handler(event, None), 'All good')

    # This test is designed to fail for demonstration purposes.
    #def test_decrement_fail(self):
    #    event = {
    #        "queryStringParameters": {
    #            "environment": 'test',
    #            "integrationIDs": ['669f586074915','669f58853d1f4','669f58d9c5804']
    #        }
    #    }
    #    
    #    self.assertEqual(lambda_handler(event, None), 'No good')

if __name__ == '__main__':
    unittest.main()
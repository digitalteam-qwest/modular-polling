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

        outcome = lambda_handler(event, None)

        self.assertEqual(outcome['result'], 'All good')

    def test_linear_no_data(self):
        event = {
            "queryStringParameters": {
                "environment": 'test',
                "integrationIDs": [
                    ['66b9d1c2ae68d'],
                    ['669f58853d1f4'],
                    ['669f58d9c5804']
                ]
            }
        }

        outcome = lambda_handler(event, None)

        self.assertEqual(outcome['result'], 'All good')

    def test_multiples(self):
        event = {
            "queryStringParameters": {
                "environment": 'test',
                "integrationIDs": [
                    ['669f586074915'],
                    ['669f58853d1f4','66bc649972920'],
                    ['669f58d9c5804']
                ]
            }
        }

        outcome = lambda_handler(event, None)

        self.assertEqual(outcome['result'], 'All good')

    def test_slowwwww(self):
        #should take at least 2 minutes to complete
        event = {
            "queryStringParameters": {
                "environment": 'test',
                "integrationIDs": [
                    ['66bdf7349f2f5'],
                    ['66bdf7b7861a5']
                ]
            }
        }

        outcome = lambda_handler(event, None)

        self.assertEqual(outcome['result'], 'All good')

    def test_specific(self):
        event = {
            "queryStringParameters": {
                "environment": 'test',
                "integrationIDs": [
                    ['5d52d3e459313'],
                    ['5d52ce9c26d98']
                ]
            }
        }

        outcome = lambda_handler(event, None)

        self.assertEqual(outcome['result'], 'All good')

if __name__ == '__main__':
    unittest.main()
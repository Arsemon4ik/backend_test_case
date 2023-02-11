import unittest
from app import app


class SimpleFlaskTestCase(unittest.TestCase):

    def test_correct_get(self):
        tester = app.test_client(self)
        response = tester.get('/list/newkey2')
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    def test_wrong_get(self):
        tester = app.test_client(self)
        response = tester.get('/list/9999abc')
        status_code = response.status_code
        self.assertEqual(status_code, 404)

    def test_content_type_get(self):
        tester = app.test_client(self)
        response = tester.get('/list/newkey2')
        content_type = response.content_type
        self.assertEqual(content_type, "application/json")

    def test_content_data_get(self):
        tester = app.test_client(self)
        response = tester.get('/list/newkey2')
        content_data = response.data
        self.assertTrue(b'somebin2' in content_data)


if __name__ == '__main__':
    unittest.main()
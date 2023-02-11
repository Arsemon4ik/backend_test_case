import unittest
from app import app

testapp = app.test_client()


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

    # def test_post_new_value(self):
    #     response = self.post(key="somenewkey", value="somenewvalue")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn(b'somenewvalue', response.data)
    #
    # def post(self, key, value):
    #     return testapp.post('/add',
    #                         data=dict(key=key, value=value))
    #
    # def get(self, key):
    #     return testapp.get(f'/list/{key}')
    #
    # def update(self, key, value):
    #     return testapp.put('/update',
    #                        data=dict(key=key, value=value))
    #
    # def test_update_new_value(self):
    #     response = self.put(key="somenewkey", value="somenewvalue2")
    #     self.assertEqual(response.status_code, 200)
    #     self.assertIn(b'somenewvalue2', response.data)


if __name__ == '__main__':
    unittest.main()

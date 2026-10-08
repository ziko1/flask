import unittest
from main import app


class ApplicationTests(unittest.TestCase):
    def test_index_remains_compatible(self):
        response = app.test_client().get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Choo Choo', response.json)

    def test_health_is_json(self):
        response = app.test_client().get('/health')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'ok': True, 'service': 'flask-example'})

    def test_debug_disabled_by_default(self):
        self.assertFalse(app.debug)

    def test_unknown_path_is_not_success(self):
        self.assertEqual(app.test_client().get('/missing').status_code, 404)


if __name__ == '__main__':
    unittest.main()

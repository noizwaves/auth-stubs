import authstubs
import unittest

class AuthStubsTestCase(unittest.TestCase):
    def setUp(self):
        authstubs.app.config['TESTING'] = True
        self.app = authstubs.app.test_client()

    def test_landing(self):
        result = self.app.get('/')
        assert result.status_code == 200

if __name__ == '__main__':
    unittest.main()

import fakeid
import unittest

class FakeIdTestCase(unittest.TestCase):
    def setUp(self):
        fakeid.app.config['TESTING'] = True
        self.app = fakeid.app.test_client()

    def test_landing(self):
        result = self.app.get('/')
        assert result.status_code == 200

if __name__ == '__main__':
    unittest.main()

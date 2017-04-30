import fakeid
import unittest
from json import loads


class FakeIdTestCase(unittest.TestCase):
    def setUp(self):
        fakeid.app.config['TESTING'] = True
        self.app = fakeid.app.test_client()

    def test_landing(self):
        result = self.app.get('/')

        assert result.status_code == 200

    def test_google_auth(self):
        result = self.app.get('/google/oauth2/auth?redirect_uri=http%3A%2F%2Fqux.com&state=garply')

        assert result.status_code == 302
        assert result.headers['Location'] == 'http://qux.com?code=baz&state=garply'

    def test_google_token(self):
        result = self.app.post('/google/oauth2/token')

        assert result.content_type == 'application/json'
        assert loads(result.data) == {'access_token': 'waldo'}

    def test_google_info(self):
        result = self.app.get('/google/oauth2/info')

        assert result.status_code == 200
        assert result.content_type == 'application/json'

        body = loads(result.data)
        assert body['id'] == 'foo-bar'
        assert body['displayName'] == 'Foo Bar'
        assert body['emails'][0]['value'] == 'foobar@example.com'

if __name__ == '__main__':
    unittest.main()

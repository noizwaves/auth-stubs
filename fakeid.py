from flask import Flask, jsonify, redirect, request
from urllib.parse import urlencode

app = Flask(__name__)


@app.route('/')
def landing():
    return ''


@app.route('/google/oauth2/auth')
def google_auth():
    uri = request.args.get('redirect_uri')
    state = request.args.get('state')

    qs = urlencode({
        'code': 'baz',
        'state': state
    })

    return redirect(uri + '?' + qs)


@app.route('/google/oauth2/token', methods=['POST'])
def google_token():
    return jsonify({'access_token': 'waldo'})


@app.route('/google/oauth2/info')
def google_info():
    return jsonify({
        'id': 'foo-bar',
        'displayName': 'Foo Bar',
        'emails': [{
            'value': 'foobar@example.com'
        }]
    })

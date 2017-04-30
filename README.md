# fakeid
Simple OAuth 2.0 stubs for automated feature tests

## Quick Start

1) Install Python 3.6.1
1) Install dependencies via `pip install -r requirements.txt`
1) Start server via `FLASK_APP=fakeid.py flask run`

## About
 
It should be easy for web developers to test their applications.
External dependencies should be mocked during feature tests, but often this is not done.
It is quicker and easier to deal with real systems that to stub them - this is very true for external authentication systems like OAuth 2.0.

In reality, these services can stubbed easily.
FakeID is an implementation of these stubs.
This project has several major goals:

1) Serve as an example of how major authentication services can be stubbed.
1) <something about being a ready to go / installable replacement for real services>.
1) Power a hosted stub service for all to use.

## Deployment

This server is hosted on Pivotal Web Services.

To deploy, run `cf push fakeid`.

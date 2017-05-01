# fakeid
Simple OAuth 2.0 stubs designed for feature testing applications.

## Quick Start

1) Install Python 3.6.1
1) Install dependencies via `pip install -r requirements.txt`
1) Start server via `FLASK_APP=fakeid.py flask run`
1) Configure your feature tests to authenticate at `http://127.0.0.1:5000/`

## About
 
It should be easy for web developers to test their applications.
External dependencies should be mocked during feature tests, but often this is not done.
It is quicker and easier to deal with real systems that to stub them - this is very true for external authentication systems like OAuth 2.0.

In reality, these services can stubbed easily.
FakeID is an implementation of these stubs.
This project has several major goals:

1) Serve as an example of how major authentication services can be stubbed.
1) <something about being a ready to go / installable replacement for real services>.
1) Power a hosted service for all to use, namely [https://fakeid.cfapps.io](https://fakeid.cfapps.io).

## Use

To use FakeID with your feature tests, simply configure your application's auth to use a FakeID server.

For example, to configure an ASP.NET Core application using Google Authentication, do:

```csharp
app.UseGoogleAuthentication(new GoogleOptions()
{
    AuthorizationEndpoint = "https://fakeid.cfapps.io/google/oauth2/auth",
    TokenEndpoint = "https://fakeid.cfapps.io/google/oauth2/token",
    UserInformationEndpoint = "https://fakeid.cfapps.io/google/oauth2/info"
});
```

Now, after "logging in" through "Google", your current user will be Foo Bar.

## Deployment

This server is hosted on Pivotal Web Services.

To deploy, run `cf push fakeid`.

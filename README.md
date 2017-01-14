# saucypy
Python Wrapper for SauceLabs API

## Usage
To import SaucyPy, simply copy `saucypy.py` into your project root and then `import saucypy`

When using the library, you must pass each function call an `auth` object, which you can create by running `sauceaccount = saucypy.auth('SauceUser', 'SauceAPIKey')`

Alternatively, if you have your credentials in the environment, such as when running in jenkins or storing configs in an SCM, you can impot these by running `sauceaccount = saucypy.auth(os.environ['sauceuser'], os.environ['saucepass'])`
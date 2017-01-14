# SaucyPy
Python Wrapper for SauceLabs API

## Usage
To import SaucyPy, simply copy `saucypy.py` into your project root and then `import saucypy`

When using the library, you must pass each function call an `auth` object, which you can create by running

```sauceaccount = saucypy.auth('SauceUser', 'SauceAPIKey')```

Alternatively, if you have your credentials in the environment, such as when running in jenkins or storing configs in an SCM, you can impot these by running

```sauceaccount = saucypy.auth(os.environ['sauceuser'], os.environ['saucepass'])```

## Plans
At the moment, SaucyPy isn't available in NPM, but I plan to polish it and create a module quite soon. Feel free to add a pull request if you'd like to contribute.

## License
Licensed under v2.0 of the Apache License. Please read the attached license contained within the `LICENSE` file in this directory.
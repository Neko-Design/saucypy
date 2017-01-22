# SaucyPy
Python Wrapper for SauceLabs API

## Available Functions
SaucyPy currently supports the below SauceLabs features:

* List Sub-Accounts
* List Siblng Accounts
* List Automated Builds
* List Individual Builds
* Fuzzy Search for Builds
* User Creation
* User Management
* SauceLabs Status Information

## Usage
To import SaucyPy, simply copy `saucypy.py` into your project root and then `from saucypy import SaucyPy`

When using the library, you must create each sauce object with its own user credentials, like so:

```sauceaccount = SaucyPy('SauceUser', 'SauceAPIKey')```

Alternatively, if you have your credentials in the environment, such as when running in jenkins or storing configs in an SCM, you can import these by running

```sauceaccount = SaucyPy(os.environ['sauceuser'], os.environ['saucepass'])```

## Plans
At the moment, SaucyPy isn't available in PIP, but I plan to polish it and create a module quite soon. Feel free to add a pull request if you'd like to contribute.

## License
Licensed under v2.0 of the Apache License. Please read the attached license contained within the `LICENSE` file in this directory.
```
 ____                         ____        
/ ___|  __ _ _   _  ___ _   _|  _ \ _   _ 
\___ \ / _` | | | |/ __| | | | |_) | | | |
 ___) | (_| | |_| | (__| |_| |  __/| |_| |
|____/ \__,_|\__,_|\___|\__, |_|    \__, |
                        |___/       |___/ 
```

# SaucyPy
Python Wrapper for SauceLabs API

## Available Functions
SaucyPy currently supports the below SauceLabs features:

* [Build Information](docs/builds.md)
  * List Automated Builds
  * List Individual Builds
  * Fuzzy Search for Builds
  * Get Build Detail
  * Get Job Detail
* [Account Information](docs/accounts.md)
  * List Sub-Accounts
  * List Siblng Accounts
  * User Creation
* [Status Information](docs/status.md)
  * SauceLabs Status Information
  * Supported Platforms

## Installation
To install SaucyPy, you can simply run `pip install saucypy` to automatically download the latest build.

Alternatively, you can clone this git repo and copy the saucypy directory into your project.

## Usage
To import SaucyPy, simply copy `saucypy.py` into your project root and then `from saucypy import SaucyPy`

When using the library, you must create each sauce object with its own user credentials, like so:

```sauceaccount = SaucyPy('SauceUser', 'SauceAPIKey')```

Alternatively, if you have your credentials in the environment, such as when running in jenkins or storing configs in an SCM, you can import these by running

```sauceaccount = SaucyPy(os.environ['sauceuser'], os.environ['saucepass'])```

## Plans
I'll try and commit new features regularly to bring SaucyPy up to feature parity with the main SauceLabs API. Feel free to add a pull request if you'd like to contribute.

## License
Licensed under v2.0 of the Apache License. Please read the attached license contained within the `LICENSE` file in this directory.

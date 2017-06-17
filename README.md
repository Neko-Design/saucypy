# SaucyPy
Python Wrapper for SauceLabs API. [Nice Documentation is Now Available!](https://docs.ewenmccahon.me/saucypy/)

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

`sauceaccount = SaucyPy('SauceUser', 'SauceAPIKey')`

Alternatively, if you have your credentials in the environment, such as when running in jenkins or storing configs in an SCM, you can import these by running

`sauceaccount = SaucyPy(os.environ['sauceuser'], os.environ['saucepass'])`

## Documentation
[SaucyPy Documentation](https://docs.ewenmccahon.me/saucypy/) is available both in this readme file and on my personal site in an easy to read format. The hosted version is located at [https://docs.ewenmccahon.me/saucypy/](https://docs.ewenmccahon.me/saucypy/)

## Projects Using SaucyPy
For some inspiration of what you can do with SaucyPy, here's a few projects built using it.

### SaucyBot
SaucyBot can be triggered to pull information from SauceLabs and Cucumber and send a compact report to a Slack channel.

![SaucyBot Screenshot](https://ewenmccahon.me/cloud/files/4f093ff108.png)

## Plans
I'll try and commit new features regularly to bring SaucyPy up to feature parity with the main SauceLabs API. Feel free to add a pull request if you'd like to contribute.

## License
Licensed under v2.0 of the Apache License. Please read the attached license contained within the `LICENSE` file in this directory.

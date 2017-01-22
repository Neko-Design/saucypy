Status Information
==================

Using SaucyPy to check SauceLabs Status. Import SaucyPy and create a new instance:

```
from saucypy import SaucyPy
sauceaccount = SaucyPy('SauceUser', 'SauceAPIKey')
```

Then you can call the status functions:

### Get SauceLabs System Status
The get_sauce_status() function returns a dictionary of system statistics:

```
status = sauceaccount.get_sauce_status()
print status['service_operational']
```

### Get Available Testing Platforms
The get_sauce_platforms() function returns a dictionary of available VMs:

```
platforms = sauceaccount.get_sauce_platforms()
for platform in platforms:
    print platform['long_name']
```
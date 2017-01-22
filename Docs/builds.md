Build Management
================

Using SaucyPy to manage builds. Import SaucyPy and create a new instance:

```
from saucypy import SaucyPy
sauceaccount = SaucyPy('SauceUser', 'SauceAPIKey')
```

Then you can list and search all builds created using that account:

### Listing all Builds
The get_builds() function will return a dictionary of all builds run under the calling account:

```
all_builds = sauceaccount.get_builds()
for build in all_builds:
    print build['name']
```

### List a Single Build
The get_build() function returns the same dictionary as a child of the get_builds() function:

```
single_build = sauceaccount.get_build('build-id-21345')
print single_build['name']
```

### Search for a Build
The search_builds() function performs a string search over the results of get_builds() returning a dictionary of matching results:

```
matching_builds = sauceaccount.search_builds('partial-build-id')
for build in matching_builds:
    print build['name']
```
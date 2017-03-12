Account Management
==================

Using SaucyPy to manage SauceLabs accounts. Import SaucyPy and create a new instance:

```
from saucypy import SaucyPy
sauceaccount = SaucyPy('SauceUser', 'SauceAPIKey')
```

Then you can list and create SauceLabs accounts:

### List All Child Accounts
The get_child_accounts() function returns a dictionary of account information:

```
child_accounts = sauceaccount.get_child_accounts()
for account in child_accounts:
    print account['first_name']
```

### List Sibling Accounts
If your account has adminstrative priviledges, the get_sibling_accounts() can list all accounts at the same level as yours:

```
sibling_accounts = sauceaccount.get_sibling_accounts()
for account in sibling_accounts:
    print account['first_name']
```

### Create Child Accounts
the create_account() function creates a new child account under the calling account:

```
result = create_user("Username", "Password", "email@server.com", "Full Name")
```
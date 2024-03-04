# OpenSMTPD-Admin

Web interface for OpenSMTPD that manages credentials for virtual email accounts. Currently limited to only regular users. Extended version with role based access management will be implemented later on. Statistics for password updates and email traffic are provided on a per-user basis.

## Development

Get started with local development in two steps:

### Configuration

Replace the values in the provided .env with your desired values:

* `ENVIRONMENT`: The environment to run your app in (either `development` or `production`)
* `FLASK_DEBUG`: Whether to enable debug logging (either `True` or `False`)
* `SECRET_KEY`: Randomly generated string of characters used to encrypt app data ([RTFM](https://flask.palletsprojects.com/en/3.0.x/config/#SECRET_KEY))
* `SQLALCHEMY_DATABASE_URI`: Connection URI of a SQL database

### Installation

Bootstrap and start the application with `make deploy`

```shell
git clone git@github.com:alenmeister/opensmtpd-admin.git
cd opensmtpd-admin
make deploy
```

## TODO
- [ ] Validate fields using regex when updating password
- [ ] Add `last_changed` column to credentials table
- [ ] Implement logic for role based identities
- [ ] Fetch statistics from the reporting API provided by OpenSMTPd
- [ ] Deploy and execute a dry-run on OpenBSD with httpd as proxy

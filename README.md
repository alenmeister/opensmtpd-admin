# OpenSMTPd-Admin

Web interface for OpenSMTPd that manages credentials for virtual email accounts. Currently limited to regular users. Extended version with administrator roles will be implemented later on. Statistics for password updates and email traffic are provided on a per-user basis.

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
- [ ] Implement regex validation for password updates
- [ ] Add `last_changed` column to credentials table
- [ ] Fetch statistics from the reporting API provided by OpenSMTPd
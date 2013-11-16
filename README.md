# bookwork

## Setup

### \*nix

The following are needed:
  - Python 2.6 or greater
  - virtualenv
  - Postgres Development Libraries and Server

```
git clone git@github.com:guharakesh/bookwork-app.git
cd bookwork-app
virtualenv --no-site-packages env
source env/bin/activate
pip install -r develop-requirements.txt
honcho start
```

You can now navigate to [http://localhost:5000](http://localhost:5000) to view the application.

### Windows
*(shrug)*

### Configurable Environment Variables

Environment Variables can be supplied by the shell environment to configure the application

* `DATABASE_URL`
    - Sample Value: `postgres://bookwork:securepassword@localhost:5432/bookwork`
    - Configures the Postgres database connection

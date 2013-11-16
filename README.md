# bookwork

## Setup

### local \*nix

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

Use Vagrant!

### Vagrant

1. Download and Install [Virtual Box](https://www.virtualbox.org/wiki/Downloads).

2. Download and Install [Vagrant](http://downloads.vagrantup.com/) version 1.3.0 or greater.

3. `git clone git@github.com:guharakesh/bookwork-app.git`

4. `cd bookwork-app`

5. `vagrant up`

6. Login and change to application user

  - `vagrant ssh`
  - `sudo su - bookwork`
  - `cd app`
  - `source env/bin/activate`
  - `honcho start`

7. You can now navigate to [http://192.168.50.2:5000](http://192.168.50.2:5000) to view the application.

### Configurable Environment Variables

Environment Variables can be supplied by the shell environment to configure the application

* `DATABASE_URL`
    - Sample Value: `postgres://bookwork:securepassword@localhost:5432/bookwork`
    - Configures the Postgres database connection

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
cp .env.sample .env
honcho -e .env start
```

You can now navigate to [http://localhost:5000](http://localhost:5000) to view the application.

### Vagrant on Windows

1. Download and Install [Virtual Box](https://www.virtualbox.org/wiki/Downloads).

2. Download and Install [Vagrant](http://downloads.vagrantup.com/) version 1.3.0 or greater.

3. Download and Install [PuTTY](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)
  - `putty.exe` needs to be available on your `Path` for step 9 to work.

4. Download and Install [PuTTYgen](http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html)

5. Convert the Vagrant private key at `~\.vagrant.d\insecure_private_key` to a PuTTY compatible key file with `puttygen.exe` and save the output to `~\.vagrant.d\insecure_private_key.ppk`

6. `git clone git@github.com:guharakesh/bookwork-app.git`

7. `cd bookwork-app`

8. `vagrant up`

9. Login and change to application user
  - `vagrant putty` 
  - `sudo su - bookwork`
  - `cd app`
  - `source env/bin/activate`
  - `cp .env.sample .env`
  - `honcho -e .env start`

10. You can now navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to view the application.

#### Note

If you'd like to perform git commits and pushes from within your Vagrant environment, before performing such operations:

```
git config --global user.name "John Doe"
git config --global user.email johndoe@example.com
```

Replacing the name and email address with your preferred name/email (match to github for fun)

**You'll need to do this after every vagrant destroy/vagrant up cycle**

### Vagrant on OS X or Linux

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
  - `honcho -e .env start`

7. You can now navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to view the application.

If you'd like to enable `DEBUG` and `TEMPLATE_DEBUG` (in DEVELOPMENT):

    cp bookwork/local_settings.py.sample bookwork/local_settings.py

### Configurable Environment Variables

Environment Variables can be supplied by the shell environment to configure the application

* `DATABASE_URL`
    - Sample Value: `postgres://bookwork:securepassword@localhost:5432/bookwork`
    - Configures the Postgres database connection
* `EMAIL_HOST`
* `DEFAULT_FROM_EMAIL`
* `MAILGUN_ACCESS_KEY`
* `MAILGUN_SERVER_NAME`
* `SECRET_KEY`

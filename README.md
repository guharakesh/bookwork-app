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
  - `honcho start`

10. You can now navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to view the application.

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
  - `honcho start`

7. You can now navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000) to view the application.

### Configurable Environment Variables

Environment Variables can be supplied by the shell environment to configure the application

* `DATABASE_URL`
    - Sample Value: `postgres://bookwork:securepassword@localhost:5432/bookwork`
    - Configures the Postgres database connection


/etc/pki/rpm-gpg/RPM-GPG-KEY-PGDG-93:
  file.managed:
    - source: salt://postgresql-server/93/config/RPM-GPG-KEY-PGDG-93

/etc/yum.repos.d/pgdg-93-centos.repo:
  file.managed:
    - source: salt://postgresql-server/93/config/pgdg-93-centos.repo
    - requre:
      - file: /etc/pki/rpm-gpg/RPM-GPG-KEY-PGDG-93

postgresql93-server:
  pkg:
    - installed
    - require:
      - file: /etc/yum.repos.d/pgdg-93-centos.repo
  service:
    - name: postgresql-9.3
    - running
    - reload: True
    - watch:
      - file: /var/lib/pgsql/9.3/data/pg_hba.conf
    - require:
      - file: /etc/yum.repos.d/pgdg-93-centos.repo
  cmd.wait:
    - name: service postgresql-9.3 initdb
    - watch:
      - pkg: postgresql93-server

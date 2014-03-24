
/etc/pki/rpm-gpg/RPM-GPG-KEY-PGDG-93:
  file.managed:
    - source: salt://postgresql-server/93/config/RPM-GPG-KEY-PGDG-93

pgdg93:
  pkgrepo.managed:
    - humanname: PostgreSQL 9.3 $releasever - $basearch
    - baseurl: http://yum.postgresql.org/9.3/redhat/rhel-$releasever-$basearch
    - gpgcheck: 1
    - gpgkey: file:///etc/pki/rpm-gpg/RPM-GPG-KEY-PGDG-93

postgresql93-server:
  pkg:
    - installed
    - require:
      - pkgrepo: pgdg93
  service:
    - name: postgresql-9.3
    - running
    - reload: True
    - watch:
      - file: /var/lib/pgsql/9.3/data/pg_hba.conf
    - require:
      - pkgrepo: pgdg93
  cmd.wait:
    - name: service postgresql-9.3 initdb
    - watch:
      - pkg: postgresql93-server

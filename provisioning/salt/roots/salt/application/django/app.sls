
include:
  - pkg.git

{% set apps = [] %}
{% for k,v in pillar.items() %}
  {% if k.startswith('django-app') %}
    {% do apps.append(v) %}
  {% endif %}
{% endfor %}

{% for app in apps %}

{% set app_name = app['friendly_name'] %}

{{ app_name }}-python-deps:
  pkg.installed:
    - pkgs:
      - python
      - python-devel
      - make
      - gcc
      - python-virtualenv

{{ app_name }}-user:
  group.present:
    - name: {{ app_name }}
  user.present:
    - name: {{ app_name }}
    - home: /home/{{ app_name }}
    - gid: {{ app_name }}
    - require:
      - group: {{ app_name }}

/home/{{ app_name }}:
  file.directory:
    - mode: 750
    - require:
      - user: {{ app_name }}

/home/{{ app_name }}/.ssh:
  file.directory:
    - user: {{ app_name }}
    - group: {{ app_name }}
    - mode: 700
    - makedirs: True

/home/{{ app_name }}/.ssh/id_rsa:
  file.managed:
    - context:
      app_name: {{ app['name'] }}
    - user: {{ app_name }}
    - group: {{ app_name }}
    - mode: 600
    - source: salt://application/django/config/private_key.jinja
    - template: jinja
    - require:
      - file: /home/{{ app_name }}/.ssh
      - user: {{ app_name }}

github.com-{{ app_name }}:
  ssh_known_hosts:
    - name: github.com
    - present
    - user: {{ app_name }}
    - hash_hostname: False
    - fingerprint: 16:27:ac:a5:76:28:2d:36:63:1b:56:4d:eb:df:a6:48

{{ app_name }}-source:
  git.latest:
    - name: {{ app['source'] }}
    - rev: {{ app['revision'] }}
    - target: /home/{{ app_name }}/app
    - runas: {{ app_name }}
    - require:
      - pkg: git
      - user: {{ app_name }}
      - file: /home/{{ app_name }}/.ssh/id_rsa
      - ssh_known_hosts: github.com-{{ app_name }}

{{ app_name }}-virtualenv:
  virtualenv.managed:
    - name: /home/{{ app_name }}/app/env
    - system_site_packages: False
    - runas: {{ app_name }}
    - requirements: /home/{{ app_name }}/app/requirements.txt

{% if 'system-deps' in app %}
{{ app_name }}-system-deps:
  pkg.installed:
    - pkgs:
      {% for package in app['system-deps'] %}
      - {{ package }}
      {% endfor %}
{% endif %}

{% endfor %}

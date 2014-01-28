include:
  - application.django.app

{% set apps = [] %}
{% for k,v in pillar.items() %}
  {% if k.startswith('django-app') %}
    {% do apps.append(v) %}
  {% endif %}
{% endfor %}

{% for app in apps %}

{% set app_name = app['friendly_name'] %}

{% if app_name == "bookwork" %}

/home/{{ app_name }}/app/bookwork/local_settings.py:
  file.managed:
    - contents_pillar: {{ app['name'] }}:local_settings
    - user: {{ app_name }}

{% endif %}

{% endfor %}

base:
  '*':
    - base.sanity

  'roles:django-app-bookwork':
    - match: grain
    - application.bookwork

django-app-bookwork:
  name: django-app-bookwork
  friendly_name: bookwork
  source: git@github.com:guharakesh/bookwork-app.git
  revision: master
  deploy_key: |
    -----BEGIN RSA PRIVATE KEY-----
    MIIEoQIBAAKCAQEAqDVM/+bskRg5X13KRoeek8oF8cHQ4L8CrpzBw+c80m0jccLH
    jiVJp+PNfH4efwjBK1AigjuzAuTYk1RVAaxv3W7gi3wYnolBDZc3cF1aesVVymls
    fpeBITBVU3f/BMv6rdYPec/JgYbU4nZKuCj2LZccF65YA5UTi1Buhg6qgv8LmkWe
    KqH5ExyKF6D1PB+JoaTiEIAEdbFZEJEpjKLc55y2ae6W+y7/DCE2upc9jJEQ+TRq
    jQO3bpixHXyvjOwNPb9MWRZVQJYZzQ1uw+yuAInRqXjGNeuH/+5NUb4ktays1si4
    pKrYKgVllBbATxz/zQsJShgyMakeqI2RZZpoZQIBIwKCAQAOavf4rWS7+sMWzYZd
    0Rw4jai881sL8x18rlnAVaYgqkTd3X7Rq2y2nn9T0EvBvuv8ZfRUTkKLOC/SHSvb
    km/9CYD2A1KRPvbyiU3lD1Dl86hEjLGHMY65s6+Kz8Vmz6fFweQRwVpqMCDgNgZn
    jnuAQCb6tywdkG9jtm/fmttqUDxmbAfARDhZ4v9aB4wwQnFfobwsePRo033u6EOa
    w96aNzSZfzyYGG8sBImWUH0kUhLXFlNaURqrfYeeJwcOLZ+RPTgvwDS30DNe/P/C
    3bmlh1POCx+wzVF54Bu2aH8iNCEffFhBEDwr8mbhfUlCTWhzMmUEAwbzX0WBwGlx
    TqqrAoGBAOA2dmO9hkaXQioVxSF7ffhI4vDh/W/VHxiAnpOCUMOxlmz5BVzHpqVm
    IFLW8ToGSLSPBJXNtUN4puYLHWtbEY2dnyaQg6c+jelcnUnlQnjfn5bVABV2bDiF
    Vz7MM0cepqgyPe8fPXWOfxYlriiAVfeamYsEMNTh6e3Iz9+Em+FtAoGBAMAOODVU
    qnZjLLzng8WNmmanuF3SVMaERC4CB4FSD57Zgjkcx3dFFfNPIUlfUE+JNYCc1ghM
    Rud6jpzdQpyMcOSsVeubevGhiy5xkyen5L9AahPF9umwzpjstcs1cmeypdeKisPj
    r/nwJPR9CEEelUWdJY5sbrbjEltLTjkMaL/ZAoGAebcqU2bifheY8kZVEi0Yf3gG
    Kv5WYUfPDU0i4lyvgC00ZwrXBnsCsY82HldtAj3s9E2jZ0PIzNsYxgYIp/48updl
    Bk5zWsovx9Mw0FfiQZ33jGUAC6avxulMnm7aAglTKBtGMVoaDJ3P9hR0fGLs1t7l
    ozzKDSouiGWyrInQ9rcCgYEAtRS4p0/T6/cbjYnUA2hBHvXoWHXa5w7+dIWSDDdt
    0ElsJzhkS+INYb+jCqpTCSmY2FlcFnPN0u/ljJYaO9TfeIU7EVgU1THpoNF8HhNU
    BMe0eQscAOiIRwsRzjm1Aq/A78vEqhEw5FdzTOrqhoqMvfqRH+KURglL0muS5VTX
    ytMCgYBKMHqbhc1NF0s6tuvc5xeTBmUo2Utw2jWLk/Qxpeh2JAZ07QnKxSDMcN3X
    5DKcJDSbGcm+cbWCZwsOZUjsi0mSwn43I61l6rPwL7NTlaNpNfLxQ7fWg5GbVETL
    0Eoi3KzZc76167IQxp924elJU5qmaHyKGM45wGEOmICYfHaoxQ==
    -----END RSA PRIVATE KEY-----
  system-deps:
    - postgresql-devel
  database:
    - type: postgres
    - name: bookwork
    - user: bookwork
    - pass: bookwork
    - host: localhost
    - port: 5432

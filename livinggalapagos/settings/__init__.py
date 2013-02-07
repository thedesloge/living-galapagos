import socket

HOST_NAME = socket.gethostname()
HOSTS = {
    'Donaldo.local': 'dons_machine',
    'prod': 'prod-server',
    'dev': 'dev-server'
}

from local import *

if HOST_NAME == HOSTS['Donaldo.local']:
    try:
        from uat import *
    except Exception, e:
        pass
elif HOST_NAME == HOSTS['dev']:
    try:
        from dev import *
    except Exception, e:
        pass
elif HOST_NAME == HOSTS['prod']:
    try:
        from production import *
    except Exception, e:
        pass

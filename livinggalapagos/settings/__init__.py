import socket

HOST_NAME = socket.gethostname()
HOSTS = {
    'dons_machine': 'Donaldo.local',
    'prod': 'prod-server',
    'dev': 'dev-server'
}

from local import *

if HOST_NAME == HOSTS['dons_machine']:
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

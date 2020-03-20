#!/usr/bin/env python
import sys

import django
from django.conf import settings
from django.core.management import call_command
from django.test.runner import DiscoverRunner

if not settings.configured:
    settings.configure(
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.sqlite3',
                'NAME': ':memory:',
            },
        },
        INSTALLED_APPS=(
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'stickymessages',
            'stickymessages.tests',
        ),
        ROOT_URLCONF=None,
        USE_TZ=True,
        SECRET_KEY='mysecretkey',
        STATIC_URL='/'
        )

django.setup()

test_runner = DiscoverRunner(verbosity=1)
failures = test_runner.run_tests(['stickymessages', ])
if failures:
    sys.exit(failures)

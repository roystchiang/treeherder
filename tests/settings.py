from treeherder.config.settings import *

DATABASES["default"]["TEST"] = {"NAME": "test_treeherder"}
TREEHERDER_TEST_PROJECT = "%s_jobs" % DATABASES["default"]["TEST"]["NAME"]

# this makes celery calls synchronous, useful for unit testing
CELERY_ALWAYS_EAGER = True
CELERY_EAGER_PROPAGATES_EXCEPTIONS = True

# Reconfigure pulse to operate on default vhost of rabbitmq
PULSE_URI = BROKER_URL
PULSE_EXCHANGE_NAMESPACE = 'test'

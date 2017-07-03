import os
import sys

sys.path.append(os.environ["PROJECT_PATH"])

os.environ["DJANGO_SETTINGS_MODULE"] = os.path.join((os.environ["PROJECT_PATH"],
                                                     "travel_platform",
                                                     "settings.py"))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()


# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    # admin
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns.append(
        url(
            r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {
                'document_root': settings.MEDIA_ROOT,
                'show_indexes': True
            }
        ),
    )

# -*- coding: utf-8 -*-
from django.conf.urls import include, url

from apps.rola.op_views import PulpitView

#from .views import UIDRedirect

urlpatterns = []
urlpatterns = [
    url(r'^$', PulpitView, name='pulpit'),

    url(r'^oferta/', include('apps.oferta.op_urls', namespace='oferta')),
    ]

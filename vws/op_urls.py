# -*- coding: utf-8 -*-
from django.conf.urls import include, url


urlpatterns = []
urlpatterns = [
    url(r'^op/', include('vws.op.urls',namespace='op')),
    ]


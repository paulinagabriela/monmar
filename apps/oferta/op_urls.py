from django.conf.urls import url
from . import op_views as v

urlpatterns = [
        url(r'^$', v.oferta_list, name='oferta-lista'),
        ]

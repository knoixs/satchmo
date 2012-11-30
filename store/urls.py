from django.conf.urls import patterns, url
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import ugettext_lazy as _

from satchmo_store.urls import urlpatterns

urlpatterns += patterns('store.localsite.views',
    (r'^$', 'index', {}, 'localsite_index'),
    (r'^impressum/$', 'impressum', {}, 'localsite_impressum'),
#    (r'^offers-and-prices/$', 'offers_and_prices', {}, 'localsite_offers_and_prices'),
)

urlpatterns += i18n_patterns('',
    url(_(r'^contact/$'), 'satchmo_store.shop.views.contact.form', {}, 'satchmo_contact'),
    url(_(r'^offers-and-prices/$'), 'store.localsite.views.offers_and_prices', name='localsite_offers_and_prices'),
)


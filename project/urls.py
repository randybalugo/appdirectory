from django.conf import settings
from django.conf.urls.defaults import patterns, url, include

from app.views import DeviceAppListView, ArtistAppListView, SearchAppListView,\
    CategoryAppListView, TopAppListView, PaidAppListView,\
    FreeAppListView, NewAppListView, UpdateAppListView, AppsByRatingView,\
    AppDetailView, TopCategoryAppListView, SequenceDetailView,\
    ChangeCurrencyView, PriceDropListView
from app.sendmail import EmailItView
from app.activitygraph import PriceGraphView, VersionGraphView, Top250GraphView
from django.contrib import admin
from django.contrib.comments.models import Comment
from django.views.generic.base import RedirectView

admin.site.register(Comment)

#FIXME remove in production
urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }))

urlpatterns += patterns('',
    (r'^comments/', include('django.contrib.comments.urls')),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    
    url(r'^$', RedirectView.as_view(url='new_apps/'), name="home"),
    
    url(r'^device/(?P<device>\w+)/$', DeviceAppListView.as_view(), name="device"),
    url(r'^top_apps/$', TopAppListView.as_view(), name="top_apps"),
    url(r'^price_drop/$', PriceDropListView.as_view(), name="price_drop"),
    url(r'^rating/$', AppsByRatingView.as_view(), name="rating"),
    url(r'^free_apps/$', FreeAppListView.as_view(), name="free_apps"),
    url(r'^paid_apps/$', PaidAppListView.as_view(), name="paid_apps"),
    url(r'^new_apps/$', NewAppListView.as_view(), name="new_apps"),
    url(r'^update_apps/$', UpdateAppListView.as_view(), name="update_apps"),
    url(r'^artist/(?P<artist_id>\d+)/$', ArtistAppListView.as_view(), name="artist_applications"),
    url(r'^category/(?P<category>[&\w\s.]+)/$', CategoryAppListView.as_view(), name="category_applications"),
    url(r'^top_category/(?P<category>[&\w\s.]+)/$', TopCategoryAppListView.as_view(), name="top_category_applications"),
    url(r'^search', SearchAppListView.as_view(), name="search"),
    url(r'^currency/$', ChangeCurrencyView.as_view(), name="change_currency"),
    
    url(r'^email/(?P<app_id>\d+)/$', EmailItView.as_view(), name="email_app"),
    url(r'^detail/(?P<pk>\d+)/$', AppDetailView.as_view(), name="app_detail"),
    url(r'^detail/(?P<pk>\d+)/(?P<slug>[-\w]+)/$', AppDetailView.as_view(), name="app_detail_slug"),
    
    
    url(r'^price_graph/(?P<app_id>\d+)/$', PriceGraphView.as_view(), name="price_graph"),
    url(r'^version_graph/(?P<app_id>\d+)/$', VersionGraphView.as_view(), name="version_graph"),
    url(r'^top_graph/(?P<app_id>\d+)/$', Top250GraphView.as_view(), name="top_graph"),
    
    
    url(r'^sequence/(?P<pk>\d+)/$', SequenceDetailView.as_view(), name="detail_sequence"),
    
)



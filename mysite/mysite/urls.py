from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)


urlpatterns += patterns('mysite.views',
	(r'^hello/$', 'hello'),
	(r'^time/$', 'current_datetime'),
	(r'^time/plus/(\d{1,2})/$', 'hours_ahead'),
    (r'^browser/$', 'display_browser'),
    (r'^meta/$', 'display_meta'),
    (r'^arhiv/(?P<year>\d{4})/(?P<month>\d{2})/$', 'show_archive_entries'),
    (r'^postevanka1/$','show_results', dict(template_name='temp1.html')),
    (r'^postevanka2/$','show_results', dict(template_name='temp2.html')),
)

urlpatterns += patterns('mysite.books.views',
    (r'^books/publishers/$', 'show_publishers'),
    (r'^search/$', 'search_book'),
)

from django.conf.urls import patterns, include, url
from movie.views import add_movie, show_movies

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^add-movie/$', add_movie),
    (r'^show-movies/$', show_movies),
    # Examples:
    # url(r'^$', 'movies.views.home', name='home'),
    # url(r'^movies/', include('movies.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

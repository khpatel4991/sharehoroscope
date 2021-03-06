from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^thank-you/', 'portfolio.views.thankyou', name='thankyou'), #url(name of site, file that's called, html name)
    url(r'^about-us/', 'portfolio.views.aboutus', name='aboutus'),
    url(r'^user-page/', 'portfolio.views.userpage', name='userpage'),
    url(r'^graph/', 'portfolio.views.graph', name='graph'),
    url(r'^suggestion/$', 'portfolio.views.suggestion', name='suggestion'),
    url(r'^add_to_portfolio/(?P<stock_id>\d+)/(?P<user_id>\d+)/$', 'portfolio.views.addtoportfolio'),
    url(r'^remove_from_portfolio/(?P<stock_id>\d+)/(?P<user_id>\d+)/$', 'portfolio.views.removefromportfolio'),
    url(r'^predict/(?P<stock_id>\d+)/(?P<period>\d+)/$', 'portfolio.views.predict'),
    url(r'^current/(?P<stock_id>\d+)/$', 'portfolio.views.current'),
    url(r'^history/(?P<stock_id>\d+)/$', 'portfolio.views.history', name='historicaldata'),
    url(r'^plot/(?P<stock_id>\d+)/(?P<time_p>\d+)/$', 'portfolio.views.plot', name='plot'),
    #url(r'^plottt/', 'portfolio.views.demo_linewithfocuschart', name='linewithfocuschart'),
    #url(r'^thank-you/', 'portfolio.views.thankyou', name='thankyou'), #url(name of site, file that's called, html name)
    #url(r'^get/(?P<article_id>\d+)/$', 'articlaphe.views.article'),
    #url(r'^accounts/profile/', ProfileView.as_view(), name='profile')
)
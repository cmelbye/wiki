from django.conf.urls.defaults import *
from yourwiki import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'yourwiki.wiki.views.index', name="index"),
	url(r'^wiki/(?P<slug_name>[\w\d\-]+)/$', 'yourwiki.wiki.views.detail', name="detail"),
	url(r'^wiki/ajax/process_sections/$', 'yourwiki.wiki.ajax.process_sections', name="ajax_process_sections"),
	url(r'^wiki/ajax/section_edit/$', 'yourwiki.wiki.ajax.section_edit', name="ajax_section_edit"),
	url(r'^wiki/ajax/show_section/$', 'yourwiki.wiki.ajax.show_section', name="ajax_show_section"),
	
    # Example:
    # (r'^wiki/', include('wiki.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT})
	)

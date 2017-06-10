from django.conf.urls import url
from django.contrib import admin
import post.views
import yansayfalar.views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', post.views.home, name="home"),
    url(r'^post/(?P<post_id>[0-9]+)/$', post.views.post_ayrintilar , name="post_ulas"),
    url(r'^hakkinda',yansayfalar.views.hakkinda, name="hakkinda"),
    url(r'^yansayfa_home',yansayfalar.views.home, name="yansayfa_home"),
    url(r'^contact',yansayfalar.views.contact, name="contact")

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

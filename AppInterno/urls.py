from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login', views.login_view, name="login"),
    url(r'^logout', views.logout_view, name="logout"),
    url(r'^istoric',views.istoric_view,name="istoric"),
    url(r'^email', views.edit,name='edit_favorites'),
    url(r'^statistici', views.statistici_view,name='statistici')
	#url(r'^delete/(?P<del_id>\d+)$', views.deleteContract, name='deleteContr'),

]
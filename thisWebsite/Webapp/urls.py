from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("", views.index, name="home"),
    path("about/",views.about,name="about"),
    path("products/",views.products,name ="products"),
    path("services/",views.services,name="services"),
    #path('test-db-connection/', views.test_db_connection, name='test_db_connection'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("about/",views.about,name="about"),
    path("products/",views.product,name ="product"),
    path("services/",views.services,name="services"),
    #path('test-db-connection/', views.test_db_connection, name='test_db_connection'),
]
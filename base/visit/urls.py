from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="homepage"),
    path('sections/', views.sections, name="sections"),

    #model sections
    path('design/', views.design, name="design"),
    path('smart/', views.smart, name="smart"),
    path('video/', views.video, name="video"),
    # path('mvphome/', include('construct.urls'))

]

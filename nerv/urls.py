from django.urls import path
from . import views

from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'nerv'

urlpatterns = [
    path('', views.index, name='index'),
    path('titanic/', views.predict_titanic, name='titanic'),
    path('iris/', views.predict_iris, name='iris'),
    path('image_classification/' , views.predict_image, name="image_classification"),
    path('sentiments/', views.predict_sentiments, name="sentiments"),
    path("favicon.ico", RedirectView.as_view(url="/static/favicon.ico")),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

from django.urls import path
from .views import HomePageView, AboutPageView, DocsPageView, ContactView, change_language

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('docs/', DocsPageView.as_view(), name='docs'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('change-language/', change_language, name='change_language'),
]

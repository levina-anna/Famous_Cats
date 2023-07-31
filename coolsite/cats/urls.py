from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', CatsHome.as_view(), name='home'), # http://127.0.0.1:8000/
    path('about/', about, name='about'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', CatsCategory.as_view(), name='category'),
]


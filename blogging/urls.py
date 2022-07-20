from django.urls import path
from blogging.views import list_view, detail_view
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    path('login', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', LogoutView.as_view(template_name='logout.html'), name='logout'),
]
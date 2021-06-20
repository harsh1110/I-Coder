from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="basehome"),
    path('<int:blog_id>/', views.blogDetails, name="blogDetails"),
    path('home/', views.homePage, name="home"),
    path('blog/', views.blog, name="blog"),
    path('signup', views.handleSignup, name="handlesignup"),
    path('login', views.handleLogin, name="handlelogin"),
    path('logout', views.handleLogout, name="handlelogout")
]
from django.urls import path
from blog import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path("about/", TemplateView.as_view(extra_context = {'about':'active'},template_name="about.html"), name='about'),
    path('login/', views.Login.as_view(), name='login'),
    path('signup/', views.Signup.as_view(), name='signup'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.user_logout, name='logout'),
    path('addblog/', views.addblog, name='addblog'),
    path('createProfile/', views.profile_form, name='profile_form'),
    path('profileView/', views.profileView, name='profileView'),
    path('changeProfile/', views.changeProfile, name='changeProfile'),
    path('changePass/', views.changePass, name='changePass'),
    path('blogview/<slug:slug>', views.blogview, name='blogview'),
    path('editeblog/<slug:slug>', views.editeblog, name='editeblog'),
    path('deletePost/<slug:slug>', views.deletePost, name='deletePost'),
]
handler404 = "blog.views.page_not_found_view"



from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

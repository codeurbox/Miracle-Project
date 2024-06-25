from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("header/", views.header, name="header"),
    path("registration/", views.registration, name="registration"),
    path("login/", views.loginUser, name="login"),
    path("logout/", views.logoutUser, name="logout"),
    path("profile/", views.profile, name="profile"),
    path("", views.field, name="fields"),
    path("editprofile/", views.Editprofile, name="editprofile"),
    path("group/<str:pk>/", views.groupPage, name="group"),
    path("add_participant/<str:pk>/", views.add_participant, name="add_participant"),
    path("create_group/", views.createGroup, name="create_group")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
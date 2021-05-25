"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from main_app import views
from main_app.views import VerificationView
from django.conf.urls import url, handler404
from django.views.static import serve

urlpatterns = [
    url(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    url(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
    path("admin/", admin.site.urls),
    path("", include("main_app.urls")),
    path("register/", views.register, name="register"),
    path("activate/<uidb64>/<token>", VerificationView.as_view(), name="activate"),
    path("", include("django.contrib.auth.urls")),
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(
            template_name="main_app/password_reset.html"
        ),
        name="reset_password",
    ),
    path(
        "reset_password_sent/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="main_app/password_reset_sent.html"
        ),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="main_app/password_reset_form.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="main_app/password_reset_done.html"
        ),
        name="password_reset_complete",
    ),
    path("accounts/", include("allauth.urls")),
    path('contact_user/', views.contact_user , name="contact_user"),
    path("404_error/", views.page_not_found, name="404_error"),
    path("delete_account/<str:username>", views.delete_account, name="delete_account"),

]
handler404 = "main_app.views.page_not_found"  # noqa

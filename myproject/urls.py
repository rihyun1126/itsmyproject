"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import blog.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog.views.home, name = "home"),
    path('blog/<int:blog_id>/', blog.views.detail, name = "detail"),
    path('newblog/', blog.views.blogpost, name = "newblog"),
    path('portfolio/', portfolio.views.portfolio, name = "portfolio"),
    path('accounts/', include('accounts.urls')),
    path('update/<int:pk>', blog.views.update, name = "update"),
    path('delete/<int:pk>', blog.views.delete, name = "delete"),
    path('blog/update/<int:comment_id>/', blog.views.comment_update, name = "comment_update"),
    path('blog/delete/<int:comment_id>/', blog.views.comment_delete, name = "comment_delete"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )

"""XXX_PROJECT_NAME_XXX URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.views.generic import TemplateView

<<<<<<< HEAD
from django.conf.urls.static import static
from django.conf import settings

=======
>>>>>>> 609159725a8427956399f25bc6c3d39cc33898e1
urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    path('myapp/', include('myapp.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
<<<<<<< HEAD
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
=======
]
>>>>>>> 609159725a8427956399f25bc6c3d39cc33898e1

"""
healthcare_bot URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.templatetags.static import static
from django.http import FileResponse
import os
from django.conf import settings


def serve_logo(request):
    """Serve logo.svg from Next.js out directory at the root path."""
    logo_path = os.path.join(settings.BASE_DIR, 'healthbot-frontend', 'out', 'logo.svg')
    return FileResponse(open(logo_path, 'rb'), content_type='image/svg+xml')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('chat/', include('chatbot.urls')),
    path('location/', include('location.urls')),
    path('admin-panel/', include('admin_panel.urls')),
    path('', RedirectView.as_view(url='/chat/', permanent=False), name='home'),
    path('logo.svg', serve_logo, name='logo'),
    path('favicon.ico', RedirectView.as_view(url=static('favicon.jpeg'), permanent=True)),
]

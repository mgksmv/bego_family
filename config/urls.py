from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from .views import HomeTemplateView, search, SearchListView

urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    
    path('admin/', admin.site.urls),

    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('', HomeTemplateView.as_view(), name='home'),
    path('search/', SearchListView.as_view(), name='search'),

    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html', redirect_authenticated_user=True),
         name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    path('profiles/', include('accounts.urls')),

    path('bego/', include('bego.urls')),
    path('regulations/', include('regulations.urls')),
    path('for-bosses/', include('for_bosses.urls')),
    path('departments/', include('departments.urls')),

    path('soc-package/', include('soc_package.urls')),

    path('inner-life/', include('inner_life.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

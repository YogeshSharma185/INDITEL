from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('accounts/', include('allauth.urls')), # all OAuth operations will be performed under this route
    path('admin/', admin.site.urls),
    path('', include('my_app.urls')),
    path('my_app/', include('my_app.urls')),
    # path('logout', LogoutView.as_view()) # default Django logout view at /logout 
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
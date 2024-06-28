from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('a_propos/', include('a_propos.urls')),
    path('solutions/', include('solutions.urls')),
    path('offres/', include('offres.urls')),
    path('blogues/', include('blogues.urls')),
]

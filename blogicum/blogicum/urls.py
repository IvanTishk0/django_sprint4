from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from pages.views import page_not_found, server_error, csrf_failure

handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'
handler403 = 'pages.views.csrf_failure'

urlpatterns = [
    path('', include('blog.urls'), name='index'),
    path('', include('blog.urls'), name='post_detail'),
    path('', include('blog.urls'), name='category_posts'),
    path('pages/', include('pages.urls'), name='about'),
    path('pages/', include('pages.urls'), name='rules'),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/', include('blog.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

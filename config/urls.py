"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

from rest_framework_simplejwt import views

"""NOTE:djoserについてのメモ↓
      api-auth/jwt/create/：トークン取得
      api-auth/jwt/refresh/：トークン再取得
      api-auth/jwt/verify/：トークン検証"""


urlpatterns = [
    # path('', ) ←TODO:何も指定しない場合どうする
    path('admin/', admin.site.urls),
    path('api-auth/jwt/', views.TokenObtainPairView.as_view()),
    path('api-auth/', include('djoser.urls.jwt')),
    path('api/blog/', include('blog_api.urls')),
    # path('accounts/', include('accounts.urls')),
    # path('blog/', include('blog.urls')),
]



# デバッグ関係
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]

    urlpatterns += static(settings.MEDIA_URL, dcument_root=settings.MEDIA_ROOT)
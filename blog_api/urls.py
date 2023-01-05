from django.urls import path
from . import views

urlpatterns = [
    # path('',)
    path('list/', views.BlogPostListAPIView.as_view()),
    path('retrieve/<str:pk>', views.BlogPostRetrieveAPIView.as_view()),
    path('retrieve_update/<str:pk>', views.BlogPostRetrieveUpdateAPIView.as_view()),
    path('create/', views.BlogPostCreateAPIView.as_view()),
    path('update/', views.BlogPostUpdateAPIView.as_view()),
    path('delete/', views.BlogPostDestroyAPIView.as_view())
]

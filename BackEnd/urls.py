from django.urls import path
from . views import AuthorListCreateView, AuthorRetrieveUpdateDestroyView, BookListCreateView, BookRetrieveUpdateDestroyView
# To get and refresh tokens
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

urlpatterns = [
    path('author/', AuthorListCreateView.as_view(), name="author-list-create"),
    path('author/<int:pk>', AuthorRetrieveUpdateDestroyView.as_view(), name="author-retrieve-update-destroy"),
    path('book/', BookListCreateView.as_view(), name="book-list-create"),
    path('book/<int:pk>', BookRetrieveUpdateDestroyView.as_view(), name="book-retrieve-update-destroy"),
    # Get and Refresh JWT token URLs
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]

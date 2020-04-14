from django.urls import path, include
from .views import BookView
# from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import routers
import rest_framework
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
router=routers.DefaultRouter()
router.register('books', BookView)
urlpatterns = [
    path('', include(router.urls), name='books_rest'), 
    path('api-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view())
]

# urlpatterns = format_suffix_patterns(urlpatterns)

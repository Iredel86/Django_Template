from django.urls import path
from . import views 

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)



urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',views.register ),
    path('test/',views.test ),
    path("ts/",views.TaskView.as_view())
    
]
# data - OK
# authentication - OK
# upload files (image) - OK

#  todo - profile table
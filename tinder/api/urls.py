from django.urls import path, include

urlpatterns=[
    path('clients/', include('user.urls')),
]

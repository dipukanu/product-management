from django.urls import path

from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create-user'),
    path('details/', views.ListUserView.as_view(), name='user-details'),
    path('<uuid:id>', views.ManageUserView.as_view(), name='user-manage'),
]

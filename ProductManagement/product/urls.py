from django.urls import path

from product import views

app_name = 'product'

urlpatterns = [
    path('create/', views.CreateProductView.as_view(), name='create-product'),
    path('details/', views.ListProductView.as_view(), name='product-details'),
    path('<slug:slug>', views.ManageProductView.as_view(), name='manage-product'),
    path('category/create/', views.CreateCategoryView.as_view(),
         name='create-category'),
    path('category/details/', views.ListCategoryView.as_view(),
         name='category-details'),
    path('category/<int:pk>/', views.ManageCategoryView.as_view(),
         name='manage-category'),
    path('images/create/', views.CreateProductImageView.as_view(),
         name='create-images'),
    path('images/details/', views.ListProductImageView.as_view(),
         name='images-details'),
    path('images/<int:pk>/', views.ManageProductImageView.as_view(),
         name='manage-images'),
]

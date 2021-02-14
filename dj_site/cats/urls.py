from django.urls import path
from . import views

app_name = 'cats'
urlpatterns = [
    path('', views.CatList.as_view(), name='all'),
    # Cat
    path('main/<int:pk>/detail', views.CatDetail.as_view(), name='cat_detail'),
    path('main/create_cat/', views.CatCreate.as_view(), name='cat_create'),
    path('main/cat/<int:pk>/update/', views.CatUpdate.as_view(), name='cat_update'),
    path('main/cat/<int:pk>/delete/', views.CatDelete.as_view(), name='cat_delete'),
    # Breed
    path('main/cats/breed/', views.BreedList.as_view(), name='breed_list'),
    path('main/create_breed/', views.BreedCreate.as_view(), name='breed_create'),
    path('main/breed/<int:pk>/update/', views.BreedUpdate.as_view(), name='breed_update'),
    path('main/breed/<int:pk>/delete/', views.BreedDelete.as_view(), name='breed_delete'),
]

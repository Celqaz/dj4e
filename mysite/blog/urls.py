from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    # post views
    # mapped to the post_list view.
    # path('', views.post_list, name='post_list'),
    path('',views.PostListView.as_view(),name='post_list'),
    # mapped to the post_detail view
    # You use angle brackets<...> to capture the values from the URL.
    # Any value specified in the URL pattern as <parameter> is captured as a string.
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
]

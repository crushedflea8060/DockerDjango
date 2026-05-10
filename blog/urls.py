from django.urls import path 


from .views import BlogListView, BlogDetailView, BlogCreateView, login_view, callback_view

urlpatterns = [
   path('', BlogListView.as_view(), name='home'),
   path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
   path('post/new/', BlogCreateView.as_view(), name='post_new'),
   path('login/', login_view, name='login'),
   path('complete/ion', callback_view, name='callback')
]

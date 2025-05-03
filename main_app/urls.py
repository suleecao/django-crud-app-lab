from django.urls import path
from . import views

#doesn't matter for single or double quotes
#kwarg is the second argument, optional but useful
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('shoes/', views.shoe_index, name='shoe-index'),
    path('shoes/<int:shoe_id>/', views.shoe_detail, name='shoe-detail'),
    path('shoes/create/', views.ShoeCreate.as_view(), name='shoe-create'),
    path('shoes/<int:pk>/update/', views.ShoeUpdate.as_view(), name='shoe-update'),
    path('shoes/<int:pk>/delete/', views.ShoeDelete.as_view(), name='shoe-delete'),
    path('shoes/<int:shoe_id>/add_outfit/', views.add_outfit, name='add-outfit'),
    path('accounts/signup/', views.signup, name='signup'),

]


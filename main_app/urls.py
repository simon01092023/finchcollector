from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finches/', views.finches_index, name="finch-index"),
    path('finches/<int:finch_id>/', views.finch_detail, name='finch-detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finch-create'),
    # CBV's expect the params to be called pk (convention), which is short for primary key,
    # which is another for id
    path('finches/<int:pk>/update/',
         views.FinchUpdate.as_view(), name='finch-update'),
    path('finches/<int:pk>/delete/',
         views.FinchDelete.as_view(), name='finch-delete'),
    path('finches/<int:finch_id>/add_feeding/', views.add_feeding, name='add_feeding')
]

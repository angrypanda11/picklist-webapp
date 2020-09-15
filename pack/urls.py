from django.urls import path

from . import views

# app_name = 'pack'
urlpatterns = [
    path('', views.upload, name='upload'),
    path('all/', views.all_orders, name='all'),
    path('page/<number>/', views.detail, name='detail'),
    path('sku/<sku>/', views.sku_view, name='sku'),
    path('delete/', views.delete_all, name='delete'),
    path('dict/', views.dictionary, name='dict'),
    path('dict/update', views.dictionary_update, name='dict_update'),
    path('download', views.download_update, name='download'),
    path('export/update', views.export_update, name='export_update'),

]

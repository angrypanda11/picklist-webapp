from django.urls import path

from . import views

# app_name = 'pack'
urlpatterns = [
    path('', views.upload, name='upload'),
    path('all/', views.all_orders, name='all'),
    path('<number>/', views.detail, name='detail'),
    path('sku/<sku>/', views.sku_view, name='sku'),

    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('shot/past', views.PastShot, name='past_shot')
]

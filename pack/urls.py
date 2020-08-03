from django.urls import path

from . import views

# app_name = 'pack'
urlpatterns = [
    path('', views.upload, name='upload')
    # path('', views.IndexView.as_view(), name='index'),
    # path('shot', views.ShotRecorderView, name='shot'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('shot/past', views.PastShot, name='past_shot')
]

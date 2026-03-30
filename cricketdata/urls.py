from django.urls import path
from cricketdata import views

urlpatterns = [
 path("",views.service_view , name='home'),
 path("currentmatches",views.currentMatches_view, name='currentmatches'),
  path('serieslist/',views.serieslist_view, name='serieslist'),
   path('series_info/<str:id>',views.series_info, name='series_info'),
   path('match_info/<str:id>',views.match_info, name='match_info'),
   path('fantacyscorecard/<str:id>',views.fantacyScorecard, name='fantacyscorecard'),
]

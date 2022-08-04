import django


from django.urls import path

from ifsc_cache.views import getLeaderBoard, ifscResponse

urlpatterns = [
    path('<str:ifsc_code>/', ifscResponse),
    path('<int:num_banks>/<str:order>', getLeaderBoard),
    path('<int:num_banks>/', getLeaderBoard),
    path('<str:order>/', getLeaderBoard),
    path('', getLeaderBoard)
]
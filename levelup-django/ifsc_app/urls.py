from django.urls import path

from ifsc_app.views import IndexView, getLeaderboard, ifscRequest, indexView

urlpatterns = [
    path('', indexView, name="ifsc_data"),
    path('<str:ifsc_code>', ifscRequest),
    path('<int:num_banks>/<str:order>', getLeaderboard)
]
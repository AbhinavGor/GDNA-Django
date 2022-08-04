import statistics
from django.apps import AppConfig
import pandas as pd

class IfscAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ifsc_app'

    def ready(self):
        global ifsc_data, bank_leaderboard, stats
        bank_leaderboard = {}
        stats = []
        ifsc_data = pd.read_csv("levelup_django/IFCB2009_04.csv")
        print(ifsc_data)
from django.test import TestCase
import requests

def test_if_return_ifsc_code_correct(self):
        res = requests.get("http://127.0.0.1:8000/ifsc/ANDB0000002")
        
        self.assertIs(res["ifsc_code"], "ANDB0000002")
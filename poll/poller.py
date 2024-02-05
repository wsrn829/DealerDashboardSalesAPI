import django
import os
import sys
import time
import json
import requests

sys.path.append("")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sales_project.settings")
django.setup()

from sales_rest.models import AutomobileVO
from sales_project.celery import app

def get_automobiles():
    response = requests.get("https://dealer-dashboard-8d7b3aea3ae7.herokuapp.com/automobiles/")
    content = json.loads(response.content)
    print(AutomobileVO.objects.all)
    print("POLLER_CONTENT", content)
    for automobile in content["autos"]:
        AutomobileVO.objects.update_or_create(
            vin=automobile["vin"], 
            defaults={
                "vin": automobile["vin"],
                "color": automobile["color"],
                "year": automobile["year"],
                "sold": automobile["sold"]
            },
        )


@app.task
def poll(repeat=True):
    while True:
        print('Before get_automobiles()')
        try:
            get_automobiles()
            print('After get_automobiles()')
        except Exception as e:
            print(e, file=sys.stderr)
        if not repeat:
            break

        time.sleep(60)
        
        
if __name__ == "__main__":
    poll()




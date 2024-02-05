# management/commands/poll_inventory.py
from django.core.management.base import BaseCommand
from sales_rest.models import AutomobileVO
import requests

class Command(BaseCommand):
    help = 'Polls inventory monolith for new automobile data'

    def handle(self, *args, **options):
        print("Starting poll_inventory command") 
        # Fetch data from inventory monolith
        try: 
            response = requests.get('https://dealer-dashboard-8d7b3aea3ae7.herokuapp.com/automobiles')
            response.raise_for_status()  # This will raise an error if the request failed
        except requests.exceptions.RequestException as e:
            print(e)
            return
        
        data = response.json()
        print(data)  # Print the data received from the inventory monolith

        # Create new AutomobileVO objects
        for item in data:
            automobile, created = AutomobileVO.objects.get_or_create(vin=item['vin'], defaults=item)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created AutomobileVO {automobile.vin}'))
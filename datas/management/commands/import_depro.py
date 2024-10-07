import csv
import os
from django.core.management.base import BaseCommand
from datas.models import DepositProduct  # Ensure this import matches your model's location
from django.conf import settings

class Command(BaseCommand):
    help = 'Load Deposit Product data from a CSV file'

    def handle(self, *args, **kwargs):
        # Path to your CSV file
        csv_file_path = os.path.join(settings.BASE_DIR, 'depro_data.csv')

        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Strip whitespace from header names
                row = {k.strip(): v for k, v in row.items()}

                # Create an instance of CIF using the CSV headers
                depro = DepositProduct(
                    field=row['Field'],
                    description=row['Description'],
                    table_name=row['Table_Name'],
                    datatype=row['Data_Types'],
                    remarks=row['Remarks']
                )
                depro.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully added: {row["Field"]}'))

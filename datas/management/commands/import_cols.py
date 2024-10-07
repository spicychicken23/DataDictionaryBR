import csv
import os
from django.core.management.base import BaseCommand
from datas.models import Collateral  # Ensure this import matches your model's location
from django.conf import settings

class Command(BaseCommand):
    help = 'Load Collateral data from a CSV file'

    def handle(self, *args, **kwargs):
        # Path to your CSV file
        csv_file_path = os.path.join(settings.BASE_DIR, 'cols_data.csv')

        with open(csv_file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Strip whitespace from header names
                row = {k.strip(): v for k, v in row.items()}

                # Create an instance of CIF using the CSV headers
                cols = Collateral(
                    field=row['Field'],
                    description=row['Description'],
                    field_name=row['Field_Name'],
                    table_name=row['Table_Name'],
                    datatype=row['Data_Types'],
                    remarks=row['Remarks']
                )
                cols.save()
                self.stdout.write(self.style.SUCCESS(f'Successfully added: {row["Field"]}'))

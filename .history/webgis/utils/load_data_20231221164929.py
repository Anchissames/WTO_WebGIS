import csv 
from wto.models import TradeYearData, Country, ProductSector

with open('data/WtoData_export.xlsx') as csv_file:
    csv_reader = csv.DictReader
#########################################
# DESCRIPTION:
# Creates CSV file with random test data.
#
# Usage example:
# csvtestdata.py test.csv 10
# csvtestdata.py -h for more options
#########################################

import argparse
from faker import Faker
import csv
import random
import os

fake = Faker()

parser = argparse.ArgumentParser(description='Creates CSV file with random test data.'
                                             'Headers: TIMESTAMP, ID, NAME, ADDRESS')
parser.add_argument("file_name",
                    help="CSV file name that is created by the script")
parser.add_argument("rows", type=int,
                    help="number of data records")
parser.add_argument("--verbose", "-v",
                    action="store_true",
                    help="increase output verbosity")
args = parser.parse_args()

rows = args.rows
file_name = args.file_name

headers = ['TIMESTAMP', 'ID', 'NAME', 'ADDRESS']

timestamp = [fake.date(pattern="%Y-%m-%d %H:%M:%S", end_datetime=None) for i in range(rows)]
id = [random.randint(1, 1000) for i in range(rows)]
name = [fake.name() for i in range(rows)]
address = [fake.address() for i in range(rows)]

with open(file_name, 'wb') as csvfile:
    writer = csv.DictWriter(csvfile, headers, dialect='excel')
    writer.writeheader()

    for i in range(rows):
        writer.writerow({headers[0]: timestamp[i], headers[1]: id[i], headers[2]: name[i], headers[3]: address[i]})

if args.verbose:
    with open(file_name, 'r') as csvfile:
        reader = csv.reader(csvfile)
        row_count = sum(1 for row in reader)
        print("File: '{}' with {} rows created successfully".format(os.path.abspath(file_name), row_count))
        print("First 10 rows of {} file:".format(file_name))
        csvfile.seek(0)
        for i in range(10):
            print(reader.next())

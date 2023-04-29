# import argparse module for parsing command-line arguments
import argparse
# import datetime and date classes for parsing dates and times
from datetime import datetime, date
# import pprint module for pretty-printing data structures
from pprint import pprint

# `count_meters` counts the number of meters in the input
# file by parsing the file and looking for the number of
# meter sections in the file.


def count_meters(file_path):
    meter_ids = set()
    with open(file_path, 'r') as file:
        for line in file:
            if 'METER|' in line:
                meter_id = line.strip().split('|')[1]
                meter_ids.add(meter_id)
    return len(meter_ids)

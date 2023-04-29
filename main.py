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

 # `parse_file`defines the schema of the file to be parsed, which consists of a header,
 # meter readings, and a footer. The structure dictionary maps the section names
 # (i.e., 'HEADER', 'METER', 'READING', 'FOOTER') to their expected data types.


def parse_file(file_path):
    structure = {
        'HEADER': str,
        'METER': {
            'meter_id': str
        },
        'READING': {
            'reading_id': str,
            'value': float,
            'date': lambda x: datetime.strptime(x, '%Y%m%d').date(),
            'status': str
        },
        'FOOTER': str
    }

    # Parse the file into a dictionary
    data = {'meter_data': []}
    footer = None
    with open(file_path, 'r') as file:
        meter_dict = {}
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split('|')
            section = parts[0]
            if section not in structure:
                raise ValueError(f'Unknown section: {section}')
            if section == 'METER':
                meter_dict = {'meter_id': parts[1], 'readings': []}
                data['meter_data'].append(meter_dict)
            elif section == 'READING':
                item = {}
                for key, transform in structure[section].items():
                    item[key] = transform(parts.pop(1))
                meter_dict['readings'].append(item)
            else:
                if section == 'HEADER':
                    data[section] = parts[1].upper()
                elif section == 'FOOTER':
                    footer = parts[1].upper()
                else:
                    data[section.lower()] = structure[section](parts[1])
    if footer is not None:
        data['FOOTER'] = footer

    return data

# `sum_valid_readings`` reads in the input file and counts the number of valid
# readings. It looks for all sections labeled "READING" that contain a reading
# value labeled "|V|".


def sum_valid_readings(file_path):
    with open(file_path, 'r') as file:
        valid_readings = sum(
            1 for line in file if 'READING' in line and '|V|' in line)
    return valid_readings


# main function takes in an input file, and allows the user to specify
# whether they want to count the number of meters in the file or find
# the sum of all valid meter readings in the file. If neither option
# is specified, it simply parses the file and prints the resulting dictionary.
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Read meter readings from a file')
    parser.add_argument('file_name', type=str, help='name of input file')
    parser.add_argument('--count', action='store_true',
                        help='display the number of meters in the file')
    parser.add_argument('--valid', action='store_true',
                        help='display the total sum of valid meter readings in the file')
    args = parser.parse_args()

    # Construct the full path to the file
    file_path = f'./{args.file_name}'

    if args.count:
        meter_count = count_meters(file_path)
        print(f'There are {meter_count} meters in the file.')
    elif args.valid:
        valid_sum = sum_valid_readings(file_path)
        print(
            f'The total sum of valid meter readings in the file is {valid_sum}.')
    else:
        data = parse_file(file_path)
        pprint(data)
        if 'FOOTER' in data:
            print(f'FOOTER: {data["FOOTER"]}')

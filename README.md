# Meter Readings
 <img width="100" alt="arrow" src="https://user-images.githubusercontent.com/19231569/213458967-d77d1ede-cbb8-4cda-8d58-7ac2a1c70503.png">

### Summary
The exercise containts a lot of messages which are sent between different participants in the form of “flows”. Flows are texted base files, and the information included in the flow is dependent on a schema. We want you to develop a command-line utility to read a flow containing meter readings (provided in a separate file).
The utility should use `argparse` which is part of the python standard library, and perform some simple data processing on it and output the results to the console.

### Expectation
We expect the whole file to be parsed into some sort of python data structure (maybe a dictionary), with the string values in the file transformed into their equivalent python data type (e.g. 20210401 would be parsed to a python datetime.date object)
<!-- A few simple unit tests utilising the `unittest` library that validate your solution -->
Clear readable code is key, with appropriate comments as you see fit


### Tech stack
```
- python3 --version
- python 3.8.10

```
### How to run this project
Clone this repository:

```
git clone https://github.com/paulinejdavis/meterRead_app.git

```
cd meterRead
python3 --version
python 3.8.10
```

```
`python3 main.py meter_readings`

```

`python3 main.py meter_readings --valid`


`python3 main.py meter_readings --count`

## Ouputs

### Command Line outputs
 
<img width="733" alt="data" src="https://user-images.githubusercontent.com/111147520/235308021-4495dd60-bb1d-4f81-9747-1b85237e6ff5.png">

<img width="518" alt="countValidReading" src="https://user-images.githubusercontent.com/111147520/235308026-a049b82c-8c70-4e1d-894b-902f3d6001a4.png">


## File Schema

```
HEADER |
METER | METER_ID |
READING | READING_ID | VALUE | DATE(YYYYMMDD) | STATUS (V = valid, F = Invalid) |
FOOTER |

The original file consists of a HEADER row followed by multiple pairs of meter and meter reading lines. The meter is on the first line and the meter reading is on the second. The file is terminated with a FOOTER row.
```

## User stories

```
The count of meters in the file
```

```
The total sum of valid meter readings within the file
```

```
The highest and lowest valid meter reading within the file
```

```
The most recent and oldest meter reading within the file
```

## background
# Meter Readings

 <img width="100" alt="arrow" src="https://user-images.githubusercontent.com/19231569/213458967-d77d1ede-cbb8-4cda-8d58-7ac2a1c70503.png">
 


### Summary

This exercise converts a raw dataset into a terminal-use programme for the end user.
The challenge uses `argparse` to perform some data processing on a `meter_readings` data file and output the results to the console.

### Tech stack

```
- python3 --version
- python 3.8.10

```
### How to run this project:

Clone this repository:

```
git clone https://github.com/paulinejdavis/readMeters_app.git

```
In the terminal:

```
cd readMeters
python3 --version
python 3.8.10
```
In the console:

```
python3 main.py meter_readings
python3 main.py meter_readings --count
python3 main.py meter_readings --valid
```

### Completed Tasks

Transforming data file using python dictionaries.

Use the following command to run:

`python3 main.py meter_readings`

The `meter_readings` file is parsed into a python dictionary, with the string values in the file transformed into their equivalent python data type (e.g. 20210401 would be parsed to a python datetime.date object).

### Using the following file schema:
HEADER |
METER | METER_ID |
READING | READING_ID | VALUE | DATE(YYYYMMDD) | STATUS (V = valid, F = Invalid) |
FOOTER |

The original file consists of a HEADER row followed by multiple pairs of meter ID number and meter reading lines. 
The meter ID number is on the first line and the meter reading is on the second. The file is terminated with a FOOTER row.

User can request number/count of meter in any file

Use the following command to run:

`python3 main.py meter_readings --count`

```
Displays the count of meters in the file to the console.
```

User can request the number of correct meter readings from file

Use the following command to run:

`python3 main.py meter_readings --valid`
```
Calculates the total sum of valid meter readings within the file.
```
```
Clear readable working code with appropriate comments:
```


## Ouputs

### Command Line outputs

<img width="666" alt="Screenshot 2023-04-29 at 15 34 56" src="https://user-images.githubusercontent.com/111147520/235308436-77c70b88-7e12-42e4-87cc-974eb74fbac1.png">

 
 <img width="651" alt="Screenshot 2023-04-29 at 15 36 14" src="https://user-images.githubusercontent.com/111147520/235308541-f36fa47d-0cc7-40e8-8648-aee34dbfc212.png">


### To complete or revisit

```
A few simple unit tests utilising the `unittest` library that validate your solution
```
```
The highest and lowest valid meter reading within the file
```
```
The most recent and oldest meter reading within the file
```

**Background**

https://docs.python.org/3/library/argparse.html?highlight=argparse
https://docs.python.org/3/library/datetime.html?highlight=datetime#datetime.datetime
https://docs.python.org/3/library/pprint.html?highlight=pprint#module-pprint
https://docs.python.org/3/howto/argparse.html

https://www.youtube.com/watch?v=FbEJN8FsJ9U

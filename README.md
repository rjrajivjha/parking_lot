## Parking Lot Problem

To run tests, run
```bash
$ pip3 install -r requirements.yml
$ python3 -m pytest -s  -v tests/
```

`main.py` runs Example 1 from the problem statement.
```bash
$ python3 src/main.py
park,Motorcycle
Parking Ticket: 001
Parking Slot: 1
Vehicle Type: Motorcycle/Scooter
Entry time: 05/11/2023, 03:01

park,Scooter
Parking Ticket: 002
Parking Slot: 2
Vehicle Type: Motorcycle/Scooter
Entry time: 05/11/2023, 03:01

park,Scooter
No space available to park Scooter

park,Bus
No space available to park Bus

unpark,003
Could not find vehicle for 003

unpark,002
Parking Ticket: 002
Receipt Number: fd31f8de-a3f9-49dd-a7ae-605fa1d7fdf8
Entry time: 05/11/2023, 03:01
Exit time: 05/11/2023, 03:01
Fee: 10

unpark,001
Parking Ticket: 001
Receipt Number: 8dd40086-5052-4d06-902a-6b75405acf6b
Entry time: 05/11/2023, 03:01
Exit time: 05/11/2023, 03:01
Fee: 10
```
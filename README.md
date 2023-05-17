# Parking Lot Problem

A parking lot is a dedicated area that is intended for parking vehicles. Parking lots are present in every city and suburban area. Shopping malls, stadiums, airports, train stations, and similar venues often feature a parking lot with a large capacity. A parking lot can spread
across
multiple buildings with multiple floors or can be in a large open area.

● The parking lot will allow different types of vehicles to be parked: 

    ○ Motorcycles/Scooters
    ○ Cars/SUVs
    ○ Buses/Trucks

● Each vehicle will occupy a single spot and the spot size will be different for different vehicles.

● The number of spots per vehicle type will be different for different parking lots. For example

    ○ Motorcycles/scooters: 100 spots
    ○ Cars/SUVs: 80 spots
    ○ Buses/Trucks: 40 spots

● When a vehicle is parked, a parking ticket should be generated with the spot number and the entry date-time.

● When a vehicle is unparked, a receipt should be generated with the entry date-time, exit date-time, and the applicable fees to be paid.
 
### Fee Models
Different locations have different fee models. Below are a few possible models:

  #### Mall 
      Per-hour flat fees

  Vehicle | Fee
  --- | ---
  Motorcycle | 10
  Car/SUV | 20
  Bus/Truck | 50
  
  #### Stadium 
      Flat rate up to a few hours and then per-hour rate. The total fee is the sum of all the previous interval fees. No parking spots for buses/trucks at the stadium.

  Vehicle | Interval | Fee
  --- | --- | --- 
  Motorcycle | [0, 4) hours | 30
  Motorcycle | [4, 8) hours | 60
  Motorcycle | [12, Infinity) hours | 100 per hour
  Car | [0, 4) hours | 60
  Car | [4, 8) hours | 120
  Car | [12, Infinity) hours | 200 per hour
  
   #### Airport 
      Flat rate up to one day. Then per-day rate. There is no summing up of the previous interval fees. No parking spots for buses/trucks at the airport.

  Vehicle | Interval | Fee
  --- | --- | --- 
  Motorcycle | [0, 1) hours | Free
  Motorcycle | [1, 8) hours | 40
  Motorcycle | [8, 24) hours | 60
  Motorcycle | Each day | 80
  Car | [0, 12) hours | 60
  Car | [12, 24) hours | 80
  Car | Each day | 100
  
## Problem Statement

Given a parking lot with details about the vehicle types that can be parked, the number of spots, and the fee model for the parking lot; compute the fees to be paid for the parked vehicles when the vehicle is unparked.


## To run tests, run
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

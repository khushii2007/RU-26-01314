# Bus Route Management System (PS No. 71)

## Project Information
- **Institution:** Rungta International Skills University
- **School:** School of Computer Science and Engineering
- **Program:** Bachelor of Technology (Computer Science and Engineering)
- **Project Title:** Bus Route Management System
- **Programming Language:** Python 3

## Overview
The Bus Route Management System is a console-based Python application that represents bus stops and their road connections. It allows users to view all available stops, check direct connections and distances, and find a route between two stops. The program also calculates the fare based on the total distance.

## Features
- Display all registered bus stops in alphabetical order.
- Show direct connections and distances for a selected stop.
- Find routes using Breadth-First Search (BFS), which chooses a route with the fewest stops.
- Calculate fare at **₹1.50 per kilometre**.
- Handle invalid stop names and disconnected routes.
- Run built-in test cases to verify the program.

## Bus Network
The network contains these stops:
- Durg
- Bhilai
- Raipur
- Bilaspur
- Dhamtari
- Rajnandgaon
- Jagdalpur
- Kondagaon

Jagdalpur and Kondagaon form a separate connected section and are disconnected from the main network.

## Concepts Used
- Python functions
- Dictionaries and nested dictionaries
- Lists
- `collections.deque`
- Graph representation (adjacency list)
- Breadth-First Search (BFS)
- Input validation and console menus

## How to Run

### Requirements
- Python 3 installed

### Start the application
```bash
python bus_route_system.py
```

### Run the test suite directly
```bash
python bus_route_system.py --test
```

You can also choose **4. Run all test cases** from the application's menu.

## Menu Options
1. Show all stops
2. Show connections
3. Find route
4. Run all test cases
5. Exit

## Fare Calculation
The fare is calculated using:

```text
Fare = Total Distance (km) × ₹1.50
```

## Example
Finding a route from **Bhilai** to **Bilaspur** gives:

```text
Route: Bhilai -> Raipur -> Bilaspur
Stops: 3 | Distance: 140 km | Fare: Rs. 210.00
```

## Notes
- Stop names are matched without case sensitivity.
- The route finder prioritizes the **fewest stops**, not necessarily the shortest distance in kilometres.
- Roads are represented as bidirectional connections.

## Author
Add your name, roll number, and other submission details here.

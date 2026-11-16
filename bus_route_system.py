"""
================================================================================
RUNGTA INTERNATIONAL SKILLS UNIVERSITY
SCHOOL OF COMPUTER SCIENCE AND ENGINEERING
Bachelor of Technology Computer Science and Engineering

Project Title : Bus Route Management System (PS No. 71)
Language      : Python 3
Concepts      : Lists, Dictionaries, Graph Basics, BFS (Breadth-First Search)
================================================================================
"""

from collections import deque
import sys

# -----------------------------------------------------------------------------
# 1. NETWORK DATA STRUCTURE
# Stored as a dictionary of dictionaries (stop -> neighbours -> distance in km).
# Roads are bidirectional (work in both directions).
# Jagdalpur and Kondagaon are disconnected from the main network.
# -----------------------------------------------------------------------------
BUS_NETWORK = {
    "Durg": {
        "Bhilai": 10,
        "Raipur": 40,
        "Rajnandgaon": 45
    },
    "Bhilai": {
        "Durg": 10,
        "Raipur": 30
    },
    "Raipur": {
        "Bhilai": 30,
        "Bilaspur": 110,
        "Dhamtari": 80,
        "Durg": 40
    },
    "Bilaspur": {
        "Raipur": 110
    },
    "Dhamtari": {
        "Raipur": 80
    },
    "Rajnandgaon": {
        "Durg": 45
    },
    "Jagdalpur": {
        "Kondagaon": 75
    },
    "Kondagaon": {
        "Jagdalpur": 75
    }
}

FARE_RATE_PER_KM = 1.50  # Rs. 1.50 per km


# -----------------------------------------------------------------------------
# 2. HELPER UTILITIES
# -----------------------------------------------------------------------------
def get_canonical_stop_name(network, stop_input):
    """
    Matches user input case-insensitively with network stop names,
    returning the canonical capitalized stop name if found.
    """
    cleaned = stop_input.strip()
    for stop in network:
        if stop.lower() == cleaned.lower():
            return stop
    return cleaned


# -----------------------------------------------------------------------------
# 3. CORE FUNCTIONALITIES
# -----------------------------------------------------------------------------
def show_all_stops(network):
    """Displays all registered bus stops in alphabetical order."""
    print("\n--- All Available Bus Stops ---")
    stops = sorted(network.keys())
    for index, stop in enumerate(stops, start=1):
        print(f"  {index}. {stop}")
    print()


def show_connections(network, stop_input):
    """
    Displays direct connections and road distances for a given stop.
    Outputs: <Stop> connects to: <Neighbor1> (<dist> km), <Neighbor2> (<dist> km), ...
    """
    stop = get_canonical_stop_name(network, stop_input)

    # Test Case 3(b): Invalid input handling
    if stop not in network:
        print(f"Stop '{stop_input}' not found.")
        return

    neighbors = network[stop]
    if not neighbors:
        print(f"{stop} has no direct connections.")
        return

    # Sort alphabetically by neighbor name for deterministic output
    sorted_neighbors = sorted(neighbors.items(), key=lambda x: x[0])
    connection_list = [f"{neighbor} ({dist} km)" for neighbor, dist in sorted_neighbors]
    print(f"{stop} connects to: {', '.join(connection_list)}")


def find_route_bfs(network, start, destination):
    """
    Finds the route with the FEWEST STOPS between two stops using BFS.
    Returns:
        route (list): Sequence of stops from start to destination.
        distance (int/float): Total route distance in km.
    """
    if start not in network or destination not in network:
        return None, 0

    if start == destination:
        return [start], 0

    # BFS Queue holds tuples of: (current_stop, path_taken)
    queue = deque([(start, [start])])
    visited = {start}

    while queue:
        current_stop, path = queue.popleft()

        for neighbor in network[current_stop]:
            if neighbor == destination:
                full_path = path + [neighbor]
                # Calculate total distance along the found path
                total_distance = sum(
                    network[full_path[i]][full_path[i + 1]]
                    for i in range(len(full_path) - 1)
                )
                return full_path, total_distance

            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None, 0


def handle_find_route(network, from_input, to_input):
    """
    Handles user queries for route discovery, calculates fare and prints
    output formatted to exact project specification.
    """
    from_stop = get_canonical_stop_name(network, from_input)
    to_stop = get_canonical_stop_name(network, to_input)

    # Check validity of stops
    if from_stop not in network:
        print(f"Stop '{from_input}' not found.")
        return
    if to_stop not in network:
        print(f"Stop '{to_input}' not found.")
        return

    # Test Case 2: Boundary / Minimum Input
    if from_stop == to_stop:
        print("Source and destination are the same. Distance: 0 km. Fare: Rs. 0.00")
        return

    route, distance = find_route_bfs(network, from_stop, to_stop)

    # Test Case 3(a): Invalid / Disconnected route
    if route is None:
        print(f"No route available between {from_stop} and {to_stop}.")
        return

    # Test Case 4: Route calculation with fare
    fare = distance * FARE_RATE_PER_KM
    num_stops = len(route)
    route_str = " -> ".join(route)

    print(f"Route: {route_str}")
    print(f"Stops: {num_stops} | Distance: {distance} km | Fare: Rs. {fare:.2f}")


# -----------------------------------------------------------------------------
# 4. AUTOMATED TEST SUITE (Verification for 4 Test Cases)
# -----------------------------------------------------------------------------
def run_all_tests():
    """Runs all 4 test cases specified in the project problem sheet."""
    print("\n========================================================")
    print("        RUNNING TEST CASES (PS No. 71 VERIFICATION)     ")
    print("========================================================")

    # Test Case 1: Normal Input
    print("\n--- Test Case 1: Normal Input ---")
    print("Input   : Menu: Show connections | Stop: Raipur")
    print("Expected: Raipur connects to: Bhilai (30 km), Bilaspur (110 km), Dhamtari (80 km), Durg (40 km)")
    print("Output  : ", end="")
    show_connections(BUS_NETWORK, "Raipur")

    # Test Case 2: Boundary / Minimum Input
    print("\n--- Test Case 2: Boundary / Minimum Input ---")
    print("Input   : Menu: Find route | From: Durg | To: Durg")
    print("Expected: Source and destination are the same. Distance: 0 km. Fare: Rs. 0.00")
    print("Output  : ", end="")
    handle_find_route(BUS_NETWORK, "Durg", "Durg")

    # Test Case 3: Invalid Input
    print("\n--- Test Case 3: Invalid Input ---")
    print("(a) Input   : Menu: Find route | From: Durg | To: Jagdalpur")
    print("    Expected: No route available between Durg and Jagdalpur.")
    print("    Output  : ", end="")
    handle_find_route(BUS_NETWORK, "Durg", "Jagdalpur")

    print("(b) Input   : Menu: Show connections | Stop: Delhi")
    print("    Expected: Stop 'Delhi' not found.")
    print("    Output  : ", end="")
    show_connections(BUS_NETWORK, "Delhi")

    # Test Case 4: Different Valid Scenario
    print("\n--- Test Case 4: Different Valid Scenario ---")
    print("Input   : Menu: Find route | From: Bhilai | To: Bilaspur")
    print("Expected:")
    print("  Route: Bhilai -> Raipur -> Bilaspur")
    print("  Stops: 3 | Distance: 140 km | Fare: Rs. 210.00")
    print("Output  :")
    handle_find_route(BUS_NETWORK, "Bhilai", "Bilaspur")
    print("\n========================================================\n")


# -----------------------------------------------------------------------------
# 5. MAIN CONSOLE INTERACTION
# -----------------------------------------------------------------------------
def main():
    # If executed with '--test', trigger the test suite directly
    if len(sys.argv) > 1 and sys.argv[1] in ("--test", "-t", "test"):
        run_all_tests()
        return

    while True:
        print("\n==========================================")
        print("       BUS ROUTE MANAGEMENT SYSTEM        ")
        print("==========================================")
        print("1. Show all stops")
        print("2. Show connections")
        print("3. Find route")
        print("4. Run all test cases")
        print("5. Exit")
        print("==========================================")

        user_choice = input("Enter your choice (1-5 or name): ").strip()

        if user_choice in ("1", "Show all stops", "show all stops"):
            show_all_stops(BUS_NETWORK)

        elif user_choice in ("2", "Show connections", "show connections"):
            stop = input("Stop: ").strip()
            show_connections(BUS_NETWORK, stop)

        elif user_choice in ("3", "Find route", "find route"):
            from_stop = input("From: ").strip()
            to_stop = input("To: ").strip()
            handle_find_route(BUS_NETWORK, from_stop, to_stop)

        elif user_choice in ("4", "Run all test cases", "test", "tests"):
            run_all_tests()

        elif user_choice in ("5", "Exit", "exit", "quit", "q"):
            print("\nThank you for using Bus Route Management System. Goodbye!")
            break

        else:
            print("Invalid choice! Please select an option from 1 to 5.")


if __name__ == "__main__":
    main()

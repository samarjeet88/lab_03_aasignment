flight_data = [
    {'Flight ID': 'AI161E90', 'From': 'BLR', 'To': 'BOM', 'Price': 5600},
    {'Flight ID': 'BR161F91', 'From': 'BOM', 'To': 'BBI', 'Price': 6750},
    {'Flight ID': 'AI161F99', 'From': 'BBI', 'To': 'BLR', 'Price': 8210},
    {'Flight ID': 'VS171E20', 'From': 'JLR', 'To': 'BBI', 'Price': 5500},
    {'Flight ID': 'AS171G30', 'From': 'HYD', 'To': 'JLR', 'Price': 4400},
    {'Flight ID': 'AI131F49', 'From': 'HYD', 'To': 'BOM', 'Price': 3499}
]
flight_data_0=[{'Flight ID': 'AI161E90', 'From': 'BLR', 'To': 'BOM', 'Price': 5600}]
flight_data_1=[{'Flight ID': 'BR161F91', 'From': 'BOM', 'To': 'BBI', 'Price': 6750}]
flight_data_2=[{'Flight ID': 'AI161F99', 'From': 'BBI', 'To': 'BLR', 'Price': 8210}]
flight_data_3=[ {'Flight ID': 'VS171E20', 'From': 'JLR', 'To': 'BBI', 'Price': 5500}]
flight_data_4=[{'Flight ID': 'AS171G30', 'From': 'HYD', 'To': 'JLR', 'Price': 4400}]
flight_data_5=[{'Flight ID': 'AI131F49', 'From': 'HYD', 'To': 'BOM', 'Price': 3499}]
def display_flights():
    print("Flight Number\tDeparture Destination\tArrival Destination\tPrice")
    print("-----------------------------------------------------------------------------------")
    for flight in flight_data:
        print(f"{flight['Flight ID']}\t\t{flight['From']}\t{flight['To']}\t{flight['Price']}")
def dispaly_blr():
    print("-----------------------------------------------------------------------------------")
    for flight in flight_data_0:
        print(f"{flight['Flight ID']}\t\t{flight['From']}\t{flight['To']}\t{flight['Price']}")
def display_bom():
    print("-----------------------------------------------------------------------------------")
    for flight in flight_data_1:
        print(f"{flight['Flight ID']}\t\t{flight['From']}\t{flight['To']}\t{flight['Price']}")
def display_bbi():
    print("-----------------------------------------------------------------------------------")
    for flight in flight_data_2:
        print(f"{flight['Flight ID']}\t\t{flight['From']}\t{flight['To']}\t{flight['Price']}")
def display_jlr():
    print("-----------------------------------------------------------------------------------")
    for flight in flight_data_3:
        print(f"{flight['Flight ID']}\t\t{flight['From']}\t{flight['To']}\t{flight['Price']}")
def display_hyd():
    print("-----------------------------------------------------------------------------------")
    for flight in flight_data_4:
        print(f"{flight['Flight ID']}\t\t{flight['From']}\t{flight['To']}\t{flight['Price']}")
while True:
    print("\nFlight Management System")
    print("1. Display Available Flights")
    print("2.Display Bengaluru")
    print("3.Display Bombay")
    print("4.Display Bhubaneswar")
    print("5.Display  Jabalpur")
    print("6.Display Hydreabad")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        display_flights()
    elif choice==2:
        dispaly_blr()
    elif choice==3:
        display_bom()
    elif choice==4:
        display_jlr()
    elif choice==5:
        display_hyd()
    else:
        print("Invalid choice. Please select a valid option.")
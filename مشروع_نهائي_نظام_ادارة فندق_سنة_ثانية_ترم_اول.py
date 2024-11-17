from abc import ABC, abstractmethod
import os


########################################################################################
class Person(ABC):
    def __init__(self, name, phone):
        self._name = name
        self._phone = phone

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @abstractmethod
    def get_role(self):
        pass
########################################################################################
class Employee(Person):
    def __init__(self, name, phone, emp_id, role):
        super().__init__(name, phone)
        self.emp_id = emp_id
        self._role = role

    def get_role(self):
        return self._role
    
    def welcome_message(self):
        print('welcome in Employees class')

########################################################################################
class Manager(Employee):
    def __init__(self, name, phone, emp_id):
        super().__init__(name, phone, emp_id, 'Manager')

########################################################################################
class Receptionist(Employee):
    def __init__(self, name, phone, emp_id):
        super().__init__(name, phone, emp_id, 'Receptionist')

########################################################################################
class Guest(Person):
    def __init__(self, name, phone, guest_id):
        super().__init__(name, phone)
        self.guest_id = guest_id

    def get_role(self):
        return "Guest"
    
    def welcome_message(self):
        print('welcome in guests class')

########################################################################################
class Room:
    def __init__(self, room_number, room_type):
        self.room_number = room_number
        self.room_type = room_type
        self.is_available = True

    def book_room(self):
        if self.is_available:
            self.is_available = False
            print(f"Room {self.room_number} has been booked.")
        else:
            print(f"Room {self.room_number} is already booked.")

    def free_room(self):
        self.is_available = True
        print(f"Room {self.room_number} is now available.")
    
    def welcome_message(self):
        print('welcome in rooms class')


########################################################################################
class Booking:
    booking_list = []

    @classmethod
    def add_booking(cls, guest, room):
        if room.is_available:
            room.book_room()
            cls.booking_list.append({"guest": guest.name, "room": room.room_number})
        else:
            print(f"Room {room.room_number} is not available.")

    @classmethod
    def display_bookings(cls):
        if cls.booking_list:
            print('='*80)
            print(' BOOKINGS '.center(80,'='))
            print('='*80)
            for booking in cls.booking_list:
                print(f"Guest: {booking['guest']}, Room: {booking['room']}")
        else:
            print("No bookings available.")
    
    def welcome_message(self):
        print('welcome in Booking class')

########################################################################################
class Services:
    def __init__(self):
        self.services_list = []

    def add_service(self, service_name):
        self.services_list.append(service_name)
        print(f"Service {service_name} added.")

    def remove_service(self, service_name):
        if service_name in self.services_list:
            self.services_list.remove(service_name)
            print(f"Service {service_name} removed.")
        else:
            print(f"Service {service_name} not found.")

    def display_services(self):
        if self.services_list:
            print('='*80)
            print(' Available services '.center(80,'='))
            print('='*80)
            for service in self.services_list:
                print(service)
        else:
            print("No services available.")

########################################################################################
class Department:
    def __init__(self, department_name, manager):
        self.department_name = department_name
        self.manager = manager
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        print(f"Employees in {self.department_name}:")
        for emp in self.employees:
            print(emp.name, "-", emp.get_role())

########################################################################################
class Hotel:
    def __init__(self):
        self.rooms = []
        self.guests = []
        self.employees = []
        self.services = Services()
    
    @staticmethod
    def name(hotel_name):
        print("="*80)
        print(f" Welcome to {hotel_name}'s Hotel Management System ".center(80,'='))
        print("="*80)
        input("Press Enter to continue...")

    def add_room(self, room):
        self.rooms.append(room)

    def add_guest(self, guest):
        self.guests.append(guest)

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_rooms(self):
        print('='*80)
        print(' rooms details '.center(80,'='))
        print('='*80)
        # print(f"Rooms in {self.name}:")
        for room in self.rooms:
            print(f"Room {room.room_number}, Type: {room.room_type}, Available: {room.is_available}")
        print('='*80)

    def display_guests(self):
        print('='*80)
        print(' guests details '.center(80,'='))
        print('='*80)
        for guest in self.guests:
            print(f"Guest ID: {guest.guest_id}, Name: {guest.name}")
        print('='*80)

    def display_employees(self):
        print('='*80)
        print(' Employees details '.center(80,'='))
        print('='*80)
        for emp in self.employees:
            print(f"Employee ID: {emp.emp_id}, Name: {emp.name}, Role: {emp.get_role()}")
        print('='*80)

########################################################################################
def clear_screen():
        os.system('cls')
########################################################################################

def login_interface():
    print('='*80)
    print(' LOGIN '.center(80,'='))
    print('='*80)
    username = input("Enter the user name: ")
    password = input("Enter the password:")

    if username == "hotel" and password == "hotel" :
        print("You enter successfully")
        print('Press Enter to Continue...')
        return True
    else:
        print("the User name or the password are wrong")
        return False

    

########################################################################################
def main():
    clear_screen()
    Hotel.name('sadiq,zain,and ahmed')
    clear_screen()
    hotel = Hotel()

    #add virtual values
    #add rooms
    room1=Room('1','single')
    room2=Room('2','double')
    hotel.add_room(room1)
    hotel.add_room(room2)
    #guests
    guest=Guest('sadiq','782764176','1')
    hotel.add_guest(guest)
    #employees
    emp1=Manager('ahmed','77654866','1')
    emp2=Receptionist('zain','735874685','2')
    hotel.add_employee(emp1)
    hotel.add_employee(emp2)
    #booking
    Booking.add_booking(guest,room2)
    #services
    hotel.services.add_service('clear')
    hotel.services.add_service('wash')
    
    clear_screen()
    authorized=login_interface()

    while authorized:
        clear_screen()
        print("="*80)
        print("  Hotel Management System  ".center(80,'='))
        print("="*80)
        print("1. Add Room")
        print("2. Display Rooms")
        print("3. Add Guest")
        print("4. Display Guests")
        print("5. Add Employee")
        print("6. Display Employees")
        print("7. Book Room")
        print("8. Display Bookings")
        print("9. Add Service")
        print("10. Display Services")
        print("11. Exit")
        print("="*80)
        
        choice = input("Choose an option: ")
        clear_screen()
        if choice == "1":
            print('='*80)
            room_number = input("Enter room number: ")
            room_type = input("Enter room type: ")
            room = Room(room_number, room_type)
            hotel.add_room(room)
            print(f"\nthe room number {room_number} and of type {room_type} was added successfuly")
            print("="*80)
            input("Press Enter to continue...")
            
        
        elif choice == "2":
            hotel.display_rooms()
            input("Press Enter to continue...")
        
        elif choice == "3":
            print("===============================================")
            guest_name = input("Enter guest name: ")
            guest_phone = input("Enter guest phone: ")
            guest_id = input("Enter guest ID: ")
            print("===============================================")
            guest = Guest(guest_name, guest_phone, guest_id)
            hotel.add_guest(guest)
            input("Press Enter to continue...")
        
        elif choice == "4":
            hotel.display_guests()
            input("Press Enter to continue...")
        
        elif choice == "5":
            emp_name = input("Enter employee name: ")
            emp_phone = input("Enter employee phone: ")
            emp_id = input("Enter employee ID: ")
            emp_role = input("Enter employee role (manager/receptionist): ").lower()
            if emp_role == "manager":
                employee = Manager(emp_name, emp_phone, emp_id)
            else:
                employee = Receptionist(emp_name, emp_phone, emp_id)
            hotel.add_employee(employee)
            input("Press Enter to continue...")
        
        elif choice == "6":
            hotel.display_employees()
            input("Press Enter to continue...")
        
        elif choice == "7":
            hotel.display_rooms()
            input("Press Enter to continue...")
            guest_name = input("Enter guest name for booking: ")
            room_number = input("Enter room number for booking: ")
            #التحقق مما اذا كان اسم الزبون موجود في قاعدة البيانات
            for g in hotel.guests:
                if g.name==guest_name:
                    guest=g
                    break
                else:
                    guest=False
            #التحقق مما اذا كانت الغرفة موجودة 
            for r in hotel.rooms:
                if r.room_number==room_number:
                    room = r
                    break
                else:
                   room=False
        
            if guest and room:
                Booking.add_booking(guest, room)
            else:
                print("Guest or Room not found.")
            input("Press Enter to continue...")
        
        elif choice == "8":
            Booking.display_bookings()
            input("Press Enter to continue...")
        
        elif choice == "9":
            service_name = input("Enter service name to add: ")
            hotel.services.add_service(service_name)
            input("Press Enter to continue...")
        
        elif choice == "10":
            hotel.services.display_services()
            input("Press Enter to continue...")
        
        elif choice == "11":
            print("Exiting...")
            input("Press Enter to continue...")
            break

if __name__ == "__main__":
    main()
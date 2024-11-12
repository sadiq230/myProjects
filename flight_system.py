import json
from datetime import datetime

class User:
    def init(self, name, phone):
        self.name = name
        self.phone = phone
        self.validate_phone()

    def validate_phone(self):
        if len(self.phone) != 9 or not self.phone.startswith(('77', '78', '73', '71')):
            raise ValueError("رقم الهاتف يجب أن يبدأ بـ 77 أو 78 أو 73 أو 71 ويتكون من 9 أرقام.")

class Passenger(User):
    def init(self, name, phone, email=None):
        super().init(name, phone)
        self.email = email

    def make_booking(self, flight):
        return flight.book_seat(self)

    def cancel_booking(self, booking):
        return booking.flight.cancel_booking(booking)

    def update_contact_info(self, email, phone_number):
        self.email = email
        self.phone = phone_number
        return "تم تحديث معلومات الاتصال بنجاح."

class Route:
    def init(self, route_id, start_point, end_point):
        self.route_id = route_id
        self.start_point = start_point
        self.end_point = end_point

class Flight:
    def init(self, flight_id, destination, price, available_seats, route, departure_time, arrival_time):
        self.flight_id = flight_id
        self.destination = destination
        self.price = price
        self.available_seats = available_seats
        self.route = route
        self.departure_time = departure_time  # وقت الإقلاع
        self.arrival_time = arrival_time  # وقت الوصول

    def book_seat(self, passenger):
        if self.available_seats > 0:
            self.available_seats -= 1
            booking = Booking(passenger, self)  # إنشاء حجز جديد
            return booking
        else:
            return None  # لا توجد مقاعد متاحة

    def cancel_booking(self, booking):
        self.available_seats += 1
        return f"تم إلغاء الحجز للراكب {booking.user.name}."

    def get_flight_duration(self):
        duration = self.arrival_time - self.departure_time
        return duration

    def update_route(self, new_route):
        self.route = new_route

class Booking:
    def init(self, user, flight):
        self.user = user
        self.flight = flight
        self.confirmed = False

    def confirm_booking(self):
        self.confirmed = True
        return "تم تأكيد الحجز."

    def change_flight(self, new_flight):
        self.flight = new_flight
        return f"تم تغيير الرحلة إلى {new_flight.flight_id}."

    def get_booking_details(self):
        return f"الراكب: {self.user.name}, الرحلة: {self.flight.flight_id}, الوجهة: {self.flight.destination}, مقاعد متاحة: {self.flight.available_seats}"

class Airline:
    def init(self, name):
        self.name = name
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def remove_flight(self, flight):
        self.flights = [f for f in self.flights if f.flight_id != flight.flight_id]

    def get_flight_schedule(self):
        return self.flights

class FlightSystem:
    def init(self):
        self.users = []
        self.flights = []
        self.bookings = []
        self.routes = []
        self.airlines = []

    def add_user(self, name, phone):
        user = Passenger(name, phone)
        self.users.append(user)

    def add_flight(self, flight_id, destination, price, available_seats, route, departure_time, arrival_time):
        flight = Flight(flight_id, destination, price, available_seats, route, departure_time, arrival_time)
        self.flights.append(flight)

    def add_route(self, route_id, start_point, end_point):
        route = Route(route_id, start_point, end_point)
        self.routes.append(route)

    def add_airline(self, airline_name):
        airline = Airline(airline_name)
        self.airlines.append(airline)

    def search_flights_by_route(self, start_point, end_point):
        available_flights = [f for f in self.flights if f.route.start_point == start_point and f.route.end_point == end_point]
        if available_flights:
            for flight in available_flights:
                print(f"معرف الرحلة: {flight.flight_id}, الوجهة: {flight.destination}, السعر: {flight.price}")
        else:
            print("لا توجد رحلات متاحة لهذا المسار.")

    def save_data(self):
        data = {
            "users": [{"name": u.name, "phone": u.phone} for u in self.users],
            "flights": [{"flight_id": f.flight_id, "destination": f.destination, "price": f.price, "available_seats": f.available_seats, "route": {"start_point": f.route.start_point, "end_point": f.route.end_point}} for f in self.flights],
            "bookings": [{"user": b.user.name, "flight": b.flight.flight_id} for b in self.bookings],
            "routes": [{"route_id": r.route_id, "start_point": r.start_point, "end_point": r.end_point} for r in self.routes]
        }
        with open('data.json', 'w') as f:
            json.dump(data, f)

    def load_data(self):
        try:
            with open('data.json', 'r') as f:
                data = json.load(f)
                self.users = [Passenger(d['name'], d['phone']) for d in data['users']]
                self.routes = [Route(d['route_id'], d['start_point'], d['end_point']) for d in data['routes']]
                self.flights = [Flight(d['flight_id'], d['destination'], d['price'], d['available_seats'], next((r for r in self.routes if r.route_id == d['route']['route_id']), None), None, None) for d in data['flights']]
                self.bookings = []
                for b in data['bookings']:
                    user = next((u for u in self.users if u.name == b['user']), None)
                    flight = next((f for f in self.flights if f.flight_id == b['flight']), None)
                    if user and flight:
                        self.bookings.append(Booking(user, flight))
        except FileNotFoundError:
            print("لا يوجد ملف بيانات لتحميله.")


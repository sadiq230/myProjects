from flight_system import FlightSystem
from datetime import datetime

def main():
    system = FlightSystem()

    while True:
        print("\n===== نظام حجز الطيران =====")
        print("1. إضافة مستخدم")
        print("2. إضافة رحلة")
        print("3. تعديل مسار رحلة")
        print("4. البحث عن رحلة")
        print("5. حجز رحلة")
        print("6. عرض تذاكر المستخدم")
        print("7. تعديل مستخدم")
        print("8. حذف مستخدم")
        print("9. تعديل رحلة")
        print("10. حذف رحلة")
        print("11. حفظ البيانات")
        print("12. تحميل البيانات")
        print("13. عرض المستخدمين")
        print("14. عرض الرحلات")
        print("15. عرض المقاعد المحجوزة لكل رحلة")
        print("16. عرض المقاعد المتاحة لكل رحلة")
        print("17. إضافة مسار")
        print("18. تعديل مسار")
        print("19. البحث عن الرحلات بناءً على المسار")
        print("20. إضافة شركة طيران")
        print("21. إنهاء البرنامج")

        choice = input("اختر عملية: ")

        if choice == "1":
            name = input("أدخل اسم المستخدم: ")
            phone = input("أدخل رقم الهاتف: ")
            try:
                system.add_user(name, phone)
                print("تمت إضافة المستخدم بنجاح.")
            except ValueError as e:
                print(f"خطأ: {e}")

        elif choice == "2":
            flight_id = input("أدخل معرف الرحلة: ")
            destination = input("أدخل وجهة الرحلة: ")
            price = float(input("أدخل سعر الرحلة: "))
            available_seats = int(input("أدخل عدد المقاعد المتاحة: "))
            route_id = input("أدخل معرف المسار: ")
            route = next((r for r in system.routes if r.route_id == route_id), None)
            if route:
                departure_time = datetime.strptime(input("أدخل وقت الإقلاع (HH:MM): "), "%H:%M")
                arrival_time = datetime.strptime(input("أدخل وقت الوصول (HH:MM): "), "%H:%M")
                system.add_flight(flight_id, destination, price, available_seats, route, departure_time, arrival_time)
                print("تمت إضافة الرحلة بنجاح.")
            else:
                print("المسار غير موجود. أضف المسار أولاً.")

        elif choice == "3":
            flight_id = input("أدخل معرف الرحلة لتعديل المسار: ")
            new_route_id = input("أدخل معرف المسار الجديد: ")
            new_route = next((r for r in system.routes if r.route_id == new_route_id), None)
            if new_route:
                result = system.update_flight_route(flight_id, new_route)
                print(result)
            else:
                print("المسار الجديد غير موجود.")

        elif choice == "4":
            flight_id = input("أدخل معرف الرحلة: ")
            flight = next((f for f in system.flights if f.flight_id == flight_id), None)
            if flight:
                print(f"الرحلة: {flight.destination}, السعر: {flight.price}, المقاعد المتاحة: {flight.available_seats}, المسار: {flight.route.start_point} -> {flight.route.end_point}")
            else:
                print("لم يتم العثور على الرحلة.")

        elif choice == "5":
            user_name = input("أدخل اسم المستخدم: ")
            flight_id = input("أدخل معرف الرحلة: ")
            user = next((u for u in system.users if u.name == user_name), None)
            flight = next((f for f in system.flights if f.flight_id == flight_id), None)
            if user and flight:
                booking = flight.book_seat(user)
                if booking:
                    system.bookings.append(booking)
                    print("تم حجز الرحلة بنجاح.")
                else:
                    print("لا توجد مقاعد متاحة.")
            else:
                print("المستخدم أو الرحلة غير موجودين.")

        elif choice == "6":
            user_name = input("أدخل اسم المستخدم لعرض تذاكره: ")
            bookings = [b for b in system.bookings if b.user.name == user_name]

            if bookings:
                for booking in bookings:
                    print(f"المستخدم: {booking.user.name}, الرحلة: {booking.flight.destination}")
            else:
                print("لا توجد تذاكر لهذا المستخدم.")

        elif choice == "7":
            old_name = input("أدخل اسم المستخدم الحالي: ")
            user = next((u for u in system.users if u.name == old_name), None)
            if user:
                new_name = input("أدخل الاسم الجديد: ")
                new_phone = input("أدخل رقم الهاتف الجديد: ")
                user.name = new_name
                user.phone = new_phone
                print("تم تعديل بيانات المستخدم بنجاح.")
            else:
                print("المستخدم غير موجود.")

        elif choice == "8":
            name = input("أدخل اسم المستخدم المراد حذفه: ")
            system.users = [u for u in system.users if u.name != name]
            print("تم حذف المستخدم.")

        elif choice == "9":
            flight_id = input("أدخل معرف الرحلة لتعديل الوجهة والسعر: ")
            flight = next((f for f in system.flights if f.flight_id == flight_id), None)
            if flight:
                new_destination = input("أدخل الوجهة الجديدة: ")
                new_price = float(input("أدخل السعر الجديد: "))
                flight.destination = new_destination
                flight.price = new_price
                print("تم تعديل بيانات الرحلة بنجاح.")
            else:
                print("الرحلة غير موجودة.")

        elif choice == "10":
            flight_id = input("أدخل معرف الرحلة المراد حذفها: ")
            system.flights = [f for f in system.flights if f.flight_id != flight_id]
            print("تم حذف الرحلة.")

        elif choice == "11":
            system.save_data()
            print("تم حفظ البيانات بنجاح.")

        elif choice == "12":
            system.load_data()
            print("تم تحميل البيانات بنجاح.")

        elif choice == "13":
            if system.users:
                for user in system.users:
                    print(f"اسم المستخدم: {user.name}, رقم الهاتف: {user.phone}")
            else:
                print("لا يوجد مستخدمين.")

        elif choice == "14":
            if system.flights:
                for flight in system.flights:
                    print(f"معرف الرحلة: {flight.flight_id}, الوجهة: {flight.destination}, السعر: {flight.price}, المقاعد المتاحة: {flight.available_seats}")
            else:
                print("لا توجد رحلات.")

        elif choice == "15":
            flight_id = input("أدخل معرف الرحلة لعرض المقاعد المحجوزة: ")
            flight = next((f for f in system.flights if f.flight_id == flight_id), None)
            if flight:
                booked_seats = len([b for b in system.bookings if b.flight.flight_id == flight_id])
                print(f"عدد المقاعد المحجوزة: {booked_seats}")
            else:
                print("الرحلة غير موجودة.")

        elif choice == "16":
            flight_id = input("أدخل معرف الرحلة لعرض المقاعد المتاحة: ")
            flight = next((f for f in system.flights if f.flight_id == flight_id), None)
            if flight:
                available_seats = flight.available_seats - len([b for b in system.bookings if b.flight.flight_id == flight_id])
                print(f"عدد المقاعد المتاحة: {available_seats}")
            else:
                print("الرحلة غير موجودة.")

        elif choice == "17":
            route_id = input("أدخل معرف المسار: ")
            start_point = input("أدخل نقطة البداية: ")
            end_point = input("أدخل نقطة النهاية: ")
            system.add_route(route_id, start_point, end_point)
            print("تمت إضافة المسار بنجاح.")

        elif choice == "18":
            route_id = input("أدخل معرف المسار: ")
            new_start_point = input("أدخل نقطة البداية الجديدة: ")
            new_end_point = input("أدخل نقطة النهاية الجديدة: ")
            system.edit_route(route_id, new_start_point, new_end_point)

        elif choice == "19":
            start_point = input("أدخل نقطة البداية: ")
            end_point = input("أدخل نقطة النهاية: ")
            system.search_flights_by_route(start_point, end_point)

        elif choice == "20":
            airline_name = input("أدخل اسم شركة الطيران: ")
            system.add_airline(airline_name)
            print("تمت إضافة شركة الطيران بنجاح.")

        elif choice == "21":
            print("إنهاء البرنامج.")
            break

        else:
            print("اختيار غير صحيح.")


main()
def available_seats(total_seats, booked_seats):
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]

def book_seat(booked_seats, seat):
    if seat not in booked_seats:
        booked_seats.append(seat)
    else:
        print("Seat already booked.")

def cancel_seat(booked_seats, seat):
    if seat in booked_seats:
        booked_seats.remove(seat)
    else:
        print("Seat not booked.")

total_seats = 10
booked_seats = [2, 5, 7]
book_seat(booked_seats, 3)
cancel_seat(booked_seats, 5)
print(f"Available seats: {available_seats(total_seats, booked_seats)}")
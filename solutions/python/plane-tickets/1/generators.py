"""Functions to automate Conda airlines ticketing system."""

ltrs = ['A', 'B', 'C', 'D']

def generate_seat_letters(number: int):
    """Generate a series of letters for airline seats.
    :param number: int - total number of seat letters to be generated.
    :return: generator - generator that yields seat letters.
    Seat letters are generated from A to D.
    After D it should start again with A.
    Example: A, B, C, D
    """
    for i in range(number):
        yield ltrs[i % len(ltrs)]

def generate_seats(number):
    """Generate a series of identifiers for airline seats.
    :param number: int - total number of seats to be generated.
    :return: generator - generator that yields seat numbers.
    A seat number consists of the row number and the seat letter.
    There is no row 13.
    Each row has 4 seats.
    Seats should be sorted from low to high.
    Example: 3C, 3D, 4A, 4B
    """
    row = 1 
    while number > 0:
        if row == 13:
            row += 1  
        for ltr in ltrs:
            if number > 0:
                yield f"{row}{ltr}"
                number -= 1
            else:
                return
        row += 1

def assign_seats(passengers):
    """Assign seats to passengers.
    :param passengers: list[str] - a list of strings containing names of passengers.
    :return: dict - with the names of the passengers as keys and seat numbers as values.
    Example output: {"Adele": "1A", "Björk": "1B"}
    """
    seats = list(generate_seats(len(passengers)))
    return {passenger: seat for passenger, seat in zip(passengers, seats)}

def generate_codes(seat_numbers: list[str], flight_id: str):
    """Generate codes for a ticket.
    :param seat_numbers: list[str] - list of seat numbers.
    :param flight_id: str - string containing the flight identifier.
    :return: generator - generator that yields 12 character long ticket codes.
    """
    for seat in seat_numbers:
        identifier = (seat + flight_id).ljust(12, '0')
        yield identifier

from db.models import CinemaHall


def get_cinema_halls() -> str:
    return CinemaHall.objects.all()


def create_cinema_hall(hall_name: str,
                       hall_rows: int,
                       hall_seats_in_row: int) -> str:
    cinema_hall = CinemaHall.objects.create(
        name=hall_name,
        rows=hall_rows,
        seats_in_row=hall_seats_in_row
    )
    return cinema_hall

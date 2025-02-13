from endpoints.create_booking import CreateBooking


class TestCreateBooking:
    def test_create_booking(self):
        self.booking_creator = CreateBooking()
        self.booking_creator.create_booking()
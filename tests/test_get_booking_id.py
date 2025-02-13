from endpoints.get_booking_id import GetBookingId


class TestGetBookingId:

    def test_get_booking_id(self):
        self.get_book_id = GetBookingId()
        self.get_book_id.get_booking_id()
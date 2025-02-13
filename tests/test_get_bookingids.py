from endpoints.get_bookingids import GetBookingids


class TestGetBookingids:
    def test_get_bookingids(self):
        self.get_book_ids = GetBookingids()
        self.get_book_ids.get_bookingids()
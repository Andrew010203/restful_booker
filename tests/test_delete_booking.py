from endpoints.delete_booking import DeleteBooking


class TestDeleteBooking:
    def test_delete_booking(self, create_booking):
        self.booking_deleter = DeleteBooking()
        self.booking_deleter.delete_booking(create_booking)
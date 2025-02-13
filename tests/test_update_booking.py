from endpoints.update_booking import UpdateBooking


class TestUpdateBooking:
    def test_update_booking(self, create_booking):
        self.booking_updater = UpdateBooking()
        self.booking_updater.update_booking(create_booking)
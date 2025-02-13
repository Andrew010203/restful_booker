from endpoints.partial_update_booking import PartialUpdateBooking


class TestPartialUpdateBooking:
    def test_partial_update_booking(self, create_booking):
        self.part_updater = PartialUpdateBooking()
        self.part_updater.partial_update_booking(create_booking)
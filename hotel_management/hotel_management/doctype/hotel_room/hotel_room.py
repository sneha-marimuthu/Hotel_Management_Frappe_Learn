import frappe
from frappe.model.document import Document


class HotelRoom(Document):
    # begin: auto-generated types
    # This code is auto-generated. Do not modify anything in this block.

    from typing import TYPE_CHECKING

    if TYPE_CHECKING:
        from frappe.types import DF

        guest_occupied: DF.Link | None
        is_available: DF.Check
        is_cleaned: DF.Check
        price: DF.Currency
        room_no: DF.Data
        type: DF.Literal["Beach View", "Single Bedroom", "Double Bedroom", "Balcony"]
    # end: auto-generated types

    def before_insert(self):
        """Runs before a new Hotel Room is inserted into the database."""
        pass

    def validate(self):
        """Runs every time the document is saved."""
        self.validate_room_number()
        self.validate_price()

    def validate_room_number(self):
        """Validate the room number."""
        if not self.room_no:
            frappe.throw("Room No is required.")

    def validate_price(self):
        """Validate that the room price is valid."""
        if self.price is not None and self.price < 0:
            frappe.throw("Room Price cannot be negative.")

    def before_save(self):
        """Runs immediately before the document is saved."""
        pass

    def on_update(self):
        """Runs after an existing document is updated."""
        pass

    def after_insert(self):
        """Runs after a new document has been inserted."""
        pass

    def on_submit(self):
        """Runs when the document is submitted."""
        pass

    def on_cancel(self):
        """Runs when the document is cancelled."""
        pass

    def on_trash(self):
        """Runs before the document is deleted."""
        pass

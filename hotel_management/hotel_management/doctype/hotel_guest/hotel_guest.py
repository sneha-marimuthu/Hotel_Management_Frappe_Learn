# Copyright (c) 2026, Sneha M Techie and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class HotelGuest(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		guest_name: DF.Data | None
		phone: DF.Data | None
		room_number: DF.Link | None
		status: DF.Literal["Checked In", "Checked Out"]
	# end: auto-generated types

	_DOCTYPE_NAME = "Hotel Guest"

	def before_insert(self) -> None:
		doc = frappe.get_doc("Hotel Room", self.room_number)
		if doc.is_available == 1:
			frappe.throw("Room is already occupied. Please choose another room.")
	def validate(self) -> None:
		doc = frappe.get_doc("Hotel Room", self.room_number)
		if doc.is_available == 1 and self.status == "Checked In":
			frappe.throw("Room is already occupied. Please choose another room.")

	def before_save(self) -> None:
		doc = frappe.get_doc("Hotel Room", self.room_number)
		if doc.is_available == 1 and self.status == "Checked In":
			frappe.throw("Room is already occupied. Please choose another room.")
		doc.is_available = 1 if self.status == "Checked In" else 0
		doc.save()

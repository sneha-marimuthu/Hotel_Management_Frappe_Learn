# Copyright (c) 2026, Sneha M Techie and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class HotelContact(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		name1: DF.Data | None
		phone_number: DF.Phone | None
		type: DF.Literal["Employee", "Customer"]
	# end: auto-generated types

	_DOCTYPE_NAME = "Hotel Contact"

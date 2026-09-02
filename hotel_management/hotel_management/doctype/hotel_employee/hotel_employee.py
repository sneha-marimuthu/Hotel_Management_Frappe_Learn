# Copyright (c) 2026, Sneha M Techie and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe

class HotelEmployee(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		age: DF.Int
		email: DF.Data | None
		employee_name: DF.Data
		guest: DF.Link | None
		leave: DF.Literal["Yes", "No"]
		salary: DF.Int
	# end: auto-generated types

	_DOCTYPE_NAME = "Hotel Employee"

	

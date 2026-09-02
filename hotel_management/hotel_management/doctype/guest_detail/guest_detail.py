# Copyright (c) 2026, Sneha M Techie and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class GuestDetail(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		comment: DF.Text | None
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		phone: DF.Phone | None
	# end: auto-generated types

	_DOCTYPE_NAME = "Guest Detail"

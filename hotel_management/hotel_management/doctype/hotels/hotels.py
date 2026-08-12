# Copyright (c) 2026, Sneha M Techie and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
import frappe


class Hotels(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING
	def validate(self):
		frappe.logger().info("validate() called")
		frappe.msgprint("Hi Lets meet")
		

	if TYPE_CHECKING:
		from frappe.types import DF

		brand: DF.Data
		comment: DF.Text
	# end: auto-generated types

	_DOCTYPE_NAME = "Hotels"

	
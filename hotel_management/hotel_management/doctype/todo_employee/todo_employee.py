# Copyright (c) 2026, Sneha M Techie and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ToDoEmployee(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		description: DF.Text | None
		status: DF.Literal["Open", "Progress", "Close"]
		title: DF.Data | None
	# end: auto-generated types

	_DOCTYPE_NAME = "ToDo Employee"

	def validate(self):
		if not self.status:
			self.status = "Open"


@frappe.whitelist()
def mark_completed(name: str) -> str:
	todo = frappe.get_doc("ToDo Employee", name)
	todo.status = "Close"
	todo.save()
	return todo.name

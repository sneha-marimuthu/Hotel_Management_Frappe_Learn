# Copyright (c) 2026, Sneha M Techie and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Test(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

    def before_save(self):
        if not self.description.strip(): 
            self.description = "Test Default Description"

    from typing import TYPE_CHECKING
    if TYPE_CHECKING:
        from frappe.types import DF

        description: DF.LongText | None
	# end: auto-generated types

    _DOCTYPE_NAME = "Test"

    

// Copyright (c) 2026, Sneha M Techie and contributors
// For license information, please see license.txt

 frappe.ui.form.on("Hotels", {
 	refresh(frm){
 	frappe.msgprint("Form Opened");
 	frm.get_field("employee_name").$input.focus();
 	},
 });

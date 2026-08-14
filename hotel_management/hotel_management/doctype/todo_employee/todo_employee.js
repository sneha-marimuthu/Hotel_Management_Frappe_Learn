// Copyright (c) 2026, Sneha M Techie and contributors
// For license information, please see license.txt

frappe.ui.form.on("ToDo Employee", {
	refresh(frm) {
        if(!frm.is_new() && frm.doc.status !== "Close") {
            frm.add_custom_button('Mark Completed', () => {
                frappe.call( {
                    method: "hotel_management.hotel_management.doctype.todo_employee.todo_employee.mark_completed",
                    args: {
                        name: frm.doc.name
                    },
                    callback(r) {
                        frappe.msgprint({
                            titile: __('Success'),
                            message: __('ToDo Employee marked as completed'),
                            indicator: 'green'
                        })
                        frm.reload_doc();
                    }
                    
                })
            })
	}}
});

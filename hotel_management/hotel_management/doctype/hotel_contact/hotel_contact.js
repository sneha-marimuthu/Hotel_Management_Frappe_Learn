// Copyright (c) 2026, Sneha M Techie and contributors
// For license information, please see license.txt

frappe.ui.form.on("Hotel Contact", {
	refresh(frm) {
        frm.add_custom_button("Create Contact", () => {
            show_contact_dialog();
        });
	}
});

function show_contact_dialog() {
    let d = new frappe.ui.Dialog({
        title: "Create Contact",
        fields: [
            {
                label: "Name",
                fieldname: "name1",
                fieldtype: "Data",
                reqd: 1
            }
        ],
        primary_action_label: "Create",
        primary_action(values) {
            d.hide();
            frappe.route_options = {
                name1: values.name1
            };
            frappe.new_doc("Hotel Contact");
        }
    });
    d.show();
}
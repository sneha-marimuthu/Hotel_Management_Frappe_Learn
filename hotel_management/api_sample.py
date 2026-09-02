#Sample_Test_logic
import frappe

def Sample_Test_logic(doc, method):
    frappe.msgprint("Hook executed!")
    frappe.msgprint(f"{doc.name} triggered {method}")

@frappe.whitelist()
def mark_employee_on_leave(doc: dict) -> str: #docname is standard parameter for docname instead of passing fieldname employee_id as parameter
    doc = frappe.parse_json(doc)
    doc = frappe.get_doc("Hotel Employee", doc["employee_name"])

    doc.leave = "Yes"
    doc.save()

    return "Employee marked as On Leave"

@frappe.whitelist()
def mark_guest_checked_out(doc: dict) -> str:
    doc = frappe.parse_json(doc)
    doc = frappe.get_doc("Hotel Guest", doc["name"])

    doc.status = "Checked Out"
    doc.save()

    return "Guest checked out successfully"

@frappe.whitelist()
def test_action() -> None:
    frappe.msgprint("Server Action is working!")

@frappe.whitelist()
def room_availability_check(doc: dict) -> str:
    doc = frappe.parse_json(doc)
    doc = frappe.get_doc("Hotel Room", doc["room_no"])

    guest = frappe.db.exists("Hotel Guest", {"room_number": doc.room_no, "status": "Checked In"})
    if guest:
        doc.is_available = 1
        doc.save()
        return "Room is Occupied"
    else:
        doc.is_available = 0
        doc.save()
        return "Room is Available"

@frappe.whitelist()
def guest_room_book(doc: dict) -> str:
    doc = frappe.parse_json(doc)
    room_doc = frappe.get_doc("Hotel Guest", doc["guest_name"])
    doc = frappe.set_value("Hotel Room", room_doc.room_number, {"is_available": 1})

    return "Room is Booked"
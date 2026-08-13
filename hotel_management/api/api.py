#Sample_Test_logic
import frappe

def Sample_Test_logic(doc, method):
    frappe.msgprint("Hook executed!")
    frappe.msgprint(f"{doc.name} triggered {method}")
import frappe

def get_context(context):
    context.user_list = frappe.get_all("Hotel Employee", #filters={"enabled": 1},
                                       fields=["employee_name", "email"])
    context.title = "Our Team - BlackPearl"
    context.no_cache = True
    return context
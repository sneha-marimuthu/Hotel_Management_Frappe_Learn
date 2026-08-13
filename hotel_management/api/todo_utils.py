import frappe
from frappe.utils import now

@frappe.whitelist()
def get_recent_todos():

    todos = frappe.get_list(
        "ToDo",
        fields = ["name", "description", "owner", "status"],
        order_by = "creation desc",
        limit = 5
    )

    result = []

    for todo in todos:
        owner_email = frappe.db.get_value(
            "User",
            todo.owner,
            "email"
        )
        result.append({
            "name": todo.name,
            "description": todo.description,
            "status": todo.status,
            "owner_email": owner_email
        })

    current_time = now()

    return {
        "todos": result,
        "current_time": current_time
    }
import frappe
from frappe.utils import now

@frappe.whitelist(allow_guest=True)
def daily_maintenance():
    
    frappe.log_error(
        title="Daily Maintenance",
        message="Scheduler executed successfully"
    )

    frappe.logger().info("Daily Maintenance executed successfully")
    return {
        "status": "success",
        "message": "Daily Maintenance executed successfully",
        "executed_at": now()
    }
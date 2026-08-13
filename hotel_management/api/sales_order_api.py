import frappe
from frappe.query_builder import DocType

@frappe.whitelist(allow_guest=True)
def process_recent_sales_orders(limit: int=5):

    #DocType Definitions
    SalesOrder = DocType("Sales Order")
    Customer = DocType("Customer")

    #Query Builder
    query = (
        frappe.qb.from_(SalesOrder)
        .join(Customer)
        .on(SalesOrder.customer == Customer.name)
        .select(
            SalesOrder.name,
            SalesOrder.customer,
            Customer.customer_name,
            SalesOrder.status,
            SalesOrder.transaction_date
        )
        .orderby(SalesOrder.transaction_date, order = frappe.qb.desc)
        .limit(limit)
    )

    records = query.run(as_dict=True)

    #Document API
    #Changes for first record only
    if records:
        first_order_name = records[0]["name"]
        sales_order_doc = frappe.get_doc("Sales Order", first_order_name)
        sales_order_doc.terms= "Updated using Document API"
        sales_order_doc.save()

    #Database API
    #Changes for all records over db
    for row in records:
        frappe.db.set_value(
            "Sales Order",
            row["name"],
            "terms",
            "Bulk updated using Database API",
            update_modified = False
        )

    frappe.db.commit()
    return records
windows.create_todo_task = function() {
    let d = new frappe.ui.Dialog({
        title: 'Create ToDo Task',
        fields: [
            {
                label: 'Task',
                fieldname: 'task',
                fieldtype: 'Data',
                reqd: 1
            }
        ],
        primary_action_label: 'Create',
        primary_action(values) {
            frappe.db.insert({
                doctype: 'ToDo Employee',
                task_title: values.task_title,
                status: 'Open'
            }).then(doc => {
                d.hide();
                frappe.msgprint({
                    title:__('Success'),
                    indicator: 'Red',
                    message: __('ToDo Employee created successfully', [doc.name])
                });
            });
        }
    });
    d.show()
}
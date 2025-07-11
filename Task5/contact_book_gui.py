import tkinter as tk
from tkinter import messagebox, Toplevel, Label, Entry, Button
import json
import os

CONTACTS_FILE = "contacts.json"


def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return []


def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)


def update_contact_list(search_query=""):
    contacts = load_contacts()
    listbox_contacts.delete(0, tk.END)
    for idx, contact in enumerate(contacts, start=1):
        if search_query.lower() in contact['name'].lower() or search_query in contact['phone']:
            listbox_contacts.insert(tk.END, f"{idx}. {contact['name']}")


def add_contact_window():
    def save_new_contact():
        name = entry_name.get().strip()
        phone = entry_phone.get().strip()
        email = entry_email.get().strip()
        address = entry_address.get().strip()

        if not name or not phone:
            messagebox.showerror("Error", "Name and Phone Number are required!")
            return

        contacts = load_contacts()
        contacts.append({
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        })
        save_contacts(contacts)
        messagebox.showinfo("Success", f"Contact '{name}' added.")
        update_contact_list(search_var.get())
        add_win.destroy()

    add_win = Toplevel(root)
    add_win.title("Add New Contact")

    Label(add_win, text="Name:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    entry_name = Entry(add_win, width=40)
    entry_name.grid(row=0, column=1, padx=5, pady=5)

    Label(add_win, text="Phone:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
    entry_phone = Entry(add_win, width=40)
    entry_phone.grid(row=1, column=1, padx=5, pady=5)

    Label(add_win, text="Email:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
    entry_email = Entry(add_win, width=40)
    entry_email.grid(row=2, column=1, padx=5, pady=5)

    Label(add_win, text="Address:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
    entry_address = Entry(add_win, width=40)
    entry_address.grid(row=3, column=1, padx=5, pady=5)

    Button(add_win, text="Save Contact", command=save_new_contact).grid(row=4, column=0, columnspan=2, pady=10)


def update_contact_window():
    selection = listbox_contacts.curselection()
    if not selection:
        messagebox.showwarning("Select Contact", "Please select a contact to update.")
        return

    index = selection[0]
    contacts = load_contacts()
    filtered_contacts = [c for c in contacts if search_var.get().lower() in c['name'].lower() or search_var.get() in c['phone']]
    contact_to_update = filtered_contacts[index]


    def save_updated_contact():
        contact_to_update['name'] = entry_name.get().strip()
        contact_to_update['phone'] = entry_phone.get().strip()
        contact_to_update['email'] = entry_email.get().strip()
        contact_to_update['address'] = entry_address.get().strip()

        if not contact_to_update['name'] or not contact_to_update['phone']:
            messagebox.showerror("Error", "Name and Phone Number are required!")
            return

        save_contacts(contacts)
        messagebox.showinfo("Updated", f"Contact '{contact_to_update['name']}' updated.")
        update_contact_list(search_var.get())
        update_win.destroy()

    update_win = Toplevel(root)
    update_win.title("Update Contact")

    Label(update_win, text="Name:").grid(row=0, column=0, sticky="w", padx=5, pady=5)
    entry_name = Entry(update_win, width=40)
    entry_name.insert(0, contact_to_update['name'])
    entry_name.grid(row=0, column=1, padx=5, pady=5)

    Label(update_win, text="Phone:").grid(row=1, column=0, sticky="w", padx=5, pady=5)
    entry_phone = Entry(update_win, width=40)
    entry_phone.insert(0, contact_to_update['phone'])
    entry_phone.grid(row=1, column=1, padx=5, pady=5)

    Label(update_win, text="Email:").grid(row=2, column=0, sticky="w", padx=5, pady=5)
    entry_email = Entry(update_win, width=40)
    entry_email.insert(0, contact_to_update['email'])
    entry_email.grid(row=2, column=1, padx=5, pady=5)

    Label(update_win, text="Address:").grid(row=3, column=0, sticky="w", padx=5, pady=5)
    entry_address = Entry(update_win, width=40)
    entry_address.insert(0, contact_to_update['address'])
    entry_address.grid(row=3, column=1, padx=5, pady=5)

    Button(update_win, text="Save Changes", command=save_updated_contact).grid(row=4, column=0, columnspan=2, pady=10)


def delete_contact():
    selection = listbox_contacts.curselection()
    if not selection:
        messagebox.showwarning("Select Contact", "Please select a contact to delete.")
        return

    index = selection[0]
    contacts = load_contacts()
    filtered_contacts = [c for c in contacts if search_var.get().lower() in c['name'].lower() or search_var.get() in c['phone']]
    contact_to_delete = filtered_contacts[index]

    if messagebox.askyesno("Delete", f"Are you sure you want to delete '{contact_to_delete['name']}'?"):
        contacts.remove(contact_to_delete)
        save_contacts(contacts)
        messagebox.showinfo("Deleted", f"Contact '{contact_to_delete['name']}' deleted.")
        update_contact_list(search_var.get())


def search_contacts(*args):
    query = search_var.get()
    update_contact_list(query)


def show_contact_details(event):
    selection = listbox_contacts.curselection()
    if not selection:
        return

    index = selection[0]
    contacts = load_contacts()
    filtered_contacts = [c for c in contacts if search_var.get().lower() in c['name'].lower() or search_var.get() in c['phone']]
    contact = filtered_contacts[index]

    details_win = Toplevel(root)
    details_win.title(f"Details - {contact['name']}")

    Label(details_win, text=f"Name: {contact['name']}").pack(anchor='w', padx=10, pady=5)
    Label(details_win, text=f"Phone: {contact['phone']}").pack(anchor='w', padx=10, pady=5)
    Label(details_win, text=f"Email: {contact['email']}").pack(anchor='w', padx=10, pady=5)
    Label(details_win, text=f"Address: {contact['address']}").pack(anchor='w', padx=10, pady=5)

root = tk.Tk()
root.title("Contact Book")



# TOP: Search Bar
search_var = tk.StringVar()
search_var.trace("w", search_contacts)

search_frame = tk.Frame(root)
search_frame.pack(fill=tk.X, padx=10, pady=5)

tk.Label(search_frame, text="Search:").pack(side=tk.LEFT)
search_entry = tk.Entry(search_frame, textvariable=search_var, width=40)
search_entry.pack(side=tk.LEFT, expand=True, fill=tk.X)



# MIDDLE: Contact List with Scrollbar
list_frame = tk.Frame(root)
list_frame.pack(padx=10, pady=5)

scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL)
listbox_contacts = tk.Listbox(list_frame, width=50, height=15, yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox_contacts.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox_contacts.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

listbox_contacts.bind('<Double-1>', show_contact_details)



# BOTTOM: Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

btn_add = tk.Button(button_frame, text="Add Contact", command=add_contact_window)
btn_add.pack(side=tk.LEFT, padx=5)

btn_update = tk.Button(button_frame, text="Update Contact", command=update_contact_window)
btn_update.pack(side=tk.LEFT, padx=5)

btn_delete = tk.Button(button_frame, text="Delete Contact", command=delete_contact)
btn_delete.pack(side=tk.LEFT, padx=5)

btn_exit = tk.Button(button_frame, text="Exit", command=root.quit)
btn_exit.pack(side=tk.LEFT, padx=5)

update_contact_list()

root.mainloop()

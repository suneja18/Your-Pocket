import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

# --- Configuration & Pastel Theme ---
DATA_FILE = "finance_data.json"

COLORS = {
    "bg": "#FDFBF7",         # Off-white minimalist background
    "green": "#B5EAD7",      # Pastel Mint
    "blue": "#C7CEEA",       # Pastel Periwinkle
    "pink": "#FFB7B2",       # Pastel Coral
    "yellow": "#F9F871",     # Pastel Lemon
    "red": "#FF9AA2",        # Pastel Red for destructive actions
    "text": "#4A4A4A"        # Soft dark grey for text
}

class YourPocket:
    def __init__(self, root):
        self.root = root
        # Updated Title Here!
        self.root.title("Your Pocket")
        self.root.geometry("600x750") 
        self.root.configure(bg=COLORS["bg"])
        
        self.load_data()
        self.setup_ui()

    def load_data(self):
        """Loads transaction data from a JSON file."""
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r") as file:
                self.transactions = json.load(file)
        else:
            self.transactions = []

    def save_data(self):
        """Saves transaction data to a JSON file."""
        with open(DATA_FILE, "w") as file:
            json.dump(self.transactions, file, indent=4)

    def setup_ui(self):
        """Builds the tabbed user interface."""
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TNotebook", background=COLORS["bg"])
        style.configure("TNotebook.Tab", background=COLORS["blue"], foreground=COLORS["text"], font=("Helvetica", 12, "bold"))
        style.map("TNotebook.Tab", background=[("selected", COLORS["green"])])

        style.configure("Treeview", font=("Helvetica", 11), rowheight=28)
        style.configure("Treeview.Heading", font=("Helvetica", 12, "bold"))

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        self.tab_dashboard = tk.Frame(self.notebook, bg=COLORS["bg"])
        self.tab_history = tk.Frame(self.notebook, bg=COLORS["bg"])

        self.notebook.add(self.tab_dashboard, text="Dashboard")
        self.notebook.add(self.tab_history, text="History & Filters")

        self.setup_dashboard_tab()
        self.setup_history_tab()

        self.update_summary()
        self.refresh_history()

    def setup_dashboard_tab(self):
        """Builds the main input and summary screen."""
        summary_frame = tk.Frame(self.tab_dashboard, bg=COLORS["blue"], pady=15)
        summary_frame.pack(fill="x", padx=10, pady=10)

        tk.Label(summary_frame, text="My Financial Summary", font=("Helvetica", 18, "bold"), bg=COLORS["blue"], fg=COLORS["text"]).pack()
        
        self.lbl_spent = tk.Label(summary_frame, text="Total Spent: ₹0.00", font=("Helvetica", 14), bg=COLORS["blue"], fg=COLORS["text"])
        self.lbl_spent.pack()
        
        self.lbl_owed = tk.Label(summary_frame, text="Owed to Me: ₹0.00", font=("Helvetica", 14), bg=COLORS["blue"], fg=COLORS["text"])
        self.lbl_owed.pack()

        input_frame = tk.Frame(self.tab_dashboard, bg=COLORS["bg"], pady=20, padx=20)
        input_frame.pack(fill="both", expand=True)

        input_frame.grid_columnconfigure(0, weight=1)
        input_frame.grid_columnconfigure(1, weight=1)

        def make_label(text, row):
            tk.Label(input_frame, text=text, bg=COLORS["bg"], fg=COLORS["text"], font=("Helvetica", 12, "bold")).grid(row=row, column=0, sticky="e", pady=10, padx=5)

        make_label("Amount (₹):", 0)
        self.entry_amount = tk.Entry(input_frame, width=22, font=("Helvetica", 12), justify="center")
        self.entry_amount.grid(row=0, column=1, pady=10, sticky="w")

        make_label("Category:", 1)
        category_options = ["Food", "Transport", "Shopping", "Bills", "Fun", "Event/Trip", "Other"]
        self.combo_category = ttk.Combobox(input_frame, values=category_options, state="readonly", width=20, justify="center", font=("Helvetica", 12))
        self.combo_category.grid(row=1, column=1, pady=10, sticky="w")
        self.combo_category.current(0)

        make_label("Event (Optional):", 2)
        self.entry_event = tk.Entry(input_frame, width=22, font=("Helvetica", 12), justify="center")
        self.entry_event.grid(row=2, column=1, pady=10, sticky="w")

        make_label("Type:", 3)
        self.combo_type = ttk.Combobox(input_frame, values=["I spent this", "Someone owes me"], state="readonly", width=20, justify="center", font=("Helvetica", 12))
        self.combo_type.grid(row=3, column=1, pady=10, sticky="w")
        self.combo_type.current(0)

        btn_add = tk.Button(input_frame, text="Add Transaction", bg=COLORS["green"], fg=COLORS["text"], font=("Helvetica", 12, "bold"), command=self.add_transaction, relief="flat", padx=15, pady=8)
        btn_add.grid(row=4, column=0, columnspan=2, pady=30)

    def setup_history_tab(self):
        """Builds the history table, filters, dynamic totals, and action buttons."""
        filter_frame = tk.Frame(self.tab_history, bg=COLORS["bg"], pady=10)
        filter_frame.pack(fill="x", padx=10)
        
        center_filter_frame = tk.Frame(filter_frame, bg=COLORS["bg"])
        center_filter_frame.pack(anchor="center")

        tk.Label(center_filter_frame, text="Search Event:", bg=COLORS["bg"], fg=COLORS["text"], font=("Helvetica", 12, "bold")).pack(side="left", padx=5)
        
        self.entry_filter = tk.Entry(center_filter_frame, font=("Helvetica", 12), width=18, justify="center")
        self.entry_filter.pack(side="left", padx=5)
        
        tk.Button(center_filter_frame, text="Filter", bg=COLORS["yellow"], fg=COLORS["text"], font=("Helvetica", 10, "bold"), command=self.refresh_history, relief="flat", padx=8, pady=2).pack(side="left", padx=5)
        tk.Button(center_filter_frame, text="Clear Filter", bg=COLORS["blue"], fg=COLORS["text"], font=("Helvetica", 10, "bold"), command=self.clear_filter, relief="flat", padx=8, pady=2).pack(side="left", padx=5)

        columns = ("Date", "Type", "Category", "Event", "Amount")
        self.tree = ttk.Treeview(self.tab_history, columns=columns, show="headings", height=12)
        
        col_widths = {"Date": 90, "Type": 130, "Category": 100, "Event": 130, "Amount": 90}
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=col_widths[col], anchor="center") 
        
        self.tree.pack(fill="both", expand=True, padx=10, pady=5)

        self.lbl_filtered_totals = tk.Label(self.tab_history, text="Filtered Spent: ₹0.00  |  Filtered Owed: ₹0.00", font=("Helvetica", 12, "bold"), bg=COLORS["bg"], fg=COLORS["text"])
        self.lbl_filtered_totals.pack(pady=10)

        action_frame = tk.Frame(self.tab_history, bg=COLORS["bg"], pady=5)
        action_frame.pack(fill="x", padx=10, pady=5)

        center_action_frame = tk.Frame(action_frame, bg=COLORS["bg"])
        center_action_frame.pack(anchor="center")

        tk.Button(center_action_frame, text="Edit Selected", bg=COLORS["green"], fg=COLORS["text"], font=("Helvetica", 10, "bold"), command=self.edit_transaction, relief="flat", padx=10, pady=4).pack(side="left", padx=5)
        tk.Button(center_action_frame, text="Delete Selected", bg=COLORS["pink"], fg=COLORS["text"], font=("Helvetica", 10, "bold"), command=self.delete_transaction, relief="flat", padx=10, pady=4).pack(side="left", padx=5)
        tk.Button(center_action_frame, text="Clear All History", bg=COLORS["red"], fg=COLORS["text"], font=("Helvetica", 10, "bold"), command=self.clear_all_history, relief="flat", padx=10, pady=4).pack(side="left", padx=5)

    def add_transaction(self):
        try:
            amount = float(self.entry_amount.get())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for the amount.")
            return

        record = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "amount": amount,
            "category": self.combo_category.get(),
            "event": self.entry_event.get(),
            "type": self.combo_type.get()
        }

        self.transactions.append(record)
        self.save_data()
        self.update_summary()
        self.refresh_history() 
        
        self.entry_amount.delete(0, tk.END)
        self.entry_event.delete(0, tk.END)
        self.notebook.select(self.tab_history)

    def edit_transaction(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a transaction to edit.")
            return
            
        idx = int(selected[0])
        t = self.transactions[idx]

        top = tk.Toplevel(self.root)
        top.title("Edit Transaction")
        top.geometry("400x480") 
        top.configure(bg=COLORS["bg"])

        tk.Label(top, text="Edit Record", font=("Helvetica", 16, "bold"), bg=COLORS["bg"], fg=COLORS["text"]).pack(pady=15)

        def make_popup_input(label_text, default_val):
            tk.Label(top, text=label_text, bg=COLORS["bg"], fg=COLORS["text"], font=("Helvetica", 12, "bold")).pack(pady=(5,0))
            entry = tk.Entry(top, font=("Helvetica", 12), justify="center", width=22)
            entry.pack(pady=5)
            entry.insert(0, default_val)
            return entry

        entry_amt = make_popup_input("Amount (₹):", str(t["amount"]))
        
        tk.Label(top, text="Category:", bg=COLORS["bg"], fg=COLORS["text"], font=("Helvetica", 12, "bold")).pack(pady=(5,0))
        category_options = ["Food", "Transport", "Shopping", "Bills", "Fun", "Event/Trip", "Other"]
        combo_cat = ttk.Combobox(top, values=category_options, state="readonly", justify="center", width=20, font=("Helvetica", 12))
        combo_cat.pack(pady=5)
        combo_cat.set(t["category"])

        entry_evt = make_popup_input("Event (Optional):", t["event"])

        tk.Label(top, text="Type:", bg=COLORS["bg"], fg=COLORS["text"], font=("Helvetica", 12, "bold")).pack(pady=(5,0))
        combo_typ = ttk.Combobox(top, values=["I spent this", "Someone owes me"], state="readonly", justify="center", width=20, font=("Helvetica", 12))
        combo_typ.pack(pady=5)
        combo_typ.set(t["type"])

        def save_edit():
            try:
                new_amt = float(entry_amt.get())
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid number.", parent=top)
                return
            
            self.transactions[idx]["amount"] = new_amt
            self.transactions[idx]["category"] = combo_cat.get()
            self.transactions[idx]["event"] = entry_evt.get()
            self.transactions[idx]["type"] = combo_typ.get()

            self.save_data()
            self.update_summary()
            self.refresh_history()
            top.destroy()

        tk.Button(top, text="Save Changes", bg=COLORS["green"], fg=COLORS["text"], font=("Helvetica", 12, "bold"), command=save_edit, relief="flat", padx=15, pady=8).pack(pady=25)

    def delete_transaction(self):
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Please select a transaction to delete.")
            return
            
        idx = int(selected[0])
        del self.transactions[idx]
        
        self.save_data()
        self.update_summary()
        self.refresh_history()

    def clear_all_history(self):
        if not self.transactions:
            return
            
        confirm = messagebox.askyesno("Hold on!", "Are you sure you want to delete ALL your financial history? This cannot be undone.")
        if confirm:
            self.transactions = []
            self.save_data()
            self.update_summary()
            self.refresh_history()

    def update_summary(self):
        total_spent = 0.0
        total_owed = 0.0

        for t in self.transactions:
            if t["type"] == "I spent this":
                total_spent += t["amount"]
            elif t["type"] == "Someone owes me":
                total_owed += t["amount"]

        self.lbl_spent.config(text=f"Total Spent: ₹{total_spent:,.2f}")
        self.lbl_owed.config(text=f"Owed to Me: ₹{total_owed:,.2f}")

    def clear_filter(self):
        self.entry_filter.delete(0, tk.END)
        self.refresh_history()

    def refresh_history(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        filter_text = self.entry_filter.get().strip().lower()
        
        filtered_spent = 0.0
        filtered_owed = 0.0

        for i in range(len(self.transactions) - 1, -1, -1):
            t = self.transactions[i]
            event_name = t.get("event", "").lower()
            
            if filter_text and filter_text not in event_name:
                continue
            
            if t["type"] == "I spent this":
                filtered_spent += t["amount"]
            elif t["type"] == "Someone owes me":
                filtered_owed += t["amount"]
            
            amount_str = f"₹{t['amount']:,.2f}"
            self.tree.insert("", "end", iid=str(i), values=(t["date"], t["type"], t["category"], t["event"], amount_str))
            
        self.lbl_filtered_totals.config(text=f"Filtered Spent: ₹{filtered_spent:,.2f}  |  Filtered Owed: ₹{filtered_owed:,.2f}")

# --- App Execution ---
if __name__ == "__main__":
    root = tk.Tk()
    # Changed variable name to reflect new class name
    app = YourPocket(root)
    root.mainloop()

# 💰 Your Pocket — Personal Expense Tracker

A lightweight Python desktop application for tracking daily expenses, managing shared debts, and monitoring budgets — all stored locally, no internet required.

---

## 📌 Project Info

| Field | Details |
|---|---|
| **Student** | Suneja Dinesh Mhanta |
| **Roll No** | 34 |
| **Enrollment ID** | 2403111049 |
| **Department** | Electronics and Computer Engineering |
| **Guide** | Dr. R. S. Khamitkar |

---

## 🖥️ What It Does

- ✅ Add expenses and track who owes you money
- ✅ Filter transactions by event name (e.g., "Goa Trip", "Party")
- ✅ Edit or delete any transaction
- ✅ See live totals — Total Spent & Owed to Me
- ✅ All data saved locally in a JSON file — no database, no login needed
- ✅ Clean pastel-themed GUI built with Python's `tkinter`

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.x | Core language |
| `tkinter` + `ttk` | GUI framework |
| `json` | Local data storage |
| `datetime` | Date management |
| Python IDLE | Development IDE |

---

## 🚀 How to Run

**1. Make sure Python 3 is installed**
```bash
python --version
```

**2. Clone this repository**
```bash
git clone https://github.com/YOUR_USERNAME/your-pocket.git
cd your-pocket
```

**3. Run the app**
```bash
python your_pocket.py
```

> No external libraries needed — only Python's standard library is used!

---

## 📁 Project Structure

```
your-pocket/
│
├── your_pocket.py       # Main application file
├── finance_data.json    # Auto-created on first run (stores your data)
└── README.md            # You're reading this!
```

---

## 📸 App Preview

> *Dashboard Tab — Add transactions with category, event, and type*

> *History & Filters Tab — View, filter, edit, and delete records*

---

## 💡 Key Features Explained

### Two Tabs
- **Dashboard** — Input new transactions (amount, category, event, type)
- **History & Filters** — View all records, search by event, edit or delete

### Data Storage
- Saves everything to `finance_data.json` automatically
- Loads your data back every time you open the app

### Input Validation
- Shows an error popup if you type letters instead of a number in the Amount field
- Prevents app crashes with `try-except` handling

---

## 🧪 Sample Test Cases

| Input | Expected Output | Status |
|---|---|---|
| 260, Food, _(none)_, I spent this | Total Spent increases by ₹260.00 | ✅ Pass |
| 160, Bills, Roommate, Someone owes me | Owed to Me increases by ₹160.00 | ✅ Pass |
| `abc`, Fun, _(none)_, I spent this | Error popup shown, no crash | ✅ Pass |
| Filter: "Goa Trip" | Only matching rows shown with filtered totals | ✅ Pass |

---

## 📝 License

This project was built for academic submission purposes.  
© 2025 Suneja Dinesh Mhanta

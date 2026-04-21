# 💸 Your Pocket

> *Because your money deserves to be tracked — not lost.*

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python)
![GUI](https://img.shields.io/badge/GUI-Tkinter-green?style=flat-square)
![Storage](https://img.shields.io/badge/Storage-JSON-yellow?style=flat-square)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)

---

## 🌸 What is Your Pocket?

**Your Pocket** is a pastel-themed personal finance desktop app built entirely in Python.  
No internet. No bank links. No subscriptions. Just you and your money.

Track what you spend. Remember who owes you. Never lose count of your Goa trip budget again. 🏖️

---

## ✨ Features

| Feature | Description |
|---|---|
| 💰 Add Transactions | Log expenses or money owed to you |
| 🗂️ Categories | Food, Transport, Bills, Fun, and more |
| 🎯 Event Tracking | Tag transactions to events like "Goa Trip" or "Party" |
| 🔍 Smart Filter | Search and filter by event name instantly |
| ✏️ Edit & Delete | Fix or remove any record anytime |
| 🗑️ Clear History | Wipe everything with one click (with confirmation!) |
| 💾 Auto Save | Everything saved locally in JSON — no database needed |

---

## 🛠️ Built With

- **Python 3.x** — Core language
- **tkinter + ttk** — GUI and tabbed interface
- **json** — Local file storage
- **datetime** — Automatic date stamping

---

## 🚀 Getting Started

**1. Make sure Python is installed**
```bash
python --version
```

**2. Clone this repo**
```bash
git clone https://github.com/suneja18/Your-Pocket.git
cd Your-Pocket
```

**3. Run it!**
```bash
python your-pocket.py
```

> No pip installs needed — runs on Python's built-in libraries only! 🎉

---

## 🧪 Test Cases

| What I tried | What happened | Result |
|---|---|---|
| Amount: 260, Food, I spent this | Total Spent went up by ₹260 | ✅ Pass |
| Amount: 160, Bills, Someone owes me | Owed to Me went up by ₹160 | ✅ Pass |
| Amount: `abc` | Error popup, no crash | ✅ Pass |
| Filter: "Goa Trip" | Only Goa Trip rows showed up | ✅ Pass |

---

## 💡 Challenges I Solved

- **Table ordering** — New entries appear on top, not bottom
- **Input validation** — App doesn't crash if you type letters in the amount field
- **Layout alignment** — Got everything centered cleanly without third-party tools

---

## 👩‍💻 Made By

**Suneja Dinesh Mhanta** — Roll No. 34  
Electronics and Computer Engineering  
Guide: Dr. R. S. Khamitkar

---

*Built with 💜 and a lot of pastel colors.*

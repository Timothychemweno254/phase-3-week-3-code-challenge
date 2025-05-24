# Freebie Tracker

A Python-based command-line application that tracks **developers**, **companies**, and the **freebies** given by companies to developers. Built using **SQLAlchemy ORM** and **SQLite**, this app allows users to create, view, and manage records in a structured relational database.

---

---

##  Features

-  **Developers**
  - Add a new developer
  - View all developers with the number of freebies received
  - Delete a developer and their associated freebies

-  **Companies**
  - Add a new company with founding year
  - View all companies with total value of freebies given

- **Freebies**
  - Add a freebie linked to a developer and a company
  - View all freebies with detailed info

---

##  Models Overview

### `Dev`
Represents a developer who can receive freebies.

- `id`: Primary key
- `name`: Unique, required
- `freebies`: One-to-many relationship with `Freebie`

### `Company`
Represents a company that gives freebies.

- `id`: Primary key
- `name`: Unique, required
- `founding_year`: Year of establishment
- `freebies`: One-to-many relationship with `Freebie`

### `Freebie`
Represents a gift from a company to a developer.

- `id`: Primary key
- `item_name`: Name of the item
- `value`: Integer value
- `dev_id`: Foreign key to `Dev`
- `company_id`: Foreign key to `Company`

---

## 🛠️ Technologies Used

- **Python 3**
- **SQLAlchemy** - ORM for defining and interacting with the database
- **SQLite** - Lightweight local database for storage

---

## Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/y/freebie-tracker.git
cd freebie-tracker
cd app

now run these commands 

pip install sqlalchemy

python app.py

Created by [Timothy Kiprop]
GitHub • tchemweno18@gmail.com


© 2025 Timothy Kiprop. All rights reserved.







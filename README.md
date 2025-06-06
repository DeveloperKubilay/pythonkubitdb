# 🔥 KubitDB 🔥

> **No cap, this is the simplest JSON database you'll ever use** 💯

## 📲 Installation

```
Download kubitdb.py to your home directory
```

## 🚀 Getting Started

```python
import kubitdb

# Create a new db (call it whatever you want)
db = kubitdb.Data("test.json")
```

## 📚 Features & Examples

### ✅ Set Data

```python
# Store your stuff like this
db.set("username", "kubit")
db.set("coins", 100)
db.set("items", ["sword", "shield"])
```

### 🔍 Get Data

```python
# Pull your data out
user = db.get("username")  # returns "kubit"
coins = db.get("coins")    # returns 100
```

### 🧮 Subtract Values

```python
# For numbers only!
db.set("coins", 100)
db.subtract("coins", 25)  # coins is now 75
```

### 📋 Push to Arrays

```python
# Add stuff to your lists
db.push("inventory", {"item": "potion", "quantity": 3})
# Creates an array if it doesn't exist yet!
```

### ❓ Check if Data Exists

```python
# See if something's there
if db.has("username"):
    print("User exists!")  # returns True or False
```

### 📊 Get All Data

```python
# Grab everything at once
all_data = db.all()  # returns the entire database as a dict
```

### 🗑️ Delete Data

```python
# Yeet that data outta there
db.delete("username")  # removes the username key and its value
```

### 💣 Clear Everything

```python
# Start fresh
db.clear()  # deletes EVERYTHING in the database
```

## 🔗 Complete Example

```python
import kubitdb

# Start fresh with a new db
db = kubitdb.Data("game_data.json")

# Set some initial data
db.set("player", "xXx_G4M3R_xXx")
db.set("level", 1)
db.set("health", 100)
db.set("inventory", [])

# Add items to inventory
db.push("inventory", {"name": "wooden sword", "damage": 5})
db.push("inventory", {"name": "health potion", "restore": 20})

# Player takes damage
db.subtract("health", 25)

# Print current stats
print(f"Player: {db.get('player')}")
print(f"Level: {db.get('level')}")
print(f"Health: {db.get('health')}")
print(f"Inventory: {db.get('inventory')}")
```

---

Made with ❤️ by DeveloperKubilay

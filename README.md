# 📝 Task Manager

> A simple and lightweight **CLI Task Manager** built with Python.

### 🛠️ Built With

`Python` · `Pydantic` · `JSON` · `Rich`

---

## ✨ Features

- ➕ Add tasks
- 📋 View tasks
- 🗑️ Delete tasks
- ✅ Mark tasks as completed

---

## 📋 Task List

```text
                         TASK LIST

┏━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ ID ┃ Title            ┃ Description          ┃ Completed ┃
┡━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━┩
│ 1  │ Learn Python     │ Practice Pydantic    │ Pending   │
│ 2  │ Build Task App   │ Finish CRUD          │ Yes       │
└────┴──────────────────┴──────────────────────┴───────────┘
```

---

## ⚙️ How It Works

```text
       User Input
           │
           ▼
   Pydantic Validation
           │
           ▼
       Task List
           │
           ▼
      tasks.json
           │
           ▼
        Rich UI
```

---

## 📂 Storage

Tasks are stored in:

`tasks.json`

The file is loaded when the application starts and updated whenever tasks are changed.

---

## 🚀 Run

```bash
python main.py
```
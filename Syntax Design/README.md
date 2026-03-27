# Ahlam Programming Language

Ahlam is a **custom, simple programming language** built on Python.  
It allows you to **store strings in variables** and **display them**, all with easy-to-read syntax.  
You can run your `.am` programs with a single command in VS Code or CMD.

---

## 📂 Folder Structure

```
Ahlam/
├── run_ahlam.py      # Python interpreter
├── Ahlam.bat         # Windows launcher
├── ahlam.am          # Example program
└── README.md         # This file
```

---

## ⚡ Requirements

- Python 3.x installed  
- Windows (for batch file)  
- Optional: VS Code terminal or CMD/PowerShell

---
## Setup

1. download this Folder 
2.copy the full path exmpl:  C:\Users\Administrator\Downloads\Syntax Design
3. Open Environment Variables:
 Win + S → type "Environment Variables" → Enter → "Edit the system environment variables" → "Environment Variables…"

 Edit Path:
 select "Path" → "Edit"

Add New Path:
Click "New" → Paste your folder path, e.g.:
 C:\Users\Administrator\Downloads\Syntax Design

 Save:
Click OK → OK → OK

## 🏃 How to Run Programs

1. Open **VS Code Terminal** or **CMD/PowerShell** in the folder.  
2. Run any `.am` file with:

```powershell
Ahlam filename.am
```

Example with included `ahlam.am`:

```powershell
 Ahlam ahlam.am

```

> ✅ Output:  

```
Hello World
Direct String Output
```

---

## 📝 Writing Ahlam Programs

- **Store a string in a variable:**

```ahlam
st"Hello World"/'Text'
```

- **Display a variable:**

```ahlam
displaY:: Text ::
```

- **Display a direct string without variable:**

```ahlam
displaY:: "Direct String Output" ::
```

---

## 🌟 Tips

- You can create **multiple `.am` files** for different programs.  
- No need to modify Python code — just edit `.am` files.  
- Use **direct strings** or **variables** for output.  

---

## 📦 Optional Enhancements

- Add **loops** and **conditions** to your programs.  
- Control **ESP or hardware** using Python extensions.  
- Organize multiple example programs in an `examples/` folder.

---

## 📜 License

This project is open-source. You can freely use, modify, and share it.

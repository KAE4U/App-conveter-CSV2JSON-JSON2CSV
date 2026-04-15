# App-conveter-CSV2JSON-JSON2CSV
# 🔄 JSON ⇄ CSV Converter

A simple and efficient desktop application to convert files between **JSON and CSV formats**, featuring **drag and drop support**.

---

## Features

*  Bidirectional conversion:
* JSON → CSV
* CSV → JSON
*  Drag and drop file support
*  Choose where to save the converted file
*  Fast and lightweight interface

---

##  Preview

<img width="1920" height="1160" alt="image" src="https://github.com/user-attachments/assets/5dcd4965-a435-442d-9b87-f8225b981774" />


---

##  Technologies Used

* Python 3
* Tkinter
* tkinterdnd2

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/json-csv-converter.git
cd json-csv-converter
```

---

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install tkinterdnd2
```

---

### 4. Run the application

```bash
python appconverter.py
```

---

##  Requirements

* Python 3.10+
* Tkinter installed on the system

On Linux (Ubuntu/ZorinOS):

```bash
sudo apt install python3-tk python3-venv
```

---

## Notes

* JSON files should be in a **list of objects format** for direct conversion
* CSV files do not preserve data types (everything is treated as string)

---

##  Future Improvements

* Modern UI using CustomTkinter
* Support for nested JSON
* Progress bar for large files
* Conversion history
* Export as executable (.exe / .AppImage)

---

## License

This project is open-source and available under the MIT License.

---

##  Author

Developed by **Pedro Lucca Rizzato**

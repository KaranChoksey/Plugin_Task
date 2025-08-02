# Dify Google Sheets Plugin

This plugin integrates Google Sheets with Dify apps.  
It allows AI workflows to:
- Append rows
- Update specific cells
- Read data from sheets

---

## Features
- **Append Row**: Add new rows to a Google Sheet.
- **Update Cell**: Modify values in specific cells.
- **Read Sheet**: Retrieve values from a sheet.

---

## Tech Stack
- **Python 3.10+**
- **Flask** (web framework)
- **gspread** (Google Sheets API)
- **Google Service Account** (for authentication)

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/dify-google-sheets-plugin.git
cd dify-google-sheets-plugin
```
### 2. Setup Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate   # For Windows
pip install -r requirements.txt
```
### 3. Run the Plugin
```bash
python app.py
```

The plugin runs on:
http://127.0.0.1:3334

## Example Test Output
The file [`output.txt`](./output.txt) which contains sample responses from API testing using `curl`.

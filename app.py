from flask import Flask, request, jsonify
import gspread
from google.oauth2.service_account import Credentials

app = Flask(__name__)


SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=SCOPES)
client = gspread.authorize(creds)

# --- Append Row ---
@app.route("/append_row", methods=["POST"])
def append_row():
    data = request.json
    sheet_id = data.get("sheet_id")
    row_values = data.get("row_values")

    if not sheet_id or not row_values:
        return jsonify({"error": "sheet_id and row_values are required"}), 400

    try:
        sheet = client.open_by_key(sheet_id).sheet1
        sheet.append_row(row_values)
        return jsonify({"status": "success", "appended": row_values})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- Read Sheet ---
@app.route("/read_sheet", methods=["POST"])
def read_sheet():
    data = request.json
    sheet_id = data.get("sheet_id")

    if not sheet_id:
        return jsonify({"error": "sheet_id is required"}), 400

    try:
        sheet = client.open_by_key(sheet_id).sheet1
        rows = sheet.get_all_values()
        return jsonify({"status": "success", "rows": rows})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# --- Update Cell ---
@app.route("/update_cell", methods=["POST"])
def update_cell():
    data = request.json
    sheet_id = data.get("sheet_id")
    cell = data.get("cell")  # Example: "B2"
    value = data.get("value")

    if not sheet_id or not cell or value is None:
        return jsonify({"error": "sheet_id, cell, and value are required"}), 400

    try:
        sheet = client.open_by_key(sheet_id).sheet1
        sheet.update(cell, value)
        return jsonify({"status": "success", "updated": {cell: value}})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3334)

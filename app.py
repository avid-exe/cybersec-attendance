from flask import Flask, render_template, request, jsonify
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

# -----------------------------
# Google Sheets Authentication
# -----------------------------
scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]
creds = ServiceAccountCredentials.from_json_keyfile_name(
    "attendanceapp-467907-0f2fc3773dd4.json", scope
)
client = gspread.authorize(creds)

# Use your sheet name and worksheet name here
sheet = client.open("Attendance").worksheet("Sheet1")

# -----------------------------
# FORM PAGE ROUTE
# -----------------------------
@app.route("/", methods=["GET"])
def index():
    # Fetch all records starting from row 2 (where your headers are)
    all_values = sheet.get_all_values()
    
    # Row 2 is index 1 (0-based indexing)
    if len(all_values) > 1:
        headers = all_values[1]  # Row 2 contains your headers
        records = []
        
        # Process rows starting from row 3 (index 2)
        for row in all_values[2:]:
            if len(row) >= 3 and any(row):  # Check if row has data
                record = {
                    "Full Name": row[0] if len(row) > 0 else "",
                    "Matric No": row[1] if len(row) > 1 else "",
                    "Department": row[2] if len(row) > 2 else ""
                }
                records.append(record)
    else:
        records = []
    
    return render_template("form.html", records=records)

# -----------------------------
# FORM SUBMISSION ROUTE
# -----------------------------
@app.route("/submit", methods=["POST"])
def submit():
    full_name = request.form.get("full_name", "").strip()
    matric_no = request.form.get("matric_no", "").strip()
    department = request.form.get("department", "").strip()
    
    if not full_name or not matric_no or not department:
        return jsonify({"status": "error", "message": "❌ All fields are required."})
    
    # Check for duplicates
    all_values = sheet.get_all_values()
    
    if len(all_values) > 2:
        for row in all_values[2:]:  # Check from row 3 onwards
            if len(row) >= 2:
                if (row[0].strip().lower() == full_name.lower() and
                    row[1].strip().lower() == matric_no.lower()):
                    return jsonify({"status": "error", "message": "❌ Record already exists."})
    
    # Append new record (it will go to the next available row)
    sheet.append_row([full_name, matric_no, department])
    
    # Return updated list of records to display
    all_values = sheet.get_all_values()
    records = []
    if len(all_values) > 1:
        for row in all_values[2:]:
            if len(row) >= 3 and any(row):
                record = {
                    "Full Name": row[0] if len(row) > 0 else "",
                    "Matric No": row[1] if len(row) > 1 else "",
                    "Department": row[2] if len(row) > 2 else ""
                }
                records.append(record)
    
    return jsonify({"status": "success", "message": "✅ Attendance submitted successfully.", "records": records})

# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

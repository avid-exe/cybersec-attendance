
from flask import Flask, render_template, request, redirect
import gspread
from oauth2client.service_account import ServiceAccountCredentials

app = Flask(__name__)

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("attendanceapp-467907-13d2150aaccb.json", scope)
client = gspread.authorize(creds)
sheet = client.open("Attendance").sheet1

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        full_name = request.form["full_name"].strip()
        matric_no = request.form["matric_no"].strip()
        department = request.form["department"].strip()

        records = sheet.get_all_records()
        for record in records:
            if (record["Full Name"].strip().lower() == full_name.lower() and
                record["Matric No"].strip().lower() == matric_no.lower()):
                return render_template("form.html", alert="❌ Record already exists.")

        sheet.append_row([full_name, matric_no, department])
        return redirect("/thankyou")
    return render_template("form.html", alert=None)

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

if __name__ == "__main__":
    app.run(debug=True)




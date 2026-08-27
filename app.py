from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/" , methods = [ "GET", "POST"])
def index():
    bmi = None
    status = None
    if request.method == "POST":
        weight = float(request.form["weight"])
        height_cm = float(request.form["height"])
        height_m = height_cm / 100
        bmi = round(weight / (height_m ** 2), 2)

        if bmi <18.5:
            status = "น้ำหนักน้อย"
        elif bmi < 23:
            status = "ปกติ"
        elif bmi < 25:
            status = "น้ำหนักเกิน"
        elif bmi < 30:
            status = "อ้วน"
        else:
            status = "อ้วนมาก(อิอ้วนมิจิ)"
    return render_template("index.html", bmi=bmi, status=status)

if __name__ == "__main__":
    app.run(debug=True, port=5001)


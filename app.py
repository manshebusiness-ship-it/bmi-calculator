from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    bmi = status = color = None
    diet_advice = exercise_advice = None

    if request.method == "POST":
        weight = float(request.form["weight"])
        height_cm = float(request.form["height"])
        height_m = height_cm / 100
        bmi = round(weight / (height_m ** 2), 2)

        if bmi < 18.5:
            status, color = "น้ำหนักน้อย", "blue"
            diet_advice = "เพิ่มพลังงานจากข้าว โปรตีน และไขมันดี เช่น ถั่ว อะโวคาโด"
            exercise_advice = "เน้นเวทเทรนนิ่งเพื่อเสริมกล้ามเนื้อ 3 วัน/สัปดาห์"
        elif bmi < 23:
            status, color = "น้ำหนักปกติ", "green"
            diet_advice = "เน้นผัก โปรตีนไม่ติดมัน และลดน้ำตาล"
            exercise_advice = "ออกกำลังกายระดับปานกลาง 150 นาที/สัปดาห์"
        elif bmi < 25:
            status, color = "น้ำหนักเกิน", "orange"
            diet_advice = "ลดของทอด น้ำตาล และแป้งขัดสี เพิ่มผักใบเขียว"
            exercise_advice = "เดินเร็วหรือปั่นจักรยาน 30 นาที/วัน อย่างน้อย 5 วัน/สัปดาห์"
        elif bmi < 30:
            status, color = "อ้วน", "red"
            diet_advice = "ควบคุมแคลอรี่ ลดของหวานและแป้ง เน้นโปรตีนไม่ติดมัน"
            exercise_advice = "คาร์ดิโอเบาๆ เช่น เดิน ว่ายน้ำ 30-45 นาที/วัน"
        else:
            status, color = "อ้วนมาก", "darkred"
            diet_advice = "ควรปรึกษาแพทย์/นักโภชนาการเพื่อวางแผนอาหารเฉพาะบุคคล"
            exercise_advice = "เริ่มจากการเดินเบาๆ และเพิ่มความหนักตามคำแนะนำแพทย์"

    return render_template("index.html", bmi=bmi, status=status, color=color,
                            diet_advice=diet_advice, exercise_advice=exercise_advice)

if __name__ == "__main__":
    app.run(debug=True)

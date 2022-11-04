from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>資訊管理導論作業 企管四C 410819617尹譔祺</h1>"
    homepage += "<a href=/aboutmatthew>MIS自傳履歷</a><br>"
    homepage += "<a href=/InterestTestResults>興趣何倫碼測驗結果</a><br><br>"
    homepage += "<a href=/job>感興趣職業</a><br><br>"
    homepage += "<a href=/futureplan>未來規劃</a><br><br>"
    return homepage

@app.route("/aboutmatthew")
def aboutmatthew():
    return render_template("aboutmatthew.html")

@app.route("/InterestTestResults.html")
def InterestTestResults():
    return render_template("InterestTestResults.html")

@app.route("/job")
def job():
    return render_template("job.html")

@app.route("/futureplan")
def futureplan():
    return render_template("futureplan.html")

if __name__ == "__main__":
    app.run()
from flask import Flask, render_template,request
import DbClass as db

app = Flask(__name__)

database = db.DbClass()

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def pageNotFound(error):
    return render_template('error.html',error=error)

@app.route('/data',methods=['GET'])
def data():
    if request.method=='GET':
        temperature= database.getTempvalueDataFromDatabase()
        tempTimestamp= database.getTempTimestampDataFromDatabase()
        tempFansOn= database.getTempFansDataFromDatabase()

        humidity = database.getHumValueDataFromDatabase()
        humTimestamp= database.getHumTimestampDataFromDatabase()
    return render_template('data.html',temperature=temperature,
                           tempTimestamp=tempTimestamp,tempFansOn=tempFansOn,
                           humidity=humidity,humTimestamp=humTimestamp)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)

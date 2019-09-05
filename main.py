from flask import Flask,render_template,redirect, url_for, request
import csv,time

app = Flask(__name__)

@app.route('/')
def home():
  return render_template("index.html")

@app.route('/log', methods=['GET'])
def log():
  tim=request.args.get("time")
  temp=request.args.get("temp")
  humi=request.args.get("humi")
  
  seconds=time.time()
  seconds=time.localtime(seconds)
  
  timee=str(seconds.tm_hour)+":"+str(seconds.tm_min)+":"+str(seconds.tm_sec)
  with open("09052019.csv","a+", newline='') as data:
    write= csv.writer(data,delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    write.writerow([tim,temp,humi,timee])
   
  return render_template("Log.html")

if __name__== '__main__':
    app.run(debug = True, host='0.0.0.0', port=8080)
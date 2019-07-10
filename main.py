from flask import Flask,abort,render_template,request, jsonify
import requests
import json
app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def main():
   return render_template('index.html')
tempDB=[
 {
   "DATE": "20130101",
   "TMAX": 34,
   "TMIN": 26
 },
 {
   "DATE": "20130102",
   "TMAX": 29.5,
   "TMIN": 15
 },
  {
    "DATE": "20190326",
    "TMAX": 69.1,
    "TMIN": 62.8
  },
  {
    "DATE": "20190327",
    "TMAX": 90.7,
    "TMIN": 68.9
  }
]
@app.route('/historical/',methods=['GET'])
def getAllDates():
    dlist1 = []
    for i in tempDB:
        for key,value in i.iteritems():
            if key == 'DATE':
                dict1 = {}
                dict1[key] = value
                dlist1.append(dict1)
    return jsonify(dlist1)
@app.route('/historical/<dateYYYYMMDD>',methods=['GET'])
def getDate(dateYYYYMMDD):
    temp = [temp for temp in tempDB if temp['DATE'] == dateYYYYMMDD]
    if len(temp) == 0:
        abort(404)
    return str(temp[0]).replace("'",'"')
@app.route('/historical/', methods = ['POST'])
def insertDate():
    if not request.json or not "DATE" in request.json:
        abort(400)
    temp = {
        "DATE": request.json["DATE"],
        "TMAX": request.json["TMAX"],
        "TMIN": request.json["TMIN"]
    }
    temp['DATE'] = (temp['DATE']).encode('ascii')
    tempDB.append(temp)
    return jsonify({'DATE': temp['DATE']}), 201
@app.route('/historical/<dateYYYYMMDD>', methods = ['DELETE'])
def deleteDate(dateYYYYMMDD):
    temp = [temp for temp in tempDB if temp['DATE'] == dateYYYYMMDD]
    if len(temp) == 0:
        abort(404)
    for i in temp:
        tempDB.remove(i)
    return jsonify({'result': True})
@app.route('/forecast/<dateYYYYMMDD>', methods=['GET'])
def forecast(dateYYYYMMDD):
    dlist=[]
    found=0
    count=1
    date_given=dateYYYYMMDD
    for j in tempDB:
        for key, value in j.items():
            ddict={}
            if key=='DATE':
                if value==dateYYYYMMDD:
                    found=1
            if found==1:
                ddict[key]=value
        if (found and count<=7):
            count=count+1;
            dlist.append(ddict)
            ddict={}
    if found==0:
         datalist = []
         for number in range(0, 7):
            tmax = 0
            tmin = 0
            for index in range(0, len(dlist)):
                if number == 0:
                    dlist[index] = dlist[index]
                if number > 0:
                    dlist[index] = dlist[index] + 1
            data_list = []
            for ind in dlist:
                if ind < len(tempDB):
                    data_list.append(tempDB[ind])
            for items in data_list:
                for key, value in items.iteritems():
                    if key == "DATE":
                        pred_temp = {"DATE": date_given[0:4] + value[4:]}
                    if key == 'TMAX':
                        tmax = tmax + value
                    if key == 'TMIN':
                        tmin = tmin + value
            pred_temp["TMAX"] = float("%.2f" % (tmax / len(dlist)))
            pred_temp["TMIN"] = float("%.2f" % (tmin / len(dlist)))
            dlist.append(pred_temp)
    if len(dlist)==0:
        abort(404)
    return jsonify(dlist)
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

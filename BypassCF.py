#coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import pycurl
import StringIO
import re
import time
import random
from retrying import retry

def test(calc):
    a = calc
    if a == '+[]':
        return '0'
    else:
        a = a.replace('+[]','')
    a = a.replace('1+1', '2')
    a = a.replace('1+2', '3')
    a = a.replace('1+3', '4')
    a = a.replace('1+4', '5')
    a = a.replace('1+5', '6')
    a = a.replace('1+6', '7')
    a = a.replace('1+7', '8')
    a = a.replace('1+8', '9')
    a = a.replace('1+9', '10')
    a = a.replace('2+1', '3')
    a = a.replace('2+2', '4')
    a = a.replace('2+3', '5')
    a = a.replace('2+4', '6')
    a = a.replace('2+5', '7')
    a = a.replace('2+6', '8')
    a = a.replace('2+7', '9')
    a = a.replace('2+8', '10')
    a = a.replace('2+9', '11')
    a = a.replace('3+1', '4')
    a = a.replace('3+2', '5')
    a = a.replace('3+3', '6')
    a = a.replace('3+4', '7')
    a = a.replace('3+5', '8')
    a = a.replace('3+6', '9')
    a = a.replace('3+7', '10')
    a = a.replace('3+8', '11')
    a = a.replace('3+9', '12')
    a = a.replace('4+1', '5')
    a = a.replace('4+2', '6')
    a = a.replace('4+3', '7')
    a = a.replace('4+4', '8')
    a = a.replace('4+5', '9')
    a = a.replace('4+6', '10')
    a = a.replace('4+7', '11')
    a = a.replace('4+8', '12')
    a = a.replace('4+9', '13')
    a = a.replace('5+1', '6')
    a = a.replace('5+2', '7')
    a = a.replace('5+3', '8')
    a = a.replace('5+4', '9')
    a = a.replace('5+5', '10')
    a = a.replace('5+6', '11')
    a = a.replace('5+7', '12')
    a = a.replace('5+8', '13')
    a = a.replace('5+9', '14')
    a = a.replace('6+1', '7')
    a = a.replace('6+2', '8')
    a = a.replace('6+3', '9')
    a = a.replace('6+4', '10')
    a = a.replace('6+5', '11')
    a = a.replace('6+6', '12')
    a = a.replace('6+7', '13')
    a = a.replace('6+8', '14')
    a = a.replace('6+9', '15')
    a = a.replace('7+1', '8')
    a = a.replace('7+2', '9')
    a = a.replace('7+3', '10')
    a = a.replace('7+4', '11')
    a = a.replace('7+5', '12')
    a = a.replace('7+6', '13')
    a = a.replace('7+7', '14')
    a = a.replace('7+8', '15')
    a = a.replace('7+9', '16')
    a = a.replace('8+1', '9')
    a = a.replace('8+2', '10')
    a = a.replace('8+3', '11')
    a = a.replace('8+4', '12')
    a = a.replace('8+5', '13')
    a = a.replace('8+6', '14')
    a = a.replace('8+7', '15')
    a = a.replace('8+8', '16')
    a = a.replace('8+9', '17')
    a = a.replace('9+1', '10')
    a = a.replace('9+2', '11')
    a = a.replace('9+3', '12')
    a = a.replace('9+4', '13')
    a = a.replace('9+5', '14')
    a = a.replace('9+6', '15')
    a = a.replace('9+7', '16')
    a = a.replace('9+8', '17')
    a = a.replace('9+9', '18')

    return a
def cacl(jsfuck,id):
    if id == 1:
        fuck1 = jsfuck.split('/')[0]
        fuck1 = fuck1[2:len(fuck1)-1]

        fuck2 = jsfuck.split('/')[1]
        fuck2 = fuck2[2:len(fuck2) - 1]

        fuck1list = re.findall('\((.*?)\)',fuck1,re.S)
        fuck2list = re.findall('\((.*?)\)', fuck2, re.S)
        f1str = ''
        f2str = ''

        for f1 in fuck1list:
            f1str+=test(f1).replace('+','')
        for f2 in fuck2list:
            f2str+=test(f2).replace('+','')
        return "%.18f" % (float(f1str)/float(f2str))
def jschl_answer(data,domain):
    text = data.replace('!![]','1').replace('!+[]','1')#.replace('+[]','0')
    temp = re.findall('\{\"(.*?)\"\:\+\(\(',text,re.S)[0]
    first = '+(('+re.findall('\+\(\((.*?)\}\;',text,re.S)[0]
    rows = re.findall('\.'+temp+"(.*?)\=" + '(.*?)\;',text,re.S)

    a = ''
    a+=cacl(first,1)
    rows = rows[0:len(rows)-1]
    for row in rows:
        if row[0] == '*' or row[0] == '/':
            a = '(' + a + ')'
        a += row[0]
        a +=cacl(row[1],1)
    return round(float("%.14f" % eval(a)),10) + len(domain)

def retry_if_result_False(result):
    return result is False

@retry(stop_max_attempt_number=2, wait_fixed=500, retry_on_result=retry_if_result_False)
def getToken(url):
    try:
        domain = url.replace('https://',"").replace("http://","").replace("/","")
        UA = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.%s.92 Safari/537.36' % str(random.randint(0001,9999))
        stime = time.time()
        headers = StringIO.StringIO()
        body = StringIO.StringIO()
        c = pycurl.Curl()
        c.setopt(pycurl.URL,url)
        c.setopt(pycurl.FOLLOWLOCATION, 1)
        c.setopt(pycurl.SSL_VERIFYPEER, 0)
        c.setopt(pycurl.SSL_VERIFYHOST, 0)
        c.setopt(pycurl.CONNECTTIMEOUT, 3)
        c.setopt(pycurl.MAXREDIRS, 3)
        c.setopt(pycurl.USERAGENT,UA)
        c.setopt(pycurl.HEADERFUNCTION, headers.write)
        c.setopt(pycurl.WRITEFUNCTION, body.write)
        c.perform()
        headers = headers.getvalue()
        body = body.getvalue()
        inputtext = re.findall('<input type="hidden" name="(.*?)" value="(.*?)"/>',body,re.S)
        text_cfduidtext = re.findall('__cfduid=(.*?);',headers,re.S)[0]
        text_pass = inputtext[1][1]
        text_jschl_vc = inputtext[0][1]
        text_jschl_answer = jschl_answer(body,domain)
        time.sleep(4)

        urlx = url + "/cdn-cgi/l/chk_jschl?jschl_vc=%s&pass=%s&jschl_answer=%s" % (text_jschl_vc,text_pass,text_jschl_answer)
        header = [ "Cookie: __cfduid=" + text_cfduidtext]
        headers = StringIO.StringIO()
        body = StringIO.StringIO()
        c = pycurl.Curl()
        c.setopt(pycurl.URL,urlx)
        c.setopt(pycurl.FOLLOWLOCATION, 1)
        c.setopt(pycurl.SSL_VERIFYPEER, 0)
        c.setopt(pycurl.SSL_VERIFYHOST, 0)
        c.setopt(pycurl.HEADER, True)  # Extend headrs
        c.setopt(pycurl.HTTPHEADER, header)
        c.setopt(pycurl.CONNECTTIMEOUT, 3)
        c.setopt(pycurl.FOLLOWLOCATION, False)  # Redirect
        c.setopt(pycurl.USERAGENT,UA)
        c.setopt(pycurl.HEADERFUNCTION, headers.write)
        c.setopt(pycurl.WRITEFUNCTION, body.write)
        c.perform()
        headers = headers.getvalue()
        text_cf_clearance = re.findall('cf_clearance=(.*?);',headers,re.S)[0]
        return {
            'UA':UA,
            'cfduid':text_cfduidtext,
            'cf_clearance':text_cf_clearance,
            'usedtime':time.time()-stime
        }
    except:
        return False

def get(url):
    try:
        return getToken(url)
    except:
        return False

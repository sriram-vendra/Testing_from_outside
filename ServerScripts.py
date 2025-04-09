import os,time,json,pyodbc,pandas as pd,requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
class C_autoScripts:
    def M_a_mail_with_attachment(value):
        print(value)
        fromaddr = "sptatvendra@gmail.com"
        toaddr = "support@vendra.co.in,sriramsp.90@gmail.com"
        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = value
        body = "Kindly find your attachment"+value
        msg.attach(MIMEText(body, 'plain'))
        filename = "D:\\tomcat\\apache-tomcat-9.0.55\\webapps\\files\\"+value
        attachment = open(filename, "rb")
        p = MIMEBase('application', 'octet-stream')
        p.set_payload((attachment).read())
        encoders.encode_base64(p)
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)
        text = msg.as_string()
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(fromaddr, "bwbylqnlzsprtnee")
        s.sendmail(fromaddr, toaddr.split(','), text)
        s.quit()
        return 'done'
        
    def M_a_Delete_and_insert(value):
        rec_date_l=datetime.datetime.now().date() if value.get('rec_date') is None else value['rec_date']
        cnxn = pyodbc.connect('DRIVER={SQL SERVER};PORT=1433;SERVER=172.17.1.2;DATABASE=Debit_UAT;UID=Vendra;PWD=Welcome@123')
        storedProc1 = "exec spm_Loyalty_Data_Compare_Insert @Mode = ?, @Bill_Date = ?"
        params1 = ('D',rec_date_l)
        storedProc2 = "exec spm_Loyalty_Data_Compare_Insert @Mode = ?, @Bill_Date = ?"
        params2 = ('T',rec_date_l)
        firstdata = {'orgdata' : {'coid' : 'NGM'}, 'sinvdate':rec_date_l,'reqtype':'ASLI'}
        firsturl = "http://103.146.234.44:8080/erpservice/erp/E01/13200582?tranid=DGTID&appstatus=approved& key1=K01& key2= K02& key3= K01&key4=K02&key5=K02"
        set = requests.post(url=firsturl, data=str(firstdata)).json()
        a=tuple((i.get('custid'),i['sinvno'],datetime.fromisoformat(i['sinvdate']).strftime('%Y/%m/%d %H:%M:%S %Z'),
         [i.get('popricingtotal').get('VAL2') if i.get('popricingtotal') is not None else 0][0],
         [i.get('popricingtotal').get('DISCOUNT') if i.get('popricingtotal') is not None else 0][0],
         'SB',i['unitid']) for i in set['resultset'])
        cursor = cnxn.cursor()
        cursor.execute('delete from CD_LyCa_Loyalty_Data_Client_T')
        cursor.execute(storedProc1, params1)
        cursor.executemany('insert into CD_LyCa_Loyalty_Data_Client_T values(?,?,?,?,?,?,?)',a)
        cursor.execute(storedProc2, params2)
        cursor.commit()
        cursor.close()
        return 'done'
        
    def M_a_cbms(value):
        #url = value['url']  
        url="https://cbapi.ird.gov.np/api/bill"
        #payload = json.dumps(value)
        payload = value
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        url='http://'+value['localip']+':8080/erpservice/erp/E01/13200582?tranid=DGTID&appstatus=approved& key1=K01&key2= K02& key3= K01&key4=K02&key5=K02'
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data={"cbmsstatus":response,"reqtype":"CBMS2"})
        if response.text=="200":
            return "SUCCESS"
        elif response.text=="104":
            return " model invalid"
        elif response.text=="102":
            return "exception while saving bill details , Please check model fields and values"
        elif response.text=="101":
            return "bill already exists"
        elif response.text=="100":
            return "API credential does not match"
        elif response.text=="103":
            return "Unknown exceptions, Please check API URL and model fields and value"
        else:
            return {"cbms_status":response.text}
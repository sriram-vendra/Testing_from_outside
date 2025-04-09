import requests,jinja2,datetime,json,string,random,math,openpyxl,io
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, attachment
from vendrareports import format,html2pdf
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from vendrareports import vlog
import num2words as nw





class C_vemail:

    def M_send_email(value):
        v=value.copy()
        value=eval(value['resultset_value'])
        if v['mail_send_type']!='SMTP':
            message = Mail(from_email=v['from'],to_emails=value['to'].split(','),subject=value['sub'],html_content=value['content'])
            message.cc=value['cc'].split(',') if value.get('cc') is not None else []
            #sg = SendGridAPIClient('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')
            #sg = SendGridAPIClient('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')
            response = sg.send(message)
            value['logger_type']='info'
            value['message']='SENDGRID mail sent successfully'
            return {"a": [str(response.status_code), response.body.decode(), str(response.headers)]}
        elif 0>1:
            sender = v['from']
            receiver = value['to']
            msg = MIMEText(value['content'])
            msg['Subject'] = value['sub']
            msg['From'] = sender
            msg['To'] = receiver
            msg['Cc']=value['cc'].split(',') if value.get('cc') is not None else ''
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls() # Secure the connection
                server.login(sender, 'bwbylqnlzsprtnee')
                server.sendmail(msg['From'],[i for i in msg['To'].split(',')]+[j for j in msg['Cc'].split(',')], msg.as_string())
                server.quit()
            v['logger_type']='info'
            v['message']='SMTP mail sent successfully'
            return('mail successfully sent')
        else:
            sender = v['from']
            receiver = value['to']
            cc = value.get('cc', '')
            subject = value['sub']
            content = value['content']  

            # Create the MIME message
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = sender
            msg['To'] = receiver
            msg['Cc'] = cc

            # Add the HTML content to the email
            msg.attach(MIMEText(content, 'html'))

            recipients = [receiver] + cc.split(',')
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()  # Secure the connection
                server.login(sender, 'bwbylqnlzsprtnee')
                print('Connected to the SMTP server')
                server.sendmail(sender, recipients, msg.as_string())
                print('Email sent successfully')
                server.quit()
                v['logger_type'] = 'info'
                v['message'] = 'SMTP mail sent successfully'
            return 'Mail successfully sent'
      
    def M_get_resultset(value):
        if value['type']=='save':
            value['reqtype']='EMAIL'
            a=value.copy()
            b="Http://"+value['localip']+":8080/erpservice/erp/E01/13200582?tranid=DGTID&appstatus=approved& key1=K01& key2= K02& key3= K01&key4=K02&key5=K02"
            c=requests.post(url=b, data=str(a)).json()
            value['resultset_value']=c
            return value

        elif value['type']=='template':
                value['printdate'] = datetime.datetime.now()
                #firstdata = {'orgdata': value['orgdata'], 'getrecord': 'true', 'key1': 'pino', 'xtrancode': 'SPIV','filter': {'xtrancode': 'SPIV', 'pino':value['pino']}}
                #firsturl = "Http://" + value['localip'] + ":8080/erpservice/erp/E01/13200582?tranid=DLI030&appstatus=approved& key1=K01& key2= K02& key3= K01&key4=K02&key5=K02"
                #data = requests.post(url=firsturl, data=str(firstdata)).json()
                #value['resultset_value'] = data
                value['resultset_value']=value
                return value

        else:
            firstdata={'orgdata' : value['orgdata'], 'getrecord' : 'true', 'key1' : 'id', 'xtrancode' : 'RGM1', 'filter': {'xtrancode':'RGM1', 'id' :value['gid']}}
            firsturl="Http://"+value['localip']+":8080/erpservice/erp/E01/13200582?tranid=DLI110&appstatus=approved& key1=K01& key2= K02& key3= K01&key4=K02&key5=K02"
            set = requests.post(url=firsturl, data=str(firstdata)).json()
            heading_data={'orgdata' : {'coid' : 'NGM'}, 'getrecord' : 'true', 'key1' : 'uqid', 'xtrancode' : 'GGRID01', 'filter': {'xtrancode':'GGRID01', 'uqid' : set['searchresults'][0]['getrecord']['ggid']}}
            heading_url="Http://"+value['localip']+":8080/erpservice/erp/E01/13200582?tranid=DLI110&appstatus=approved& key1=K01& key2= K02& key3= K01&key4=K02&key5=K02"
            heading = requests.post(url=heading_url, data=str(heading_data)).json()
            resultset_data = value
            resultset_url="Http://"+value['localip']+":8080/erpservice/erp/E01/13200582?tranid=DGTID&appstatus=approved& key1=K01& key2= K02& key3= K01&key4=K02&key5=K02"
            resultset = requests.post(url=resultset_url, data=str(resultset_data)).json()
            vv = []
            for i in resultset['resultset']:
                cc = {}
                for j in heading["searchresults"][0]["getrecord"][heading_data['filter']['uqid']]['order']:
                    cc[heading["searchresults"][0]["getrecord"][heading_data['filter']['uqid']]['header'][j]] = i.get(j)
                vv.append(cc)
            value['resultset_value']=[{"resultset":vv}]
            return value
          
        
    def M_table(value):
        if value['reqtype']!='EMAIL':
            value['numtoword']=nw
            #html=jinja2.Template(format.Templates.get_template([value['reqtype']])[0]).render(value=value)
            #env = jinja2.Environment(loader=jinja2.FileSystemLoader('./templates'))
            #html = env.get_template(value['reqtype']+'.txt').render(value=value)
            #value['html']=html
            value['py_template']=format.Templates.get_template([value['reqtype']])[0]
            print(value['reqtype'])
            print(value['py_template'])
            return value
        else:
            htmll = jinja2.Template(format.Templates.table("table and image", format.Templates.css("general_css"))).\
                render(jj=value['resultset_value'][0]['resultset'])
        return htmll
        
    def implement_jinja(value):
        line=[]
        temp=value
        jin=[]
        pageno=1    #raghu
        sno=1
        for i in value['lineitems']:
            i['rpsno']=sno
            line.append(i)
            sno+=1
            if len(line)==33:
                temp['pageno']=pageno     #raghu
                temp['lineitems']=line
                jin.append(jinja2.Template(value['py_template']).render(value=temp))
                line=[]
                pageno+=1       #raghu
        if len(line)>0:
            line[0]['eof']=True
            temp['pageno']=pageno     #raghu
            temp['lineitems']=line
            jin.append(jinja2.Template(value['py_template']).render(value=temp))
            line=[]
        i['eof']=True
        value['html']=jin
        return value
        

    def M_save(value):
        a=value
        b=jinja2.Template(str(a['resultset_value'])).render(value)
        value['resultset_value']=b
        return value
    
    def M_attachment(value):
         at = attachment.Attachment(file_content=x, file_name=value['file_name'], file_type=value["file_type"],disposition=value["disposition"])
         message.attachment = at

    def M_choose(value):
        #vlog.Log.logg(["debug('A debug message')", "info('An info message')", "warning('Something is not right.')","error('A Major error has happened.')", "critical('Fatal error. Cannot continue')"])
        if value['reqtype'] == 'EMAIL':
        #if value.get('gid')==None:
            value['type']='save'
            bb=C_vemail.M_send_email(C_vemail.M_save(C_vemail.M_get_resultset(value)))
            return bb
        elif value['reqtype'] != 'EMAIL':
            value['type']='template'
            a=C_vemail.M_get_resultset(value)
            b=C_vemail.M_table(a)
            #c=html2pdf.jsontoreport.page_process(b)
            d=C_vemail.implement_jinja(b)
            e=html2pdf.jsontoreport.pdf_process(d)
            return e
            
            
            #if value.get('rtnvalue')!='html':
             #   c=html2pdf.jsontoreport.pdf_process(b)
              #  return c
            #else:
             #   return b
      
    def M_chart(value):
        import matplotlib.pyplot as plt
        import requests
        import uuid
        url='http://'+value['localip']+':8080/erpservice/erp/E01/13200582?tranid=DGTID&appstatus=approved& key1=K01& key2= K02& key3= K01&key4=K02&key5=K02'
        data='{"reqtype":"DB01"}'
        set = requests.post(url=url, data=str(data)).json()

        x=[]
        y=[]
        z=[]
        for i in set['resultset']:
            if i.get('gid')==1:
                x.append(i.get('noofdays'))
                y.append(i.get('val'))
                z.append((i.get('cnt')))

        fig, ax1 = plt.subplots(1,2,figsize=(12,6))
        ax1[0].plot(x,y)
        ax1[0].set_ylabel('Amount')
        ax1[0].set_xlabel('No of Days')
        ax1[0].set_title('Day wise Sales volume')


        ax1[1].plot(x,z)
        ax1[1].set_ylabel('No of Sale order')
        ax1[1].set_xlabel('No of Days')
        ax1[1].set_title('Sale Order Count')
        
        
        uuid4 = uuid.uuid4()

        plt.savefig(value['file_path']+str(uuid4)+'.pdf')
        return str(uuid4)+'.pdf'
        

    def M_SOT3P(value):
        url = "https://fsclaravel.ngmhero.com/api/connect_login"
        payload = {'reg_no': 'PRADESH302003PA8711','contact_no': '9841538330'}
        headers = {}
        response = requests.request("POST", url, headers=headers, data=payload)
        #print(json.loads(response.text)['data']['token'])
        
        url = "https://fsclaravel.ngmhero.com/api/fetch_jobcards"
        payload = {'token-id':json.loads(response.text)['data']['token']}
        headers = {'Content-Type': 'application/json'}
        response = requests.request("POST", url, headers=headers, data=payload)
        #print(response.text)
        return response.text

        
        #url='http://'+value['localip']+':8080/erpservice/erp/E01/13200582?tranid=DGTID&appstatus=approved& key1=K01& #key2= K02& key3= K01&key4=K02&key5=K02'
        #data=value
        #data['reqtype']="GRA"
        #from_java = requests.post(url=url, data=str(data)).json()
        #return from_java
        
    def M_toexcel(value):
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 10))
        rownumber=1
        col=1
        workbook = openpyxl.Workbook()
        worksheet = workbook.active
        for i in value['name']:
            worksheet.cell(row=rownumber,column=col).value=i
            col+=1
        rownumber+=1
        col=1
        for i in value['values']:
            for j in i:
                worksheet.cell(row=rownumber,column=col).value=j
                col+=1
            rownumber+=1
            col=1
        output = io.BytesIO()
        workbook.save(output)
        output.seek(0)
        return {"file":output}
        #workbook.save("D:\\tomcat\\apache-tomcat-9.0.55\\webapps\\files\\"ran"+".xlsx")
        #return {"file":workbook,"name":ran+".xlsx"} #{"path":"D:\\tomcat\\apache-tomcat-9.0.55\\webapps\\files\\","file":"ran"+".xlsx"}
        
    def fill_Excel_template(value):    
        wb = openpyxl.load_workbook(value['conf_set']['D_Settings']['template']+"\\Excel_Template\\Invoice_06_apr_25.xlsx")
        template_ws = wb.active
        num_items = len(value["items"])
        max_item_per_page = 10
        num_pages = math.ceil(num_items / max_item_per_page)
        page_total = []
        for page in range(num_pages):
            ws = wb.copy_worksheet(template_ws)
            ws.title = f"Page {page + 1}"
            placeholders = {f"{{{{ {key} }}}}": value.get(key, " ") for key in value if key != "items"}
            item_keys = []
            for row in ws.iter_rows():
                for cell in row:
                    if cell.value == "<< page_total_ref >>":
                        page_total_row = cell.row
                        page_total_column = cell.column
                        cell.value = ""
                    if cell.value and isinstance(cell.value, str):
                        if cell.value.startswith("<<") and cell.value.endswith(">>"):
                            items_row_start = cell.row
                            key = cell.value.strip("<> ").strip()
                            item_keys.append(key)
                        else:
                            for key, val in placeholders.items():
                                if key in cell.value:
                                    cell.value = cell.value.replace(key, str(val))
            start_index = page * max_item_per_page
            end_index = start_index + max_item_per_page
            for index, item in enumerate(value["items"][start_index:end_index]):
                row_num = items_row_start + index
                for col_index, key in enumerate(item_keys, start=1):
                    ws.cell(row=row_num, column=col_index, value=item.get(key, "")).alignment = openpyxl.styles.Alignment(wrap_text=True)
            page_total_cell_ref = f"'{ws.title}'!{openpyxl.utils.get_column_letter(page_total_column+1)}{page_total_row}"
            page_total.append(page_total_cell_ref)
            if (page + 1) != 1:
                label1 = "Grand Total" if (page + 1) == num_pages else "Cumulative Total"
                grand_total_formula = f"=SUM({', '.join(page_total)})"
                ws.cell(row=page_total_row + 1, column=page_total_column - 1, value=label1).font = openpyxl.styles.Font(bold=True)
                ws.cell(row=page_total_row + 1, column=page_total_column + 1, value=grand_total_formula).border = openpyxl.styles.Border(bottom=openpyxl.styles.Side(style='thin'))
        wb.remove(template_ws)
        output = io.BytesIO()
        wb.save(output)
        output.seek(0)
        value["excel_report"]=output
        return value
from vendrareports import ServerScripts,validation,vmail,sri_gdrive,sri_Encrypt,html2pdf
import datetime,configparser
class C_check:
    def M_a_script(value):
        if value.get('reqtype')=='delete_suk':
            a=ServerScripts.C_autoScripts.M_a_Delete_and_insert(value)
        else:
            a=ServerScripts.C_autoScripts.M_a_mail_with_attachment(value)
        return a
    def M_validation(value):
        value['d2']=datetime.datetime.now().microsecond//1000
        a=validation.C_validation.M_payments(value)
        value['d5']=datetime.datetime.now().microsecond//1000
        return a
    def M_chart(value):
        ch=vmail.C_vemail.M_chart(value)
        return ch
        
    def M_cbms(value):
        #value['payload']['isrealtime']='False'
        c=ServerScripts.C_autoScripts.M_a_cbms(value)
        return c
        
    def C_SOT3P(value):
        s=vmail.C_vemail.M_SOT3P(value)
        return s

    def C_toexcel(value):
        e=vmail.C_vemail.M_toexcel(value)
        return e
    def C_setting(value):
        config = configparser.ConfigParser()
        config.read('C:\\inetpub\\wwwroot\\testing_iis\\settings\\settings.ini')
        value['conf_set']=config
        return value
    
    def C_gdrive(value):
        temp=value.copy()
        obj=sri_gdrive.gdrive()
        obj1=sri_Encrypt.Encryp()
        for i,j in temp.items():
            if i=='Fetch_files':
                value['file_name']=j['value'].split(',')
                a=obj.find_file(value)
                b=obj.read_file_content(a)
                e=obj1.fetch_key(b)
                f=obj1.decry_file(e)
                return f
            elif i=='Update_file':
                f=obj1.encry_file(j)
                g=obj1.save_key(f)
                h=obj.file_upload(f)
                print(type(h))
                return(g)
        #c=obj1.encry_file(b)
        #d=obj1.save_key(c)
        #e=obj1.fetch_key(b)
        #print(e)
        #f=obj1.decry_file(e)
    
    def excel_template(value):
        excel_file=vmail.C_vemail.fill_Excel_template(value)
        excel_file=html2pdf.jsontoreport.excel_process(excel_file)
        return excel_file
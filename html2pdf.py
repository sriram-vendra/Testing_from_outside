import json,jinja2,pdfkit,os,math
import time
from vendrareports import format as ss
class jsontoreport:
    def page_process(value):
        """global b
        b= []
        increased = {}
        td = {}
        tr = []
        rownumber = 0
        for i in inp['lineitems']:
            for j in i:
                td[j]=i[j]
                print(td)
                #td+='<td>'+str(i[j])+'</td>'
                if len(str(i[j]))>inp[j]:
                    if increased.get(j) is None:
                        increased[j] = math.ceil(len(str(i[j])) / inp[j])
                    elif increased.get(j)<math.ceil(len(str(i[j])) / inp[j]):
                        increased[j]=math.ceil(len(str(i[j])) / inp[j])
                else:
                    if increased.get(j) is None:
                        increased[j]=1
                    else:
                        if increased.get(j)<=1:
                            increased[j]=1

            #tr.append('<tr>'+td+'</tr>')
            tr.append(td)
            td={}
            print(td)
            #if increased[max(increased, key=lambda x: increased[x])] > rownumber:
            rownumber+=increased[max(increased, key=lambda x: increased[x])]

            #else:
             #   rownumber += 1
            #rownumber = increased[max(increased, key=lambda x: increased[x])] if increased[max(increased, key=lambda x: increased[x])]>rownumber else rownumber+=1
            if rownumber>=5:
                exit()
                for i in range(inp['total'] - rownumber):
                    tr.append("<tr><td>ggggg</td><td>&nbsp</td><td>&nbsp</td><td>&nbsp</td><td>&nbsp</td><td>&nbsp</td></tr>")

                aa=json.loads(ss.Templates.get_template("self",["Purchase_order"]))
                c=jinja2.Template(aa["Purchase_order"]).render(tr=tr)
                b.append(c)
                rownumber=0
                increased={}
                tr=[]
        if increased is not None:
            for k in range(inp['total']-rownumber):
                tr.append("<tr><td> &nbsp </td><td>&nbsp</td><td>&nbsp</td><td>&nbsp</td><td>&nbsp</td><td>&nbsp</td></tr>")
            aa = json.loads(ss.Templates.get_template("self", ["Purchase_order"]))
            c = jinja2.Template(aa["Purchase_order"]).render(tr=tr)
            b.append(c)
            rownumber = 0
            increased = {}
            return b"""
        total_page=math.ceil(len(value['lineitems'])/20)
        lst=[]
        val=[]
        z=0
        aa=value
        for j,i in enumerate(aa['lineitems']):
            lst.append(i)
            if len(lst)==20:
                #print([i['itemcode'] for i in lst])
                z+=1
                aa['lineitems']=lst
                val.append(aa)
                lst=[]
                #print(len(val))
        #if len(lst)>0: 
         #   aa['lineitems']=lst
          #  val.append(aa)
        return val
            

    def pdf_process(bb):
        if type(bb)==list:
            options = {'enable-local-file-access': True}
            config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
            filename = (time.thread_time_ns() + time.time_ns()) * int(max(list(str(time.time_ns()))))
            a=pdfkit.from_string(''.join(map(str,bb)), False, options=options,configuration=config)
            return {'file':a,'name':filename,'value':bb,'html':''.join(map(str,bb))}
        elif type(bb)==dict:
            options = {'enable-local-file-access': True, }
            config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
            filename = (time.thread_time_ns() + time.time_ns()) * int(max(list(str(time.time_ns()))))
            #for i in bb['html']:
             #   with open('C:\\inetpub\\wwwroot\\testing_iis\\files\\sss.txt','w',encoding='utf-8') as f:
              #      f.write(i)
            a=pdfkit.from_string(''.join(map(str,bb['html'])), False, options=options,configuration=config)
            return {'file':a,"name":filename,'value':bb,'html':''.join(map(str,bb['html']))}
            
        elif type(bb.get('html'))!=str:
            options = {'enable-local-file-access': True,}
            config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
            count=0
            folder=(time.thread_time_ns()+time.time_ns())*int(max(list(str(time.time_ns()))))
            path="c:\\"+str(folder)
            pdf_name='sriram.pdf'
            os.mkdir(path)
            for i in bb:
                
                i.replace("""\n""", '').replace("""\t""", '')
                with open(str(path)+"\\sri"+str(folder)+str(count)+".html",'w') as f:
                    f.write(i)
                    count+=1
            pdfkit.from_file(list(map(lambda a:str(path)+"\\"+a,os.listdir(str(path)+"\\"))),str(path)+"\\"+pdf_name,options=options,configuration=config)
            return path,pdf_name
            
    def excel_process(value):
        folder_path=value['conf_set']['D_Settings']['file_save_path']
        filename = (time.thread_time_ns() + time.time_ns()) * int(max(list(str(time.time_ns()))))
        with open(folder_path+'\\'+str(filename)+'.xlsx','wb') as f:
            f.write(value['excel_report'].getvalue())
        value['folder_path']=folder_path
        value['filename']=str(filename)+'.xlsx'
        return value
        
        
        




"""a={'a':'d',"lineitems": [
    {
      "qty": 100,
      "uom": "UNT",
      "rate": 100,
      "itemcode": "K86426AAND1918S",
      "myvalues": {
        "QTY": 100,
        "RATE": 100,
        "MM001": {
          "BSOBJ": "upload",
          "model": 245.4,
          "partno": "K86426AAND1918S",
          "porate": 639.78,
          "baseuom": "NOS",
          "mrprate": "Dead Stock",
          "mtlname": "KIT RIM TAPE GREEN- D1",
          "mtltype": "TG",
          "orgdata": {
            "roleid": "CNTRLSALES"
          },
          "domainid": 27150499,
          "filename": {
            "size": 758262,
            "filename": "parts number.xlsx"
          },
          "salerate": 722.95,
          "uploadcc": "{\"heading\":\"A1:Z1\",\"isheading\":false,\"orient\":\"records\"}",
          "xtrancode": "MM001",
          "loginempid": "R001"
        },
        "MTLPRICE": 10000,
        "VMGPRICE": 0,
        "NOOFCARTONS": 100
      },
      "itemcodeobj": {
        "key1": "K86426AAND1918S",
        "key2": "KIT RIM TAPE GREEN- D1",
        "myerpdata_iid": 178759
      },
      "Total runtime": "00:00:00.092409",
      "pricingmycalc": {
        "QTY": 100,
        "RATE": 100,
        "MM001": {
          "BSOBJ": "upload",
          "model": 245.4,
          "partno": "K86426AAND1918S",
          "porate": 639.78,
          "baseuom": "NOS",
          "mrprate": "Dead Stock",
          "mtlname": "KIT RIM TAPE GREEN- D1",
          "mtltype": "TG",
          "orgdata": {
            "roleid": "CNTRLSALES"
          },
          "domainid": 27150499,
          "filename": {
            "size": 758262,
            "filename": "parts number.xlsx"
          },
          "salerate": 722.95,
          "uploadcc": "{\"heading\":\"A1:Z1\",\"isheading\":false,\"orient\":\"records\"}",
          "xtrancode": "MM001",
          "loginempid": "R001"
        },
        "MTLPRICE": 10000,
        "VMGPRICE": 0,
        "NOOFCARTONS": 100
      }
    },
    {
      "qty": 200,
      "uom": "UNT",
      "rate": 100,
      "itemcode": "K50507AAWA000LS",
      "myvalues": {
        "QTY": 200,
        "RATE": 100,
        "MM001": {
          "BSOBJ": "upload",
          "model": 226.76,
          "partno": "K50507AAWA000LS",
          "porate": 591.19,
          "baseuom": "NOS",
          "mrprate": "Very Slow Moving",
          "mtlname": "PILLION L STEP",
          "mtltype": "TG",
          "orgdata": {
            "roleid": "CNTRLSALES"
          },
          "domainid": 27150499,
          "filename": {
            "size": 758262,
            "filename": "parts number.xlsx"
          },
          "salerate": 668.04,
          "uploadcc": "{\"heading\":\"A1:Z1\",\"isheading\":false,\"orient\":\"records\"}",
          "xtrancode": "MM001",
          "loginempid": "R001"
        },
        "MTLPRICE": 20000,
        "VMGPRICE": 0,
        "NOOFCARTONS": 100
      },
      "itemcodeobj": {
        "key1": "K50507AAWA000LS",
        "key2": "PILLION L STEP",
        "myerpdata_iid": 178739
      },
      "Total runtime": "00:00:00.169617",
      "pricingmycalc": {
        "QTY": 200,
        "RATE": 100,
        "MM001": {
          "BSOBJ": "upload",
          "model": 226.76,
          "partno": "K50507AAWA000LS",
          "porate": 591.19,
          "baseuom": "NOS",
          "mrprate": "Very Slow Moving",
          "mtlname": "PILLION L STEP",
          "mtltype": "TG",
          "orgdata": {
            "roleid": "CNTRLSALES"
          },
          "domainid": 27150499,
          "filename": {
            "size": 758262,
            "filename": "parts number.xlsx"
          },
          "salerate": 668.04,
          "uploadcc": "{\"heading\":\"A1:Z1\",\"isheading\":false,\"orient\":\"records\"}",
          "xtrancode": "MM001",
          "loginempid": "R001"
        },
        "MTLPRICE": 20000,
        "VMGPRICE": 0,
        "NOOFCARTONS": 100
      }
    }
  ],
  "unitidobj": {
    "key1": "23",
    "key2": "23"
  },
  "validfrom": "8-Mar-2023",
  "xtrancode": "SLO10",
  "loginempid": "R001",
  "sorderdata": [
    {
      "seqno": 5,
      "seqkey": {
        "storder": 5,
        "status": "Draft",
        "sdesc": "Draft"
      }
    },
    {
      "seqno": 20,
      "seqkey": {
        "storder": 20,
        "status": "Final",
        "sdesc": "Final"
      }
    },
    {
      "seqno": 30,
      "seqkey": {
        "storder": 30,
        "status": "Shortclosed",
        "sdesc": "Shortclosed"
      }
    },
    {
      "seqno": 30,
      "seqkey": {
        "storder": 30,
        "status": "Closed",
        "sdesc": "Closed"
      }
    },
    {
      "seqno": 30,
      "seqkey": {
        "storder": 30,
        "status": "Cancelled",
        "sdesc": "Cancelled"
      }
    },
    {
      "seqno": 22,
      "seqkey": {
        "storder": 22,
        "status": "PI",
        "sdesc": "Create Proforma Invoice"
      }
    },
    {
      "seqno": 24,
      "seqkey": {
        "storder": 24,
        "status": "PAYMENT",
        "sdesc": "Payment Done"
      }
    }
  ],
  "tmltdetail": [
    {
      "ruleid": "select * from mydata($1, jsonb_build_object('xtrancode', 'MM001', 'partno',  $3->'itemcode')),  jsonb_each(mydata) b  where jsonb_typeof(b.value) != 'array';",
      "ruleorder": 0,
      "condivalue": {
        "BSOBJ": "upload",
        "model": 226.76,
        "partno": "K50507AAWA000LS",
        "porate": 591.19,
        "baseuom": "NOS",
        "mrprate": "Very Slow Moving",
        "mtlname": "PILLION L STEP",
        "mtltype": "TG",
        "orgdata": {
          "roleid": "CNTRLSALES"
        },
        "domainid": 27150499,
        "filename": {
          "size": 758262,
          "filename": "parts number.xlsx"
        },
        "salerate": 668.04,
        "uploadcc": "{\"heading\":\"A1:Z1\",\"isheading\":false,\"orient\":\"records\"}",
        "xtrancode": "MM001",
        "loginempid": "R001"
      },
      "componentid": "MM001",
      "componentdesc": "MM001"
    },
    {
      "ruleid": "select b.value->'pervalue'  from myerp.rrdata($1, jsonb_build_object('filter', jsonb_build_object('xtrancode', 'MM001', 'partno', $3->'itemcode'))), jsonb_array_elements(rrdata->'erp_data'->'condidef2') b where b.value->>'condicode' = 'RATE' ;",
      "ruleorder": 0,
      "componentid": "D",
      "componentdesc": "DISCOUNT"
    },
    {
      "ruleid": "select to_jsonb(100 ::numeric) ;",
      "ruleorder": 0,
      "condivalue": 200,
      "componentid": "NOOFCARTONS",
      "componentdesc": "No. of Cartons"
    },
    {
      "ruleid": "select $3->'qty'",
      "ruleorder": 0,
      "condivalue": 300,
      "componentid": "QTY",
      "componentdesc": "Quantity"
    },
    {
      "ruleid": "select coalesce(getsomgprice($1, $3 || jsonb_build_object('sodate', $4->'sodate') || rrd($3,'ORGDATA')), to_jsonb(0 ::numeric)) ;",
      "ruleorder": 0,
      "condivalue": 0,
      "componentid": "VMGPRICE",
      "componentdesc": "Material Group Pricing"
    },
    {
      "ruleid": "select to_jsonb(100 ::numeric) ;",
      "ruleorder": 0,
      "condivalue": 200,
      "componentid": "RATE",
      "componentdesc": "Rate"
    },
    {
      "formula": "{QTY} * {RATE}",
      "ruleorder": 10,
      "condivalue": 30000,
      "componentid": "MTLPRICE",
      "componentdesc": "Material Price"
    }
  ],
  "itemtmltdet": [
    {
      "ruleid": "select * from mydata($1, jsonb_build_object('xtrancode', 'MM001', 'partno',  $3->'itemcode')),  jsonb_each(mydata) b  where jsonb_typeof(b.value) != 'array';",
      "ruleorder": 0,
      "condivalue": {
        "BSOBJ": "upload",
        "model": 226.76,
        "partno": "K50507AAWA000LS",
        "porate": 591.19,
        "baseuom": "NOS",
        "mrprate": "Very Slow Moving",
        "mtlname": "PILLION L STEP",
        "mtltype": "TG",
        "orgdata": {
          "roleid": "CNTRLSALES"
        },
        "domainid": 27150499,
        "filename": {
          "size": 758262,
          "filename": "parts number.xlsx"
        },
        "salerate": 668.04,
        "uploadcc": "{\"heading\":\"A1:Z1\",\"isheading\":false,\"orient\":\"records\"}",
        "xtrancode": "MM001",
        "loginempid": "R001"
      },
      "componentid": "MM001",
      "componentdesc": "MM001"
    },
    {
      "ruleid": "select b.value->'pervalue'  from myerp.rrdata($1, jsonb_build_object('filter', jsonb_build_object('xtrancode', 'MM001', 'partno', $3->'itemcode'))), jsonb_array_elements(rrdata->'erp_data'->'condidef2') b where b.value->>'condicode' = 'RATE' ;",
      "ruleorder": 0,
      "componentid": "D",
      "componentdesc": "DISCOUNT"
    },
    {
      "ruleid": "select to_jsonb(100 ::numeric) ;",
      "ruleorder": 0,
      "condivalue": 100,
      "componentid": "NOOFCARTONS",
      "componentdesc": "No. of Cartons"
    },
    {
      "ruleid": "select $3->'qty'",
      "ruleorder": 0,
      "condivalue": 200,
      "componentid": "QTY",
      "componentdesc": "Quantity"
    },
    {
      "ruleid": "select coalesce(getsomgprice($1, $3 || jsonb_build_object('sodate', $4->'sodate') || rrd($3,'ORGDATA')), to_jsonb(0 ::numeric)) ;",
      "ruleorder": 0,
      "condivalue": 0,
      "componentid": "VMGPRICE",
      "componentdesc": "Material Group Pricing"
    },
    {
      "ruleid": "select to_jsonb(100 ::numeric) ;",
      "ruleorder": 0,
      "condivalue": 100,
      "componentid": "RATE",
      "componentdesc": "Rate"
    },
    {
      "formula": "{QTY} * {RATE}",
      "ruleorder": 10,
      "condivalue": 20000,
      "componentid": "MTLPRICE",
      "componentdesc": "Material Price"
    }
  ],
  "popricingtotal": {
    "QTY": 300,
    "RATE": 200,
    "MTLPRICE": 30000,
    "VMGPRICE": 0,
    "NOOFCARTONS": 200
  },
  "saledeptid": None,
  "stid": None,
  "contractno": None,
  "docdt": "14-Mar-2023",
  "vendoridobj": None,
  "filter": {
    "xtrancode": "SLO10",
    "sono": "SO/22/0016"
  },
  "total":15
}

#js=jsontoreport()
#js.page_process(a)"""



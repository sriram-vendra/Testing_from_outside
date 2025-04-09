import json
class Templates:
    def get_template(temp_name):
        ret_value=[]
        Template={"Purchase_order":"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="C:/Users/srira/Downloads/pdf_template_20-092022-master/pdf_template_20-092022-master/template.css">
    <title>MyTemplate</title>
</head>
<body>
        <table class="fullbox" cellspacing="0">
            <!-- template1 -->
            <tr class="tr1">
                 <!-- template-1-A -->
                <td class="box1"  colspan="3">
                    <p class="s1 header1" >JB ENTERPRISES - SIPCOT UNIT</p>
                    <p class="s2 address2" >G63, SIPCOT INDUSTRIAL PARK, VALLAM VADAGAL - B, SRIPERUMBUDUR KANCHIPURAM 602105</p>
                    <p class="s2 address3">TAMIL NADU,INDIA</p>
                    <p class="s3 gst">GST: <span class="s2">33AAGFJ9208F1ZI</span></p>
                    <p class="gst"><a class="email" href="mailto:rjesh22ka@gmail.com"  target="_blank">Email ID: </a><a href="mailto:rjesh22ka@gmail.com" class="s4" target="_blank">rjesh22ka@gmail.com</a></p>
                </td>
                <!-- template-1-B -->
                <td class="podetails"  colspan="3">
                    <p class="smallbox12"><br/></p>
                    <p class="logobox">
                        <span>
                            <table border="0" cellspacing="0" cellpadding="0">
                                <tr>
                                    <td>
                                        <img id="logoimg" width="108" height="70" src="C:/Users/srira/Downloads/pdf_template_20-092022-master/pdf_template_20-092022-master/logo.jpg" alt="logo">
                                    </td>
                                </tr>
                            </table>
                        </span>
                    </p>
                    <p class="s5 left_header">PURCHASE ORDER</p>
                </td>
            </tr>
            <tr class="tr2">
                <!-- template-1-C -->
                <td class="box1"  colspan="3" rowspan="4">
                   <p class="s3 box4">To</p>
                   <p class="s3 box2">JIANGMEN HUA CHUANG TRADING CO. LTD</p>
                   <p class="s2 address1" >No. 32, HUA MAO BUILDING, SOUTH ZHIZHENG ROAD,XINHUI, JIANGMEN CITY, GUANGDONG PROVINCE, PRC</p>
                   <p class="smallbox12"><br/></p>
                   <p class="s2 box4">CHINA</p>
                   <p class="s3 box2">Email ID:</p>
                </td>
                  <!-- template-1-D 1-->
                <td class="podetails" colspan="3">
                    <p class="s3 box3" >PO Number:
                        <span class="s2">JB03/20/0368</span>
                    </p>
                </td>
            </tr>
             <!-- template-1-D 2-->
            <tr class="tr2">
                <td class="podetails" colspan="3">
                    <p class="s3 box3">Date:
                        <span class="s2">06-Aug-2020</span>
                    </p>
                </td>
            </tr>
             <!-- template-1-D 3-->
            <tr class="tr2">
                <td class="podetails" colspan="3">
                    <p class="s3 box3" >Your Proforma No:</p>
                </td>
            </tr>
             <!-- template-1-D 4-->
            <tr class="tr2">
                <td class="podetails" colspan="3">
                    <p class="s3 box3" >Dated:</p>
                </td>
            </tr>
            <!-- template2 -->
            <tr class="tr3">
                <td class="box5">
                    <p class="s6 smallbox1">S_NO</p>
                </td>
                <td class="box6">
                    <p class="s6 smallbox2">PARTICULARS</p>
                </td>
                <td class="box7">
                    <p class="s6 smallbox3">QTY</p>
                </td>
                <td class="box8">
                    <p class="s6 smallbox4">UOM</p>
                </td>
                <td class="box9">
                    <p class="s6 smallbox5">RATE(USD)</p>
                </td>
                <td class="box10">
                    <p class="s6 smallbox6">AMOUNT(USD)</p>
                </td>
            </tr>
            <!-- template3 -->
			{% for tem in tr %}
            <tbody>
                <tr class="tr4" >
                    <td class="bodybox5">
                        <div class="smallbox12 textlinecutter"> <p>{{tem["S_No"]}}</p>
                        </div>
                    </td>
                    <td class="bodybox6">
                        <div class="smallbox12  textlinecutter  textalign"> <p>{{tem["PARTICULARS"]}}</p>
                       </div>
                    </td>
                    <td class="bodybox7">
                        <div class="smallbox12 textlinecutter"><p>{{tem["QTY"]}}</p>
                        </div>
                    </td>
                    <td class="bodybox8">
                        <div class="smallbox12 textlinecutter"><p>{{tem["UOM"]}}</p>
                        </div>
                    </td>
                    <td class="bodybox9">
                        <div class="smallbox12 textlinecutter"><p>{{tem["RATE(USD)"]}}</p>
                        </div>
                    </td>
                    <td class="bodybox10">
                        <div class="smallbox12 textlinecutter"><p>{{tem["AMOUNT(USD)"]}}</p>
                        </div>
                    </td>
                </tr>


            </tbody>
			{% endfor %}
            <!--template4 -->
            <tr >
                <td class="smallbox13" colspan="4">
                    <p class="s3 box3">Amount (In words): <span class="s8">USD Twelve Thousand Seven Hundred And Ten Only</span>
                    </p>
                </td>
                <td class="box9">
                    <p class="s3 smallbox7"></p>
                </td>
                <td class="box10">
                    <p class="s3 smallbox11"></p>
                </td>
            </tr>
            <tr class="tr5">
                <td class="box11" colspan="6">
                    <p class="s3 box3">DELIVERY:</p>
                </td>
            </tr>
            <tr class="tr5">
                <td class="box11" colspan="6">
                    <p class="s3 box3">PAYMENT:
                        <span class="s9">30% DEPOSIT; 70% TO BE PAID OFF BEFORE DELIVERY FROM THE SELLER&#39;S FACTORY AFTER INSPECTION</span>
                    </p>
                </td>
            </tr>
            <tr class="tr5">
                <td class="box11" colspan="6">
                    <p class="s3 box3">Remarks:</p>
                </td>
            </tr>
            <!-- template5 -->
            <tr class="tr6">
                <td class="smallbox14"  colspan="2">
                    <p class="s3 box4" >We accept this Purchase Order</p>
                </td>
                <td  class="smallbox14" colspan="4">
                    <p class="s10 smallbox15">JB ENTERPRISES - SIPCOT UNIT</p>
                    <p class="smallbox12"><img id="signimg" width="88" height="55" src="./logo.jpg" alt="logo"></p>
                    <p class="s3 smallbox16" >AUTHORIZED SIGNATORY</p>
                </td>
            </tr>
        </table>
    </body>
</html>""",
    "monrecp":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            .table,th,tr,td{
                font-size: 11px;
                font-family: Calibri;
                text-align: left;
            }
            .preinv{
                font-size: 15px;
                font-family: calibri;
            }
            .tabl{
                border: 1px solid black;
                border-right: none;
                border-left: none;
            }
            .imag{
                width: 70px;
                height: 85px;
            }
            .theight{
                height: 500px;
            }
            .heading{
                font-size: 15px;
                line-height: 0px;
                text-align: left;
                margin-top: 0px;
                padding-top: 0px;
            }
            .num{
                text-align: left;
            }
            .snum{
                text-align: center;
            }
            .rnum{
                text-align: right;
            }
            .tleft{
                text-align: left;
                float: left;
            }
            .tright{
                text-align: right;
                float: right;
            }
            .ltop{
                text-decoration: overline;
            }
            .foot{
                border-top: 1px solid black;
                font-size: 11px;
                text-align: right;
            }
            .boxx{
                border: 1px solid black;
            }
        </style>
    </head>
    <body>
        <div class="preinv">
            <table style="width: 100%;">
                <tbody>
                    <tr>
                        <td class="heading">
                            <h2>{{value['resultset_value']['CO010']['coname']}}</h2>
                            <p>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</p>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <h2 class="snum">Money Receipt</h2>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </body>
</html>"""
}
        for i in temp_name:
            ret_value.append(Template[i])
        return ret_value
        
        
    def css(css_name):
        a={"general_css":"""
            #datagrid {
              font-family: Arial, Helvetica, calibri;
              border-collapse: collapse;
              width: 100%;
            }

            #datagrid td, #datagrid th {
              border: 1px solid #ddd;
              padding: 8px;
            }

            .number {
                text-align: right;
            }

            .bold {
              font-weight: bold;
            }

            .index {
                text-align: center;
            }

            #datagrid tr:nth-child(even){background-color: #f2f2f2;}

            #datagrid th {
              padding-top: 12px;
              padding-bottom: 12px;
              text-align: left;
              background-color: #5759d8;
              color: white;
            }"""}
        return a.get(css_name)
        
        
    def table(table_name,css):
        b={"table and image":"""<html><title> Email </title> <style>"""
                        +css +"""</style><body>
                        <img src='data:image/png;base64, {{aa}} 'alt="" width="500" height="600">
                        <table id='datagrid'>
                {% for i in jj[0] %}
                <th>{{i}}</th>
                {% endfor %}
                {% for i in jj %}
                <tr>{% for j in i.values() %}<td {% if j|int %} class='number' {% endif %}>{{j}}</td>{% endfor %}</tr>
                {% endfor %}
                </table></body></html>
                """}
        return b.get(table_name)
    
    



    
    def template_settings(value):
        a={"quotation7":{"Category":'N',"T":['head1.txt','body1.txt','footer1.txt'],'path':'./templates/quotation7'}}
        return a[value['reqtype']]
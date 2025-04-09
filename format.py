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
    "allinv":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,tr,th,td{
                font-size: 11px;
                font-family: calibri;
                text-align: left;
            }
            .preinv{
                font-size: 11px;
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
            div.table_items {
                height: 200px !important;
                border: 1px solid #ccc;
            }
            .theight{
                height: 275px;
            }
            .heading{
                font-size: 15px;
                line-height: 0px;
                text-align: left;
                margin-top: 0%;
                padding-top: 0%;
            }
            .collapse_table{
                border-collapse: collapse;
                width: 100%;
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
            .desc{
                padding-right: 150px;
            }
            .prin{
                page-break-before: always;
            }
        </style>
    </head>
    <body>
    {% if value['resultset_value']['prncnt'] == 0 %}
        <div class="preinv">
            <table style="width: 100%; border-bottom: 1px solid black;">
                <tbody>
                    <tr>
                        <td>
                            <img class="imag" src="http://103.146.234.44:8080/img/NGMlogo1.jpg">
                        </td>
                        <td class="heading">
                                <h2 class="snum">Tax Invoice</h2>
                            <h2>{{value['resultset_value']['CO010']['coname']}}</h2>
                            <p><span style="margin-left: 3mm;"></span>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</p>
                            <p>VAT No. :<span style="margin-left: 3mm;"></span><b>{{value['resultset_value']['CO010']['covatno']}}</b></p>
                            <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OU010']['unitname']}}</b></p> 
                        </td>
                        <td class="tright">
                            <br><br><br>
                            {% if value['resultset_value']['invtype'] == 'CA' %}
                                <p>Mode of Payment: <b>Cash Bill</b></p>
                            {% elif value['resultset_value']['invtype'] == 'CR' %}
                                <p>Mode of Payment: <b>CREDIT</b></p>
                            {% else %}
                                <p>Mode of Payment: <b>CREDIT</b></p>
                            {% endif %}
                            {% if 'OD10' in value['resultset_value'] %}
                                <p>Phone No:{{value['resultset_value']['OD10']['phoneno']}}</p>
                            {% else %}
                                <p>Phone No:{{value['resultset_value']['CO010']['phoneno']}}</p>
                            {% endif %}
                        </td>
                    </tr>
                </tbody>
            </table>
            <table class="tleft">
                <tbody>
                    {% if value['resultset_value']['invtype'] =='R' %}
                        <tr>
                        <td>Buyer's Name</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['CM010']['custname']}}</td>
                    </tr>
                    <tr>
                        <td>Address</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['CM010']['address'][0]['adrs1']}}</td>
                    </tr>
                    <tr>
                        <td>Phone No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['CM010']['phone']}}</td>
                    </tr>
                    <tr>
                        <td>Buyer's VAT No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['CM010']['pan']}}</td>
                    </tr>
                {% else %}
                    <tr>
                        <td>Buyer's Name</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custname']}}</td>
                    </tr>
                    <tr>
                        <td>Address</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custaddress']}}</td>
                    </tr>
                    <tr>
                        <td>Phone No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['phoneno']}}</td>
                    </tr>
                    <tr>
                        <td>Buyer's VAT No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['vatno']}}</td>  
                    </tr>
                {% endif %}
                </tbody>
            </table>
            <table class="tright">
                <tbody>
                    <tr>
                        <td>Invoice No.</td>
                        <td>:</td>
                        <td><b>{{value['resultset_value']['sinvno']}}</b></td>
                    </tr>
                    <tr>
                        <td>Invoice Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['sinvdate']}}</td>
                    </tr>
                    <tr>
                        <td>BS Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['sinvbs']}}</td>
                    </tr>
                    <tr>
                        <td>Transaction Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docdt']}}</td>  
                    </tr>
                    <tr>
                        <td>Print Date & Time</td>
                        <td>:</td>
                        <td>{{ value['printdate'].strftime('%d/%m/%Y') }} {{ value['printdate'].strftime('%H:%M:%S') }}</td>
                    </tr>
                </tbody>
            </table>
             <div class="theight">
                <table class="collapse_table">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th class="num">H.S.Code</th>
                        <th>Code</th>
                        <th class="desc">Description</th>
                        <th class="rnum">Qty</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                    {% set nctr = -1 %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                        {% set nctr = nctr+1 %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                {% if 'MM001' in value['resultset_value']['lineitems'][nctr]['myvalues'] %}
                                    <td class="num">{{i['myvalues']['MM001']['hsncode']}}</td>
                                {% else %}
                                    <td></td>
                                {% endif %}
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                    </tbody>
                </table>
            </div>
            <table class="tright" style="border-collapse: collapse;">
                <tbody>
                    <tr>
                        <td class="rnum"><b>Total</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['MTLPRICE']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Discount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        {% if value['resultset_value']['discount'][0] is defined %}
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['discount'][0]['discrate'])}}%</td>
                        {% else %}
                        <td></td>
                        {% endif %}
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Taxable Amount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['VAL1']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Add:VAT</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VATPER'])}}%</td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VAT'])}}</td> 
                    </tr>
                    <tr>
                        <td class="rnum"><b>Net Amount</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;">{{value['resultset_value']['popricingtotal']['VAL2']}}</td>
                    </tr>
                </tbody>
            </table>
            <div>
                <table class="tleft">
                <tbody>
                <tr>
                    <td class="num">Amount in Words:</td>                        <td>{{value['numtoword'].num2words(value['resultset_value']['popricingtotal']['VAL2']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</td>
                    </tr>
                    <tr>
                    <td class="num">Remarks:</td>
                    <td>{{value['resultset_value']['remarks']}}</td>
                    </tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr><td class="num">{{(value['resultset_value']['USR01']['username'])}}</td></tr>
                    <tr>
                        <td class="ltop num">Prepared By</td>
                        <td></td>
                        <td class="ltop snum">Receiver's Signature</td>
                    </tr>
                </tbody>
            </table>
            </div>
                <div>
                <br><br><br><br><br><br><br>
                <p class="tright"><b>For  {{value['resultset_value']['CO010']['coname']}}</b></p>
                <p class="tleft">E & OE<br>Goods once sold are not exchangeable or returnable</p>
            </div> 
        </div>
        <div class="preinv prin">
            <table style="width: 100%; border-bottom: 1px solid black;">
                <tbody>
                    <tr>
                        <td>
                            <img class="imag" src="http://103.146.234.44:8080/img/NGMlogo1.jpg">
                        </td>
                        <td class="heading">
                            <h2 class="snum">Invoice</h2>
                            <h2>{{value['resultset_value']['CO010']['coname']}}</h2>
                            <p><span style="margin-left: 3mm;"></span>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</p>
                            <p>VAT No. :<span style="margin-left: 3mm;"></span><b>{{value['resultset_value']['CO010']['covatno']}}</b></p>
                            <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OU010']['unitname']}}</b></p> 
                        </td>
                        <td class="tright">
                            <br><br><br>
                            {% if value['resultset_value']['invtype'] == 'CA' %}
                                <p>Mode of Payment: <b>Cash Bill</b></p>
                            {% elif value['resultset_value']['invtype'] == 'CR' %}
                                <p>Mode of Payment: <b>CREDIT</b></p>
                            {% else %}
                                <p>Mode of Payment: <b>CREDIT</b></p>
                            {% endif %}
                            {% if 'OD10' in value['resultset_value'] %}
                                <p>Phone No:{{value['resultset_value']['OD10']['phoneno']}}</p>
                            {% else %}
                                <p>Phone No:{{value['resultset_value']['CO010']['phoneno']}}</p>
                            {% endif %}
                        </td>
                    </tr>
                </tbody>
            </table>
            <table class="tleft">
                <tbody>
                    {% if value['resultset_value']['invtype'] =='R' %}
                        <tr>
                        <td>Buyer's Name</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['CM010']['custname']}}</td>
                    </tr>
                    <tr>
                        <td>Address</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['CM010']['address'][0]['adrs1']}}</td>
                    </tr>
                    <tr>
                        <td>Phone No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['CM010']['phone']}}</td>
                    </tr>
                    <tr>
                        <td>Buyer's VAT No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['CM010']['pan']}}</td>
                    </tr>
                {% else %}
                    <tr>
                        <td>Buyer's Name</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custname']}}</td>
                    </tr>
                    <tr>
                        <td>Address</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custaddress']}}</td>
                    </tr>
                    <tr>
                        <td>Phone No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['phoneno']}}</td>
                    </tr>
                    <tr>
                        <td>Buyer's VAT No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['vatno']}}</td>  
                    </tr>
                {% endif %}
                </tbody>
            </table>
            <table class="tright">
                <tbody>
                    <tr>
                        <td>Invoice No.</td>
                        <td>:</td>
                        <td><b>{{value['resultset_value']['sinvno']}}</b></td>
                    </tr>
                    <tr>
                        <td>Invoice Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['sinvdate']}}</td>
                    </tr>
                    <tr>
                        <td>BS Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['sinvbs']}}</td>
                    </tr>
                    <tr>
                        <td>Transaction Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docdt']}}</td>  
                    </tr>
                    <tr>
                        <td>Print Date & Time</td>
                        <td>:</td>
                        <td>{{ value['printdate'].strftime('%d/%m/%Y') }} {{ value['printdate'].strftime('%H:%M:%S') }}</td>
                    </tr>
                </tbody>
            </table>
             <div class="theight">
                <table class="collapse_table">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th class="num">H.S.Code</th>
                        <th>Code</th>
                        <th class="desc">Description</th>
                        <th class="rnum">Qty</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                    {% set nctr = -1 %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                        {% set nctr = nctr+1 %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                {% if 'MM001' in value['resultset_value']['lineitems'][nctr]['myvalues'] %}
                                    <td class="num">{{i['myvalues']['MM001']['hsncode']}}</td>
                                {% else %}
                                    <td></td>
                                {% endif %}
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                    </tbody>
                </table>
            </div>
            <table class="tright" style="border-collapse: collapse;">
                <tbody>
                    <tr>
                        <td class="rnum"><b>Total</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['MTLPRICE']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Discount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        {% if value['resultset_value']['discount'][0] is defined %}
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['discount'][0]['discrate'])}}%</td>
                        {% else %}
                        <td></td>
                        {% endif %}
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Taxable Amount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['VAL1']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Add:VAT</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VATPER'])}}%</td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VAT'])}}</td> 
                    </tr>
                    <tr>
                        <td class="rnum"><b>Net Amount</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;">{{value['resultset_value']['popricingtotal']['VAL2']}}</td>
                    </tr>
                </tbody>
            </table>
           <div>
                <table class="tleft">
                <tbody>
                <tr>
                    <td class="num">Amount in Words:</td>                        <td>{{value['numtoword'].num2words(value['resultset_value']['popricingtotal']['VAL2']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</td>
                    </tr>
                    <tr>
                    <td class="num">Remarks:</td>
                    <td>{{value['resultset_value']['remarks']}}</td>
                    </tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr><td class="num">{{(value['resultset_value']['USR01']['username'])}}</td></tr>
                    <tr>
                        <td class="ltop num">Prepared By</td>
                        <td></td>
                        <td class="ltop snum">Receiver's Signature</td>
                    </tr>
                </tbody>
            </table>
            </div>
                <div>
                <br><br><br><br><br><br><br>
                <p class="tright"><b>For  {{value['resultset_value']['CO010']['coname']}}</b></p>
                <p class="tleft">E & OE<br>Goods once sold are not exchangeable or returnable</p>
            </div> 
        </div>
        {% else %}
            <div class="preinv">
            <table style="width: 100%; border-bottom: 1px solid black;">
                <tbody>
                    <tr>
                        <td>
                            <img class="imag" src="http://103.146.234.44:8080/img/NGMlogo1.jpg">
                        </td>
                        <td class="heading">
                            {% if value['resultset_value']['status'] != 'C' %}
                                <h2 class="snum">Invoice - DRAFT</h2>
                            {% elif 'prncnt' in value['resultset_value'] %}
                                {% if value['resultset_value']['prncnt'] <= 0 %}
                                     <h2 class="snum">Tax Invoice</h2>
                                {% else %}
                                    <h2 class="snum">Invoice (COPY OF ORIGINAL :  {{value['resultset_value']['prncnt']}} )</h2>
                                {% endif %}
                            {% endif %}
                            <h2>{{value['resultset_value']['CO010']['coname']}}</h2>
                            <p><span style="margin-left: 3mm;"></span>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</p>
                            <p>VAT No. :<span style="margin-left: 3mm;"></span><b>{{value['resultset_value']['CO010']['covatno']}}</b></p>
                            <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OU010']['unitname']}}</b></p> 
                        </td>
                        <td class="tright">
                            <br><br><br>
                            {% if value['resultset_value']['invtype'] == 'CA' %}
                                <p>Mode of Payment: <b>Cash Bill</b></p>
                            {% else %}
                                <p>Mode of Payment: <b>CREDIT</b></p>
                            {% endif %}
                            {% if 'OD10' in value['resultset_value'] %}
                                <p>Phone No:{{value['resultset_value']['OD10']['phoneno']}}</p>
                            {% else %}
                                <p>Phone No:{{value['resultset_value']['CO010']['phoneno']}}</p>
                            {% endif %}
                        </td>
                    </tr>
                </tbody>
            </table>
            <table class="tleft">
                <tbody>
                    {% if value['resultset_value']['invtype'] =='R' %}
                        <tr>
                        <td>Buyer's Name</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['CM010']['custname']}}</td>
                    </tr>
                    <tr>
                        <td>Address</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['CM010']['address'][0]['adrs1']}}</td>
                    </tr>
                    <tr>
                        <td>Phone No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['CM010']['phone']}}</td>
                    </tr>
                    <tr>
                        <td>Buyer's VAT No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['CM010']['pan']}}</td>
                    </tr>
                {% else %}
                    <tr>
                        <td>Buyer's Name</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custname']}}</td>
                    </tr>
                    <tr>
                        <td>Address</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custaddress']}}</td>
                    </tr>
                    <tr>
                        <td>Phone No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['phoneno']}}</td>
                    </tr>
                    <tr>
                        <td>Buyer's VAT No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['vatno']}}</td>  
                    </tr>
                {% endif %}
                </tbody>
            </table>
            <table class="tright">
                <tbody>
                    <tr>
                        <td>Invoice No.</td>
                        <td>:</td>
                        <td><b>{{value['resultset_value']['sinvno']}}</b></td>
                    </tr>
                    <tr>
                        <td>Invoice Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['sinvdate']}}</td>
                    </tr>
                    <tr>
                        <td>BS Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['sinvbs']}}</td>
                    </tr>
                    <tr>
                        <td>Transaction Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docdt']}}</td>  
                    </tr>
                    <tr>
                        <td>Print Date & Time</td>
                        <td>:</td>
                        <td>{{ value['printdate'].strftime('%d/%m/%Y') }} {{ value['printdate'].strftime('%H:%M:%S') }}</td>
                    </tr>
                </tbody>
            </table>
             <div class="theight">
                <table class="collapse_table">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th class="num">H.S.Code</th>
                        <th>Code</th>
                        <th class="desc">Description</th>
                        <th class="rnum">Qty</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                    {% set nctr = -1 %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                        {% set nctr = nctr+1 %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                {% if 'MM001' in value['resultset_value']['lineitems'][nctr]['myvalues'] %}
                                    <td class="num">{{i['myvalues']['MM001']['hsncode']}}</td>
                                {% else %}
                                    <td></td>
                                {% endif %}
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                    </tbody>
                </table>
            </div>
            <table class="tright" style="border-collapse: collapse;">
                <tbody>
                    <tr>
                        <td class="rnum"><b>Total</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['MTLPRICE']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Discount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        {% if value['resultset_value']['discount'][0] is defined %}
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['discount'][0]['discrate'])}}%</td>
                        {% else %}
                        <td></td>
                        {% endif %}
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Taxable Amount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['VAL1']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Add:VAT</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VATPER'])}}%</td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VAT'])}}</td> 
                    </tr>
                    <tr>
                        <td class="rnum"><b>Net Amount</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;">{{value['resultset_value']['popricingtotal']['VAL2']}}</td>
                    </tr>
                </tbody>
            </table>
           <div>
                <table class="tleft">
                <tbody>
                <tr>
                    <td class="num">Amount in Words:</td>                        <td>{{value['numtoword'].num2words(value['resultset_value']['popricingtotal']['VAL2']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</td>
                    </tr>
                    <tr>
                    <td class="num">Remarks:</td>
                    <td>{{value['resultset_value']['remarks']}}</td>
                    </tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr><td class="snum">{{(value['resultset_value']['USR01']['username'])}}</td></tr>
                    <tr>
                        <td class="ltop num">Prepared By</td>
                        <td></td>
                        <td class="ltop snum">Receiver's Signature</td>
                    </tr>
                </tbody>
            </table>
            </div>
                <div>
                <br><br><br><br><br><br><br>
                <p class="tright"><b>For  {{value['resultset_value']['CO010']['coname']}}</b></p>
                <p class="tleft">E & OE<br>Goods once sold are not exchangeable or returnable</p>
            </div> 
        </div>
        {% endif %}
    </body>
</html>""",
    "agent":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,tr,th,td{
                font-size: 11px;
                font-family: calibri;
                text-align: left;
            }
            .preinv{
                font-size: 11px;
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
            div.table_items {
                height: 200px !important;
                border: 1px solid #ccc;
            }
            .theight{
                height: 275px;
            }
            .heading{
                font-size: 15px;
                line-height: 0px;
                text-align: left;
                margin-top: 0%;
                padding-top: 0%;
            }
            .collapse_table{
                border-collapse: collapse;
                width: 100%;
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
            .desc{
                padding-right: 150px;
            }
            .prin{
                page-break-before: always;
            }
        </style>
    </head>
    <body>
    {% if value['resultset_value']['prncnt'] == 0 %}
        <div class="preinv">
            <table style="width: 100%; border-bottom: 1px solid black;">
                <tbody>
                    <tr>
                        <td>
                            <img class="imag" src="http://103.146.234.44:8080/img/NGMlogo1.jpg">
                        </td>
                        <td class="heading">
                            <h2 class="snum">Tax Invoice</h2>               
                            <h2>{{value['resultset_value']['CO010']['coname']}}</h2>
                            {% if 'OD10' in value['resultset_value'] %}
                            <p><span style="margin-left: 3mm;"></span>{{value['resultset_value']['OD10']['address'][0]['postbox']}}</p>
                            {% else %}
                            <p><span style="margin-left: 3mm;"></span>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</p>
                            {% endif %}
                            <p>VAT No. :<span style="margin-left: 3mm;"></span><b>{{value['resultset_value']['CO010']['covatno']}}</b></p>
                            {% if 'OD10' in value['resultset_value'] %}
                            <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OD10']['unitidobj']['key2']}}</b></p> 
                            {% else %}
                            <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OU010']['unitname']}}</b></p> 
                            {% endif %}
                        </td>
                        <td class="tright">
                            <br><br><br>
                            <p>Mode of Payment: {{value['resultset_value']['dzpm']}}</p>
                            {% if 'OD10' in value['resultset_value'] %}
                                <p>Phone No:{{value['resultset_value']['OD10']['phoneno']}}</p>
                            {% else %}
                                <p>Phone No:{{value['resultset_value']['CO010']['phoneno']}}</p>
                            {% endif %}
                        </td>
                    </tr>
                </tbody>
            </table>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td>Buyer's Name</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custname']}}</td>
                    </tr>
                    <tr>
                        <td>Address</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custaddress']}}</td>
                    </tr>
                    <tr>
                        <td>Phone No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['phoneno']}}</td>
                    </tr>
                    <tr>
                        <td>Buyer's VAT No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['vatno']}}</td>  
                    </tr>
                </tbody>
            </table>
            <table class="tright">
                <tbody>
                    <tr>
                        <td>Invoice No.</td>
                        <td>:</td>
                        <td><b>{{value['resultset_value']['sinvno']}}</b></td>
                    </tr>
                    <tr>
                        <td>Invoice Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['sinvdate']}}</td>
                    </tr>
                    <tr>
                        <td>BS Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['sinvbs']}}</td>
                    </tr>
                    <tr>
                        <td>Transaction Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docdt']}}</td>  
                    </tr>
                    <tr>
                        <td>Print Date & Time</td>
                        <td>:</td>
                        <td>{{ value['printdate'].strftime('%d/%m/%Y') }} {{ value['printdate'].strftime('%H:%M:%S') }}</td>
                    </tr>
                </tbody>
            </table>
            <div class="theight">
                <table class="collapse_table">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th>H.S.Code</th>
                        <th>Code</th>
                        <th class="desc">Description</th>
                        <th class="rnum">Qty</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                    {% set nctr = -1 %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                        {% set nctr = nctr+1 %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                {% if 'MM001' in value['resultset_value']['lineitems'][nctr]['myvalues'] %}
                                    <td class="num">{{i['myvalues']['MM001']['hsncode']}}</td>
                                {% else %}
                                    <td></td>
                                {% endif %}
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                    </tbody>
                </table>
            </div>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td class="num">Amount in Words:</td>
                        <td colspan="3">{{value['numtoword'].num2words(value['resultset_value']['popricingtotal']['VAL2']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</td> 
                    </tr>
                    <tr><td><br></td></tr>
                    <tr>
                        <td>Inv.:{{value['resultset_value']['dzinvno']}}</td>
                        <td>Tracking ID:{{value['resultset_value']['dztrkid']}}<span style="margin-left: 3mm;"></td>
                        <td>Payment Method:{{value['resultset_value']['dzpm']}}<span style="margin-left: 3mm;"></td>
                        <td>Scheme(if any):{{value['resultset_value']['dzscheme']}}</td>
                    </tr>
                    <tr>
                        <td style="text-align: center;">{{(value['resultset_value']['USR01']['username'])}}</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td class="ltop" style="text-align: center;">Prepared By</td>
                        <td class="ltop" style="text-align: right; float:right;">Receiver's Signature</td>
                    </tr>
                </tbody>
            </table>
            <table class="tright" style="border-collapse: collapse;">
                <tbody>
                    <tr>
                        <td class="rnum"><b>Total</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['MTLPRICE']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Discount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        {% if value['resultset_value']['discount'][0] is defined %}
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['discount'][0]['discamt'])}}%</td>
                        {% else %}
                        <td></td>
                        {% endif %}
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Taxable Amount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['VAL1']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Add:VAT</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VATPER'])}}%</td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{value['resultset_value']['popricingtotal']['VAT']}}</td> 
                    </tr>
                    <tr>
                        <td class="rnum"><b>Net Amount</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;">{{value['resultset_value']['popricingtotal']['VAL2']}}</td>
                    </tr>
                </tbody>
            </table>
            <div>
                <br><br><br><br><br><br><br>
                <p class="tright"><b>For  {{value['resultset_value']['CO010']['coname']}}</b></p>
                <p class="tleft">E & OE<br>Goods once sold are not exchangeable or returnable</p>
            </div> 
        </div>
        <div class="preinv prin">
            <table style="width: 100%; border-bottom: 1px solid black;">
                <tbody>
                    <tr>
                        <td>
                            <img class="imag" src="http://103.146.234.44:8080/img/NGMlogo1.jpg">
                        </td>
                        <td class="heading">
                            <h2 class="snum">Invoice</h2>
                            <h2>{{value['resultset_value']['CO010']['coname']}}</h2>
                            {% if 'OD10' in value['resultset_value'] %}
                            <p><span style="margin-left: 3mm;"></span>{{value['resultset_value']['OD10']['address'][0]['postbox']}}</p>
                            {% else %}
                            <p><span style="margin-left: 3mm;"></span>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</p>
                            {% endif %}
                            <p>VAT No. :<span style="margin-left: 3mm;"></span><b>{{value['resultset_value']['CO010']['covatno']}}</b></p>
                            {% if 'OD10' in value['resultset_value'] %}
                            <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OD10']['unitidobj']['key2']}}</b></p> 
                            {% else %}
                            <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OU010']['unitname']}}</b></p> 
                            {% endif %}
                        </td>
                        <td class="tright">
                            <br><br><br>
                            <p>Mode of Payment: {{value['resultset_value']['dzpm']}}</p>
                            {% if 'OD10' in value['resultset_value'] %}
                                <p>Phone No:{{value['resultset_value']['OD10']['phoneno']}}</p>
                            {% else %}
                                <p>Phone No:{{value['resultset_value']['CO010']['phoneno']}}</p>
                            {% endif %}
                        </td>
                    </tr>
                </tbody>
            </table>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td>Buyer's Name</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custname']}}</td>
                    </tr>
                    <tr>
                        <td>Address</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custaddress']}}</td>
                    </tr>
                    <tr>
                        <td>Phone No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['phoneno']}}</td>
                    </tr>
                    <tr>
                        <td>Buyer's VAT No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['vatno']}}</td>  
                    </tr>
                </tbody>
            </table>
            <table class="tright">
                <tbody>
                    <tr>
                        <td>Invoice No.</td>
                        <td>:</td>
                        <td><b>{{value['resultset_value']['sinvno']}}</b></td>
                    </tr>
                    <tr>
                        <td>Invoice Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['sinvdate']}}</td>
                    </tr>
                    <tr>
                        <td>BS Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['sinvbs']}}</td>
                    </tr>
                    <tr>
                        <td>Transaction Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docdt']}}</td>  
                    </tr>
                    <tr>
                        <td>Print Date & Time</td>
                        <td>:</td>
                        <td>{{ value['printdate'].strftime('%d/%m/%Y') }} {{ value['printdate'].strftime('%H:%M:%S') }}</td>
                    </tr>
                </tbody>
            </table>
            <div class="theight">
                <table class="collapse_table">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th>H.S.Code</th>
                        <th>Code</th>
                        <th class="desc">Description</th>
                        <th class="rnum">Qty</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                    {% set nctr = -1 %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                        {% set nctr = nctr+1 %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                {% if 'MM001' in value['resultset_value']['lineitems'][nctr]['myvalues'] %}
                                    <td class="num">{{i['myvalues']['MM001']['hsncode']}}</td>
                                {% else %}
                                    <td></td>
                                {% endif %}
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                    </tbody>
                </table>
            </div>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td class="num">Amount in Words:</td>
                        <td colspan="3">{{value['numtoword'].num2words(value['resultset_value']['popricingtotal']['VAL2']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</td> 
                    </tr>
                    <tr><td><br></td></tr>
                    <tr>
                        <td>Inv.:{{value['resultset_value']['dzinvno']}}</td>
                        <td>Tracking ID:{{value['resultset_value']['dztrkid']}}<span style="margin-left: 3mm;"></td>
                        <td>Payment Method:{{value['resultset_value']['dzpm']}}<span style="margin-left: 3mm;"></td>
                        <td>Scheme(if any):{{value['resultset_value']['dzscheme']}}</td>
                    </tr>
                    <tr>
                        <td style="text-align: center;">{{(value['resultset_value']['USR01']['username'])}}</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td class="ltop" style="text-align: center;">Prepared By</td>
                        <td class="ltop" style="text-align: right; float:right;">Receiver's Signature</td>
                    </tr>
                </tbody>
            </table>
            <table class="tright" style="border-collapse: collapse;">
                <tbody>
                    <tr>
                        <td class="rnum"><b>Total</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['MTLPRICE']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Discount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        {% if value['resultset_value']['discount'][0] is defined %}
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['discount'][0]['discamt'])}}%</td>
                        {% else %}
                        <td></td>
                        {% endif %}
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Taxable Amount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['VAL1']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Add:VAT</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VATPER'])}}%</td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{value['resultset_value']['popricingtotal']['VAT']}}</td> 
                    </tr>
                    <tr>
                        <td class="rnum"><b>Net Amount</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;">{{value['resultset_value']['popricingtotal']['VAL2']}}</td>
                    </tr>
                </tbody>
            </table>
            <div>
                <br><br><br><br><br><br><br>
                <p class="tright"><b>For  {{value['resultset_value']['CO010']['coname']}}</b></p>
                <p class="tleft">E & OE<br>Goods once sold are not exchangeable or returnable</p>
            </div> 
        </div>
        {% else %}
        <div class="preinv">
            <table style="width: 100%; border-bottom: 1px solid black;">
                <tbody>
                    <tr>
                        <td>
                            <img class="imag" src="http://103.146.234.44:8080/img/NGMlogo1.jpg">
                        </td>
                        <td class="heading">
                            {% if value['resultset_value']['status'] != 'C' %}
                                <h2 class="snum">Invoice - DRAFT</h2>
                            {% elif 'prncnt' in value['resultset_value'] %}
                                {% if value['resultset_value']['prncnt'] <= 0 %}
                                     <h2 class="snum">Tax Invoice</h2>
                                {% else %}
                                    <h2 class="snum">Invoice (COPY OF ORIGINAL :  {{value['resultset_value']['prncnt']}} )</h2>
                                {% endif %}
                            {% endif %}
                            <h2>{{value['resultset_value']['CO010']['coname']}}</h2>
                            {% if 'OD10' in value['resultset_value'] %}
                            <p><span style="margin-left: 3mm;"></span>{{value['resultset_value']['OD10']['address'][0]['postbox']}}</p>
                            {% else %}
                            <p><span style="margin-left: 3mm;"></span>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</p>
                            {% endif %}
                            <p>VAT No. :<span style="margin-left: 3mm;"></span><b>{{value['resultset_value']['CO010']['covatno']}}</b></p>
                            {% if 'OD10' in value['resultset_value'] %}
                            <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OD10']['unitidobj']['key2']}}</b></p> 
                            {% else %}
                            <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OU010']['unitname']}}</b></p> 
                            {% endif %}
                        </td>
                        <td class="tright">
                            <br><br><br>
                            <p>Mode of Payment: {{value['resultset_value']['dzpm']}}</p>
                            {% if 'OD10' in value['resultset_value'] %}
                                <p>Phone No:{{value['resultset_value']['OD10']['phoneno']}}</p>
                            {% else %}
                                <p>Phone No:{{value['resultset_value']['CO010']['phoneno']}}</p>
                            {% endif %}
                        </td>
                    </tr>
                </tbody>
            </table>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td>Buyer's Name</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custname']}}</td>
                    </tr>
                    <tr>
                        <td>Address</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custaddress']}}</td>
                    </tr>
                    <tr>
                        <td>Phone No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['phoneno']}}</td>
                    </tr>
                    <tr>
                        <td>Buyer's VAT No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['vatno']}}</td>  
                    </tr>
                </tbody>
            </table>
            <table class="tright">
                <tbody>
                    <tr>
                        <td>Invoice No.</td>
                        <td>:</td>
                        <td><b>{{value['resultset_value']['sinvno']}}</b></td>
                    </tr>
                    <tr>
                        <td>Invoice Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['sinvdate']}}</td>
                    </tr>
                    <tr>
                        <td>BS Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['sinvbs']}}</td>
                    </tr>
                    <tr>
                        <td>Transaction Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docdt']}}</td>  
                    </tr>
                    <tr>
                        <td>Print Date & Time</td>
                        <td>:</td>
                        <td>{{ value['printdate'].strftime('%d/%m/%Y') }} {{ value['printdate'].strftime('%H:%M:%S') }}</td>
                    </tr>
                </tbody>
            </table>
            <div class="theight">
                <table class="collapse_table">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th>H.S.Code</th>
                        <th>Code</th>
                        <th class="desc">Description</th>
                        <th class="rnum">Qty</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                    {% set nctr = -1 %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                        {% set nctr = nctr+1 %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                {% if 'MM001' in value['resultset_value']['lineitems'][nctr]['myvalues'] %}
                                    <td class="num">{{i['myvalues']['MM001']['hsncode']}}</td>
                                {% else %}
                                    <td></td>
                                {% endif %}
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                    </tbody>
                </table>
            </div>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td class="num">Amount in Words:</td>
                        <td colspan="3">{{value['numtoword'].num2words(value['resultset_value']['popricingtotal']['VAL2']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</td> 
                    </tr>
                    <tr><td><br></td></tr>
                    <tr>
                        <td>Inv.:{{value['resultset_value']['dzinvno']}}</td>
                        <td>Tracking ID:{{value['resultset_value']['dztrkid']}}<span style="margin-left: 3mm;"></td>
                        <td>Payment Method:{{value['resultset_value']['dzpm']}}<span style="margin-left: 3mm;"></td>
                        <td>Scheme(if any):{{value['resultset_value']['dzscheme']}}</td>
                    </tr>
                    <tr>
                        <td style="text-align: center;">{{(value['resultset_value']['USR01']['username'])}}</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td class="ltop" style="text-align: center;">Prepared By</td>
                        <td class="ltop" style="text-align: right; float:right;">Receiver's Signature</td>
                    </tr>
                </tbody>
            </table>
            <table class="tright" style="border-collapse: collapse;">
                <tbody>
                    <tr>
                        <td class="rnum"><b>Total</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['MTLPRICE']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Discount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        {% if value['resultset_value']['discount'][0] is defined %}
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['discount'][0]['discamt'])}}%</td>
                        {% else %}
                        <td></td>
                        {% endif %}
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Taxable Amount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['VAL1']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Add:VAT</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VATPER'])}}%</td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{value['resultset_value']['popricingtotal']['VAT']}}</td> 
                    </tr>
                    <tr>
                        <td class="rnum"><b>Net Amount</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;">{{value['resultset_value']['popricingtotal']['VAL2']}}</td>
                    </tr>
                </tbody>
            </table>
            <div>
                <br><br><br><br><br><br><br>
                <p class="tright"><b>For  {{value['resultset_value']['CO010']['coname']}}</b></p>
                <p class="tleft">E & OE<br>Goods once sold are not exchangeable or returnable</p>
            </div> 
        </div>
        {% endif %}
    </body>
</html>""",
    "pre_sale":"""<!DOCTYPE html>
<html>
    <head>

    </head>
    <body>
         <div class="preinv">
            <table style="width: 100%;">
                <tr>
                    <td class="num" style="width: 200px;">
                        <p>Invoice No.:{{value['resultset_value']['pino']}}</p>
                        <p>Miti:2079/09/20</p>
                        <p>Order From:{{value['resultset_value']['custidobj']['key2']}}</p>
                    </td>
                    <td class="snum" style="font-size: 13px;">
                        <p style="font-size: 17px;">{{value['resultset_value']['coidobj']['key2']}}</p>
                        <p>{{value['resultset_value']['unitidobj']['key2']}}<br>Ph No: {{value['resultset_value']['phoneno']}}</p>                   
                        <p><b><u>PRE INVOICE-MANUAL ORDER</u></b></p>
                    </td>               
                    <td>
                        <p>Print Date:{{value['printdate'].strftime('%d/%m/%Y')}}</p>
                        <p>Print Time:{{value['printdate'].strftime('%H:%M:%S')}}</p>
                    <td>
                </tr>
            </table>
        </div>
        <div>
            <table style="width: 100%;" class="collapse_table">
                <thead class="tabl">
                    <th class="snum">S.N</th>
                    <th class="num">Part No</th>
                    <th class="num">Part Name</th>
                    <th>Quantity</th>
                    <th>Alloted</th>
                    <th>Back Order</th>
                    <th>Rate</th>
                    <th>Amount</th>
                    <th>Order No</th>
                </thead>
				{%- for i in value['resultset_value']['lineitems'] %}	
                <tr>
                    <td class="snum">{{loop.index}}</td>
                    <td class="num">{{i['itemcode']}}</td>
                    <td class="num">{{i['itemcodeobj']['key2']}}</td>
                    <td>{{i.reqqty}}</td>
                    <td>{{i['qty']}}</td>
                    <td>{{i['psoqty']}}</td>
                    <td>{{\"%.2f\"|format(i['rate'])}}</td>
                    <td>{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                    <td>{{i['orderno']}}</td>
                </tr>
                {% endfor -%}
                <tr>
                    <td></td>
                    <td></td>
                    <td class="num"><B>TOTAL</B></td>
                    <td><B>{{value['resultset_value']['popricingtotal']['REQQTY']}}</td>
                    <td><B>{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['QTY'])}}</td>
                    <td></td>
                    <td></td>
                    <td><B>{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['ACTMTLPRICE'])}}</td>
                    <td></td>
                </tr>
            </table>
        </div>
        <footer class="foot">1</footer>
    </body>
</html>

<style>
    table,tr,th,td{
        font-size: 13px;
        font-family: calibri;
        text-align: right;
    }
    .preinv{
        font-size: 14px;
        font-family: calibri;
    }
    .tabl{
        border: 1px solid black;
        border-right: none;
        border-left: none;         
    }
    
    div.table_items {
        height: 200px !important;
        border: 1px solid #ccc;
    }
    
    .collapse_table{
        border-collapse: collapse;
    }
    .num{
        text-align: left;
    }
    .snum{
        text-align: center;
    }
    .foot{
         margin-top: 100%;
        border-top: 1px solid black;
        text-align: right;
    }
</style> """,
    "packinglist":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,tr,td{
                border: 1px solid black;
                border-collapse: collapse;
                font-family: calibri;
                font-size: 15px;
                text-align: center;
            }
            .pack{
                width: 100%;
            }
            .lalign{
                text-align: left;
            }
            .box{
                width: 150px;
            }
        </style>
    </head>
    <body>
        <table class="pack">
            <tr>
                <td colspan="5" style="text-align: center;">Packing List</td>
            </tr>
            <tr>
                <td colspan="3">{{value['resultset_value']['custidobj']['key2']}}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Bill No {{value['resultset_value']['docno']}}</td>
                <td colspan="2">Date:{{value['resultset_value']['docdt']}}</td>
            </tr>
            <tr>
                <td>S.N</td>
                <td class="lalign">Part No</td>
                <td class="lalign">Part Name</td>
                <td>Quantity</td>
                <td class="box">Box No</td>
            </tr>
			{%- for i in value['resultset_value']['packingdtl'] %}
            <tr>
                <td class="snum">{{loop.index}}</td>
                <td class="lalign">{{i['itemcode']}}</td>
                <td class="lalign">{{i['itemcodeobj']['key2']}}</td>
                <td>{{i.qty}}</td>
                <td  class="box">{{i.packingcode}}</td>
            </tr>
			{% endfor -%}
            
        </table>
    </body>
</html> """,
    "taxinv1":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,tr,th,td{
                font-size: 15px;
                font-family: calibri;
                text-align: left;
            }
            .preinv{
                font-size: 16px;
                font-family: calibri;
                width: 100%;
            }
            .heading{
                font-size: 18px;
                line-height: 0px;
                width: 100%;
                padding-left: 0%;
                text-align: center;
                margin-top: 0%;
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
            .collapse_table{
                border-collapse: collapse;
                margin-top: 100px;
                width: 100%;
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
            .foot{
                margin-top: 100%;
                border-top: 1px solid black;
                text-align: right;
                font-size: 11px;
            }
            .theight1{
                height: 500px;
            }
            .sign{
                text-align: center;
                font-size: 18px;
                border-top: 1px solid black;;
            }
            
        </style>
    </head>
    <body>
        <table class="preinv">
            <tr>
                <td>
                    <img class="imag" src="http://103.146.234.44:8080/img/NGMlogo1.jpg">
                </td>
                <td class="heading">
                    {% if value['resultset_value']['status'] != 'C' %}
                        <h2 class="snum">Invoice - DRAFT</h2>
                        {% elif 'prncnt' in value['resultset_value'] %}
                            {% if value['resultset_value']['prncnt'] <= 0 %}
                                <h2 class="rnum">Tax Invoice</h2>
                            {% else %}
                            <h2 class="rnum">Invoice (COPY OF ORIGINAL :  {{value['resultset_value']['prncnt']}} )</h2>
                        {% endif %}
                    {% endif %}
                    <h2>{{value['resultset_value']['CO010']['coname']}}</h2>
                    <h5>{{value['resultset_value']['OU010']['unitname']}}</h5>
                    {% if 'OD10' in value['resultset_value'] %}
                        <h5>Phone No:{{value['resultset_value']['OD10']['phoneno']}}</h5>
                    {% else %}
                        <h5>Phone No:{{value['resultset_value']['CO010']['phoneno']}}</h5>
                    {% endif %}
                    <h2>VAT No. {{value['resultset_value']['CO010']['covatno']}}</h2>
                    <h4>{{value['resultset_value']['OU010']['unitname']}}</h4>
                </td>
            </tr>
        </table>
        <hr>
        <table class="tleft">
            <tr>
                <td>Buyer's Name</td>
                <td>:</td>
                <td>{{value['resultset_value']['CM010']['custname']}}</td>
            </tr>
            <tr>
                <td>Address</td>
                <td>:</td>
                <td>{{value['resultset_value']['CM010']['address'][0]['adrs1']}}</td>
            </tr>
            <tr>
                <td>Phone No.</td>
                <td>:</td>
                <td>{{value['resultset_value']['CM010']['phone']}}</td>
            </tr>
            <tr>
                <td>Buyer's VAT No.</td>
                <td>:</td>
                <td>{{value['resultset_value']['CM010']['pan']}}</td>
            </tr>
        </table>
        <table class="tright">
            <tr>
                <td><b>Invoice No.</b></td>
                <td>:</td>
                <td><b>{{value['resultset_value']['sinvno']}}</b></td>
            </tr>
            <tr>
                <td><b>Bill Issue Date</b></td>
                <td>:</td>
                <td>{{value['resultset_value']['sinvdate']}}</td>
            </tr>
            <tr>
                <td><b>BS Date</b> </td>
                <td>:</td>
                <td>{{value['resultset_value']['docbs']}}</td>
            </tr>
            <tr>
                <td><b>Transaction Date</b></td>
                <td>:</td>
                <td>{{value['resultset_value']['docdt']}}</td>  
            </tr>
        </table>
        <div class="theight1">
        <table class="collapse_table">
            <thead class="tabl">
                <th>S.N.</th>
                <th>H.S.Code</th>
                <th>Code</th>
                <th class="desc">Description</th>
                <th class="rnum">Qty</th>
                <th class="rnum">Rate</th>
                <th class="rnum">Amount</th>
            </thead>
            <tbody>
            {% set nctr = -1 %}
		        {%- for i in value['resultset_value']['lineitems'] %}
                {% set nctr = nctr+1 %}
                    <tr>
                        <td class="snum">{{loop.index}}</td>
                        {% if 'MM001' in value['resultset_value']['lineitems'][nctr]['myvalues'] %}
                            <td class="num">{{i['myvalues']['MM001']['hsncode']}}</td>
                        {% else %}
                            <td></td>
                        {% endif %}
                        <td>{{i['itemcode']}}</td>
                        <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                        <td class="rnum">{{i.qty}}</td>
                        <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                        <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                    </tr>
                {% endfor -%}                      
               </tbody>
            </table>
            </div>
            <table class="fcont" style="float: right; text-align: left; border-collapse: collapse;">
                <tr class="foot">
                    <td><b>Sub Total</b></td>
                    <td></td>
                    <td>{{value['resultset_value']['popricingtotal']['MTLPRICE']}}</td>
                </tr>
                <tr>
                    <td>Discount</td>
                    {% if value['resultset_value']['discount'][0] is defined %}
                    <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['discount'][0]['discrate'])}}%</td>
                    {% else %}
                    <td>0.00%</td>
                    {% endif %}
                    <td>{{value['resultset_value']['popricingtotal']['DISCOUNT']}}</td>
                </tr>
                <tr>
                    <td>Total Amount</td>
                    <td></td>
                    <td>{{value['resultset_value']['popricingtotal']['VAL1']}}</td>
                </tr>
                <tr>
                    <td>Add:VAT</td>
                    <td>{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VATPER'])}}%</td>
                    <td>{{value['resultset_value']['popricingtotal']['VAT']}}</td> 
                </tr>
                <tr class="tabl">
                    <td><b>Total</b></td>
                    <td></td>
                    <td>{{value['resultset_value']['popricingtotal']['VAL2']}}</td>
                </tr>
            </table>
            <table class="fcont" style="float: left; text-align: left;">
                <tr>
                    <td><b>Mode Of Payment:</b></td>
                </tr>
                <tr>
                    <td><b>Bank Name:</b></td>
                </tr>
                <tr>
                    <td><b>Destination:</b></td>
                </tr>
                <tr>
                    <td><b>LC No.:</b></td>
                </tr>
                <tr>
                    <td><b>D/O No.:</b></td>
                </tr>
            </table>
            <table class="fcont" style="float: left; text-align: left;">
                {%- for i in value['resultset_value']['payment'] %}
                    <tr>
                        <td>{{i['paytype']}}</td>
                    </tr>
                    <tr>
                        <td>{{i['bankname']}}</td>
                    </tr>
                    <tr>
                        <td></td>
                    </tr>
                    <tr>
                        <td>{{i['pdocnumber']}}</td>  
                    </tr>
                {% endfor -%}
            </table>
            <table class="fcont" style="float: left; text-align: left;">
                <br><br><br><br><br>
                <tr>
                    <td></td>
                    <td><b>D/O Date/BS Date:{{value['resultset_value']['docbs']}}</b></td>
                </tr>
            </table>
            <table class="fcont" style="float: left; text-align: left;">
                {%- for i in value['resultset_value']['payment'] %}
                    <td><b></b></td>
                {% endfor -%}
            </table>
            <br>
            <div class="preinv">
                <p class="tabl"><b>Amount in Words:</b>  {{value['numtoword'].num2words(value['resultset_value']['popricingtotal']['VAL2']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</p>
                <p style="line-height:0px; font-size:15px;">Print Date and Time: 12/01/2023 3:02:34 PM</p>
            </div>
        <table style="width: 100%;">
            <tr>
                <td></td>
                <td class="rnum" style="width:30%">{{(value['resultset_value']['USR01']['username'])}}</td>
                <td></td>
            </tr>
            <tr>
                <td class="num" style="text-decoration: overline;">Receiver's Signature</td>
                <td class="rnum" style="text-decoration: overline; width: 30%">Prepared By</td>
                <td class="rnum" style="text-decoration: overline;">Authorized Signature</td>
            </tr>
            <tr>
            <td><br></td>
            </tr>
            <tr>
                <td></td>
                <td></td>
                <td class="rnum" style="font-size: 15px;">For {{value['resultset_value']['CO010']['coname']}}</td>
            </tr>
        </table>
    </body>
</html>""",
    "service":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,tr,th,td{
                font-size: 11px;
                font-family: calibri;
                text-align: left;
            }
            .preinv{
                font-size: 11px;
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
            div.table_items {
                height: 200px !important;
                border: 1px solid #ccc;
            }
            .theight{
                height: 275px;
            }
            .theight1{
                height: 800px;
            }
            .heading{
                font-size: 15px;
                line-height: 0px;
                text-align: left;
                margin-top: 0%;
                padding-top: 0%;
            }
            .collapse_table{
                border-collapse: collapse;
                width: 100%;
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
            .desc{
                padding-right: 150px;
            }
            .prin{
                page-break-before: always;
            }
        </style>
    </head>
    <body>
    {% if value['resultset_value']['prncnt'] == 0 %}
        <div class="preinv">
            <table style="width: 100%; border-bottom: 1px solid black;">
                <tbody>
                    <tr>
                        <td>
                            <img class="imag" src="http://103.146.234.44:8080/img/NGMlogo1.jpg">
                        </td>
                        <td class="heading">
                            <h2 class="snum">Tax Invoice</h2>
                            <h2>{{value['resultset_value']['CO010']['coname']}}</h2>
                            {% if 'OD10' in value['resultset_value'] %}
                                <h4><span style="margin-left: 3mm;"></span>{{value['resultset_value']['OD10']['address'][0]['postbox']}}</h4>
                            {% else %}
                                <p><span style="margin-left: 3mm;"></span>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</p>
                            {% endif %}
                            <p>VAT No. :<span style="margin-left: 3mm;"></span><b>{{value['resultset_value']['CO010']['covatno']}}</b></p>
                           {% if 'OD10' in value['resultset_value'] %}
                                <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OD10']['unitidobj']['key2']}}</b></p> 
                            {% else %}
                                <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OU010']['unitname']}}</b></p>
                            {% endif %}
                        </td>
                        <td class="tright">
                            <br><br><br>
                            <p>Mode of Payment: Cash Bill</p>
                            {% if 'OD10' in value['resultset_value'] %}
                            <p>Phone No:{{value['resultset_value']['OD10']['phoneno']}}</p>
                            {% else %}
                            <p>Phone No:{{value['resultset_value']['CO010']['phoneno']}}</p>
                            {% endif %}
                        </td>
                    </tr>
                </tbody>
            </table>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td>Buyer's Name</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custname']}}</td>
                    </tr>
                    <tr>
                        <td>Address</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custaddress']}}</td>
                    </tr>
                    <tr>
                        <td>Phone No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['phoneno']}}</td>
                    </tr>
                    <tr>
                        <td>Buyer's VAT No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['vatno']}}</td>  
                    </tr>
                </tbody>
            </table>
            <table class="tright">
                <tbody>
                    <tr>
                        <td>Invoice No.</td>
                        <td>:</td>
                        <td><b>{{value['resultset_value']['sinvno']}}</b></td>
                    </tr>
                    <tr>
                        <td>Invoice Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['sinvdate']}}</td>
                    </tr>
                    <tr>
                        <td>BS Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docbs']}}</td>
                    </tr>
                    <tr>
                        <td>Transaction Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docdt']}}</td>  
                    </tr>
                    <tr>
                        <td>Print Date & Time</td>
                        <td>:</td>
                        <td>{{ value['printdate'].strftime('%d/%m/%Y') }} {{ value['printdate'].strftime('%H:%M:%S') }}</td>
                    </tr>
                </tbody>
            </table>
            {% if value['resultset_value']['lineitems']|length <11 %}
            <div class="theight">
                <table class="collapse_table">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th>H.S.Code</th>
                        <th>Code</th>
                        <th class="desc">Description</th>
                        <th class="rnum">Qty</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                    {% if (value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none) and (value['resultset_value']['svitems'][0]['itemcodeobj'] is not none) %}
                    {% set nctr = -1 %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                        {% set nctr = nctr+1 %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                {% if 'MM001' in value['resultset_value']['lineitems'][nctr]['myvalues'] %}
                                    <td class="num">{{i['myvalues']['MM001']['hsncode']}}</td>
                                {% else %}
                                    <td></td>
                                {% endif %}
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                        {%- for i in value['resultset_value']['svitems'] %}
                        <tr>
                           {% if value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                            <td class="snum">{{loop.index + (value['resultset_value']['lineitems']|length)}}</td>
							{% else %}
								<td class="snum">{{loop.index0 + (value['resultset_value']['lineitems']|length)}}</td>
							{% endif %}
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}
                        {% elif value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                        {% elif value['resultset_value']['svitems'][0]['itemcodeobj'] is not none %}
                        {%- for i in value['resultset_value']['svitems'] %}
                        <tr>
                           {% if value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                            <td class="snum">{{loop.index + (value['resultset_value']['lineitems']|length)}}</td>
							{% else %}
								<td class="snum">{{loop.index0 + (value['resultset_value']['lineitems']|length)}}</td>
							{% endif %}
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}
                        {% endif %}
                    </tbody>
                </table>
            </div>
            {% else %} 
            <div class="theight1">
                <table class="collapse_table">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th>Code</th>
                        <th class="desc">Description</th>
                        <th class="rnum">Qty</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                        {% if (value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none) and (value['resultset_value']['svitems'][0]['itemcodeobj'] is not none) %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                        {%- for i in value['resultset_value']['svitems'] %}
                        <tr>
                           {% if value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                            <td class="snum">{{loop.index + (value['resultset_value']['lineitems']|length)}}</td>
							{% else %}
								<td class="snum">{{loop.index0 + (value['resultset_value']['lineitems']|length)}}</td>
							{% endif %}
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}
                        {% elif value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                        {% elif value['resultset_value']['svitems'][0]['itemcodeobj'] is not none %}
                        {%- for i in value['resultset_value']['svitems'] %}
                        <tr>
                           {% if value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                            <td class="snum">{{loop.index + (value['resultset_value']['lineitems']|length)}}</td>
							{% else %}
								<td class="snum">{{loop.index0 + (value['resultset_value']['lineitems']|length)}}</td>
							{% endif %}
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}
                        {% endif %}
                    </tbody>
                </table>
            </div>
            {% endif %}
            <table class="tleft">
                <tbody>
                    <tr>
                        <td class="num">Amount in Words:</td>
                        <td>{{value['numtoword'].num2words(value['resultset_value']['popricingtotal']['VAL2']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</td>
                    </tr>
                    <tr><td><br><br></td></tr>
                    <tr>
                        <td style="text-align: center;">{{(value['resultset_value']['USR01']['username'])}}</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td class="ltop" style="text-align: center;">Prepared By</td>
                        <td class="ltop" style="text-align: right;">Receiver's Signature</td>
                    </tr>
                </tbody>
            </table>
            <table class="tright" style="border-collapse: collapse;">
                <tbody>
                    <tr>
                        <td class="rnum"><b>Total</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['MTLPRICE']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Discount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        {% if value['resultset_value']['discount'][0] is defined %}
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['discount'][0]['discrate'])}}%</td>
                        {% else %}
                        <td></td>
                        {% endif %}
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Taxable Amount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['VAL1']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Add:VAT</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VATPER'])}}%</td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{value['resultset_value']['popricingtotal']['VAT']}}</td> 
                    </tr>
                    <tr>
                        <td class="rnum"><b>Net Amount</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;">{{value['resultset_value']['popricingtotal']['VAL2']}}</td>
                    </tr>
                </tbody>
            </table>
            <div>
                <br><br><br><br><br><br>
                <p class="tright"><b>For {{value['resultset_value']['CO010']['coname']}}</b></p>
                <p class="tleft">E & OE<br>Goods once sold are not exchangeable or returnable</p>
            </div> 
        </div>
        <div class="preinv prin">
            <table style="width: 100%; border-bottom: 1px solid black;">
                <tbody>
                    <tr>
                        <td>
                            <img class="imag" src="http://103.146.234.44:8080/img/NGMlogo1.jpg">
                        </td>
                        <td class="heading">
                                <h2 class="snum">Invoice</h2>
                            <h2>{{value['resultset_value']['CO010']['coname']}}</h2>
                            {% if 'OD10' in value['resultset_value'] %}
                                <h4><span style="margin-left: 3mm;"></span>{{value['resultset_value']['OD10']['address'][0]['postbox']}}</h4>
                            {% else %}
                                <p><span style="margin-left: 3mm;"></span>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</p>
                            {% endif %}
                            <p>VAT No. :<span style="margin-left: 3mm;"></span><b>{{value['resultset_value']['CO010']['covatno']}}</b></p>
                           {% if 'OD10' in value['resultset_value'] %}
                                <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OD10']['unitidobj']['key2']}}</b></p> 
                            {% else %}
                                <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OU010']['unitname']}}</b></p>
                            {% endif %}
                        </td>
                        <td class="tright">
                            <br><br><br>
                            <p>Mode of Payment: Cash Bill</p>
                            {% if 'OD10' in value['resultset_value'] %}
                            <p>Phone No:{{value['resultset_value']['OD10']['phoneno']}}</p>
                            {% else %}
                            <p>Phone No:{{value['resultset_value']['CO010']['phoneno']}}</p>
                            {% endif %}
                        </td>
                    </tr>
                </tbody>
            </table>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td>Buyer's Name</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custname']}}</td>
                    </tr>
                    <tr>
                        <td>Address</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custaddress']}}</td>
                    </tr>
                    <tr>
                        <td>Phone No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['phoneno']}}</td>
                    </tr>
                    <tr>
                        <td>Buyer's VAT No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['vatno']}}</td>  
                    </tr>
                </tbody>
            </table>
            <table class="tright">
                <tbody>
                    <tr>
                        <td>Invoice No.</td>
                        <td>:</td>
                        <td><b>{{value['resultset_value']['sinvno']}}</b></td>
                    </tr>
                    <tr>
                        <td>Invoice Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['sinvdate']}}</td>
                    </tr>
                    <tr>
                        <td>BS Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docbs']}}</td>
                    </tr>
                    <tr>
                        <td>Transaction Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docdt']}}</td>  
                    </tr>
                    <tr>
                        <td>Print Date & Time</td>
                        <td>:</td>
                        <td>{{ value['printdate'].strftime('%d/%m/%Y') }} {{ value['printdate'].strftime('%H:%M:%S') }}</td>
                    </tr>
                </tbody>
            </table>
            {% if value['resultset_value']['lineitems']|length <11 %}
            <div class="theight">
                <table class="collapse_table">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th>H.S.Code</th>
                        <th>Code</th>
                        <th class="desc">Description</th>
                        <th class="rnum">Qty</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                    {% if (value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none) and (value['resultset_value']['svitems'][0]['itemcodeobj'] is not none) %}
                    {% set nctr = -1 %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                        {% set nctr = nctr+1 %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                {% if 'MM001' in value['resultset_value']['lineitems'][nctr]['myvalues'] %}
                                    <td class="num">{{i['myvalues']['MM001']['hsncode']}}</td>
                                {% else %}
                                    <td></td>
                                {% endif %}
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                        {%- for i in value['resultset_value']['svitems'] %}
                        <tr>
                           {% if value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                            <td class="snum">{{loop.index + (value['resultset_value']['lineitems']|length)}}</td>
							{% else %}
								<td class="snum">{{loop.index0 + (value['resultset_value']['lineitems']|length)}}</td>
							{% endif %}
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}
                        {% elif value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                        {% elif value['resultset_value']['svitems'][0]['itemcodeobj'] is not none %}
                        {%- for i in value['resultset_value']['svitems'] %}
                        <tr>
                           {% if value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                            <td class="snum">{{loop.index + (value['resultset_value']['lineitems']|length)}}</td>
							{% else %}
								<td class="snum">{{loop.index0 + (value['resultset_value']['lineitems']|length)}}</td>
							{% endif %}
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}
                        {% endif %}
                    </tbody>
                </table>
            </div>
            {% else %} 
            <div class="theight1">
                <table class="collapse_table">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th>Code</th>
                        <th class="desc">Description</th>
                        <th class="rnum">Qty</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                        {% if (value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none) and (value['resultset_value']['svitems'][0]['itemcodeobj'] is not none) %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                        {%- for i in value['resultset_value']['svitems'] %}
                        <tr>
                           {% if value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                            <td class="snum">{{loop.index + (value['resultset_value']['lineitems']|length)}}</td>
							{% else %}
								<td class="snum">{{loop.index0 + (value['resultset_value']['lineitems']|length)}}</td>
							{% endif %}
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}
                        {% elif value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                        {% elif value['resultset_value']['svitems'][0]['itemcodeobj'] is not none %}
                        {%- for i in value['resultset_value']['svitems'] %}
                        <tr>
                           {% if value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                            <td class="snum">{{loop.index + (value['resultset_value']['lineitems']|length)}}</td>
							{% else %}
								<td class="snum">{{loop.index0 + (value['resultset_value']['lineitems']|length)}}</td>
							{% endif %}
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}
                        {% endif %}
                    </tbody>
                </table>
            </div>
            {% endif %}
            <table class="tleft">
                <tbody>
                    <tr>
                        <td class="num">Amount in Words:</td>
                        <td>{{value['numtoword'].num2words(value['resultset_value']['popricingtotal']['VAL2']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</td>
                    </tr>
                    <tr><td><br><br></td></tr>
                    <tr>
                        <td style="text-align: center;">{{(value['resultset_value']['USR01']['username'])}}</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td class="ltop" style="text-align: center;">Prepared By</td>
                        <td class="ltop" style="text-align: right;">Receiver's Signature</td>
                    </tr>
                </tbody>
            </table>
            <table class="tright" style="border-collapse: collapse;">
                <tbody>
                    <tr>
                        <td class="rnum"><b>Total</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['MTLPRICE']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Discount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        {% if value['resultset_value']['discount'][0] is defined %}
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['discount'][0]['discrate'])}}%</td>
                        {% else %}
                        <td></td>
                        {% endif %}
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Taxable Amount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['VAL1']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Add:VAT</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VATPER'])}}%</td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{value['resultset_value']['popricingtotal']['VAT']}}</td> 
                    </tr>
                    <tr>
                        <td class="rnum"><b>Net Amount</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;">{{value['resultset_value']['popricingtotal']['VAL2']}}</td>
                    </tr>
                </tbody>
            </table>
            <div>
                <br><br><br><br><br><br>
                <p class="tright"><b>For {{value['resultset_value']['CO010']['coname']}}</b></p>
                <p class="tleft">E & OE<br>Goods once sold are not exchangeable or returnable</p>
            </div> 
        </div>
        {% else %}
        <div class="preinv">
            <table style="width: 100%; border-bottom: 1px solid black;">
                <tbody>
                    <tr>
                        <td>
                            <img class="imag" src="http://103.146.234.44:8080/img/NGMlogo1.jpg">
                        </td>
                        <td class="heading">
                            {% if value['resultset_value']['status'] != 'C' %}
                                <h2 class="snum">Invoice - DRAFT</h2>
                            {% elif 'prncnt' in value['resultset_value'] %}
                                {% if value['resultset_value']['prncnt'] <= 0 %}
                                     <h2 class="snum">Tax Invoice</h2>
                                {% else %}
                                    <h2 class="snum">Invoice (COPY OF ORIGINAL :  {{value['resultset_value']['prncnt']}} )</h2>
                                {% endif %}
                            {% endif %}
                            <h2>{{value['resultset_value']['CO010']['coname']}}</h2>
                            {% if 'OD10' in value['resultset_value'] %}
                                <h4><span style="margin-left: 3mm;"></span>{{value['resultset_value']['OD10']['address'][0]['postbox']}}</h4>
                            {% else %}
                                <p><span style="margin-left: 3mm;"></span>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</p>
                            {% endif %}
                            <p>VAT No. :<span style="margin-left: 3mm;"></span><b>{{value['resultset_value']['CO010']['covatno']}}</b></p>
                           {% if 'OD10' in value['resultset_value'] %}
                                <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OD10']['unitidobj']['key2']}}</b></p> 
                            {% else %}
                                <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OU010']['unitname']}}</b></p>
                            {% endif %}
                        </td>
                        <td class="tright">
                            <br><br><br>
                            <p>Mode of Payment: Cash Bill</p>
                            {% if 'OD10' in value['resultset_value'] %}
                            <p>Phone No:{{value['resultset_value']['OD10']['phoneno']}}</p>
                            {% else %}
                            <p>Phone No:{{value['resultset_value']['CO010']['phoneno']}}</p>
                            {% endif %}
                        </td>
                    </tr>
                </tbody>
            </table>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td>Buyer's Name</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custname']}}</td>
                    </tr>
                    <tr>
                        <td>Address</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custaddress']}}</td>
                    </tr>
                    <tr>
                        <td>Phone No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['phoneno']}}</td>
                    </tr>
                    <tr>
                        <td>Buyer's VAT No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['vatno']}}</td>  
                    </tr>
                </tbody>
            </table>
            <table class="tright">
                <tbody>
                    <tr>
                        <td>Invoice No.</td>
                        <td>:</td>
                        <td><b>{{value['resultset_value']['sinvno']}}</b></td>
                    </tr>
                    <tr>
                        <td>Invoice Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['sinvdate']}}</td>
                    </tr>
                    <tr>
                        <td>BS Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docbs']}}</td>
                    </tr>
                    <tr>
                        <td>Transaction Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docdt']}}</td>  
                    </tr>
                    <tr>
                        <td>Print Date & Time</td>
                        <td>:</td>
                        <td>{{ value['printdate'].strftime('%d/%m/%Y') }} {{ value['printdate'].strftime('%H:%M:%S') }}</td>
                    </tr>
                </tbody>
            </table>
            {% if value['resultset_value']['lineitems']|length <11 %}
            <div class="theight">
                <table class="collapse_table">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th>H.S.Code</th>
                        <th>Code</th>
                        <th class="desc">Description</th>
                        <th class="rnum">Qty</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                    {% if (value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none) and (value['resultset_value']['svitems'][0]['itemcodeobj'] is not none) %}
                    {% set nctr = -1 %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                        {% set nctr = nctr+1 %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                {% if 'MM001' in value['resultset_value']['lineitems'][nctr]['myvalues'] %}
                                    <td class="num">{{i['myvalues']['MM001']['hsncode']}}</td>
                                {% else %}
                                    <td></td>
                                {% endif %}
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                        {%- for i in value['resultset_value']['svitems'] %}
                        <tr>
                           {% if value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                            <td class="snum">{{loop.index + (value['resultset_value']['lineitems']|length)}}</td>
							{% else %}
								<td class="snum">{{loop.index0 + (value['resultset_value']['lineitems']|length)}}</td>
							{% endif %}
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}
                        {% elif value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                        {% elif value['resultset_value']['svitems'][0]['itemcodeobj'] is not none %}
                        {%- for i in value['resultset_value']['svitems'] %}
                        <tr>
                           {% if value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                            <td class="snum">{{loop.index + (value['resultset_value']['lineitems']|length)}}</td>
							{% else %}
								<td class="snum">{{loop.index0 + (value['resultset_value']['lineitems']|length)}}</td>
							{% endif %}
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}
                        {% endif %}
                    </tbody>
                </table>
            </div>
            {% else %} 
            <div class="theight1">
                <table class="collapse_table">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th>Code</th>
                        <th class="desc">Description</th>
                        <th class="rnum">Qty</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                        {% if (value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none) and (value['resultset_value']['svitems'][0]['itemcodeobj'] is not none) %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                        {%- for i in value['resultset_value']['svitems'] %}
                        <tr>
                           {% if value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                            <td class="snum">{{loop.index + (value['resultset_value']['lineitems']|length)}}</td>
							{% else %}
								<td class="snum">{{loop.index0 + (value['resultset_value']['lineitems']|length)}}</td>
							{% endif %}
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}
                        {% elif value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                        {% elif value['resultset_value']['svitems'][0]['itemcodeobj'] is not none %}
                        {%- for i in value['resultset_value']['svitems'] %}
                        <tr>
                           {% if value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                            <td class="snum">{{loop.index + (value['resultset_value']['lineitems']|length)}}</td>
							{% else %}
								<td class="snum">{{loop.index0 + (value['resultset_value']['lineitems']|length)}}</td>
							{% endif %}
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}
                        {% endif %}
                    </tbody>
                </table>
            </div>
            {% endif %}
            <table class="tleft">
                <tbody>
                    <tr>
                        <td class="num">Amount in Words:</td>
                        <td>{{value['numtoword'].num2words(value['resultset_value']['popricingtotal']['VAL2']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</td>
                    </tr>
                    <tr><td><br><br></td></tr>
                    <tr>
                        <td style="text-align: center;">{{(value['resultset_value']['USR01']['username'])}}</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td class="ltop" style="text-align: center;">Prepared By</td>
                        <td class="ltop" style="text-align: right;">Receiver's Signature</td>
                    </tr>
                </tbody>
            </table>
            <table class="tright" style="border-collapse: collapse;">
                <tbody>
                    <tr>
                        <td class="rnum"><b>Total</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['MTLPRICE']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Discount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        {% if value['resultset_value']['discount'][0] is defined %}
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['discount'][0]['discrate'])}}%</td>
                        {% else %}
                        <td></td>
                        {% endif %}
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Taxable Amount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['VAL1']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Add:VAT</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VATPER'])}}%</td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{value['resultset_value']['popricingtotal']['VAT']}}</td> 
                    </tr>
                    <tr>
                        <td class="rnum"><b>Net Amount</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;">{{value['resultset_value']['popricingtotal']['VAL2']}}</td>
                    </tr>
                </tbody>
            </table>
            <div>
                <br><br><br><br><br><br>
                <p class="tright"><b>For {{value['resultset_value']['CO010']['coname']}}</b></p>
                <p class="tleft">E & OE<br>Goods once sold are not exchangeable or returnable</p>
            </div> 
        </div>
        {% endif %}
    </body>
</html>""",
    "warrenty":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,tr,th,td{
                font-size: 13px;
                font-family: calibri;
                text-align: left;
            }
            .preinv{
                font-size: 14px;
                font-family: calibri;
                width: 100%;
                line-height: 5px;
            }
            .heading{
                font-size: 23px;
                line-height: 0px;
                width: 100%;
                text-align: center;
            }
            .imag{
                width: 70px;
                height: 85px;
            }
            .tabl{
                border: 1px solid black;
                border-right: none;
                border-left: none;
            }
            .collapse_table{
                border-collapse: collapse;
                width: 100%;
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
                text-align: center;
            }
            .foot{
                margin-top: 100%;
                border-top: 1px solid black;
                text-align: left;
                font-size: 13px;
                width: 100%;
            }
        </style>
    </head>
    <body>   
        <table class="preinv">
            <tbody>
                <tr>
                    <td style="width: 200px">
                        <img class="imag" src="http://103.146.234.44:8080/img/NGMlogo1.jpg">
                        <p>Challan No: {{value['resultset_value']['docno']}}</p>
                        <p>Miti: 2080/03/12</p>
                    </td>
                    <td class="snum"> 
                        <h4 class="heading">{{value['resultset_value']['CO010']['coname']}}</h4> 
                        {% if value['resultset_value']['OD10'] is not none %}
                        <h4>{{value['resultset_value']['OD10']['address'][0]['postbox']}}</h4>
                        {% else %}
                        <h4>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</h4>
                        {% endif %}
                        <p>Phone No. {{value['resultset_value']['OD10']['phoneno']}}</p>
                        <p>VAT No. {{value['resultset_value']['CO010']['covatno']}}</p>
                        <h4><u>SALES CHALLAN</u></h4>
                    </td>
                    <td class="rnum">
                        <p>Print Date: {{value['printdate'].strftime('%d/%m/%Y')}}</p>
                        <p>Print Time: {{value['printdate'].strftime('%H:%M:%S')}}</p>
                    </td>
                </tr>
            </tbody>
        </table>
        <table style="width:100%">
            <tbody>
                <tr>
                    <td><u>To: NEPAL GENERAL MARKETING SERVICE DIVISION (WARRENTY)</u></td>
                    <td>Customer VAT No:{{value['resultset_value']['vatno']}}</td>
                </tr>
            </tbody>
        </table>
        <table class="collapse_table">
            <thead class="tabl">
                <th class="snum">S.N.</th>
                <th>Part No</th>
                <th style="width:300px">Part Name</th>
                <th class="rnum">Quantity</th>
                <th class="rnum">Rate</th>
                <th class="rnum">Amount</th>
            </thead>
            <tbody>
                {%- for i in value['resultset_value']['lineitems'] %}                                 
                    <tr>
                        <td class="snum">{{loop.index}}</td>
                        <td>{{i['itemcode']}}</td>
                        <td>{{i['itemcodeobj']['key2']}}</td>
                        <td class="rnum">{{i.qty}}</td>
                        <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                        <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                    </tr>
                {% endfor -%}
                <tr><td><br></td></tr>
                <tr>
                    <td></td>
                    <td>{{value['numtoword'].num2words(value['resultset_value']['popricingtotal']['VAL2']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</td>
                    <td></td>
                    <td class="rnum">Total</td>
                    <td class="rnum" style="border-right: none;"></td>
                    <td class="rnum" style="border-left: none;">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['MTLPRICE'])}}</td>
                </tr>
                <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td class="rnum">Discount</td>
                    {% if value['resultset_value']['discount'][0] is defined %}
                    <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['discount'][0]['discrate'])}}%</td>
                    {% else %}
                    <td></td>
                    {% endif %}
                    <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</td>
                </tr>
                <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td class="rnum">Net Amount</td>
                    <td class="rnum" style="border-right: none;"></td>
                    <td class="rnum" style="border-left: none;">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VAL2'])}}</td>
                </tr>
            </tbody>
        </table>
        <table style="width: 100%">
            <tbody>
                <br>
                <br>
                <tr>
                    <td class="snum">{{(value['resultset_value']['USR01']['username'])}}</td>
                    <td class="snum"></td>
                    <td class="snum"></td>
                    <td class="snum"></td>
                </tr>
                <tr>
                    <td class="ltop">Prepared By</td>
                    <td class="ltop">Checked By</td>
                    <td class="ltop">Delivery By</td>
                    <td class="ltop">Received By</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>""",
    "fonepay":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,tr,th,td{
                font-size: 11px;
                font-family: calibri;
                text-align: left;
            }
            .preinv{
                font-size: 11px;
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
            div.table_items {
                height: 200px !important;
                border: 1px solid #ccc;
            }
            .theight{
                height: 275px;
            }
            .heading{
                font-size: 15px;
                line-height: 0px;
                text-align: left;
                margin-top: 0%;
                padding-top: 0%;
            }
            .collapse_table{
                border-collapse: collapse;
                width: 100%;
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
            .desc{
                padding-right: 150px;
            }
            .prin{
                page-break-before: always;
            }
        </style>
    </head>
    <body>
    {% if value['resultset_value']['prncnt'] == 0 %}
        <div class="preinv">
            <table style="width: 100%; border-bottom: 1px solid black;">
                <tbody>
                    <tr>
                        <td>
                            <img class="imag" src="http://103.146.234.44:8080/img/NGMlogo1.jpg">
                        </td>
                        <td class="heading">
                            <h2 class="snum">Tax Invoice</h2>
                            <h2>{{value['resultset_value']['CO010']['coname']}}</h2>
                            <p>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</p>
                            <p>VAT No. :<span style="margin-left: 3mm;"></span><b>{{value['resultset_value']['CO010']['covatno']}}</b></p>
                            <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OU010']['unitname']}}</b></p> 
                        </td>
                        <td class="tright">
                            <br><br><br>
                            <p>Mode of Payment: Fonepay Bill</p>
                            {% if 'OD10' in value['resultset_value'] %}
                                <p>Phone No:{{value['resultset_value']['OD10']['phoneno']}}</p>
                            {% else %}
                                <p>Phone No:{{value['resultset_value']['CO010']['phoneno']}}</p>
                            {% endif %}
                        </td>
                    </tr>
                </tbody>
            </table>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td>Buyer's Name</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custname']}}</td>
                    </tr>
                    <tr>
                        <td>Address</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custaddress']}}</td>
                    </tr>
                    <tr>
                        <td>Phone No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['phoneno']}}</td>
                    </tr>
                    <tr>
                        <td>Buyer's VAT No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['vatno']}}</td>  
                    </tr>
                </tbody>
            </table>
            <table class="tright">
                <tbody>
                    <tr>
                        <td>Invoice No.</td>
                        <td>:</td>
                        <td><b>{{value['resultset_value']['sinvno']}}</b></td>
                    </tr>
                    <tr>
                        <td>Invoice Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['sinvdate']}}</td>
                    </tr>
                    <tr>
                        <td>BS Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docbs']}}</td>
                    </tr>
                    <tr>
                        <td>Transaction Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docdt']}}</td>  
                    </tr>
                    <tr>
                        <td>Print Date & Time</td>
                        <td>:</td>
                        <td>{{ value['printdate'].strftime('%d/%m/%Y') }} {{ value['printdate'].strftime('%H:%M:%S') }}</td>
                    </tr>
                </tbody>
            </table>
            <div class="theight">
                <table class="collapse_table">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th>H.S.Code</th>
                        <th>Code</th>
                        <th class="desc">Description</th>
                        <th class="rnum">Qty</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                    {% set nctr = -1 %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                        {% set nctr = nctr+1 %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                {% if 'MM001' in value['resultset_value']['lineitems'][nctr]['myvalues'] %}
                                    <td class="num">{{i['myvalues']['MM001']['hsncode']}}</td>
                                {% else %}
                                    <td></td>
                                {% endif %}
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                    </tbody>
                </table>
            </div>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td class="num">Amount in Words:</td>                        <td>{{value['numtoword'].num2words(value['resultset_value']['popricingtotal']['VAL2']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</td> 
                    </tr>
                    <tr>
                    <td class="num">Remarks:</td>
                    <td>{{value['resultset_value']['remarks']}}</td>
                    </tr>
                    <tr>
                    <td>Fonepay No:{{value['resultset_value']['fonepayno']}}</td>
                    <td class="snum">RRN:{{value['resultset_value']['rrn']}}<span style="margin-left: 2mm;"></td>
                    <td class="rnum">Amount:{{value['resultset_value']['fpamt']}}<span style="margin-left: 2mm;"></td>
                    </tr>
                    <tr>
                        <td style="text-align: center;">{{(value['resultset_value']['USR01']['username'])}}</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td class="ltop" style="text-align: center;">Prepared By</td>
                        <td class="ltop" style="text-align: right;">Receiver's Signature</td>
                    </tr>
                </tbody>
            </table>
            <table class="tright" style="border-collapse: collapse;">
                <tbody>
                    <tr>
                        <td class="rnum"><b>Total</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['MTLPRICE']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Discount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        {% if value['resultset_value']['discount'][0] is defined %}
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['discount'][0]['discrate'])}}%</td>
                        {% else %}
                        <td></td>
                        {% endif %}
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Taxable Amount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['VAL1']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Add:VAT</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VATPER'])}}%</td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{value['resultset_value']['popricingtotal']['VAT']}}</td> 
                    </tr>
                    <tr>
                        <td class="rnum"><b>Net Amount</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;">{{value['resultset_value']['popricingtotal']['VAL2']}}</td>
                    </tr>
                </tbody>
            </table>
            <div>
                <br><br><br><br><br><br><br>                
                <p class="tleft">E & OE<br>Goods once sold are not exchangeable or returnable</p>
                <p class="tright"><b>For  {{value['resultset_value']['CO010']['coname']}}</b></p>
            </div>  
        </div>
        <div class="preinv prin">
            <table style="width: 100%; border-bottom: 1px solid black;">
                <tbody>
                    <tr>
                        <td>
                            <img class="imag" src="http://103.146.234.44:8080/img/NGMlogo1.jpg">
                        </td>
                        <td class="heading">
                            <h2 class="snum">Invoice</h2>
                            <h2>{{value['resultset_value']['CO010']['coname']}}</h2>
                            <p>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</p>
                            <p>VAT No. :<span style="margin-left: 3mm;"></span><b>{{value['resultset_value']['CO010']['covatno']}}</b></p>
                            <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OU010']['unitname']}}</b></p> 
                        </td>
                        <td class="tright">
                            <br><br><br>
                            <p>Mode of Payment: Fonepay Bill</p>
                            {% if 'OD10' in value['resultset_value'] %}
                                <p>Phone No:{{value['resultset_value']['OD10']['phoneno']}}</p>
                            {% else %}
                                <p>Phone No:{{value['resultset_value']['CO010']['phoneno']}}</p>
                            {% endif %}
                        </td>
                    </tr>
                </tbody>
            </table>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td>Buyer's Name</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custname']}}</td>
                    </tr>
                    <tr>
                        <td>Address</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custaddress']}}</td>
                    </tr>
                    <tr>
                        <td>Phone No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['phoneno']}}</td>
                    </tr>
                    <tr>
                        <td>Buyer's VAT No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['vatno']}}</td>  
                    </tr>
                </tbody>
            </table>
            <table class="tright">
                <tbody>
                    <tr>
                        <td>Invoice No.</td>
                        <td>:</td>
                        <td><b>{{value['resultset_value']['sinvno']}}</b></td>
                    </tr>
                    <tr>
                        <td>Invoice Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['sinvdate']}}</td>
                    </tr>
                    <tr>
                        <td>BS Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docbs']}}</td>
                    </tr>
                    <tr>
                        <td>Transaction Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docdt']}}</td>  
                    </tr>
                    <tr>
                        <td>Print Date & Time</td>
                        <td>:</td>
                        <td>{{ value['printdate'].strftime('%d/%m/%Y') }} {{ value['printdate'].strftime('%H:%M:%S') }}</td>
                    </tr>
                </tbody>
            </table>
            <div class="theight">
                <table class="collapse_table">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th>H.S.Code</th>
                        <th>Code</th>
                        <th class="desc">Description</th>
                        <th class="rnum">Qty</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                    {% set nctr = -1 %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                        {% set nctr = nctr+1 %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                {% if 'MM001' in value['resultset_value']['lineitems'][nctr]['myvalues'] %}
                                    <td class="num">{{i['myvalues']['MM001']['hsncode']}}</td>
                                {% else %}
                                    <td></td>
                                {% endif %}
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                    </tbody>
                </table>
            </div>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td class="num">Amount in Words:</td>
                        <td>{{value['numtoword'].num2words(value['resultset_value']['popricingtotal']['VAL2']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</td> 
                    </tr>
                    <tr>
                    <td class="num">Remarks:</td>
                    <td>{{value['resultset_value']['remarks']}}</td>
                    </tr>
                    <tr>
                    <td>Fonepay No:{{value['resultset_value']['fonepayno']}}</td>
                    <td class="snum">RRN:{{value['resultset_value']['rrn']}}<span style="margin-left: 2mm;"></td>
                    <td class="rnum">Amount:{{value['resultset_value']['fpamt']}}<span style="margin-left: 2mm;"></td>
                    </tr>
                    <tr>
                        <td style="text-align: center;">{{(value['resultset_value']['USR01']['username'])}}</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td class="ltop" style="text-align: center;">Prepared By</td>
                        <td class="ltop" style="text-align: right;">Receiver's Signature</td>
                    </tr>
                </tbody>
            </table>
            <table class="tright" style="border-collapse: collapse;">
                <tbody>
                    <tr>
                        <td class="rnum"><b>Total</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['MTLPRICE']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Discount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        {% if value['resultset_value']['discount'][0] is defined %}
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['discount'][0]['discrate'])}}%</td>
                        {% else %}
                        <td></td>
                        {% endif %}
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Taxable Amount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['VAL1']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Add:VAT</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VATPER'])}}%</td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{value['resultset_value']['popricingtotal']['VAT']}}</td> 
                    </tr>
                    <tr>
                        <td class="rnum"><b>Net Amount</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;">{{value['resultset_value']['popricingtotal']['VAL2']}}</td>
                    </tr>
                </tbody>
            </table>
            <div>
                <br><br><br><br><br><br><br>                
                <p class="tleft">E & OE<br>Goods once sold are not exchangeable or returnable</p>
                <p class="tright"><b>For  {{value['resultset_value']['CO010']['coname']}}</b></p>
            </div>
        </div>
        {% else %}
        <div class="preinv">
            <table style="width: 100%; border-bottom: 1px solid black;">
                <tbody>
                    <tr>
                        <td>
                            <img class="imag" src="http://103.146.234.44:8080/img/NGMlogo1.jpg">
                        </td>
                        <td class="heading">
                            {% if value['resultset_value']['status'] != 'C' %}
                                <h2 class="rnum">Invoice - DRAFT</h2>
                            {% elif 'prncnt' in value['resultset_value'] %}
                                {% if value['resultset_value']['prncnt'] <= 0 %}
                                     <h2 class="rnum">Tax Invoice</h2>
                                {% else %}
                                    <h2 class="rnum">Invoice (COPY OF ORIGINAL :  {{value['resultset_value']['prncnt']}} )</h2>
                                {% endif %}
                            {% endif %}
                            <h2>{{value['resultset_value']['CO010']['coname']}}</h2>
                            <p>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</p>
                            <p>VAT No. :<span style="margin-left: 3mm;"></span><b>{{value['resultset_value']['CO010']['covatno']}}</b></p>
                            <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OU010']['unitname']}}</b></p> 
                        </td>
                        <td class="tright">
                            <br><br><br>
                            <p>Mode of Payment: Fonepay Bill</p>
                            {% if 'OD10' in value['resultset_value'] %}
                                <p>Phone No:{{value['resultset_value']['OD10']['phoneno']}}</p>
                            {% else %}
                                <p>Phone No:{{value['resultset_value']['CO010']['phoneno']}}</p>
                            {% endif %}
                        </td>
                    </tr>
                </tbody>
            </table>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td>Buyer's Name</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custname']}}</td>
                    </tr>
                    <tr>
                        <td>Address</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custaddress']}}</td>
                    </tr>
                    <tr>
                        <td>Phone No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['phoneno']}}</td>
                    </tr>
                    <tr>
                        <td>Buyer's VAT No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['vatno']}}</td>  
                    </tr>
                </tbody>
            </table>
            <table class="tright">
                <tbody>
                    <tr>
                        <td>Invoice No.</td>
                        <td>:</td>
                        <td><b>{{value['resultset_value']['sinvno']}}</b></td>
                    </tr>
                    <tr>
                        <td>Invoice Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['sinvdate']}}</td>
                    </tr>
                    <tr>
                        <td>BS Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docbs']}}</td>
                    </tr>
                    <tr>
                        <td>Transaction Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docdt']}}</td>  
                    </tr>
                    <tr>
                        <td>Print Date & Time</td>
                        <td>:</td>
                        <td>{{ value['printdate'].strftime('%d/%m/%Y') }} {{ value['printdate'].strftime('%H:%M:%S') }}</td>
                    </tr>
                </tbody>
            </table>
            <div class="theight">
                <table class="collapse_table">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th>H.S.Code</th>
                        <th>Code</th>
                        <th class="desc">Description</th>
                        <th class="rnum">Qty</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                    {% set nctr = -1 %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                        {% set nctr = nctr+1 %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                {% if 'MM001' in value['resultset_value']['lineitems'][nctr]['myvalues'] %}
                                    <td class="num">{{i['myvalues']['MM001']['hsncode']}}</td>
                                {% else %}
                                    <td></td>
                                {% endif %}
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                    </tbody>
                </table>
            </div>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td class="num">Amount in Words:</td>                        <td>{{value['numtoword'].num2words(value['resultset_value']['popricingtotal']['VAL2']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</td> 
                    </tr>
                    <tr>
                    <td class="num">Remarks:</td>
                    <td>{{value['resultset_value']['remarks']}}</td>
                    </tr>
                    <tr>
                    <td>Fonepay No:{{value['resultset_value']['fonepayno']}}</td>
                    <td class="snum">RRN:{{value['resultset_value']['rrn']}}<span style="margin-left: 2mm;"></td>
                    <td class="rnum">Amount:{{value['resultset_value']['fpamt']}}<span style="margin-left: 2mm;"></td>
                    </tr>
                    <tr>
                        <td style="text-align: center;">{{(value['resultset_value']['USR01']['username'])}}</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td class="ltop" style="text-align: center;">Prepared By</td>
                        <td class="ltop" style="text-align: right;">Receiver's Signature</td>
                    </tr>
                </tbody>
            </table>
            <table class="tright" style="border-collapse: collapse;">
                <tbody>
                    <tr>
                        <td class="rnum"><b>Total</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['MTLPRICE']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Discount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        {% if value['resultset_value']['discount'][0] is defined %}
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['discount'][0]['discrate'])}}%</td>
                        {% else %}
                        <td></td>
                        {% endif %}
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Taxable Amount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['VAL1']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Add:VAT</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VATPER'])}}%</td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{value['resultset_value']['popricingtotal']['VAT']}}</td> 
                    </tr>
                    <tr>
                        <td class="rnum"><b>Net Amount</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;">{{value['resultset_value']['popricingtotal']['VAL2']}}</td>
                    </tr>
                </tbody>
            </table>
            <div>
                <br><br><br><br><br><br><br>                
                <p class="tleft">E & OE<br>Goods once sold are not exchangeable or returnable</p>
                <p class="tright"><b>For  {{value['resultset_value']['CO010']['coname']}}</b></p>
            </div> 
        </div>
        {% endif %}
    </body>
</html>""",
    "sfonepay":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,tr,th,td{
                font-size: 11px;
                font-family: calibri;
                text-align: left;
            }
            .preinv{
                font-size: 11px;
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
            div.table_items {
                height: 200px !important;
                border: 1px solid #ccc;
            }
            .theight{
                height: 275px;
            }
            .heading{
                font-size: 15px;
                line-height: 0px;
                text-align: left;
                margin-top: 0%;
                padding-top: 0%;
            }
            .collapse_table{
                border-collapse: collapse;
                width: 100%;
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
            .desc{
                padding-right: 150px;
            }
            .prin{
                page-break-before: always;
            }
        </style>
    </head>
    <body>
    {% if value['resultset_value']['prncnt'] == 0 %}
        <div class="preinv">
            <table style="width: 100%; border-bottom: 1px solid black;">
                <tbody>
                    <tr>
                        <td>
                            <img class="imag" src="http://103.146.234.44:8080/img/NGMlogo1.jpg">
                        </td>
                        <td class="heading">
                            <h2 class="snum">Tax Invoice</h2>}
                            <h2>{{value['resultset_value']['CO010']['coname']}}</h2>
                            <p><span style="margin-left: 3mm;"></span>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</p>
                            <p>VAT No. :<span style="margin-left: 3mm;"></span><b>{{value['resultset_value']['CO010']['covatno']}}</b></p>
                            <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OU010']['unitname']}}</b></p> 
                        </td>
                        <td class="tright">
                            <br><br><br>
                            <p>Mode of Payment: Fonepay Bill</p>
                            {% if 'OD10' in value['resultset_value'] %}
                                <p>Phone No:{{value['resultset_value']['OD10']['phoneno']}}</p>
                            {% else %}
                                <p>Phone No:{{value['resultset_value']['CO010']['phoneno']}}</p>
                            {% endif %}
                        </td>
                    </tr>
                </tbody>
            </table>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td>Buyer's Name</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custname']}}</td>
                    </tr>
                    <tr>
                        <td>Address</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custaddress']}}</td>
                    </tr>
                    <tr>
                        <td>Phone No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['phoneno']}}</td>
                    </tr>
                    <tr>
                        <td>Buyer's VAT No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['vatno']}}</td>  
                    </tr>
                </tbody>
            </table>
            <table class="tright">
                <tbody>
                    <tr>
                        <td>Invoice No.</td>
                        <td>:</td>
                        <td><b>{{value['resultset_value']['sinvno']}}</b></td>
                    </tr>
                    <tr>
                        <td>Invoice Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['sinvdate']}}</td>
                    </tr>
                    <tr>
                        <td>BS Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docbs']}}</td>
                    </tr>
                    <tr>
                        <td>Transaction Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docdt']}}</td>  
                    </tr>
                    <tr>
                        <td>Print Date & Time</td>
                        <td>:</td>
                        <td>{{ value['printdate'].strftime('%d/%m/%Y') }} {{ value['printdate'].strftime('%H:%M:%S') }}</td>
                    </tr>
                </tbody>
            </table>
            {% if value['resultset_value']['lineitems']|length <11 %}
            <div class="theight">
                <table class="collapse_table">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th>H.S.Code</th>
                        <th>Code</th>
                        <th class="desc">Descriptionnn</th>
                        <th class="rnum">Qty</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                    {% if (value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none) and (value['resultset_value']['svitems'][0]['itemcodeobj'] is not none) %}
                    {% set nctr = -1 %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                        {% set nctr = nctr+1 %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                {% if 'MM001' in value['resultset_value']['lineitems'][nctr]['myvalues'] %}
                                    <td class="num">{{i['myvalues']['MM001']['hsncode']}}</td>
                                {% else %}
                                    <td></td>
                                {% endif %}
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                        {%- for i in value['resultset_value']['svitems'] %}
                        <tr>
                           {% if value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                            <td class="snum">{{loop.index + (value['resultset_value']['lineitems']|length)}}</td>
							{% else %}
								<td class="snum">{{loop.index0 + (value['resultset_value']['lineitems']|length)}}</td>
							{% endif %}
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}
                        {% elif value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                        {% elif value['resultset_value']['svitems'][0]['itemcodeobj'] is not none %}
                        {%- for i in value['resultset_value']['svitems'] %}
                        <tr>
                           {% if value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                            <td class="snum">{{loop.index + (value['resultset_value']['lineitems']|length)}}</td>
							{% else %}
								<td class="snum">{{loop.index0 + (value['resultset_value']['lineitems']|length)}}</td>
							{% endif %}
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}
                        {% endif %}
                    </tbody>
                </table>
            </div>
            {% else %} 
            <div class="theight1">
                <table class="collapse_table">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th>Code</th>
                        <th class="desc">Description</th>
                        <th class="rnum">Qty</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                        {% if (value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none) and (value['resultset_value']['svitems'][0]['itemcodeobj'] is not none) %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                        {%- for i in value['resultset_value']['svitems'] %}
                        <tr>
                           {% if value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                            <td class="snum">{{loop.index + (value['resultset_value']['lineitems']|length)}}</td>
							{% else %}
								<td class="snum">{{loop.index0 + (value['resultset_value']['lineitems']|length)}}</td>
							{% endif %}
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}
                        {% elif value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                        {% elif value['resultset_value']['svitems'][0]['itemcodeobj'] is not none %}
                        {%- for i in value['resultset_value']['svitems'] %}
                        <tr>
                           {% if value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                            <td class="snum">{{loop.index + (value['resultset_value']['lineitems']|length)}}</td>
							{% else %}
								<td class="snum">{{loop.index0 + (value['resultset_value']['lineitems']|length)}}</td>
							{% endif %}
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}
                        {% endif %}
                    </tbody>
                </table>
            </div>
            {% endif %}
            <table class="tleft">
                <tbody>
                    <tr>
                        <td class="num">Amount in Words:</td>
                        <td>{{value['numtoword'].num2words(value['resultset_value']['popricingtotal']['VAL2']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</td> 
                    </tr>
                    <tr>
                    <td class="num">Remarks:</td>
                    <td>{{value['resultset_value']['remarks']}}</td>
                    </tr>
                    <tr>
                    <td>Fonepay No:{{value['resultset_value']['fonepayno']}}</td>
                    <td class="snum">RRN:{{value['resultset_value']['rrn']}}<span style="margin-left: 3mm;"></td>
                    <td class="rnum">Amount:{{value['resultset_value']['fpamt']}}<span style="margin-left: 3mm;"></td>
                    </tr>
                    <tr>
                        <td style="text-align: center;">{{(value['resultset_value']['USR01']['username'])}}</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td class="ltop" style="text-align: center;">Prepared By</td>
                        <td class="ltop" style="text-align: right;">Receiver's Signature</td>
                    </tr>
                </tbody>
            </table>
            <table class="tright" style="border-collapse: collapse;">
                <tbody>
                    <tr>
                        <td class="rnum"><b>Total</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['MTLPRICE']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Discount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        {% if value['resultset_value']['discount'][0] is defined %}
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['discount'][0]['discrate'])}}%</td>
                        {% else %}
                        <td></td>
                        {% endif %}
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Taxable Amount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['VAL1']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Add:VAT</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VATPER'])}}%</td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{value['resultset_value']['popricingtotal']['VAT']}}</td> 
                    </tr>
                    <tr>
                        <td class="rnum"><b>Net Amount</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;">{{value['resultset_value']['popricingtotal']['VAL2']}}</td>
                    </tr>
                </tbody>
            </table>
            <div>
                <br><br><br><br><br><br>
                <p class="tright"><b>For  {{value['resultset_value']['CO010']['coname']}}</b></p>
                <p class="tleft">E & OE<br>Goods once sold are not exchangeable or returnable</p>
            </div> 
        </div>
        <div class="preinv prin">
            <table style="width: 100%; border-bottom: 1px solid black;">
                <tbody>
                    <tr>
                        <td>
                            <img class="imag" src="http://103.146.234.44:8080/img/NGMlogo1.jpg">
                        </td>
                        <td class="heading">
                            <h2 class="snum">Invoice</h2>
                            <h2>{{value['resultset_value']['CO010']['coname']}}</h2>
                            <p><span style="margin-left: 3mm;"></span>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</p>
                            <p>VAT No. :<span style="margin-left: 3mm;"></span><b>{{value['resultset_value']['CO010']['covatno']}}</b></p>
                            <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OU010']['unitname']}}</b></p> 
                        </td>
                        <td class="tright">
                            <br><br><br>
                            <p>Mode of Payment: Fonepay Bill</p>
                            {% if 'OD10' in value['resultset_value'] %}
                                <p>Phone No:{{value['resultset_value']['OD10']['phoneno']}}</p>
                            {% else %}
                                <p>Phone No:{{value['resultset_value']['CO010']['phoneno']}}</p>
                            {% endif %}
                        </td>
                    </tr>
                </tbody>
            </table>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td>Buyer's Name</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custname']}}</td>
                    </tr>
                    <tr>
                        <td>Address</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custaddress']}}</td>
                    </tr>
                    <tr>
                        <td>Phone No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['phoneno']}}</td>
                    </tr>
                    <tr>
                        <td>Buyer's VAT No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['vatno']}}</td>  
                    </tr>
                </tbody>
            </table>
            <table class="tright">
                <tbody>
                    <tr>
                        <td>Invoice No.</td>
                        <td>:</td>
                        <td><b>{{value['resultset_value']['sinvno']}}</b></td>
                    </tr>
                    <tr>
                        <td>Invoice Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['sinvdate']}}</td>
                    </tr>
                    <tr>
                        <td>BS Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docbs']}}</td>
                    </tr>
                    <tr>
                        <td>Transaction Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docdt']}}</td>  
                    </tr>
                    <tr>
                        <td>Print Date & Time</td>
                        <td>:</td>
                        <td>{{ value['printdate'].strftime('%d/%m/%Y') }} {{ value['printdate'].strftime('%H:%M:%S') }}</td>
                    </tr>
                </tbody>
            </table>
            {% if value['resultset_value']['lineitems']|length <11 %}
            <div class="theight">
                <table class="collapse_table">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th>H.S.Code</th>
                        <th>Code</th>
                        <th class="desc">Descriptionnn</th>
                        <th class="rnum">Qty</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                    {% if (value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none) and (value['resultset_value']['svitems'][0]['itemcodeobj'] is not none) %}
                    {% set nctr = -1 %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                        {% set nctr = nctr+1 %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                {% if 'MM001' in value['resultset_value']['lineitems'][nctr]['myvalues'] %}
                                    <td class="num">{{i['myvalues']['MM001']['hsncode']}}</td>
                                {% else %}
                                    <td></td>
                                {% endif %}
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                        {%- for i in value['resultset_value']['svitems'] %}
                        <tr>
                           {% if value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                            <td class="snum">{{loop.index + (value['resultset_value']['lineitems']|length)}}</td>
							{% else %}
								<td class="snum">{{loop.index0 + (value['resultset_value']['lineitems']|length)}}</td>
							{% endif %}
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}
                        {% elif value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                        {% elif value['resultset_value']['svitems'][0]['itemcodeobj'] is not none %}
                        {%- for i in value['resultset_value']['svitems'] %}
                        <tr>
                           {% if value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                            <td class="snum">{{loop.index + (value['resultset_value']['lineitems']|length)}}</td>
							{% else %}
								<td class="snum">{{loop.index0 + (value['resultset_value']['lineitems']|length)}}</td>
							{% endif %}
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}
                        {% endif %}
                    </tbody>
                </table>
            </div>
            {% else %} 
            <div class="theight1">
                <table class="collapse_table">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th>Code</th>
                        <th class="desc">Description</th>
                        <th class="rnum">Qty</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                        {% if (value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none) and (value['resultset_value']['svitems'][0]['itemcodeobj'] is not none) %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                        {%- for i in value['resultset_value']['svitems'] %}
                        <tr>
                           {% if value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                            <td class="snum">{{loop.index + (value['resultset_value']['lineitems']|length)}}</td>
							{% else %}
								<td class="snum">{{loop.index0 + (value['resultset_value']['lineitems']|length)}}</td>
							{% endif %}
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}
                        {% elif value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                        {% elif value['resultset_value']['svitems'][0]['itemcodeobj'] is not none %}
                        {%- for i in value['resultset_value']['svitems'] %}
                        <tr>
                           {% if value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                            <td class="snum">{{loop.index + (value['resultset_value']['lineitems']|length)}}</td>
							{% else %}
								<td class="snum">{{loop.index0 + (value['resultset_value']['lineitems']|length)}}</td>
							{% endif %}
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}
                        {% endif %}
                    </tbody>
                </table>
            </div>
            {% endif %}
            <table class="tleft">
                <tbody>
                    <tr>
                        <td class="num">Amount in Words:</td>
                        <td>{{value['numtoword'].num2words(value['resultset_value']['popricingtotal']['VAL2']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</td> 
                    </tr>
                    <tr>
                    <td class="num">Remarks:</td>
                    <td>{{value['resultset_value']['remarks']}}</td>
                    </tr>
                    <tr>
                    <td>Fonepay No:{{value['resultset_value']['fonepayno']}}</td>
                    <td class="snum">RRN:{{value['resultset_value']['rrn']}}<span style="margin-left: 3mm;"></td>
                    <td class="rnum">Amount:{{value['resultset_value']['fpamt']}}<span style="margin-left: 3mm;"></td>
                    </tr>
                    <tr>
                        <td style="text-align: center;">{{(value['resultset_value']['USR01']['username'])}}</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td class="ltop" style="text-align: center;">Prepared By</td>
                        <td class="ltop" style="text-align: right;">Receiver's Signature</td>
                    </tr>
                </tbody>
            </table>
            <table class="tright" style="border-collapse: collapse;">
                <tbody>
                    <tr>
                        <td class="rnum"><b>Total</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['MTLPRICE']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Discount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        {% if value['resultset_value']['discount'][0] is defined %}
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['discount'][0]['discrate'])}}%</td>
                        {% else %}
                        <td></td>
                        {% endif %}
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Taxable Amount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['VAL1']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Add:VAT</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VATPER'])}}%</td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{value['resultset_value']['popricingtotal']['VAT']}}</td> 
                    </tr>
                    <tr>
                        <td class="rnum"><b>Net Amount</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;">{{value['resultset_value']['popricingtotal']['VAL2']}}</td>
                    </tr>
                </tbody>
            </table>
            <div>
                <br><br><br><br><br><br>
                <p class="tright"><b>For  {{value['resultset_value']['CO010']['coname']}}</b></p>
                <p class="tleft">E & OE<br>Goods once sold are not exchangeable or returnable</p>
            </div> 
        </div>
        {% else %}
        <div class="preinv">
            <table style="width: 100%; border-bottom: 1px solid black;">
                <tbody>
                    <tr>
                        <td>
                            <img class="imag" src="http://103.146.234.44:8080/img/NGMlogo1.jpg">
                        </td>
                        <td class="heading">
                             {% if value['resultset_value']['status'] != 'C' %}
                                <h2 class="snum">Invoice - DRAFT</h2>
                            {% elif 'prncnt' in value['resultset_value'] %}
                                {% if value['resultset_value']['prncnt'] <= 0 %}
                                     <h2 class="snum">Tax Invoice</h2>
                                {% else %}
                                    <h2 class="snum">Invoice (COPY OF ORIGINAL :  {{value['resultset_value']['prncnt']}} )</h2>
                                {% endif %}
                            {% endif %}
                            <h2>{{value['resultset_value']['CO010']['coname']}}</h2>
                            <p><span style="margin-left: 3mm;"></span>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</p>
                            <p>VAT No. :<span style="margin-left: 3mm;"></span><b>{{value['resultset_value']['CO010']['covatno']}}</b></p>
                            <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OU010']['unitname']}}</b></p> 
                        </td>
                        <td class="tright">
                            <br><br><br>
                            <p>Mode of Payment: Fonepay Bill</p>
                            {% if 'OD10' in value['resultset_value'] %}
                                <p>Phone No:{{value['resultset_value']['OD10']['phoneno']}}</p>
                            {% else %}
                                <p>Phone No:{{value['resultset_value']['CO010']['phoneno']}}</p>
                            {% endif %}
                        </td>
                    </tr>
                </tbody>
            </table>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td>Buyer's Name</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custname']}}</td>
                    </tr>
                    <tr>
                        <td>Address</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custaddress']}}</td>
                    </tr>
                    <tr>
                        <td>Phone No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['phoneno']}}</td>
                    </tr>
                    <tr>
                        <td>Buyer's VAT No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['vatno']}}</td>  
                    </tr>
                </tbody>
            </table>
            <table class="tright">
                <tbody>
                    <tr>
                        <td>Invoice No.</td>
                        <td>:</td>
                        <td><b>{{value['resultset_value']['sinvno']}}</b></td>
                    </tr>
                    <tr>
                        <td>Invoice Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['sinvdate']}}</td>
                    </tr>
                    <tr>
                        <td>BS Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docbs']}}</td>
                    </tr>
                    <tr>
                        <td>Transaction Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docdt']}}</td>  
                    </tr>
                    <tr>
                        <td>Print Date & Time</td>
                        <td>:</td>
                        <td>{{ value['printdate'].strftime('%d/%m/%Y') }} {{ value['printdate'].strftime('%H:%M:%S') }}</td>
                    </tr>
                </tbody>
            </table>
            {% if value['resultset_value']['lineitems']|length <11 %}
            <div class="theight">
                <table class="collapse_table">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th>H.S.Code</th>
                        <th>Code</th>
                        <th class="desc">Descriptionnn</th>
                        <th class="rnum">Qty</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                    {% if (value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none) and (value['resultset_value']['svitems'][0]['itemcodeobj'] is not none) %}
                    {% set nctr = -1 %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                        {% set nctr = nctr+1 %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                {% if 'MM001' in value['resultset_value']['lineitems'][nctr]['myvalues'] %}
                                    <td class="num">{{i['myvalues']['MM001']['hsncode']}}</td>
                                {% else %}
                                    <td></td>
                                {% endif %}
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                        {%- for i in value['resultset_value']['svitems'] %}
                        <tr>
                           {% if value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                            <td class="snum">{{loop.index + (value['resultset_value']['lineitems']|length)}}</td>
							{% else %}
								<td class="snum">{{loop.index0 + (value['resultset_value']['lineitems']|length)}}</td>
							{% endif %}
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}
                        {% elif value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                        {% elif value['resultset_value']['svitems'][0]['itemcodeobj'] is not none %}
                        {%- for i in value['resultset_value']['svitems'] %}
                        <tr>
                           {% if value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                            <td class="snum">{{loop.index + (value['resultset_value']['lineitems']|length)}}</td>
							{% else %}
								<td class="snum">{{loop.index0 + (value['resultset_value']['lineitems']|length)}}</td>
							{% endif %}
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}
                        {% endif %}
                    </tbody>
                </table>
            </div>
            {% else %} 
            <div class="theight1">
                <table class="collapse_table">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th>Code</th>
                        <th class="desc">Description</th>
                        <th class="rnum">Qty</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                        {% if (value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none) and (value['resultset_value']['svitems'][0]['itemcodeobj'] is not none) %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                        {%- for i in value['resultset_value']['svitems'] %}
                        <tr>
                           {% if value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                            <td class="snum">{{loop.index + (value['resultset_value']['lineitems']|length)}}</td>
							{% else %}
								<td class="snum">{{loop.index0 + (value['resultset_value']['lineitems']|length)}}</td>
							{% endif %}
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}
                        {% elif value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                        {% elif value['resultset_value']['svitems'][0]['itemcodeobj'] is not none %}
                        {%- for i in value['resultset_value']['svitems'] %}
                        <tr>
                           {% if value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                            <td class="snum">{{loop.index + (value['resultset_value']['lineitems']|length)}}</td>
							{% else %}
								<td class="snum">{{loop.index0 + (value['resultset_value']['lineitems']|length)}}</td>
							{% endif %}
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}
                        {% endif %}
                    </tbody>
                </table>
            </div>
            {% endif %}
            <table class="tleft">
                <tbody>
                    <tr>
                        <td class="num">Amount in Words:</td>
                        <td>{{value['numtoword'].num2words(value['resultset_value']['popricingtotal']['VAL2']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</td> 
                    </tr>
                    <tr>
                    <td class="num">Remarks:</td>
                    <td>{{value['resultset_value']['remarks']}}</td>
                    </tr>
                    <tr>
                    <td>Fonepay No:{{value['resultset_value']['fonepayno']}}</td>
                    <td class="snum">RRN:{{value['resultset_value']['rrn']}}<span style="margin-left: 3mm;"></td>
                    <td class="rnum">Amount:{{value['resultset_value']['fpamt']}}<span style="margin-left: 3mm;"></td>
                    </tr>
                    <tr>
                        <td style="text-align: center;">{{(value['resultset_value']['USR01']['username'])}}</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td class="ltop" style="text-align: center;">Prepared By</td>
                        <td class="ltop" style="text-align: right;">Receiver's Signature</td>
                    </tr>
                </tbody>
            </table>
            <table class="tright" style="border-collapse: collapse;">
                <tbody>
                    <tr>
                        <td class="rnum"><b>Total</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['MTLPRICE']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Discount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        {% if value['resultset_value']['discount'][0] is defined %}
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['discount'][0]['discrate'])}}%</td>
                        {% else %}
                        <td></td>
                        {% endif %}
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Taxable Amount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['VAL1']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Add:VAT</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VATPER'])}}%</td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{value['resultset_value']['popricingtotal']['VAT']}}</td> 
                    </tr>
                    <tr>
                        <td class="rnum"><b>Net Amount</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;">{{value['resultset_value']['popricingtotal']['VAL2']}}</td>
                    </tr>
                </tbody>
            </table>
            <div>
                <br><br><br><br><br><br>
                <p class="tright"><b>For  {{value['resultset_value']['CO010']['coname']}}</b></p>
                <p class="tleft">E & OE<br>Goods once sold are not exchangeable or returnable</p>
            </div> 
        </div>
        {% endif %}
    </body>
</html>""",
    "del_order":"""<!DOCTYPE html>
<html>
    <head>    
        <style>
            table,tr,th,td{
                font-size: 15px;
                font-family: calibri;
                text-align: right;
            }
            .preinv{
                font-size: 16px;
                font-family: calibri;
            }
            .tabl{
                border: 1px solid black;
                border-right: none;
                border-left: none;         
            }
            .collapse_table{
                border-collapse: collapse;
            }
            .num{
                text-align: left;
            }
            .snum{
                text-align: center;
            }
            .foot{
                margin-top: 100%;
                border-top: 1px solid black;
                text-align: right;
            }
        </style>
    </head>
    <body>
        <div class="preinv">
            <table style="width: 100%;">
                    <h2 class="snum" style="font-size: 25px;">{{value['resultset_value']['CO010']['coname']}}</h2>
                <tr>
                    <td class="num" style="width: 200px;">
                        <p>DO No.:{{value['resultset_value']['docno']}}</p>
                        <p>BS Date:</p>
                        {% if 'custidobj' in value['resultset_value'] %}                        
                        <p>Order From: {{value['resultset_value']['custid']}}-{{value['resultset_value']['custidobj']['key2']}}</p>
                        {% else %} 
                        <p>Order From: {{value['resultset_value']['tunitid']}}-{{value['resultset_value']['tunitidobj']['key2']}}</p>
                        {% endif %}
                    </td>
                    <td class="snum" style="font-size: 17px;">
                        {% if 'OD10' in value['resultset_value'] %}
                            <p>Phone No:{{value['resultset_value']['OD10']['phoneno']}}</p>
                        {% else %}
                            <p>Phone No:{{value['resultset_value']['CO010']['phoneno']}}</p>
                        {% endif %}
                        <p><b><u>PRE INVOICE APPROVAL FOR WAREHOUSE</u></b></p>
                    </td>               
                    <td>
                        <p>Print Date:{{ value['printdate'].strftime('%d/%m/%Y')}}</p>
                        <p>Print Time:{{ value['printdate'].strftime('%H:%M:%S')}}</p>
                    <td>
                </tr>
            </table>
        </div>
        <div>
            <table style="width: 100%;" class="collapse_table">
                <thead class="tabl">
                    <th class="snum">S.N</th>
                    <th class="num">Part No</th>
                    <th class="num">Part Name</th>
                    <th class="num">Sloc.</th>
                    <th class="num">Bin</th>
                    <th class="num">Lot</th>
                    <th>CB</th>
                    <th>Alloted Qty</th>
                </thead>
				{%- for i in value['resultset_value']['lineitems'] %}	
                    <tr>
                        <td class="snum">{{loop.index}}</td>
                        <td class="num">{{i['itemcode']}}</td>
                        <td class="num">{{i['mtlname']}}</td>
                        <td class="num">{{i['slocid']}}</td>
                        <td class="num">{{i['binid']}}</td>
                        <td class="num">{{i['lotno']}}</td>
                        <td>{{i['cb']}}</td>
                        <td>{{\"%.2f\"|format(i['qty'])}}</td>
                    </tr>
                {% endfor -%}
                <tr>
                    <td></td>
                    <td></td>
                    <td class="num"><B>TOTAL</B></td>
                    <td></td>
                    <td><B></B></td>
                </tr>
            </table>
        </div>
    </body>
</html>""",
    "quotation":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,tr,th,td{
                font-size: 13px;
                font-family: calibri;
                text-align: left;
            }
            .preinv{
                font-size: 14px;
                font-family: calibri;
                width: 100%;
                line-height: 5px;
            }
            .heading{
                font-size: 18px;
                line-height: 0px;
                width: 100%;
                text-align: center;
            }
            .tabl{
                border: 1px solid black;
                border-right: none;
                border-left: none;
            }
            .collapse_table{
                border-collapse: collapse;
                width: 100%;
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
            .fheight{
                height: 100%
                border-top: 1px solid black;
                text-align: left;
                font-size: 13px;
                width: 100%;
            }
            .foot{
                margin-top: 100%;
                border-top: 1px solid black;
                text-align: left;
                font-size: 13px;
                width: 100%;
            }
        </style>
    </head>
    <body>   
        <table class="preinv">
            <tbody>
                <tr>
                    <td style="width: 200px">
                        <p>Quotation No: {{value['resultset_value']['docno']}}</p>
                        <p>Miti: 2080/03/12</p>
                        <p>Customer Name: {{value['resultset_value']['custname']}}</p>
                        <p>Bike No: {{value['resultset_value']['regno']}}</p>
                        <p>Phone No: {{value['resultset_value']['phoneno']}}</p>
                    </td>
                    <td class="snum">
                        <h4 class="heading">{{value['resultset_value']['CO010']['coname']}}</h4> 
                        {% if value['resultset_value']['OD10'] is not none %}
                        {% if value['resultset_value']['OD10']['unitidobj'] is not none %}
                            <h4>{{value['resultset_value']['OD10']['unitidobj']['key2']}}</h4>
                        {% endif %}
                        {% else %} 
                            <h4>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</h4>
                        {% endif %}
                        <p>Phone No. {{value['resultset_value']['CO010']['phoneno']}}</p>
                        <h4><u>QUOTATION</u></h4>
                    </td>
                    <td class="rnum">
                        <p>Print Date: {{ value['printdate'].strftime('%d/%m/%Y') }}</p>
                        <p>Print Time: {{ value['printdate'].strftime('%H:%M:%S') }}</p>
                    </td>
                </tr>
            </tbody>
        </table>
        <table class="collapse_table">
            <thead class="tabl">
                <th class="snum">S.N.</th>
                <th>Part No</th>
                <th>Part Name</th>
                <th class="rnum">Quantity</th>
                <th class="rnum">Rate</th>
                <th class="rnum">Amount</th>
            </thead>
            <tbody>
                {%- for i in value['resultset_value']['lineitems'] %}                                 
                    <tr>
                        <td class="snum">{{loop.index}}</td>
                        <td>{{i['itemcode']}}</td>
                        <td>{{i['itemcodeobj']['key2']}}</td>
                        <td class="rnum">{{i.reqqty}}</td>
                        <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                        <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                    </tr>
                {% endfor -%}
                <tr><td><br></td></tr>
                <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td class="rnum">Total</td>
                    <td class="rnum" style="border-right: none;"></td>
                    <td class="rnum" style="border-left: none;">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['MTLPRICE'])}}</td>
                </tr>
                <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td class="rnum">Discount</td>
                    <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNTPERC'])}}%</td>
                    <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</td>
                </tr>     
                <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td class="rnum">Taxable Amount</td>
                    <td class="rnum" style="border-right: none;"></td>
                    <td class="rnum" style="border-left: none;">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VAL1'])}}</td>
                </tr>
                <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td class="rnum">VAT</td>
                    <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VATPER'])}}%</td>
                    <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VAT'])}}</td>
                </tr>
                <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td class="rnum">Net Amount</td>
                    <td class="rnum" style="border-right: none;"></td>
                    <td class="rnum" style="border-left: none;">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VAL2'])}}</td>
                </tr>
            </tbody>
        </table>
        <table class="foot">
            <tbody>
                <td> Note: All the above product rates are subject to change withour prior notice.</td>
                <td class="rnum">1</td>
            </tbody>
        </table>
    </body>
</html>""",
    "quotation7":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,tr,th,td{
                font-size: 13px;
                font-family: calibri;
                text-align: left;
            }
            .preinv{
                font-size: 14px;
                font-family: calibri;
                width: 100%;
                line-height: 5px;
            }
            .heading{
                font-size: 18px;
                line-height: 0px;
                width: 100%;
                text-align: center;
            }
            .tabl{
                border: 1px solid black;
                border-right: none;
                border-left: none;
            }
            /*.tablbor{
                border: 1px solid black;
                text-align: right;
                padding-right: 10px;
            }*/
            .collapse_table{
                border-collapse: collapse;
                width: 100%;
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
            .foot{
                margin-top: 100%;
                border-top: 1px solid black;
                text-align: left;
                font-size: 13px;
                width: 100%;
            }
        </style>
    </head>
    <body>   
        <table class="preinv">
            <thead>
                <tr>
                    <td style="width: 33%">
                        <p>Quotation No: {{value['resultset_value']['docno']}}</p>
                        <p>Miti: 2080/03/12</p>
                        <p>Customer Name: {{value['resultset_value']['CM010']['custname']}}</p>
                        <p>Bike No: {{value['resultset_value']['CM010']['regno']}}</p>
                        <p>Phone No: {{value['resultset_value']['OD10']['phoneno']}}</p>
                    </td>
                    <td class="snum"> 
                        <h4 class="heading">{{value['resultset_value']['CO010']['coname']}}</h4>                    
                        <h4>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</h4>
                        <p>Phone No. {{value['resultset_value']['CO010']['phoneno']}}</p>
                        <h4><u>QUOTATION</u></h4>
                    </td>
                    <td class="rnum">
                        <p>Print Date: {{ value['printdate'].strftime('%d/%m/%Y') }}</p>
                        <p>Print Time: {{ value['printdate'].strftime('%H:%M:%S') }}</p>
                    </td>
                </tr>
            </thead>
        </table>
        
        <table class="collapse_table">
            <thead class="tabl">
                <th class="snum">S.N.</th>
                <th>Part No</th>
                <th>Part Name</th>
                <th class="rnum">Quantity</th>
                <th class="rnum">Rate</th>
                <th class="rnum">Amount</th>
            </thead>
            <tbody>
                {%- for i in value['resultset_value']['lineitems'] %}                                 
                    <tr>
                        <td class="snum">{{i['rpsno']}}</td>
                        <td>{{i['itemcode']}}</td>
                        <td>{{i['itemcodeobj']['key2']}}</td>
                        <td class="rnum">{{i.reqqty}}</td>
                        <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                        <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                    </tr>
                {% endfor -%}
                <tr><td><br></td></tr>
               {%- if value['resultset_value']['lineitems'][0]['eof'] %}
                <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td class="rnum">Total</td>
                    <td class="rnum" style="border-right: none;"></td>
                    <td class="rnum" style="border-left: none;">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['MTLPRICE'])}}</td>
                </tr>
                <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td class="rnum">Discount</td>
                    <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNTPERC'])}}%</td>
                    <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</td>
                </tr>     
                <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td class="rnum">Taxable Amount</td>
                    <td class="rnum" style="border-right: none;"></td>
                    <td class="rnum" style="border-left: none;">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VAL1'])}}</td>
                </tr>
                <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td class="rnum">VAT</td>
                    <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VATPER'])}}%</td>
                    <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VAT'])}}</td>
                </tr>
                <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td class="rnum">Net Amount</td>
                    <td class="rnum" style="border-right: none;"></td>
                    <td class="rnum" style="border-left: none;">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VAL2'])}}</td>
                </tr>
                {%- endif %}
            </tbody>
        </table>
        <table class="foot">
            <tbody>
                <td> Note: All the above product rates are subject to change withour prior notice.</td>
                <td class="rnum">1</td>
            </tbody>
        </table>
    </body>
</html>""",
    "mrq":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,tr,th,td{
                font-size: 13px;
                font-family: calibri;
                text-align: left;
            }
            .preinv{
                font-size: 14px;
                font-family: calibri;
                width: 100%;
                line-height: 5px;
            }
            .heading{
                font-size: 18px;
                line-height: 0px;
                width: 100%;
                text-align: center;
            }
            .tabl{
                border: 1px solid black;
                border-right: none;
                border-left: none;
            }
            .collapse_table{
                border-collapse: collapse;
                width: 100%;
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
            .foot{
                margin-top: 100%;
                border-top: 1px solid black;
                text-align: left;
                font-size: 13px;
                width: 100%;
            }
        </style>
    </head>
    <body>   
        <table class="preinv">
            <tbody>
                <tr>
                    <td style="width: 200px">
                        <p>Quotation No: {{value['resultset_value']['docno']}}</p>
                        <p>Miti: 2080/03/12</p>
                        <p>Customer Name: {{value['resultset_value']['OD10']['unitidobj']}}</p>
                        <p>Bike No: {{value['resultset_value']['regno']}}</p>
                        <p>Phone No: {{value['resultset_value']['phoneno']}}</p>
                    </td>
                    <td class="snum"> 
                        <h4 class="heading">{{value['resultset_value']['CO010']['coname']}}</h4>                    
                        <h4>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</h4>
                        <p>Phone No. {{value['resultset_value']['CO010']['phoneno']}}</p>
                        <h4><u>QUOTATION</u></h4>
                    </td>
                    <td class="rnum">
                        <p>Print Date: {{ value['printdate'].strftime('%d/%m/%Y') }}</p>
                        <p>Print Time: {{ value['printdate'].strftime('%H:%M:%S') }}</p>
                    </td>
                </tr>
            </tbody>
        </table>
        <table class="collapse_table">
            <thead class="tabl">
                <th class="snum">S.N.</th>
                <th>Part No</th>
                <th>Part Name</th>
                <th class="rnum">Quantity</th>
                <th class="rnum">Alloted</th>
                <th class="rnum">Back Order</th>
                <th class="rnum">Rate</th>
                <th class="rnum">Amount</th>
                <th class="rnum">Order No.</th>
            </thead>
            <tbody>
                {%- for i in value['resultset_value']['lineitems'] %}                                 
                    <tr>
                        <td class="snum">{{loop.index}}</td>
                        <td>{{i['itemcode']}}</td>
                        <td>{{i['itemcodeobj']['key2']}}</td>
                        <td class="rnum">{{i.reqqty}}</td>
                        <td class="rnum">{{i.qty}}</td>
                        <td>{{i.psoqty}}</td>
                        <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                        <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        <td>{{i['orderno']}}</td>
                    </tr>
                {% endfor -%}
                <tr><td><br></td></tr>
                <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td class="rnum">Total</td>
                    <td class="rnum" style="border-right: none;"></td>
                    <td class="rnum" style="border-left: none;">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['MTLPRICE'])}}</td>
                </tr>
                <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td class="rnum">Discount</td>
                    <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNTPERC'])}}%</td>
                    <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</td>
                </tr>     
                <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td class="rnum">Taxable Amount</td>
                    <td class="rnum" style="border-right: none;"></td>
                    <td class="rnum" style="border-left: none;">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VAL1'])}}</td>
                </tr>
                <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td class="rnum">VAT</td>
                    <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VATPER'])}}%</td>
                    <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VAT'])}}</td>
                </tr>
                <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td class="rnum">Net Amount</td>
                    <td class="rnum" style="border-right: none;"></td>
                    <td class="rnum" style="border-left: none;">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VAL2'])}}</td>
                </tr>
            </tbody>
        </table>
        <table class="foot">
            <tbody>
                <td> Note: All the above product rates are subject to change withour prior notice.</td>
                <td class="rnum">1</td>
            </tbody>
        </table>
    </body>
</html>""",
    "intdc":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,tr,th,td{
                font-size: 13px;
                font-family: calibri;
                text-align: left;
            }
            .preinv{
                font-size: 14px;
                font-family: calibri;
                width: 100%;
                line-height: 5px;
            }
            .heading{
                font-size: 23px;
                line-height: 0px;
                width: 100%;
                text-align: center;
            }
            .imag{
                width: 70px;
                height: 85px;
            }
            .tabl{
                border: 1px solid black;
                border-right: none;
                border-left: none;
            }
            .collapse_table{
                border-collapse: collapse;
                width: 100%;
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
                text-align: center;
            }
            .foot{
                margin-top: 100%;
                border-top: 1px solid black;
                text-align: left;
                font-size: 13px;
                width: 100%;
            }
        </style>
    </head>
    <body>   
        <table class="preinv">
            <tbody>
                <tr>
                    <td style="width: 200px">
                        <img class="imag" src="http://103.146.234.44:8080/img/NGMlogo1.jpg">
                        <p>Challan No: {{value['resultset_value']['docno']}}</p>
                        <p>BS Date: {{value['resultset_value']['docbs']}}</p>
                    </td>
                    <td class="snum"> 
                        <h4 class="heading">{{value['resultset_value']['CO010']['coname']}}</h4> 
                        {% if 'OD10' in value['resultset_value'] %}
                        <h4>{{value['resultset_value']['OD10']['address'][0]['postbox']}}</h4>
                        {% else %}
                        <h4>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</h4>
                        {% endif %}
                        {% if 'OD10' in value['resultset_value'] %}
                            <p>Phone No:{{value['resultset_value']['OD10']['phoneno']}}</p>
                        {% else %}
                            <p>Phone No:{{value['resultset_value']['CO010']['phoneno']}}</p>
                        {% endif %}
                        <p>VAT No. {{value['resultset_value']['CO010']['covatno']}}</p>
                        <h4><u>SALES CHALLAN</u></h4>
                    </td>
                    <td class="rnum">
                        <p>Print Date: {{value['printdate'].strftime('%d/%m/%Y')}}</p>
                        <p>Print Time: {{value['printdate'].strftime('%H:%M:%S')}}</p>
                    </td>
                </tr>
            </tbody>
        </table>
        <table style="width:100%">
            <tbody>
                <tr>
                    <td><u>To: {{value['resultset_value']['TOD10']['unitidobj']['key2']}}</u></td>
                    <td>Customer VAT No:</td>
                </tr>
            </tbody>
        </table>
        <table class="collapse_table">
            <thead class="tabl">
                <th class="snum">S.N.</th>
                <th>Part No</th>
                <th style="width:300px">Part Name</th>
                <th class="rnum">Quantity</th>
                <th></th>
                <th class="rnum">Rate</th>
                <th class="rnum">Amount</th>
            </thead>
            <tbody>
                {%- for i in value['resultset_value']['lineitems'] %}                                 
                    <tr>
                        <td class="snum">{{loop.index}}</td>
                        <li class="{{ loop.cycle('itemcode') }}"></li>
                        <td>{{i['itemcode']}}</td>
                        <td>{{i['itemcodeobj']['key2']}}</td>
                        <td class="rnum">{{i.qty}}</td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                        <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                    </tr>
                {% endfor -%}
                <tr><td><br></td></tr>
                <tr>
                    <td></td>
                    <td>{{value['numtoword'].num2words(value['resultset_value']['popricingtotal']['VAL2']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</td>
                    <td></td>
                    <td class="rnum">Total</td>
                    <td class="rnum" style="border-right: none;"></td>
                    <td class="rnum" style="border-left: none;">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['MTLPRICE'])}}</td>
                </tr>
                <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td class="rnum">Discount</td>
                    {% if value['resultset_value']['discount'][0] is defined %}
                    <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['discount'][0]['discrate'])}}%</td>
                    {% else %}
                    <td></td>
                    {% endif %}
                    <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</td>
                </tr>
                <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td class="rnum">Net Amount</td>
                    <td class="rnum" style="border-right: none;"></td>
                    <td class="rnum" style="border-left: none;">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VAL2'])}}</td>
                </tr>
            </tbody>
        </table>
        <table style="width: 100%">
            <tbody>
                <br>
                <br>
                <tr>
                    <td class="snum">{{(value['resultset_value']['USR01']['username'])}}</td>
                    <td class="snum"></td>
                    <td class="snum"></td>
                    <td class="snum"></td>
                </tr>
                <tr>
                    <td class="ltop">Prepared By</td>
                    <td class="ltop">Checked By</td>
                    <td class="ltop">Delivery By</td>
                    <td class="ltop">Received By</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>""",
    "dc":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,tr,th,td{
                font-size: 15px;
                font-family: calibri;
                text-align: left;
            }
            .preinv{
                font-size: 16px;
                font-family: calibri;
                width: 100%;
            }
            .heading{
                font-size: 18px;
                line-height: 0px;
                width: 100%;
                padding-left: 0%;
                text-align: center;
                margin-top: 0%;
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
            .collapse_table{
                border-collapse: collapse;
                margin-top: 100px;
                width: 100%;
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
            .foot{
                margin-top: 100%;
                border-top: 1px solid black;
                text-align: right;
                font-size: 11px;
            }
            .theight1{
                height: 480px;
            }
            .sign{
                text-align: center;
                font-size: 18px;
                border-top: 1px solid black;;
            }
            .container {
                position: relative;
                max-width: 800px;
                margin: 0 auto;
            }
            .container img {vertical-align: middle;}
            .container .content {
                position: absolute;
                bottom: 0;
                background: rgb(0, 0, 0); /* Fallback color */
                background: rgba(0, 0, 0, 0.5); /* Black background with 0.5 opacity */
                color: #f1f1f1;
                width: 100%;
                padding: 20px;
            }          
        </style>
    </head>
    <body>
        <table class="preinv">
            <tr>
                <td>
                    <img class="imag" src="http://103.146.234.44:8080/img/NGMlogo1.jpg">
                </td>
                <td class="heading">
                    <h2>{{value['resultset_value']['CO010']['coname']}}</h2>
                    {% if 'OD10' in value['resultset_value'] %}
                    <h5>{{value['resultset_value']['OD10']['odname']}}</h5>
                    {% else %}
                    <h5>{{value['resultset_value']['OU010']['unitname']}}</h5>
                    {% endif %}
                    <h5>Phone No. {{value['resultset_value']['CO010']['phoneno']}}</h5>
                    <h2>VAT No. {{value['resultset_value']['CO010']['covatno']}}</h2>
                    {% if 'OD10' in value['resultset_value'] %}
                    <h4>{{value['resultset_value']['OD10']['odname']}}</h4>
                    {% else %}
                    <h4>{{value['resultset_value']['OU010']['unitname']}}</h4>
                    {% endif %}
                    <h2>Delivery Challan</h2>
                </td>
            </tr>
        </table>
        <hr>
        <table class="tleft">
            <tr>
                <td><b>Buyer's Name</b></td>
                <td>:</td>
                <td>{{value['resultset_value']['tunitid']}} - {{value['resultset_value']['tunitidobj']['key2']}}</td>
            </tr>
            <tr><td><b>Address</b></td>
                <td>:</td>
                <td>{{value['resultset_value']['TOD10']['address'][0]['postbox']}}</td>
            </tr>
            <tr>
                <td><b>Phone No.</b></td>
                <td>:</td>
                <td>{{value['resultset_value']['TOD10']['phoneno']}}</td>
            </tr>
            <tr>
                <td><b>Buyer's VAT No.</b></td>
                <td>:</td>
                <td>{{value['resultset_value']['CO010']['covatno']}}</td>  
            </tr>
        </table>
        <table class="tright">
            <tr>
                <td><b>Delivery Challan No.</b></td>
                <td>:</td>
                <td><b>{{value['resultset_value']['docno']}}</b></td>
            </tr>
            <tr>
                <td><b>Bill Issue Date</b></td>
                <td>:</td>
                <td>{{value['resultset_value']['sinvdate']}}</td>
            </tr>
            <tr>
                <td><b>BS Date</b> </td>
                <td>:</td>
                <td>{{value['resultset_value']['docbs']}}</td>
            </tr>
            <tr>
                <td><b>Transaction Date</b></td>
                <td>:</td>
                <td>{{value['resultset_value']['docdt']}}</td>  
            </tr>
        </table>
        <div class="theight1">
        <table class="collapse_table">
            <thead class="tabl">
                <th>S.N.</th>
                <th>Code</th>
                <th class="desc">Description</th>
                <th class="rnum">Qty</th>
                <th class="rnum">Rate</th>
                <th class="rnum">Amount</th>
            </thead>
            <tbody>
		        {% if value['resultset_value']['bunit'] == 'BIKE' %}
                    {%  set nctr1 = -1 %}
                    {%- for i in value['resultset_value']['lineitems'] %}
                            {% set nctr1 = nctr1 +1 %}
                            <tr>
                                <td>{{loop.index}}</td>
                                <td>{{i['itemcode']}}</td>
                                <td class="desc"><b>Model<span style="margin-left: 6mm;"></span>:</b><span style="margin-left: 3mm;"></span></b>{{i['itemcodeobj']['key2']}}<br><b>Reg No<span style="margin-left: 6mm;"></span>:</b><span style="margin-left: 3mm;"></span></b>{{value['resultset_value']['scannedItems'][loop.index-1]['regno']}}<br><b>Chasis Noo<span style="margin-left: 6mm;"></span>:</b><span style="margin-left: 3mm;"></span></b>{{value['resultset_value']['scannedItems'][loop.index-1]['chasisno']}}<br><b>Motor No<span style="margin-left: 6mm;"></span>:</b><span style="margin-left: 3mm;"></span></b>{{value['resultset_value']['scannedItems'][loop.index-1]['motorno']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                    {%  endfor -%}
                {% else %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                        <tr>
                            <td>{{loop.index}}</td>
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}  
                    {% endif %}                    
               </tbody>
            </table>
            </div>
            <table class="fcont" style="float: right; text-align: left; border-collapse: collapse;">
                <tr class="foot">
                    <td><b>Sub Total</b></td>
                    <td></td>
                    <td class="snum">{{value['resultset_value']['popricingtotal']['MTLPRICE']}}</td>
                </tr>
                <tr>
                    <td>Discount</td>
                    {% if value['resultset_value']['discount'][0] is defined %}
                    <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['discount'][0]['discrate'])}}%</td>
                    {% else %}
                    <td></td>
                    {% endif %}
                    <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</td>
                </tr>
                <tr>
                    <td>Total Amount</td>
                    <td></td>
                    <td class="snum">{{value['resultset_value']['popricingtotal']['VAL1']}}</td>
                </tr>
                <tr class="tabl">
                    <td><b>Total</b></td>
                    <td></td>
                    <td class="snum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VAL2'])}}</td>
                </tr>
            </table>
            <table class="fcont" style="float: left; text-align: left;">
                <tr>
                    <td><b>Mode Of Payment:</b></td>
                </tr>
                <tr>
                    <td><b>Bank Name:</b></td>
                </tr>
                <tr>
                    <td><b>Destination:</b></td>
                </tr>
                <tr>
                    <td><b>LC No.:</b></td>
                </tr>
                <tr>
                    <td><b>D/O No.:</b></td>
                </tr>
            </table>
            <table class="fcont" style="float: left; text-align: left;">
                {%- for i in value['resultset_value']['payment'] %}
                    <tr>
                        <td>{{i['paytype']}}</td>
                    </tr>
                    <tr>
                        <td>{{i['bankname']}}</td>
                    </tr>
                    <tr>
                        <td></td>
                    </tr>
                    <tr>
                        <td>{{i['pdocnumber']}}</td>  
                    </tr>
                {% endfor -%}
            </table>
            <table class="fcont" style="float: left; text-align: left;">
                <br><br><br><br><br>
                <tr>
                    <td></td>
                    <td><b>D/O Date/Miti:</b></td>
                </tr>
            </table>
            <table class="fcont" style="float: left; text-align: left;">
                {%- for i in value['resultset_value']['payment'] %}
                    <td><b></b></td>
                {% endfor -%}
            </table>
            <br>
            <div class="preinv">
                <p class="tabl"><b>Amount in Words:</b>  {{value['numtoword'].num2words(value['resultset_value']['popricingtotal']['VAL2']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</p>
                <p style="line-height:0px; font-size:15px;">Print Date and Time: {{value['printdate'].strftime('%d/%m/%Y')}}  {{value['printdate'].strftime('%H:%M:%S')}}</p>
            </div>
        <table style="width: 100%;">
            <tr>
                <td></td>
                <td class="snum">{{(value['resultset_value']['USR01']['username'])}}</td>
                <td></td>
            </tr>
            <tr>
                <td style="text-decoration: overline;">Receiver's Signature</td>
                <td class="snum" style="text-decoration: overline; width: 30%">Prepared By</td>
                <td style="text-decoration: overline;">Authorized Signature</td>
            </tr>
            <tr>
            <td><br></td>
            </tr>
            <tr>
                <td></td>
                <td></td>
                <td class="rnum" style="font-size: 15px;">For {{value['resultset_value']['CO010']['coname']}}</td>
            </tr>
        </table>
    </body>
</html>""",
    "dcsr":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,tr,th,td{
                font-size: 13px;
                font-family: calibri;
                text-align: left;
            }
            .preinv{
                font-size: 14px;
                font-family: calibri;
                width: 100%;
                line-height: 5px;
            }
            .heading{
                font-size: 23px;
                line-height: 0px;
                width: 100%;
                text-align: center;
            }
            .imag{
                width: 70px;
                height: 85px;
            }
            .tabl{
                border: 1px solid black;
                border-right: none;
                border-left: none;
            }
            .collapse_table{
                border-collapse: collapse;
                width: 100%;
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
                text-align: center;
            }
            .foot{
                margin-top: 100%;
                border-top: 1px solid black;
                text-align: left;
                font-size: 13px;
                width: 100%;
            }
        </style>
    </head>
    <body>   
        <table class="preinv">
            <tbody>
                <tr>
                    <td style="width: 225px">
                        <img class="imag" src="http://103.146.234.44:8080/img/NGMlogo1.jpg">
                        <p>Challan No: {{value['resultset_value']['docno']}}</p>
                        <p>BS Date: {{value['resultset_value']['docbs']}}</p>
                    </td>
                    <td class="snum"> 
                        <h4 class="heading">{{value['resultset_value']['CO010']['coname']}}</h4> 
                        {% if 'OD10' in value['resultset_value'] %}
                        <h4>{{value['resultset_value']['OD10']['address'][0]['postbox']}}</h4>
                        {% else %}
                        <h4>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</h4>
                        {% endif %}
                        {% if 'OD10' in value['resultset_value'] %}
                            <p>Phone No:{{value['resultset_value']['OD10']['phoneno']}}</p>
                        {% else %}
                            <p>Phone No:{{value['resultset_value']['CO010']['phoneno']}}</p>
                        {% endif %}
                        <p>VAT No. {{value['resultset_value']['CO010']['covatno']}}</p>
                        <h4><u>SALES CHALLAN</u></h4>
                    </td>
                    <td class="rnum">
                        <p>Print Date: {{value['printdate'].strftime('%d/%m/%Y')}}</p>
                        <p>Print Time: {{value['printdate'].strftime('%H:%M:%S')}}</p>
                    </td>
                </tr>
            </tbody>
        </table>
        <table style="width:100%">
            <tbody>
                <tr>
                    <td><u>To: {{value['resultset_value']['TOD10']['unitidobj']['key2']}}</u></td>
                    <td>Customer VAT No:</td>
                </tr>
            </tbody>
        </table>
        <table class="collapse_table">
            <thead class="tabl">
                <th class="snum">S.N.</th>
                <th>Part No</th>
                <th>Part Name</th>
                <th class="rnum">Quantity</th>
                <th class="rnum">Rate</th>
                <th class="rnum">Amount</th>
                <th class="rnum">Lotno</th>
            </thead>
            <tbody>
                {%- for i in value['resultset_value']['lineitems'] %}                                 
                    <tr>
                        <td class="snum">{{loop.index}}</td>
                        <li class="{{ loop.cycle('itemcode') }}"></li>
                        <td>{{i['itemcode']}}</td>
                        <td>{{i['itemcodeobj']['key2']}}</td>
                        <td class="rnum">{{i.qty}}</td>
                        <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                        <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        {% if ['flotno'] in value['resultset_value']['lineitems'] %}
                            <td class="rnum">{{i.flotno}}</td>
                        {% else %}
                            <td></td>
                        {% endif %}
                    </tr>
                {% endfor -%}
                <tr><td><br></td></tr>
                <tr>
                    <td></td>
                    <td>{{value['numtoword'].num2words(value['resultset_value']['popricingtotal']['VAL2']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</td>
                    <td></td>
                    <td class="rnum">Total</td>
                    <td class="rnum" style="border-right: none;"></td>
                    <td class="rnum" style="border-left: none;">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['MTLPRICE'])}}</td>
                </tr>
                <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td class="rnum">Discount</td>
                    {% if value['resultset_value']['discount'][0] is defined %}
                    <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['discount'][0]['discrate'])}}%</td>
                    {% else %}
                    <td></td>
                    {% endif %}
                    <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</td>
                </tr>
                <tr>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td class="rnum">Net Amount</td>
                    <td class="rnum" style="border-right: none;"></td>
                    <td class="rnum" style="border-left: none;">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VAL2'])}}</td>
                </tr>
            </tbody>
        </table>
        <table style="width: 100%">
            <tbody>
                <br>
                <br>
                <tr>
                    <td class="snum">{{(value['resultset_value']['USR01']['username'])}}</td>
                    <td class="snum"></td>
                    <td class="snum"></td>
                    <td class="snum"></td>
                </tr>
                <tr>
                    <td class="ltop">Prepared By</td>
                    <td class="ltop">Checked By</td>
                    <td class="ltop">Delivery By</td>
                    <td class="ltop">Received By</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>""",
    "dscfd":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,tr,th,td{
                font-size: 12px;
                font-family: calibri;
                text-align: left;
            }
            .preinv{
                font-size: 11px;
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
            div.table_items {
                height: 200px !important;
                border: 1px solid #ccc;
            }
            .theight{
                height: 275px;
            }
            .heading{
                font-size: 15px;
                line-height: 0px;
                text-align: left;
                margin-top: 0%;
                padding-top: 0%;
            }
            .collapse_table{
                border-collapse: collapse;
                width: 100%;
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
            .desc{
                padding-right: 150px;
            }
            .he{
                background-color: black;
                color: white;
            }
        </style>
    </head>
    <body>
        <div class="preinv">
            <table  style="width: 100%;">
                <tbody>
                <tr>
                    <td><img class="imag" src="http://103.146.234.44:8080/img/NGMlogo1.jpg"></td>
                    <td class="heading">
                        <h2 class="snum">CENTRAL FINANCE DIVSION</h2>
                        <h2 class="snum">{{(value['resultset_value']['CO010']['coaddress2'])}}</h2>
                        <p class="snum">Depositor Copy</p>
                    </td>
                    <td class="rnum">
                        <br><br><br>
                        <h2><b><u>Cheque/Draft Deposit Slip</u></b></h2>
                        <p>###: </p>
                        <p>Date:{{value['resultset_value']['dsdate']}}</p>
                    </td>
                </tr>
                <tr><td>{{(value['resultset_value']['dsno'])}}</td></tr>
                </tbody>
            </table>
            <table class="tleft"  style="width:50%;">
                <tbody>
                    <tr>
                        <td>
                            Account Holder's Name (##############):
                        </td>
                    </tr>
                    <tr>
                        <td>HI KATHMANDU DIPO</td>
                    </tr>
                    <tr><td>Account Number (#############):{{(value['resultset_value']['accno'])}}</td></tr>
                    <tr><td>Amount (in Figures)(###########):{{(value['resultset_value']['custid'])}}</td></tr>
                    <tr><td>Amount (In Words)(##############):</td></tr>
                    <tr><td>Details(############):{{(value['resultset_value']['narr'])}}</td></tr>
                </tbody>
            </table>
            <table class="tright">
                <tbody>
                    <tr>
                        <td>Chq/Draft/T.Chq.No.</td>
                        <td><u>______________</u></td>
                    </tr>
                    <tr>
                        <td>Date</td>
                        <td><u>{{value['resultset_value']['dsdate']}}</u></td>
                    </tr>
                    <tr>
                        <td>Drawn on</td>
                        <td><u>______________</u></td>
                    </tr>
                    <tr>
                        <td>Branch</td>
                        <td><u>______________</u></td>
                    </tr>
                    <tr>
                        <td colspan="2" class="snum">Separate Slip for each Cheque/Draft ##########</td>
                    </tr>
                    <tr><td colspan="2" class="snum">For Teller Use Only</td></tr>
                    <tr><td>Bank:</td></tr>
                    <tr><td>Bank account No.:</td></tr>
                    <tr><td>Deposited By:</td></tr>
                </tbody>
            </table>
            <table style="width: 100%;">
                <tr>
                    <td></td>
                    <td class="rnum">{{(value['resultset_value']['USR01']['username'])}}</td>
                    <td></td>
                </tr>
                <tr>
                    <td class="num" style="text-decoration: overline;">Depositer</td>
                    <td class="rnum" style="text-decoration: overline; width: 30%">Prepared By</td>
                    <td class="rnum" style="text-decoration: overline;">Deposited By</td>
                </tr>
                <tr><br><br></tr>
            </table>
            <table style="width: 100%;">
                <tr><td></td></tr>
                <tr><td></td></tr>
                <tr><td></td></tr>
                <tr><td></td></tr>
                <tr>
                    <td class="num">In-charge</td>
                    <td class="rnum" style="width: 30%">Teller</td>
                    <td class="rnum">Transaction No.</td>
                </tr>
                <tr>
                    <td></td>
                    <td style="width: 30%"></td>
                    <td class="rnum" style="text-decoration: overline;">##################</td>
                </tr> 
            </table>
            <p class="snum">Not Valid Without Transaction No. Must be returned if obtaining monet receipt. Vod after money receipt issued.</p>
            <p class="snum">################################# ##########################################    ###############################</p>
        </div>
    </body>
</html>""",
    "pscfd":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,tr,th,td{
                font-size: 12px;
                font-family: calibri;
                text-align: left;
            }
            .preinv{
                font-size: 11px;
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
            div.table_items {
                height: 200px !important;
                border: 1px solid #ccc;
            }
            .theight{
                height: 275px;
            }
            .heading{
                font-size: 15px;
                line-height: 0px;
                text-align: left;
                margin-top: 0%;
                padding-top: 0%;
            }
            .collapse_table{
                border-collapse: collapse;
                width: 100%;
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
            .desc{
                padding-right: 150px;
            }
            .he{
                background-color: black;
                color: white;
            }
            .hr{
                border: none;
                border-top: 1px dotted black;
                color: #fff;
                background-color: #fff;
                height: 1px;
                width: 50%;
            }
        </style>
    </head>
    <body>
        <div class="preinv">
            <table  style="width: 100%;">
                <tbody>
                <tr>
                    <td class="num">C.No.</td>
                    <td class="heading">
                        <p class="snum">Pay Slip</p>
                    </td>
                    <td class="rnum">Account No.</td>
                    <td></td>
                </tr>
                </tbody>
            </table>
            <table class="tleft">
               <tbody>
                    <tr>
                        <td>P.No. </td>
                    </tr>
                    <tr>
                        <td></td>
                    </tr>
               </tbody> 
            </table>
            <table class="tright">
                <tbody>
                    <tr>
                        <td>{{value['resultset_value']['docdt']}}</td>
                    </tr>
                    <tr>
                        <td>Date: {{value['resultset_value']['docbs']}}</td>
                    </tr>
                    <tr>
                        <td>{{ value['printdate'].strftime('%d/%m/%Y') }} {{ value['printdate'].strftime('%H:%M:%S') }}</td>
                    </tr>
                </tbody> 
             </table>
            <p><u></u>in the calculation</p>
            <p>Mister.<u></u>to</p>
            <p>rupees {{value['numtoword'].num2words(value['resultset_value']['popricingtotal']['VAL2']*1.00, 
                lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</p>
            <br>
            <p>Please pay in the following ways</p>
            <form>
                <input type="checkbox" id="opt1" name="opt1" value="Bike">
                <label for="opt1">Cash</label>
                <input type="checkbox" id="opt2" name="opt2" value="Bike">
                <label for="opt2"> Berarer Check</label>
                <input type="checkbox" id="opt3" name="opt3" value="Bike">
                <label for="opt3"> Deposit</label>
                <input type="checkbox" id="opt4" name="opt4" value="Bike">
                <label for="opt4"> Bank Advice</label>
                <input type="checkbox" id="opt5" name="opt5" value="Bike">
                <label for="opt5"> A/C Payee Cheque Advice</label>
            </form>
            <table class="tleft"  style="width:50%;">
                <tbody>
                    <tr>
                        <td>
                            Signature of Payee
                        </td>
                    </tr>
                    <tr>
                        <td><u>______________</u></td>
                    </tr>
                </tbody>
            </table>
            <table class="tright">
                <tbody>
                   
                </tbody>
            </table>
            <p>for <hr></p>
            <hr>
            <hr>
            <br>
            <br>
            <table>
                <tbody>
                    <tr>
                        <td></td>
                        <td class="snum"><span style="margin-left: 2mm;"></td>
                        <td class="rnum"><span style="margin-left: 2mm;"></td>
                    </tr>
                    <tr>
                        <td>Accountant</td>
                        <td class="snum">to prepare<span style="margin-left: 2mm;"></td>
                        <td class="rnum">giving orders<span style="margin-left: 2mm;"></td>
                    </tr>
                </tbody>
            </table>
            <table class="tleft"  style="width:50%;">
                <tbody>
                    <tr>
                        <td>
                           Back.<hr>
                        </td>
                    </tr>
                </tbody>
            </table>
            <table class="tright">
                <tbody>
                    <tr>
                        <td>
                           Cheque no.<hr>
                        </td>
                    </tr> 
                </tbody>
            </table>
            <p>After understanding the amount as above, I/we paid it. </p>
            <p>The office company to which the amount is to be paid <hr></p>
            <p>Name of the amount to be paid <hr></p> 
            <p>Full Signatue <hr> <span style="margin-left: 3cm;"></span>Date <hr></p>
        </div>
    </body>
</html>""",
    "binv":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,tr,th,td{
                font-size: 12px;
                font-family: calibri;
                text-align: left;
            }
            .preinv{
                font-size: 16px;
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
            div.table_items {
                height: 200px !important;
                border: 1px solid #ccc;
            }
            .theight{
                height: 200px;
            }
            .heading{
                font-size: 16px;
                line-height: 0px;
                text-align: left;
                margin-top: 0%;
                padding-top: 0%;
            }
            .collapse_table{
                border-collapse: collapse;
                width: 100%;
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
                font-size: 12px;
                text-align: right;
            }
            .desc{
                padding-right: 150px;
            }
            .prin{
                page-break-before: always;
            }
        </style>
    </head>
    <body>
    {% if value['resultset_value']['prncnt'] == 0 %}
        <div class="preinv">
            <table style="width: 100%; border-bottom: 1px solid black;">
                <tbody>
                    <tr>
                        <td>
                            <img class="imag" src="http://103.146.234.44:8080/img/NGMlogo1.jpg">
                        </td>
                        <td class="heading">
                            {% if value['resultset_value']['status'] != 'C' %}
                                <h2 class="snum">Invoice - DRAFT</h2>
                            {% elif 'prncnt' in value['resultset_value'] %}
                                {% if value['resultset_value']['prncnt'] <= 0 %}
                                     <h2 class="rnum">Tax Invoice</h2>
                                {% else %}
                                    <h2 class="rnum">Invoice (COPY OF ORIGINAL :  {{value['resultset_value']['prncnt']}} )</h2>
                                {% endif %}
                            {% endif %}                       
                            <h2>{{value['resultset_value']['CO010']['coname']}}</h2>
                            <p>H/O:<span style="margin-left: 3mm;"></span>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</p>
                            <p>VAT No. :<span style="margin-left: 3mm;"></span><b>{{value['resultset_value']['CO010']['covatno']}}</b></p>
                            <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OU010']['unitname']}}</b></p> 
                            {% if 'OD10' in value['resultset_value'] %}
                                <p>Phone No:{{value['resultset_value']['OD10']['phoneno']}}</p>
                            {% else %}
                                <p>Phone No:{{value['resultset_value']['CO010']['phoneno']}}</p>
                            {% endif %}
                        </td>
                        <td class="tright">
                            <br><br><br>
                            {% if value['resultset_value']['invtype'] == 'CA' %}
                                <p>Mode of Payment: <b>Cash Bill</b></p>
                            {% elif value['resultset_value']['invtype'] == 'FP' %}
                                <p>Mode of Payment: <b>Fonepay Bill</b></p>
                            {% else %}
                                <p>Mode of Payment: <b>CREDIT</b></p>
                            {% endif %}
                        </td>
                    </tr>
                </tbody>
            </table>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td>Buyer's Name</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custname']}}</td>
                    </tr>
                    <tr>
                        <td>Address</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custaddress']}}</td>
                    </tr>
                    <tr>
                        <td>Cell No.</td>
                        <td>:</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Phone No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['phoneno']}}</td>
                    </tr>
                    <tr>
                        <td>C/O</td>
                        <td>:</td>
                        {% if 'careof' in value['resultset_value']%}
                                <td>{{value['resultset_value']['careof']}}</td>
                        {% else 
                                <td></td>                            
                    </tr>
                    <tr>
                        <td>Buyer's PAN No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['vatno']}}</td>  
                    </tr>
                </tbody>
            </table>
            <table class="tright">
                <tbody>
                    <tr>
                        <td>Invoice No.</td>
                        <td>:</td>
                        <td><b>{{value['resultset_value']['sinvno']}}</b></td>
                    </tr>
                    <tr>
                        <td>Date</td>
                        <td>:</td>
                         <td>{{value['resultset_value']['sinvdate']}}</td>
                    </tr>
                    <tr>
                        <td>BS Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docbs']}}</td>
                    </tr>
                    <tr>
                        <td>PP No</td>
                        <td>:</td>
                        <td></td>  
                    </tr>
                    <tr>
                        <td>PP BS Date</td>
                        <td>:</td>
                        <td></td>  
                    </tr>
                    <tr>
                        <td>Print Date & Time</td>
                        <td>:</td>
                        <td>{{ value['printdate'].strftime('%d/%m/%Y') }} {{ value['printdate'].strftime('%H:%M:%S') }}</td>
                    </tr>
                </tbody>
            </table>
            <div>
                <table class="collapse_table" style="width:100%">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th class="num">H.S.Code</th>
                        <th></th>
                        <th class="desc">Description</th>
                        <th class="rnum">Quantity</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                        {%- set nctr = -1 %}
                        {%- for i in value['resultset_value']['scannedItems'] %}
                            {% set nctr = nctr+1 %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                {% if 'MM001' in value['resultset_value']['lineitems'][nctr]['myvalues'] %}
                                    <td class="num"> {{(value['resultset_value']['lineitems'][nctr]['myvalues']['MM001']['hsncode'])}}</td>
                                {% else %}
                                    <td></td>
                                {% endif %}                               
                                <td></td>                                
                                {% if value['motornoobj']['key2']['RegNo'] is not none %}
                                    <td class="desc"><br><b>Model<span style="margin-left: 6mm;"></span>:</b><span style="margin-left: 3mm;"></span>{{(value['resultset_value']['lineitems'][nctr]['myvalues']['MM001']['mtlname'])}}<br><b>Frame No.<span style="margin-left: 1.5mm;">:</b><span style="margin-left: 3mm;"></span>{{i.chasisno}}<br><b>Engine No.<span style="margin-left: 1mm;">:</b><span style="margin-left: 3mm;"></span>{{i.motorno}}<br><b>Colour<span style="margin-left: 6mm;">:</b><span style="margin-left: 3mm;"></span>{{i.colour}}<br><b>RegNo.<span style="margin-left: 5.5mm;">:</b><span style="margin-left: 3mm;"></span>{{i.regno}}<br><b>Ref No.<span style="margin-left: 3mm;">:</b><span style="margin-left: 3mm;"></span>123</td>
                                    <td  class="rnum">{{value['resultset_value']['lineitems'][nctr]['qty']}}</td>
                                    <td  class="rnum">{{value['resultset_value']['lineitems'][nctr]['rate']}}</td>
                                    <td  class="rnum">{{\"%.2f\"|format(value['resultset_value']['lineitems'][nctr]['myvalues']['MTLPRICE'])}}</td>
                                   <br><br>                                    
                                {% else %}
                                    <td>{{i['itemcode']}}</td>
                                {% endif %}   
                            </tr>                                
                        {%- endfor %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                        {% if loop.index > 1 %}
                        <tr><td></td></tr>
                        <tr><td></td></tr>
                            <tr>
                                <td class="snum">{{loop.index0+1}}</td>
                                <td></td>
                                <td></td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i['qty']}}</td>
                                <td class="rnum">{{i['rate']}}</td>
                                <td class="rnum">{{i['myvalues']['MTLPRICE']}}</td>              
                            </tr>
                            {% endif %}
                        {%- endfor %}
                    </tbody>
                </table>
            </div>
            <h4><u>MR/HR Details:</u></h4>
            <table style="width: 100%;">
                <thead>
                    <th class="snum"><u>BS Date</u></th>
                    <th class="snum"><u>Rec No.</u></th>
                    <th class="snum"><u>Amount</u></th>
                    <td class="rnum">Total Amount</td>
                    <td>:</td>
                    <td class="rnum" class="ltop">{{value['resultset_value']['popricingtotal']['MTLPRICE']}}</td>
                </thead>
                <tbody>
                {%- for i in value['resultset_value']['receipts'] %}
                    <tr>
                        <td class="snum">{{value['resultset_value']['docbs']}}</td>
                        <td class="snum">{{i.docno}}</td>
                        <td class="snum">{{i.amount}}</td>
                        <td class="rnum"></td>
                        <td></td>
                        <td></td>
                    </tr>
                {% endfor %}
                    <tr>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum">Discount</td>
                        <td>:</td>
                        <td class="rnum"><u>{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</u></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum">Taxable Amount</td>
                        <td>:</td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VAL1'])}}</td>
                    </tr>
                    <tr>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum">VAT {{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VATPER'])}}%</td>
                        <td>:</td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VAT'])}}</td>
                    </tr>
                    <tr>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum"><b>Bill Amount</b></td>
                        <td><b>:</b></td>
                        <td class="rnum"><b><u>{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VAL2'])}}</u></b></td>
                    </tr>
                </tbody>
            </table>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td>FSC No.</td>
                        <td>:</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Coupon No.</td>
                        <td>:</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Exchanger</td>
                        <td>:</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Exchanger certificate No.</td>
                        <td>:</td>
                        <td></td>  
                    </tr>
                </tbody>
            </table>
            <table style="margin-left: 300px;">
                <tbody>
                    <tr>
                        <td>Agent </td>
                        <td>:</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Coupon Amt</td>
                        <td>:</td>
                        <td></td>  
                    </tr>
                    <tr>
                        <td>Exchange Amt</td>
                        <td>:</td>
                        <td></td>  
                    </tr>
                    <tr>
                        <td>Code</td>
                        <td>:</td>
                        <td></td>
                    </tr>
                </tbody>
            </table>
            <div class="theight" style ="width: 75%; border-bottom:100%">
            <br><br><br><br>
                <p><b>Amount in Words:</b>  {{value['numtoword'].num2words(value['resultset_value']['popricingtotal']['VAL2']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</p>
                <p style="font-size:16px;">Remarks:{{value['resultset_value']['remarks']}}</p>
            </div>
            <div style="line-height:15px">
                <hr style="border: 0.5px solid black;">
                <p class="tleft"><b>Receiver's Signature</b></p>
                <p class="tright"><b>For  {{value['resultset_value']['CO010']['coname']}}</b></p>
                <p class="tleft">E & OE<br>Goods once sold are not exchangeable or returnable<br> In case of two wheeler purchase customer must do the transfer of ownership within 15 days from the bill date.</p>
                <p class="tleft">Prepared By: {{(value['resultset_value']['USR01']['username'])}}</p>
            </div> 
        </div>
        <div class="preinv prin">
            <table style="width: 100%; border-bottom: 1px solid black;">
                <tbody>
                    <tr>
                        <td>
                            <img class="imag" src="http://103.146.234.44:8080/img/NGMlogo1.jpg">
                        </td>
                        <td class="heading">
                            {% if value['resultset_value']['status'] != 'C' %}
                                <h2 class="snum">Invoice - DRAFT</h2>
                            {% elif 'prncnt' in value['resultset_value'] %}
                                {% if value['resultset_value']['prncnt'] <= 0 %}
                                     <h2 class="rnum">Invoice</h2>
                                {% else %}
                                    <h2 class="rnum">Invoice (COPY OF ORIGINAL :  {{value['resultset_value']['prncnt']}} )</h2>
                                {% endif %}
                            {% endif %}                       
                            <h2>{{value['resultset_value']['CO010']['coname']}}</h2>
                            <p>H/O:<span style="margin-left: 3mm;"></span>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</p>
                            <p>VAT No. :<span style="margin-left: 3mm;"></span><b>{{value['resultset_value']['CO010']['covatno']}}</b></p>
                            <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OU010']['unitname']}}</b></p> 
                            {% if 'OD10' in value['resultset_value'] %}
                                <p>Phone No:{{value['resultset_value']['OD10']['phoneno']}}</p>
                            {% else %}
                                <p>Phone No:{{value['resultset_value']['CO010']['phoneno']}}</p>
                            {% endif %}
                        </td>
                        <td class="tright">
                            <br><br><br>
                            {% if value['resultset_value']['invtype'] == 'CA' %}
                                <p>Mode of Payment: <b>Cash Bill</b></p>
                            {% elif value['resultset_value']['invtype'] == 'FP' %}
                                <p>Mode of Payment: <b>Fonepay Bill</b></p>
                            {% else %}
                                <p>Mode of Payment: <b>CREDIT</b></p>
                            {% endif %}
                        </td>
                    </tr>
                </tbody>
            </table>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td>Buyer's Name</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custname']}}</td>
                    </tr>
                    <tr>
                        <td>Address</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custaddress']}}</td>
                    </tr>
                    <tr>
                        <td>Cell No.</td>
                        <td>:</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Phone No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['phoneno']}}</td>
                    </tr>
                    <tr>
                        <td>C/O</td>
                        <td>:</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Buyer's PAN No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['vatno']}}</td>  
                    </tr>
                </tbody>
            </table>
            <table class="tright">
                <tbody>
                    <tr>
                        <td>Invoice No.</td>
                        <td>:</td>
                        <td><b>{{value['resultset_value']['sinvno']}}</b></td>
                    </tr>
                    <tr>
                        <td>Date</td>
                        <td>:</td>
                         <td>{{value['resultset_value']['sinvdate']}}</td>
                    </tr>
                    <tr>
                        <td>BS Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docbs']}}</td>
                    </tr>
                    <tr>
                        <td>PP No</td>
                        <td>:</td>
                        <td></td>  
                    </tr>
                    <tr>
                        <td>PP BS Date</td>
                        <td>:</td>
                        <td></td>  
                    </tr>
                    <tr>
                        <td>Print Date & Time</td>
                        <td>:</td>
                        <td>{{ value['printdate'].strftime('%d/%m/%Y') }} {{ value['printdate'].strftime('%H:%M:%S') }}</td>
                    </tr>
                </tbody>
            </table>
            <div>
                <table class="collapse_table" style="width:100%">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th class="num">H.S.Code</th>
                        <th></th>
                        <th class="desc">Description</th>
                        <th class="rnum">Quantity</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                        {%- set nctr = -1 %}
                        {%- for i in value['resultset_value']['scannedItems'] %}
                            {% set nctr = nctr+1 %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                {% if 'MM001' in value['resultset_value']['lineitems'][nctr]['myvalues'] %}
                                    <td class="num"> {{(value['resultset_value']['lineitems'][nctr]['myvalues']['MM001']['hsncode'])}}</td>
                                {% else %}
                                    <td></td>
                                {% endif %}                               
                                <td></td>                                
                                {% if value['motornoobj']['key2']['RegNo'] is not none %}
                                    <td class="desc"><br><b>Model<span style="margin-left: 6mm;"></span>:</b><span style="margin-left: 3mm;"></span>{{(value['resultset_value']['lineitems'][nctr]['myvalues']['MM001']['mtlname'])}}<br><b>Frame No.<span style="margin-left: 1.5mm;">:</b><span style="margin-left: 3mm;"></span>{{i.chasisno}}<br><b>Engine No.<span style="margin-left: 1mm;">:</b><span style="margin-left: 3mm;"></span>{{i.motorno}}<br><b>Colour<span style="margin-left: 6mm;">:</b><span style="margin-left: 3mm;"></span>{{i.colour}}<br><b>RegNo.<span style="margin-left: 5.5mm;">:</b><span style="margin-left: 3mm;"></span>{{i.regno}}<br><b>Ref No.<span style="margin-left: 3mm;">:</b><span style="margin-left: 3mm;"></span>123</td>
                                    <td  class="rnum">{{value['resultset_value']['lineitems'][nctr]['qty']}}</td>
                                    <td  class="rnum">{{value['resultset_value']['lineitems'][nctr]['rate']}}</td>
                                    <td  class="rnum">{{\"%.2f\"|format(value['resultset_value']['lineitems'][nctr]['myvalues']['MTLPRICE'])}}</td>
                                   <br><br>                                    
                                {% else %}
                                    <td>{{i['itemcode']}}</td>
                                {% endif %}   
                            </tr>                                
                        {%- endfor %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                        {% if loop.index > 1 %}
                        <tr><td></td></tr>
                        <tr><td></td></tr>
                            <tr>
                                <td class="snum">{{loop.index0+1}}</td>
                                <td></td>
                                <td></td>
                                <td class="desc">{{i['itemcode']}}</td>
                                <td class="rnum">{{i['qty']}}</td>
                                <td class="rnum">{{i['rate']}}</td>
                                <td class="rnum">{{i['myvalues']['MTLPRICE']}}</td>              
                            </tr>
                            {% endif %}
                        {%- endfor %}
                    </tbody>
                </table>
            </div>
            <h4><u>MR/HR Details:</u></h4>
            <table style="width: 100%;">
                <thead>
                    <th class="snum"><u>BS Date</u></th>
                    <th class="snum"><u>Rec No.</u></th>
                    <th class="snum"><u>Amount</u></th>
                    <td class="rnum">Total Amount</td>
                    <td>:</td>
                    <td class="rnum" class="ltop">{{value['resultset_value']['popricingtotal']['MTLPRICE']}}</td>
                </thead>
                <tbody>
                {%- for i in value['resultset_value']['receipts'] %}
                    <tr>
                        <td class="snum">{{value['resultset_value']['docbs']}}</td>
                        <td class="snum">{{i.docno}}</td>
                        <td class="snum">{{i.amount}}</td>
                        <td class="rnum"></td>
                        <td></td>
                        <td></td>
                    </tr>
                {% endfor %}
                    <tr>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum">Discount</td>
                        <td>:</td>
                        <td class="rnum"><u>{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</u></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum">Taxable Amount</td>
                        <td>:</td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VAL1'])}}</td>
                    </tr>
                    <tr>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum">VAT {{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VATPER'])}}%</td>
                        <td>:</td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VAT'])}}</td>
                    </tr>
                    <tr>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum"><b>Bill Amount</b></td>
                        <td><b>:</b></td>
                        <td class="rnum"><b><u>{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VAL2'])}}</u></b></td>
                    </tr>
                </tbody>
            </table>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td>FSC No.</td>
                        <td>:</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Coupon No.</td>
                        <td>:</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Exchanger</td>
                        <td>:</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Exchanger certificate No.</td>
                        <td>:</td>
                        <td></td>  
                    </tr>
                </tbody>
            </table>
            <table style="margin-left: 300px;">
                <tbody>
                    <tr>
                        <td>Agent </td>
                        <td>:</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Coupon Amt</td>
                        <td>:</td>
                        <td></td>  
                    </tr>
                    <tr>
                        <td>Exchange Amt</td>
                        <td>:</td>
                        <td></td>  
                    </tr>
                    <tr>
                        <td>Code</td>
                        <td>:</td>
                        <td></td>
                    </tr>
                </tbody>
            </table>
            <div class="theight" style ="width: 75%; border-bottom:100%">
            <br><br><br><br>
                <p><b>Amount in Words:</b>  {{value['numtoword'].num2words(value['resultset_value']['popricingtotal']['VAL2']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</p>
                <p style="font-size:16px;">Remarks:{{value['resultset_value']['remarks']}}</p>
            </div>
            <div style="line-height:15px">
                <hr style="border: 0.5px solid black;">
                <p class="tleft"><b>Receiver's Signature</b></p>
                <p class="tright"><b>For  {{value['resultset_value']['CO010']['coname']}}</b></p>
                <p class="tleft">E & OE<br>Goods once sold are not exchangeable or returnable<br> In case of two wheeler purchase customer must do the transfer of ownership within 15 days from the bill date.</p>
                <p class="tleft">Prepared By: {{(value['resultset_value']['USR01']['username'])}}</p>
            </div> 
        </div>
    {% else %}
        <div class="preinv">
            <table style="width: 100%; border-bottom: 1px solid black;">
                <tbody>
                    <tr>
                        <td>
                            <img class="imag" src="http://103.146.234.44:8080/img/NGMlogo1.jpg">
                        </td>
                        <td class="heading">
                            {% if value['resultset_value']['status'] != 'C' %}
                                <h2 class="snum">Invoice - DRAFT</h2>
                            {% elif 'prncnt' in value['resultset_value'] %}
                                {% if value['resultset_value']['prncnt'] <= 0 %}
                                     <h2 class="rnum">Tax Invoice</h2>
                                {% else %}
                                    <h2 class="rnum">Invoice (COPY OF ORIGINAL :  {{value['resultset_value']['prncnt']}} )</h2>
                                {% endif %}
                            {% endif %}                       
                            <h2>{{value['resultset_value']['CO010']['coname']}}</h2>
                            <p>H/O:<span style="margin-left: 3mm;"></span>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</p>
                            <p>VAT No. :<span style="margin-left: 3mm;"></span><b>{{value['resultset_value']['CO010']['covatno']}}</b></p>
                            <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OU010']['unitname']}}</b></p> 
                            {% if 'OD10' in value['resultset_value'] %}
                                <p>Phone No:{{value['resultset_value']['OD10']['phoneno']}}</p>
                            {% else %}
                                <p>Phone No:{{value['resultset_value']['CO010']['phoneno']}}</p>
                            {% endif %}
                        </td>
                        <td class="tright">
                            <br><br><br>
                            {% if value['resultset_value']['invtype'] == 'CA' %}
                                <p>Mode of Payment: <b>Cash Bill</b></p>
                            {% elif value['resultset_value']['invtype'] == 'FP' %}
                                <p>Mode of Payment: <b>Fonepay Bill</b></p>
                            {% else %}
                                <p>Mode of Payment: <b>CREDIT</b></p>
                            {% endif %}
                        </td>
                    </tr>
                </tbody>
            </table>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td>Buyer's Name</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custname']}}</td>
                    </tr>
                    <tr>
                        <td>Address</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custaddress']}}</td>
                    </tr>
                    <tr>
                        <td>Cell No.</td>
                        <td>:</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Phone No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['phoneno']}}</td>
                    </tr>
                    <tr>
                        <td>C/O</td>
                        <td>:</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Buyer's PAN No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['vatno']}}</td>  
                    </tr>
                </tbody>
            </table>
            <table class="tright">
                <tbody>
                    <tr>
                        <td>Invoice No.</td>
                        <td>:</td>
                        <td><b>{{value['resultset_value']['sinvno']}}</b></td>
                    </tr>
                    <tr>
                        <td>Date</td>
                        <td>:</td>
                         <td>{{value['resultset_value']['sinvdate']}}</td>
                    </tr>
                    <tr>
                        <td>BS Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docbs']}}</td>
                    </tr>
                    <tr>
                        <td>PP No</td>
                        <td>:</td>
                        <td></td>  
                    </tr>
                    <tr>
                        <td>PP BS Date</td>
                        <td>:</td>
                        <td></td>  
                    </tr>
                    <tr>
                        <td>Print Date & Time</td>
                        <td>:</td>
                        <td>{{ value['printdate'].strftime('%d/%m/%Y') }} {{ value['printdate'].strftime('%H:%M:%S') }}</td>
                    </tr>
                </tbody>
            </table>
            <div>
                <table class="collapse_table" style="width:100%">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th class="num">H.S.Code</th>
                        <th></th>
                        <th class="desc">Description</th>
                        <th class="rnum">Quantity</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                        {%- set nctr = -1 %}
                        {%- for i in value['resultset_value']['scannedItems'] %}
                            {% set nctr = nctr+1 %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                {% if 'MM001' in value['resultset_value']['lineitems'][nctr]['myvalues'] %}
                                    <td class="num"> {{(value['resultset_value']['lineitems'][nctr]['myvalues']['MM001']['hsncode'])}}</td>
                                {% else %}
                                    <td></td>
                                {% endif %}                               
                                <td></td>                                
                                {% if value['motornoobj']['key2']['RegNo'] is not none %}
                                    <td class="desc"><br><b>Model<span style="margin-left: 6mm;"></span>:</b><span style="margin-left: 3mm;"></span>{{(value['resultset_value']['lineitems'][nctr]['myvalues']['MM001']['mtlname'])}}<br><b>Frame No.<span style="margin-left: 1.5mm;">:</b><span style="margin-left: 3mm;"></span>{{i.chasisno}}<br><b>Engine No.<span style="margin-left: 1mm;">:</b><span style="margin-left: 3mm;"></span>{{i.motorno}}<br><b>Colour<span style="margin-left: 6mm;">:</b><span style="margin-left: 3mm;"></span>{{i.colour}}<br><b>RegNo.<span style="margin-left: 5.5mm;">:</b><span style="margin-left: 3mm;"></span>{{i.regno}}<br><b>Ref No.<span style="margin-left: 3mm;">:</b><span style="margin-left: 3mm;"></span>123</td>
                                    <td  class="rnum">{{value['resultset_value']['lineitems'][nctr]['qty']}}</td>
                                    <td  class="rnum">{{value['resultset_value']['lineitems'][nctr]['rate']}}</td>
                                    <td  class="rnum">{{\"%.2f\"|format(value['resultset_value']['lineitems'][nctr]['myvalues']['MTLPRICE'])}}</td>
                                   <br><br>                                    
                                {% else %}
                                    <td>{{i['itemcode']}}</td>
                                {% endif %}   
                            </tr>                                
                        {%- endfor %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                        {% if loop.index > 1 %}
                        <tr><td></td></tr>
                        <tr><td></td></tr>
                            <tr>
                                <td class="snum">{{loop.index0+1}}</td>
                                <td></td>
                                <td></td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i['qty']}}</td>
                                <td class="rnum">{{i['rate']}}</td>
                                <td class="rnum">{{i['myvalues']['MTLPRICE']}}</td>              
                            </tr>
                            {% endif %}
                        {%- endfor %}
                    </tbody>
                </table>
            </div>
            <h4><u>MR/HR Details:</u></h4>
            <table style="width: 100%;">
                <thead>
                    <th class="snum"><u>BS Date</u></th>
                    <th class="snum"><u>Rec No.</u></th>
                    <th class="snum"><u>Amount</u></th>
                    <td class="rnum">Total Amount</td>
                    <td>:</td>
                    <td class="rnum" class="ltop">{{value['resultset_value']['popricingtotal']['MTLPRICE']}}</td>
                </thead>
                <tbody>
                {%- for i in value['resultset_value']['receipts'] %}
                    <tr>
                        <td class="snum">{{value['resultset_value']['docbs']}}</td>
                        <td class="snum">{{i.docno}}</td>
                        <td class="snum">{{i.amount}}</td>
                        <td class="rnum"></td>
                        <td></td>
                        <td></td>
                    </tr>
                {% endfor %}
                    <tr>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum">Discount</td>
                        <td>:</td>
                        <td class="rnum"><u>{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</u></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum">Taxable Amount</td>
                        <td>:</td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VAL1'])}}</td>
                    </tr>
                    <tr>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum">VAT {{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VATPER'])}}%</td>
                        <td>:</td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VAT'])}}</td>
                    </tr>
                    <tr>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum"><b>Bill Amount</b></td>
                        <td><b>:</b></td>
                        <td class="rnum"><b><u>{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VAL2'])}}</u></b></td>
                    </tr>
                </tbody>
            </table>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td>FSC No.</td>
                        <td>:</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Coupon No.</td>
                        <td>:</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Exchanger</td>
                        <td>:</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Exchanger certificate No.</td>
                        <td>:</td>
                        <td></td>  
                    </tr>
                </tbody>
            </table>
            <table style="margin-left: 300px;">
                <tbody>
                    <tr>
                        <td>Agent </td>
                        <td>:</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Coupon Amt</td>
                        <td>:</td>
                        <td></td>  
                    </tr>
                    <tr>
                        <td>Exchange Amt</td>
                        <td>:</td>
                        <td></td>  
                    </tr>
                    <tr>
                        <td>Code</td>
                        <td>:</td>
                        <td></td>
                    </tr>
                </tbody>
            </table>
            <div class="theight" style ="width: 75%; border-bottom:100%">
            <br><br><br><br>
                <p><b>Amount in Words:</b>  {{value['numtoword'].num2words(value['resultset_value']['popricingtotal']['VAL2']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</p>
                <p style="font-size:16px;">Remarks:{{value['resultset_value']['remarks']}}</p>
            </div>
            <div style="line-height:15px">
                <hr style="border: 0.5px solid black;">
                <p class="tleft"><b>Receiver's Signature</b></p>
                <p class="tright"><b>For  {{value['resultset_value']['CO010']['coname']}}</b></p>
                <p class="tleft">E & OE<br>Goods once sold are not exchangeable or returnable<br> In case of two wheeler purchase customer must do the transfer of ownership within 15 days from the bill date.</p>
                <p class="tleft">Prepared By: {{(value['resultset_value']['USR01']['username'])}}</p>
            </div> 
        </div>
    {% endif %}
    </body>
</html>""",
    "monrecp":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,tr,th,td{
                font-size: 11px;
                font-family: calibri;
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
            div.table_items {
                height: 200px !important;
                border: 1px solid #ccc;
            }
            .theight{
                height: 500px;
            }
            .heading{
                font-size: 15px;
                line-height: 0px;
                text-align: left;
                margin-top: 0%;
                padding-top: 0%;
            }
            .collapse_table{
                border-collapse: collapse;
                width: 100%;
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
            .desc{
                padding-right: 150px;
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
            <table class="tleft">
                <tbody>
                    <tr>
                        <td><b>BRANCH</b></td>
                        <td><b>{{value['resultset_value']['custaddress']}}</b></td>
                    </tr>
                    <tr>
                        <br><br>
                    </tr>
                    <tr>
                        <td>Receipt No.</td>
                        <td>{{value['resultset_value']['docno']}}</td>
                    </tr>
                    <tr>
                        <td>Customer Code</td>
                        <td>{{value['resultset_value']['custid']}}</td>
                    </tr>
                </tbody>
            </table>
            <table class="tright">
                <tbody>
                    <tr>
                        <td>Phone No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['phoneno']}}</td>
                    </tr>
                    <tr>
                        <td>Teller No</td>
                        <td>:</td>
                        <td></td>  
                    </tr>
                    <tr>
                        <td>Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['sinvdate']}}</td>
                    </tr>
                    <tr>
                        <td>BS Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docbs']}}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <table style="width: 100%;">
            <tbody>
                <tr><td><i>Received with thanks from</i><span style="margin-left: 3mm;"></span></td></tr>
                <tr><td><i>the sum of</i><span style="margin-left: 3mm;"></span> {{value['numtoword'].num2words(value['resultset_value']['amount']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</td></tr>
                <tr><td><i>by cheque/cash No</i><span style="margin-left: 3mm;"></span></td></tr>
                <tr><td><i>on account of</i><span style="margin-left: 3mm;"></span></td></tr>
            </tbody>
        </table>
        <br>
        <table style="width: 100%;">
            <tr>
                <td class="boxx">Rs {{value['resultset_value']['amount']}}</td>
                <td class="snum">This receipt is valid subject to realisation of cheque.</td>
            </tr>
            <tr>
                <td><br><br></td>
            </tr>
            <tr>
                <td class="ltop">Customer's Signature</td>
                <td class="snum">Prepared By   {{value['resultset_value']['USR01']['username']}}</td>
                <td class="ltop">Authorized Signature</td>
            </tr>
            <tr>
                <td></td>
                <td class="snum">Date:{{value['resultset_value']['docdt']}}</td>
                <td></td>
            </tr>
        </table>
    </body>
</html>""",
    "holdrecp":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,tr,th,td{
                font-size: 11px;
                font-family: calibri;
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
            div.table_items {
                height: 200px !important;
                border: 1px solid #ccc;
            }
            .theight{
                height: 500px;
            }
            .heading{
                font-size: 15px;
                line-height: 0px;
                text-align: left;
                margin-top: 0%;
                padding-top: 0%;
            }
            .collapse_table{
                border-collapse: collapse;
                width: 100%;
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
            .desc{
                padding-right: 150px;
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
                            <h2 class="snum">Hold Receipt</h2>
                        </td>
                    </tr>
                </tbody>
            </table>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td><b>BRANCH</b></td>
                        <td><b>{{value['resultset_value']['custaddress']}}</b></td>
                    </tr>
                    <tr>
                        <br><br>
                    </tr>
                    <tr>
                        <td>Receipt No.</td>
                        <td>{{value['resultset_value']['docno']}}</td>
                    </tr>
                    <tr>
                        <td>Customer Code</td>
                        <td>{{value['resultset_value']['custid']}}</td>
                    </tr>
                </tbody>
            </table>
            <table class="tright">
                <tbody>
                    <tr>
                        <td>Phone No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['phoneno']}}</td>
                    </tr>
                    <tr>
                        <td>Teller No</td>
                        <td>:</td>
                        <td></td>  
                    </tr>
                    <tr>
                        <td>Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['sinvdate']}}</td>
                    </tr>
                    <tr>
                        <td>BS Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docbs']}}</td>
                    </tr>
                </tbody>
            </table>
        </div>
        <table style="width: 100%;">
            <tbody>
                <tr><td><i>Received with thanks from</i><span style="margin-left: 3mm;"></span></td></tr>
                <tr><td><i>the sum of</i><span style="margin-left: 3mm;"></span> {{value['numtoword'].num2words(value['resultset_value']['amount']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</td></tr>
                <tr><td><i>by cheque/cash No</i><span style="margin-left: 3mm;"></span></td></tr>
                <tr><td><i>on account of</i><span style="margin-left: 3mm;"></span></td></tr>
            </tbody>
        </table>
        <br>
        <table style="width: 100%;">
            <tr>
                <td class="boxx">Rs {{value['resultset_value']['amount']}}</td>
                <td class="snum">This receipt is valid subject to realisation of cheque.</td>
            </tr>
            <tr>
                <td><br><br></td>
            </tr>
            <tr>
                <td class="ltop">Customer's Signature</td>
                <td class="snum">Prepared By {{value['resultset_value']['USR01']['username']}}</td>
                <td class="ltop">Authorized Signature</td>
            </tr>
            <tr>
                <td></td>
                <td class="snum">Date:{{value['resultset_value']['docdt']}}</td>
                <td></td>
            </tr>
        </table>
    </body>
</html>""",
    "mv01":"""<!DOCTYPE html>
<html lang="en">
    <head>
       <meta charset="UTF-8">
        <style>
            table,tr,th,td{
                font-size: 8px;
                font-family: calibri;
                text-align: left;
            }
            .preinv{
                font-size: 11px;
                font-family: calibri;
            }
            .tabl{
                border: 1px solid black;
                border-right: none;
                border-left: none;
                text-align: center;
            }
            .imag{
                width: 70px;
                height: 85px;
            }
            div.table_items {
                height: 200px !important;
                border: 1px solid #ccc;
            }
            .theight{
                height: 275px;
            }
            .heading{
                font-size: 15px;
                line-height: 0px;
                text-align: left;
                margin-top: 0%;
                padding-top: 0%;
            }
            .collapse_table{
                border-collapse: collapse;
                width: 100%;
                padding:100px;
                margin-top:10px;
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
            .desc{
                padding-right: 150px;
            }
            .tot{
                width: 100%;
                border-bottom: 1px solid black;
                border-top: 1px solid black;
            }
            .footer{
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                color: black;
                border-top: 1px solid black;
                font-size: 11px;
            }
            .head{
                position: fixed;
                display:block;
                left: 0;
                top: 0;
                width: 100%;
                font-size: 15px;
                line-height: 0px;
                color: black;
                z-index: 999;
            }
            .pagebreak {
                clear: both;
                page-break-before: always;
            }
            .breakhead{
                clear: both;
                page-break-before: always;
                line-height: 0px;
                padding-top:3px;
            }
        </style>
    </head>
    <body>
        <header class="breakhead">
        <h2 class="snum">{{value['resultset_value']['coidobj']['key2']}}</h2>
        {% if "OU010" in value['resultset_value'] %}
            {% if value['resultset_value']['OU010']['unitname'] is not none %}
                <p class="snum">{{value['resultset_value']['OU010']['unitname']}}</p>
            {% endif %}
        {% endif %}
        {% if "OU010" in value['resultset_value'] %}
            {% if value['resultset_value']['OU010']['address'][0]['adrs1'] is not none %}
                <p class="snum" style="font-size:9px;">{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</p>
            {% endif %}
        {% endif %}
        <p class="snum" style="font-size:9px;">Phone:{{value['resultset_value']['CO010']['phoneno']}} Email:</p>
        <br>
        <h4 class="snum" style="font-size:12px;">Materialized View</h4>
        <h4 class="snum" style="font-size:11px;">Annexure - 5 details</h4>
        <p class="snum" style="font-size:9px;"><b>From</b> {{value['resultset_value']['fromdate']}} <b>to</b> {{value['resultset_value']['todate']}}</p>
        </header>
        <div>
        <table class="collapse_table">
            <thead class="tabl">
                <th>Slno</th>
                <th>Field</th>
                <th>Fiscal Year</th>
                <th>Bill No.</th>
                <th>Customer Name</th>
                <th>Customer PAN</th>
                <th>Bill Date</th>
                <th class="rnum">Amount</th>
                <th class="rnum">Discount</th>
                <th class="rnum">Taxable Amount</th>
                <th class="rnum">Tax Amount</th>
                <th class="rnum">Total Amount</th>
                <th>Sync with IRD</th>
                <th>Is Printed</th>
                <th>Is Active</th>
                <th>Printed Time</th>
                <th>Entered By</th>
                <th>Printed By</th>
                <th>Is Realtime</th>
                <th>Payment Method</th>
                <th>VAT Refund Amount</th>
                <th>Transaction Id</th>
            </thead>
            <tbody>
                {%- for i in value['resultset_value']['lineitems'] %}
                <tr>
                    <td>{{i['rpsno']}}</td>
                    <td>{{i['rectype']}}</td>
                    <td>{{i['fyear']}}</td>
                    <td>{{i['sinvno']}}</td>
                    <td>{{i['custname']}}</td>
                    <td>{{i['panno']}}</td>
                    <td>{{i['sinvdate']}}</td>
                    <td class="rnum">{{\"%.2f\"|format(i['mtlprice'])}}</td>
                    <td class="rnum">{{\"%.2f\"|format(i['discount'])}}</td>
                    <td class="rnum">{{\"%.2f\"|format(i['val1'])}}</td>
                    <td class="rnum">{{\"%.2f\"|format(i['vat'])}}</td>
                    <td class="rnum">{{\"%.2f\"|format(i['val2'])}}</td>
                    <td class="snum">{{i['syncwithird']}}</td>
                    <td class="snum">{{i['isprinted']}}</td>
                    <td class="snum">{{i['isactive']}}</td>
                    <td>{{i['printtime']}}</td>
                    <td>{{i['username']}}</td>
                    <td>{{i['loginempid']}}</td>
                    <td class="snum">{{i['isrealtime']}}</td>
                    <td class="snum"></td>
                    <td class="snum"></td>
                    <td class="snum"></td>                   
                </tr>
                {% endfor -%}
                <tr class="tot">
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td><b>Total</b></td>
                    <td><b></b></td>
                    <td><b></b></td>
                    <td><b></b></td>
                    <td><b></b></td>
                    <td><b></b></td>   
                </tr>
                </tbody>
        </table>
        </div>                             
        <div>
            <p style="font-size:11px; font-family:calibri;" class="tleft">Printed User:{{(value['resultset_value']['loginempid'])}}<span style="margin-left: 6cm;"></span>Page : {{(value['resultset_value']['pageno'])}} <span style="margin-left: 6cm;"></span>{{ value['printdate'].strftime('%d/%m/%Y') }} {{ value['printdate'].strftime('%H:%M:%S') }}</p>
            <br>
        </div>
    </body>
</html>""",
    "auditrpt1":"""<!DOCTYPE html>
<html lang="en">
    <head>
       <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <style>
            table,tr,th,td{
                font-size: 10px;
                font-family: calibri;
                text-align: left;
            }
            .preinv{
                font-size: 11px;
                font-family: calibri;
            }
            .tabl{
                border: 1px solid black;
                border-right: none;
                border-left: none;
                text-align: center;
            }
            .imag{
                width: 70px;
                height: 85px;
            }
            div.table_items {
                height: 200px !important;
                border: 1px solid #ccc;
            }
            .theight{
                height: 275px;
            }
            .heading{
                font-size: 15px;
                line-height: 0px;
                text-align: left;
                margin-top: 0%;
                padding-top: 0%;
            }
            .collapse_table{
                border-collapse: collapse;
                width: 100%;
                padding:100px;
                margin-top:10px;
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
            .desc{
                padding-right: 150px;
            }
            .tot{
                width: 100%;
                border-bottom: 1px solid black;
                border-top: 1px solid black;
            }
            .footer{
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                color: black;
                border-top: 1px solid black;
                font-size: 11px;
            }
            .head{
                position: fixed;
                display:block;
                left: 0;
                top: 0;
                width: 100%;
                font-size: 15px;
                line-height: 0px;
                color: black;
                z-index: 999;
            }
            .pagebreak {
                clear: both;
                page-break-before: always;
            }
            .breakhead{
                clear: both;
                page-break-before: always;
                line-height: 0px;
                padding-top:3px;
            }
        </style>
    </head>
    <body>
        <header class="breakhead">
        <h2 class="snum">{{value['resultset_value']['coidobj']['key2']}}</h2>
        {% if "OU010" in value['resultset_value'] %}
            {% if value['resultset_value']['OU010']['unitname'] is not none %}
                <p class="snum">{{value['resultset_value']['OU010']['unitname']}}</p>
            {% endif %}
        {% endif %}
        {% if "OU010" in value['resultset_value'] %}
            {% if value['resultset_value']['OU010']['address'][0]['adrs1'] is not none %}
                <p class="snum" style="font-size:9px;">{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</p>
            {% endif %}
        {% endif %}
            <p class="snum" style="font-size:9px;">Phone: Email:</p>
        <br>
        <h4 class="snum" style="font-size:11px;">Audit Log between {{value['resultset_value']['fromdate']}} and {{value['resultset_value']['todate']}}</h4>
        </header>
        <div>
        <table class="collapse_table">
            <thead class="tabl">
                <th>Slno</th>
                <th>Log Date & Time</th>
                <th>Log User</th>
                <th>Screen Name</th>
                <th>Log Description</th>
            </thead>
            <tbody>
                {%- for i in value['resultset_value']['lineitems'] %}
                <tr>
                    <td>{{i['rpsno']}}</td>
                    <td>{{i['logtime']}}</td>
                    <td>{{i['userid']}}</td>
                    <td>{{i['screencode']}}</td>
                    <td>{{i['logdesc']}}</td>                 
                </tr>
                {% endfor -%}
            </tbody>
        </table>
        </div>                             
        <div>
            <p class="tleft">Printed User:{{(value['resultset_value']['loginempid'])}}<span style="margin-left: 8cm;"></span>Page : {{(value['resultset_value']['pageno'])}} <span style="margin-left: 8cm;"></span>{{ value['printdate'].strftime('%d/%m/%Y') }} {{ value['printdate'].strftime('%H:%M:%S') }}</p>
            <br>
        </div>
    </body>
</html>""",
    "salesrpt":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,tr,th,td{
                font-size: 10px;
                font-family: calibri;
                text-align: left;
            }
            .preinv{
                font-size: 11px;
                font-family: calibri;
            }
            .tabl{
                border: 1px solid black;
                border-right: none;
                border-left: none;
                text-align: center;
            }
            .imag{
                width: 70px;
                height: 85px;
            }
            .theight{
                height: 275px;
            }
            .heading{
                font-size: 15px;
                line-height: 0px;
                text-align: left;
                margin-top: 0%;
                padding-top: 0%;
            }
            .collapse_table{
                border-collapse: collapse;
                width: 100%;
                padding:100px;
                margin-top:10px;
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
            .desc{
                padding-right: 150px;
            }
            .tot{
                width: 100%;
                border-bottom: 1px solid black;
                border-top: 1px solid black;
            }
            .footer{
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                color: black;
                background-color: white;
                border-top: 1px solid black;
                font-size: 11px;
            }
            .head{
                position: fixed;
                display:block;
                left: 0;
                top: 0;
                width: 100%;
                font-size: 15px;
                line-height: 0px;
                color: black;
                z-index: 999;
            }
            .pagebreak {
                clear: both;
                page-break-before: always;
            }
            .breakhead{
                clear: both;
                page-break-before: always;
                line-height: 0px;
                padding-top:3px;
            }
            .headbor{
                border-right: 1px solid black;
                text-align: center;
                border-collapse: collapse;
            }
        </style>
    </head>
    <body>
        <header class="breakhead">
        <div class="preinv">
            <table style="width: 100%;">
                <tbody>
                    <tr>
                        <td class="heading">
                            <br><br>
                            <h2 class="snum" style="font-size:18px;"><b>Sales Account</b></h2>
                            <p class="snum" style="font-size:11px;">(Relating to clause (h) of sub-rule (1) of rule 23)</p>
                            <br><br>
                            <p class="snum" style="font-size:10px;"><b>Taxpayer Registration No (PAN) :{{value['resultset_value']['panno']}}  Name of Taxpayer :{{value['resultset_value']['CO010']['coname']}}  Year :{{value['resultset_value']['bsyyyy']}}  Tax Period :{{value['resultset_value']['bsmnth']}} </b></p>
                        </td>
                    </tr>
                </tbody>
            </table>
            <table class="collapse_table">
                <thead class="tabl">
                    <tr>
                    <th colspan="4" class="headbor">Invoice</th>
                    <th></th>
                    <th></th>
                    <th colspan="2" class="headbor" style="border-left: 1px solid black;">Taxable Sales</th>
                    <th colspan="4" class="snum">Withdrawal</th>
                    </tr>
                    <tr style="border-top: 1px solid black;">
                        <th>Date</th>
                        <th>Invoice<br>number</th>
                        <th>Buyer's<br>Name</th>
                        <th>Buyer's Permanent<br>Account Number</th>
                        <th class="rnum">Total Sales /<br> Withdrawals (Rs.)</th>
                        <th class="rnum">Selling price <br>excluding local tax<br> (Rs.)</th>
                        <th class="rnum" style="border-left: 1px solid black;">Price<br> (Rs.)</th>
                        <th class="headbor" style="text-align:right;">Tax<br> (Rs.)</th>
                        <th class="snum">Value of goods or<br>services exported<br>(Rs.)</th>
                        <th class="rnum">Country<br>of Export</th>
                        <th class="rnum">Export<br>Notification<br>No.</th>
                        <th class="rnum">Clearance<br>Certificate<br>Date</th>
                    </tr>
                </thead>
                <tbody>
                {%- for i in value['resultset_value']['lineitems'] %}
                    <tr>
                    {% if value['resultset_value']['lineitems']['sinvbs'] is not none %}
                        <td>{{i['sinvbs']}}</td>
                    {% else %}
                        <td></td>
                    {% endif %}
                        <td>{{i['sinvno']}}</td>
                        <td>{{i['custname']}}</td>
                        <td>{{i['panno']}}</td>
                        <td class="rnum">{{\"%.2f\"|format(i['val2'])}}</td>
                        <td class="rnum">{{\"%.2f\"|format(i['val1'])}}</td>
                        <td class="rnum">{{\"%.2f\"|format(i['val1'])}}</td>
                        <td class="rnum">{{\"%.2f\"|format(i['vat'])}}</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                {% endfor -%}
                    <tr style= "border-top:1px solid black;">
                        <td colspan="4" class="snum"><b>Total</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                </tbody>               
            </table>
        </div>
        <div class="footer">
        <br><br>
            <p class="rnum">Page : {{(value['resultset_value']['pageno'])}}</p>
        </div>
    </body>
</html>""",
    "salesrtn_old":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,tr,th,td{
                font-size: 10px;
                font-family: calibri;
                text-align: left;
            }
            .preinv{
                font-size: 11px;
                font-family: calibri;
            }
            .tabl{
                border: 1px solid black;
                border-right: none;
                border-left: none;
                text-align: center;
            }
            .imag{
                width: 70px;
                height: 85px;
            }
            div.table_items {
                height: 200px !important;
                border: 1px solid #ccc;
            }
            .theight{
                height: 275px;
            }
            .heading{
                font-size: 15px;
                line-height: 0px;
                text-align: left;
                margin-top: 0%;
                padding-top: 0%;
            }
            .collapse_table{
                border-collapse: collapse;
                width: 100%;
                padding:100px;
                margin-top:10px;
            }
            .th{
                border: 1px solid black;
                border-collapse: collapse;
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
            .desc{
                padding-right: 150px;
            }
            .tot{
                width: 100%;
                border-bottom: 1px solid black;
                border-top: 1px solid black;
            }
            .footer{
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                color: black;
                background-color: white;
                border-top: 1px solid black;
                font-size: 11px;
            }
            .head{
                position: fixed;
                display:block;
                left: 0;
                top: 0;
                width: 100%;
                font-size: 15px;
                line-height: 0px;
                color: black;
                z-index: 999;
            }
            .pagebreak {
                clear: both;
                page-break-before: always;
            }
            .breakhead{
                clear: both;
                page-break-before: always;
                line-height: 0px;
                padding-top:3px;
            }
            .headbor{
                border-right: 1px solid black;
                text-align: center;
                border-collapse: collapse;
            }
        </style>
    </head>
    <body>
        <header class="breakhead">
        <div class="preinv">
            <table style="width: 100%;">
                <tbody>
                    <tr>
                        <td class="heading">
                            <br><br>
                            <h2 class="snum" style="font-size:18px;"><b>Sales Return Account</b></h2>
                            <p class="snum" style="font-size:11px;">(Relating to clause (h) of sub-rule (1) of rule 23)</p>
                            <br><br>
                            <p class="snum" style="font-size:10px;"><b>Taxpayer Registration No (PAN) :  Name of Taxpayer :  Year :  Tax Period : </b></p>
                        </td>
                    </tr>
                </tbody>
            </table>
            <table class="collapse_table">
                <thead class="tabl">
                    <tr>
                    <th colspan="7" class="headbor">Invoice</th>
                    <th></th>
                    <th></th>
                    <th colspan="2" class="snum" style="border-left: 1px solid black;">Taxable Return</th>
                    </tr>
                    <tr style="border-top: 1px solid black;">
                        <th>Date</th>
                        <th class="snum">Invoice<br>number</th>
                        <th>Buyer's<br>Name</th>
                        <th>Buyer's Permanent<br>Account Number</th>
                        <th class="rnum">The name of<br>the product<br>or service</th>
                        <th class="rnum">Quantity of<br>goods or<br>services</th>
                        <th class="headbor">a Unit of<br>goods or<br>services</th>
                        <th class="rnum">Deposit<br>Refund (Rs.)</th>
                        <th class="snum">Return value<br>of Local Tax<br>Exemption<br>(Rs.)</th>
                        <th class="headbor" style="border-left: 1px solid black;">Price<br> (Rs.)</th>
                        <th class="snum">Tax<br> (Rs.)</th>
                    </tr>
                </thead>
                <tbody>
                {%- for i in value['resultset_value']['lineitems'] %}
                    <tr>
                        <td>{{i['sinvbs']}}</td>
                        <td>{{i['sinvno']}}</td>
                        <td>{{i['custname']}}</td>
                        <td>{{i['panno']}}</td>
                        <td class="rnum">{{\"%.2f\"|format(i['val2'])}}</td>
                        <td class="rnum">{{\"%.2f\"|format(i['val1'])}}</td>
                        <td class="rnum">{{\"%.2f\"|format(i['val1'])}}</td>
                        <td class="rnum">{{\"%.2f\"|format(i['vat'])}}</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                {% endfor -%}
                    <tr>
                        <td colspan="4" class="snum"><b>Total</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                </tbody>               
            </table>
        </div>
        <div class="footer">
        <br><br>
            <p class="rnum">Page : {{(value['resultset_value']['pageno'])}}</p>
        </div>
    </body>
</html>""",
    "salesrtn":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,tr,th,td{
                font-size: 10px;
                font-family: calibri;
                text-align: left;
            }
            .preinv{
                font-size: 11px;
                font-family: calibri;
            }
            .tabl{
                border: 1px solid black;
                border-right: none;
                border-left: none;
                text-align: center;
            }
            .imag{
                width: 70px;
                height: 85px;
            }
            div.table_items {
                height: 200px !important;
                border: 1px solid #ccc;
            }
            .theight{
                height: 275px;
            }
            .heading{
                font-size: 15px;
                line-height: 0px;
                text-align: left;
                margin-top: 0%;
                padding-top: 0%;
            }
            .collapse_table{
                border-collapse: collapse;
                width: 100%;
                padding:100px;
                margin-top:10px;
            }
            .th{
                border: 1px solid black;
                border-collapse: collapse;
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
            .desc{
                padding-right: 150px;
            }
            .tot{
                width: 100%;
                border-bottom: 1px solid black;
                border-top: 1px solid black;
            }
            .footer{
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                color: black;
                background-color: white;
                border-top: 1px solid black;
                font-size: 11px;
            }
            .head{
                position: fixed;
                display:block;
                left: 0;
                top: 0;
                width: 100%;
                font-size: 15px;
                line-height: 0px;
                color: black;
                z-index: 999;
            }
            .pagebreak {
                clear: both;
                page-break-before: always;
            }
            .breakhead{
                clear: both;
                page-break-before: always;
                line-height: 0px;
                padding-top:3px;
            }
            .headbor{
                border-right: 1px solid black;
                text-align: center;
                border-collapse: collapse;
            }
        </style>
    </head>
    <body>
        <header class="breakhead">
        <div class="preinv">
            <table style="width: 100%;">
                <tbody>
                    <tr>
                        <td class="heading">
                            <br><br>
                            <h2 class="snum" style="font-size:18px;"><b>Sales Return Account</b></h2>
                            <p class="snum" style="font-size:11px;">(Relating to clause (h) of sub-rule (1) of rule 23)</p>
                            <br><br>
                            <p class="snum" style="font-size:10px;"><b>Taxpayer Registration No (PAN) :  Name of Taxpayer :  Year :  Tax Period : </b></p>
                        </td>
                    </tr>
                </tbody>
            </table>
            <table class="collapse_table">
                <thead class="tabl">
                    <tr>
                        <th>S.no</th>
                        <th class="snum">Invoice Date</th>
                        <th>Bill No.</th>
                        <th>Ref Bill No.</th>
                        <th>Ref Bill Date</th>
                        <th>Buyer's Name</th>
                        <th>Buyer's PAN</th>
                        <th class="rnum">Total Sales</th>
                        <th class="rnum">Non Taxable Sales</th>
                        <th class="rnum">Export Sales</th>
                        <th class="rnum">Discount</th>
                        <th class="rnum">Taxable Aamount</th>
                        <th class="rnum">Tax Amount</th>
                    </tr>
                </thead>
                <tbody>
                {%- for i in value['resultset_value']['lineitems'] %}
                    <tr>
                        <td class="snum">{{loop.index}}</td>
                        <td>{{i['srbs']}}</td>
                        <td>{{i['srno']}}</td>
                        <td>{{i['sinvno']}}</td>
                        <td>{{i['sinvbs']}}</td>
                        <td>{{i['custname']}}</td>
                        <td>{{i['panno']}}</td>
                        <td class="rnum">{{\"%.2f\"|format(i['val2'])}}</td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(i['discount'])}}</td>
                        <td class="rnum">{{\"%.2f\"|format(i['val1'])}}</td>
                        <td class="rnum">{{\"%.2f\"|format(i['vat'])}}</td>
                    </tr>
                {% endfor -%}
                    <tr>
                        <td colspan="3" class="snum"><b>TOTAL</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                    </tr>
                </tbody>               
            </table>
        </div>
        <div class="footer">
        <br><br>
            <p class="rnum">Page : {{(value['resultset_value']['pageno'])}}</p>
        </div>
    </body>
</html>""",
    "svr":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,tr,th,td{
                font-size: 10px;
                font-family: calibri;
                text-align: left;
            }
            .preinv{
                font-size: 11px;
                font-family: calibri;
            }
            .tabl{
                border: 1px solid black;
                border-right: none;
                border-left: none;
                text-align: center;
            }
            .imag{
                width: 70px;
                height: 85px;
            }
            div.table_items {
                height: 200px !important;
                border: 1px solid #ccc;
            }
            .theight{
                height: 275px;
            }
            .heading{
                font-size: 15px;
                line-height: 0px;
                text-align: left;
                margin-top: 0%;
                padding-top: 0%;
            }
            .collapse_table{
                border-collapse: collapse;
                width: 100%;
                padding:100px;
                margin-top:60px;
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
            .desc{
                padding-right: 150px;
            }
            .tot{
                width: 100%;
                border-bottom: 1px solid black;
                border-top: 1px solid black;
            }
            .footer{
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                color: black;
                border-top: 1px solid black;
                font-size: 11px;
            }
            .pagebreak {
                clear: both;
                page-break-before: always;
            }
            .breakhead{
                clear: both;
                page-break-before: always;
                line-height: 0px;
                padding-top:3px;
            }
        </style>
    </head>
    <body>
        <header class="breakhead">
            <h2 class="snum">{{value['resultset_value']['CO010']['coname']}}</h2>
            <p class="snum"></p>
            <p class="snum" style="font-size:9px;">address</p>
            <p class="snum" style="font-size:9px;">Phone:{{value['resultset_value']['CO010']['phoneno']}} Email:</p>            
            <b><hr></b>
            <p class="snum" style="font-size:11px"><b>Sales VAT Register Report for the date between{{value['resultset_value']['fromdate']}} and {{value['resultset_value']['todate']}}</h4></b></p>
        </header>
        <div>
            <table class="collapse_table">
                <thead class="tabl">
                    <th>Slno</th>
                    <th>Inv.Date</th>
                    <th>Inv.No.</th>
                    <th>HIS No.</th>
                    <th>Name</th>
                    <th>Buyers<br>PAN No.</th>
                    <th>Gross Sales</th>
                    <th>Non Taxable<br>Amount</th>
                    <th>Zero Rate<br>sales/Export</th>
                    <th>Taxable Sales<br>Amount</th>
                    <th><br>VAT</th>
                    <th>Discount</th>
                </thead>
                <tbody>
                    <tr>
                        <td></td>
                        <td><b><u>Sales Details</u></b></td>
                    </tr>
                    {%- for i in value['resultset_value']['lineitems'] %}
                    <tr>
                        <td>{{i['rpsno']}}</td>
                        <td class="rnum">{{i['sinvdate']}}</td>
                        <td class="rnum">{{i['sinvno']}}</td>
                        <td></td>
                        <td>{{i['custname']}}</td>
                        <td class="snum">{{i['panno']}}</td>
                        <td></td>
                        <td class="rnum"></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(i['val1'])}}</td>
                        <td class="rnum">{{\"%.2f\"|format(i['vat'])}}</td>
                        <td class="rnum">{{\"%.2f\"|format(i['discount'])}}</td>
                    </tr>
                    {% endfor -%}
                    <tr class="tot">
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td><b>Total Sales Details</b></td>
                        <td><b></b></td>
                        <td><b></b></td>
                        <td><b></b></td>
                        <td><b></b></td>
                        <td><b></b></td>
                        <td><b></b></td>
                    </tr>
                </tbody>
            </table>
            <div class="footer">
            <p></p>
            </div>
        </div>
    </body>
</html>""",
    "svr1":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,tr,th,td{
                font-size: 10px;
                font-family: calibri;
                text-align: left;
            }
            .preinv{
                font-size: 11px;
                font-family: calibri;
            }
            .tabl{
                border: 1px solid black;
                border-right: none;
                border-left: none;
                text-align: center;
            }
            .tabl1{
                border: 1px solid black;
                text-align: center;
                border-collapse: collapse;
            }
            .imag{
                width: 70px;
                height: 85px;
            }
            div.table_items {
                height: 200px !important;
                border: 1px solid #ccc;
            }
            .theight{
                height: 275px;
            }
            .heading{
                font-size: 15px;
                line-height: 0px;
                text-align: left;
                margin-top: 0%;
                padding-top: 0%;
            }
            .collapse_table{
                border-collapse: collapse;
                width: 100%;
                padding:100px;
                margin-top:60px;
            }
            .collapse_table1{
                border-collapse: collapse;
                width: 800%;
                padding:100px;
                margin-top:60px;
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
            .desc{
                padding-right: 150px;
            }
            .tot{
                width: 100%;
                border-bottom: 1px solid black;
                border-top: 1px solid black;
            }
            .footer{
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                color: black;
                border-top: 1px solid black;
                font-size: 11px;
            }
            .pagebreak {
                clear: both;
                page-break-before: always;
            }
            .breakhead{
                clear: both;
                page-break-before: always;
                line-height: 0px;
                padding-top:3px;
            }
        </style>
    </head>
    <body>
        <header class="breakhead">
            <h2 class="snum">{{value['resultset_value']['coid']}}</h2>
            <p class="snum">{{value['resultset_value']['unitid']}}</p>
            <p class="snum" style="font-size:9px;">address</p>
            <p class="snum" style="font-size:9px;">Phone: Email:</p>  
            <b><hr></b>
            <p class="snum"><b>Sales VAT Register Report for the date between</b></p>
            <p class="num"></p>
        </header>
        <div>
            <table class="collapse_table">
                <thead class="tabl">
                    <th>Slno</th>
                    <th>Inv.Date</th>
                    <th>Inv.No.</th>
                    <th>HIS No.</th>
                    <th>Name</th>
                    <th>Buyers<br>PAN No.</th>
                    <th>Gross Sales</th>
                    <th>Non Taxable<br>Amount</th>
                    <th>Zero Rate<br>sales/Export</th>
                    <th>Taxable Sales<br>Amount</th>
                    <th><br>VAT</th>
                    <th>Discount</th>
                </thead>
                <tbody>
                    <tr>
                        <td></td>
                        <td><b><u>Sales Details</u></b></td>
                    </tr>
                    {%- for i in value['resultset_value']['lineitems'] %}
                    <tr>
                        <td>{{i['rpsno']}}</td>
                        <td class="rnum">{{i['sinvdate']}}</td>
                        <td class="rnum">{{i['sinvno']}}</td>
                        <td></td>
                        <td>{{i['custname']}}</td>
                        <td class="snum">{{i['panno']}}</td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(i['totalamt'])}}</td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(i['taxableamt'])}}</td>
                        <td class="rnum">{{\"%.2f\"|format(i['taxamt'])}}</td>
                        <td class="rnum">{{\"%.2f\"|format(i['discount'])}}</td>
                    </tr>
                    {% endfor -%}
                    <tr class="tot">
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td><b>Total Sales Details</b></td>
                        <td><b></b></td>
                        <td><b></b></td>
                        <td><b></b></td>
                        <td><b></b></td>
                        <td><b></b></td>
                        <td><b></b></td>
                    </tr>
                    <tr class="tot">
                        <td></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td><b>Differnce/Net</b></td>
                        <td><b></b></td>
                        <td><b></b></td>
                        <td><b></b></td>
                        <td><b></b></td>
                        <td><b></b></td>
                        <td><b></b></td>
                    </tr>
                </tbody>
            </table>
            <table class="collapse">
                <thead class="tabl1">
                    <th>Total</th>
                    <th>Gross Sales</th>
                    <th>Non Taxable Sales</th>
                    <th>Zero Rate<br>Sales/Export</th>
                    <th>Taxable Sales</th>
                    <th>VAT Amount</th>
                    <th>Discount</th>
                </thead>
                <tbody>
                    <tr>
                        <td>Sales</td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Return</td>
                        <td></td>
                        <td></td>
                    </tr>
                    <tr>
                        <td>Difference</td>
                        <td></td>
                        <td></td>
                    </tr>
                </tbody>
            </table>
            <div class="footer">
            <p></p>
            </div>
        </div>
    </body>
</html>""",
    "rfmv":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,tr,th,td{
                font-size: 11px;
                font-family: calibri;
                text-align: left;
            }
            .preinv{
                font-size: 11px;
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
            div.table_items {
                height: 200px !important;
                border: 1px solid #ccc;
            }
            .theight{
                height: 275px;
            }
            .heading{
                font-size: 15px;
                line-height: 0px;
                text-align: left;
                margin-top: 0%;
                padding-top: 0%;
            }
            .collapse_table{
                border-collapse: collapse;
                width: 100%;
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
            .desc{
                padding-right: 150px;
            }
        </style>
    </head>
    <body>
        <div class="preinv">
            <table style="width: 100%; border-bottom: 1px solid black;">
                <tbody>
                    <tr>
                        <td>
                            <img class="imag" src="http://103.146.234.44:8080/img/NGMlogo1.jpg">
                        </td>
                        <td class="heading">
                            <h2 class="snum">SALES RETURN</h2>
                            <h2>{{value['resultset_value']['CO010']['coname']}}</h2>
                            <p><span style="margin-left: 3mm;"></span>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</p>
                            <p>VAT No. :<span style="margin-left: 3mm;"></span><b>{{value['resultset_value']['CO010']['covatno']}}</b></p>
                            <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OU010']['unitname']}}</b></p> 
                        </td>
                        <td class="tright">
                            <br><br><br>
                            {% if value['resultset_value']['invtype'] == 'CA' %}
                                <p>Mode of Payment: <b>Cash Bill</b></p>
                            {% else %}
                                <p>Mode of Payment: <b>CREDIT</b></p>
                            {% endif %}
                            {% if 'OD10' in value['resultset_value'] %}
                                <p>Phone No:{{value['resultset_value']['OD10']['phoneno']}}</p>
                            {% else %}
                                <p>Phone No:{{value['resultset_value']['CO010']['phoneno']}}</p>
                            {% endif %}
                        </td>
                    </tr>
                </tbody>
            </table>
            <table class="tleft">
                <tbody>
                    {% if value['resultset_value']['invtype'] =='R' %}
                        <tr>
                        <td>Buyer's Name</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['CM010']['custname']}}</td>
                    </tr>
                    <tr>
                        <td>Address</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['CM010']['address'][0]['adrs1']}}</td>
                    </tr>
                    <tr>
                        <td>Phone No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['CM010']['phone']}}</td>
                    </tr>
                    <tr>
                        <td>Buyer's VAT No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['CM010']['pan']}}</td>
                    </tr>
                {% else %}
                    <tr>
                        <td>Buyer's Name</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custname']}}</td>
                    </tr>
                    <tr>
                        <td>Address</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custaddress']}}</td>
                    </tr>
                    <tr>
                        <td>Phone No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['phoneno']}}</td>
                    </tr>
                    <tr>
                        <td>Buyer's VAT No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['vatno']}}</td>  
                    </tr>
                {% endif %}
                </tbody>
            </table>
            <table class="tright">
                <tbody>
                    <tr>
                        <td>Return No.</td>
                        <td>:</td>
                        <td><b>{{value['resultset_value']['docno']}}</b></td>
                    </tr>
                    <tr>
                        <td>Return Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docbs']}}</td>
                    </tr>
                    <tr>
                        <td>Invoice No.</td>
                        <td>:</td>
                        <td><b>{{value['resultset_value']['sinvno']}}</b></td>
                    </tr>
                    <tr>
                        <td>BS Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['sinvbs']}}</td>
                    </tr>
                    <tr>
                        <td>Transaction Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docdt']}}</td>  
                    </tr>
                    <tr>
                        <td>Print Date & Time</td>
                        <td>:</td>
                        <td>{{ value['printdate'].strftime('%d/%m/%Y') }} {{ value['printdate'].strftime('%H:%M:%S') }}</td>
                    </tr>
                </tbody>
            </table>
             <div class="theight">
                <table class="collapse_table">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th>H.S.Code</th>
                        <th>Code</th>
                        <th class="desc">Description</th>
                        <th class="rnum">Qty</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                    {% set nctr = -1 %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                            {% set nctr = nctr+1 %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                {% if 'MM001' in value['resultset_value']['lineitems'][nctr]['myvalues'] %}
                                    <td class="num">{{i['myvalues']['MM001']['hsncode']}}</td>
                                {% else %}
                                    <td></td>
                                {% endif %} 
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                    </tbody>
                </table>
            </div>
            <table class="tright" style="border-collapse: collapse;">
                <tbody>
                    <tr>
                        <td class="rnum"><b>Total</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['MTLPRICE']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Discount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        {% if value['resultset_value']['discount'][0] is defined %}
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['discount'][0]['discrate'])}}%</td>
                        {% else %}
                        <td></td>
                        {% endif %}
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Taxable Amount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['VAL1']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Add:VAT</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VATPER'])}}%</td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VAT'])}}</td> 
                    </tr>
                    <tr>
                        <td class="rnum"><b>Net Amount</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;">{{value['resultset_value']['popricingtotal']['VAL2']}}</td>
                    </tr>
                </tbody>
            </table>
           <div>
                <table class="tleft">
                <tbody>
                <tr>
                    <td class="num">Amount in Words:</td>                        <td>{{value['numtoword'].num2words(value['resultset_value']['popricingtotal']['VAL2']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</td>
                    </tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr></tr>
                    <tr>
                        <td class="ltop num">Prepared By</td>
                        <td></td>
                        <td class="ltop num">Receiver's Signature</td>
                    </tr>
                </tbody>
            </table>
            </div>
                <div>
                <br><br><br><br><br><br><br>
                <p class="tright"><b>For  {{value['resultset_value']['CO010']['coname']}}</b></p>
                <p class="tleft">E & OE<br>Goods once sold are not exchangeable or returnable</p>
            </div>
        </div>
    </body>
</html>""",
    "dbtnt":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,tr,th,td{
                font-size: 11px;
                font-family: calibri;
                text-align: left;
            }
            .preinv{
                font-size: 11px;
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
            div.table_items {
                height: 200px !important;
                border: 1px solid #ccc;
            }
            .theight{
                height: 275px;
            }
            .heading{
                font-size: 15px;
                line-height: 0px;
                text-align: left;
                margin-top: 0%;
                padding-top: 0%;
            }
            .collapse_table{
                border-collapse: collapse;
                width: 100%;
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
            .desc{
                padding-right: 150px;
            }
        </style>
    </head>
    <body>
        <div class="preinv">
            <table style="width: 100%; border-bottom: 1px solid black;">
                <tbody>
                    <tr>
                        <td>
                            <img class="imag" src="http://103.146.234.44:8080/img/NGMlogo1.jpg">
                        </td>
                        <td class="heading">
                            {% if value['resultset_value']['status'] != 'C' %}
                                <h2 class="rnum">DEBIT NOTE - DRAFT</h2>
                            {% elif 'prncnt' in value['resultset_value'] %}
                                {% if value['resultset_value']['prncnt'] <= 0 %}
                                     <h2 class="rnum">DEBIT NOTE</h2>
                                {% else %}
                                    <h2 class="rnum">DEBIT NOTE (COPY OF ORIGINAL :  {{value['resultset_value']['prncnt']}} )</h2>
                                {% endif %}
                            {% endif %}
                            <h2>{{value['resultset_value']['CO010']['coname']}}</h2>
                            <p><span style="margin-left: 3mm;"></span>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</p>
                            <p>VAT No. :<span style="margin-left: 3mm;"></span><b>{{value['resultset_value']['CO010']['covatno']}}</b></p>
                            <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OU010']['unitname']}}</b></p> 
                        </td>
                        <td class="tright">
                            <br><br><br>
                            <p>Mode of Payment: Cash Bill</p>
                            <p>Phone No:{{value['resultset_value']['OD10']['phoneno']}}</p>
                        </td>
                    </tr>
                </tbody>
            </table>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td>Buyer's Name</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custname']}}</td>
                    </tr>
                    <tr>
                        <td>Address</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custaddress']}}</td>
                    </tr>
                    <tr>
                        <td>Phone No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['phoneno']}}</td>
                    </tr>
                    <tr>
                        <td>Buyer's VAT No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['vatno']}}</td>  
                    </tr>
                </tbody>
            </table>
            <table class="tright">
                <tbody>
                    <tr>
                        <td>Credit Memo No.</td>
                        <td>:</td>
                        <td><b>{{value['resultset_value']['docno']}}</b></td>
                    </tr>
                    <tr>
                        <td>Credit Memo Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docdt']}}</td>
                    </tr>
                    <tr>
                        <td>BS Invoice Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docbs']}}</td>
                    </tr>
                    <tr>
                        <td>Invoice Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['sinvdate']}}</td>  
                    </tr>
                    <tr>
                        <td>Print Date & Time</td>
                        <td>:</td>
                        <td>{{ value['printdate'].strftime('%d/%m/%Y') }} {{ value['printdate'].strftime('%H:%M:%S') }}</td>
                    </tr>
                </tbody>
            </table>
            <div class="theight">
                <table class="collapse_table">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th>Code</th>
                        <th class="desc">Description</th>
                        <th>Reason</th>
                        <th class="rnum">Qty</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                        {%- for i in value['resultset_value']['lineitems'] %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td>{{i['reason']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                    </tbody>
                </table>
            </div>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td class="num">Amount in Words:</td>
                        <td>{{value['numtoword'].num2words(value['resultset_value']['popricingtotal']['VAL2']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</td> 
                    </tr>
                    <tr><td><br><br></td></tr>
                    <tr>
                        <td style="text-align: center;">{{(value['resultset_value']['USR01']['username'])}}</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td class="ltop" style="text-align: center;">Prepared By</td>
                        <td class="ltop" style="text-align: right;">Receiver's Signature</td>
                    </tr>
                </tbody>
            </table>
            <table class="tright" style="border-collapse: collapse;">
                <tbody>
                    <tr>
                        <td class="rnum"><b>Total</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['MTLPRICE']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Discount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        {% if value['resultset_value']['discount'][0] is defined %}
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['discount'][0]['discrate'])}}%</td>
                        {% else %}
                        <td></td>
                        {% endif %}
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Taxable Amount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['VAL1']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Add:VAT</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VATPER'])}}%</td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VAT'])}}</td> 
                    </tr>
                    <tr>
                        <td class="rnum"><b>Net Amount</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;">{{value['resultset_value']['popricingtotal']['VAL2']}}</td>
                    </tr>
                </tbody>
            </table>
            <div>
                <br><br><br><br><br><br>
                <p class="tright"><b>For  {{value['resultset_value']['CO010']['coname']}}</b></p>
                <p class="tleft">E & OE<br>Goods once sold are not exchangeable or returnable</p>
            </div> 
        </div>
    </body>
</html>""",   
    "crmemo":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,tr,th,td{
                font-size: 11px;
                font-family: calibri;
                text-align: left;
            }
            .preinv{
                font-size: 11px;
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
            div.table_items {
                height: 200px !important;
                border: 1px solid #ccc;
            }
            .theight{
                height: 275px;
            }
            .heading{
                font-size: 15px;
                line-height: 0px;
                text-align: left;
                margin-top: 0%;
                padding-top: 0%;
            }
            .collapse_table{
                border-collapse: collapse;
                width: 100%;
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
            .desc{
                padding-right: 150px;
            }
        </style>
    </head>
    <body>
        <div class="preinv">
            <table style="width: 100%; border-bottom: 1px solid black;">
                <tbody>
                    <tr>
                        <td>
                            <img class="imag" src="http://103.146.234.44:8080/img/NGMlogo1.jpg">
                        </td>
                        <td class="heading">
                            {% if value['resultset_value']['status'] != 'C' %}
                                <h2 class="rnum">CREDIT MEMO - DRAFT</h2>
                            {% elif 'prncnt' in value['resultset_value'] %}
                                {% if value['resultset_value']['prncnt'] <= 0 %}
                                     <h2 class="rnum">CREDIT MEMO</h2>
                                {% else %}
                                    <h2 class="rnum">CREDIT MEMO (COPY OF ORIGINAL :  {{value['resultset_value']['prncnt']}} )</h2>
                                {% endif %}
                            {% endif %}
                            <h2>{{value['resultset_value']['CO010']['coname']}}</h2>
                            <p><span style="margin-left: 3mm;"></span>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</p>
                            <p>VAT No. :<span style="margin-left: 3mm;"></span><b>{{value['resultset_value']['CO010']['covatno']}}</b></p>
                            <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OU010']['unitname']}}</b></p> 
                        </td>
                        <td class="tright">
                            <br><br><br>
                            <p>Mode of Payment: Cash Bill</p>
                            <p>Phone No:{{value['resultset_value']['OD10']['phoneno']}}</p>
                        </td>
                    </tr>
                </tbody>
            </table>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td>Buyer's Name</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custname']}}</td>
                    </tr>
                    <tr>
                        <td>Address</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custaddress']}}</td>
                    </tr>
                    <tr>
                        <td>Phone No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['phoneno']}}</td>
                    </tr>
                    <tr>
                        <td>Buyer's VAT No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['vatno']}}</td>  
                    </tr>
                </tbody>
            </table>
            <table class="tright">
                <tbody>
                    <tr>
                        <td>Credit Memo No.</td>
                        <td>:</td>
                        <td><b>{{value['resultset_value']['docno']}}</b></td>
                    </tr>
                    <tr>
                        <td>Credit Memo Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docdt']}}</td>
                    </tr>
                    <tr>
                        <td>BS Invoice Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docbs']}}</td>
                    </tr>
                    <tr>
                        <td>Invoice Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['sinvdate']}}</td>  
                    </tr>
                    <tr>
                        <td>Print Date & Time</td>
                        <td>:</td>
                        <td>{{ value['printdate'].strftime('%d/%m/%Y') }} {{ value['printdate'].strftime('%H:%M:%S') }}</td>
                    </tr>
                </tbody>
            </table>
            <div class="theight">
                <table class="collapse_table">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th>Code</th>
                        <th class="desc">Description</th>
                        <th>Reason</th>
                        <th class="rnum">Qty</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                        {%- for i in value['resultset_value']['lineitems'] %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td>{{i['reason']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                    </tbody>
                </table>
            </div>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td class="num">Amount in Words:</td>
                        <td>{{value['numtoword'].num2words(value['resultset_value']['popricingtotal']['VAL2']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</td> 
                    </tr>
                    <tr><td><br><br></td></tr>
                    <tr>
                        <td style="text-align: center;">{{(value['resultset_value']['USR01']['username'])}}</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td class="ltop" style="text-align: center;">Prepared By</td>
                        <td class="ltop" style="text-align: right;">Receiver's Signature</td>
                    </tr>
                </tbody>
            </table>
            <table class="tright" style="border-collapse: collapse;">
                <tbody>
                    <tr>
                        <td class="rnum"><b>Total</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['MTLPRICE']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Discount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        {% if value['resultset_value']['discount'][0] is defined %}
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['discount'][0]['discrate'])}}%</td>
                        {% else %}
                        <td></td>
                        {% endif %}
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Taxable Amount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['VAL1']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Add:VAT</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VATPER'])}}%</td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VAT'])}}</td> 
                    </tr>
                    <tr>
                        <td class="rnum"><b>Net Amount</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;">{{value['resultset_value']['popricingtotal']['VAL2']}}</td>
                    </tr>
                </tbody>
            </table>
            <div>
                <br><br><br><br><br><br>
                <p class="tright"><b>For  {{value['resultset_value']['CO010']['coname']}}</b></p>
                <p class="tleft">E & OE<br>Goods once sold are not exchangeable or returnable</p>
            </div> 
        </div>
    </body>
</html>""",
    "crdtnt":"""<!DOCTYPE html>
<html>
    <head>
        <style>
            table,tr,th,td{
                font-size: 11px;
                font-family: calibri;
                text-align: left;
            }
            .preinv{
                font-size: 11px;
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
            div.table_items {
                height: 200px !important;
                border: 1px solid #ccc;
            }
            .theight{
                height: 275px;
            }
            .theight1{
                height: 800px;
            }
            .heading{
                font-size: 15px;
                line-height: 0px;
                text-align: left;
                margin-top: 0%;
                padding-top: 0%;
            }
            .collapse_table{
                border-collapse: collapse;
                width: 100%;
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
            .desc{
                padding-right: 150px;
            }
        </style>
    </head>
    <body>
        <div class="preinv">
            <table style="width: 100%; border-bottom: 1px solid black;">
                <tbody>
                    <tr>
                        <td>
                            <img class="imag" src="http://103.146.234.44:8080/img/NGMlogo1.jpg">
                        </td>
                        <td class="heading">
                            {% if value['resultset_value']['status'] == 'x' %}
                                {% if value['resultset_value']['prncnt'] <= 0 %}
                                    <h2 class="rnum">Invoice - REFUND(COPY OF ORIGINAL)</h2>
                                {% endif %}
                            {% else %}
                            {% if value['resultset_value']['prncnt'] <= 0 %}
                            <h2 class="rnum">Invoice</h2>
                            {% endif %}
                            {% if value['resultset_value']['prncnt'] > 0 %}
                            <h2 class="rnum">Invoice (COPY OF ORIGINAL :  {{value['resultset_value']['prncnt']}})</h2>
                            {% endif %}
                            {% endif %}
                            <h2>{{value['resultset_value']['CO010']['coname']}}</h2>
                            {% if value['resultset_value']['OD10'] is not none %}
                            <h4><span style="margin-left: 3mm;"></span>{{value['resultset_value']['OD10']['address'][0]['postbox']}}</h4>
                            {% else %}
                            <p><span style="margin-left: 3mm;"></span>{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</p>
                            {% endif %}
                            <p>VAT No. :<span style="margin-left: 3mm;"></span><b>{{value['resultset_value']['CO010']['covatno']}}</b></p>
                            {% if value['resultset_value']['OD10']is not none %}
                            <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OD10']['unitidobj']['key2']}}</b></p> 
                            {% else %}
                            <p>Showroom:<span style="margin-left: 3mm;"><b>{{value['resultset_value']['OU010']['unitname']}}</b></p>
                            {% endif %}
                        </td>
                        <td class="tright">
                            <br><br><br>
                            <p>Mode of Payment: Cash Bill</p>
                            <p>Phone No:{{value['resultset_value']['OD10']['phoneno']}}</p>
                        </td>
                    </tr>
                </tbody>
            </table>
            <table class="tleft">
                <tbody>
                    <tr>
                        <td>Buyer's Name</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custname']}}</td>
                    </tr>
                    <tr>
                        <td>Address</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['custaddress']}}</td>
                    </tr>
                    <tr>
                        <td>Phone No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['phoneno']}}</td>
                    </tr>
                    <tr>
                        <td>Buyer's VAT No.</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['vatno']}}</td>  
                    </tr>
                </tbody>
            </table>
            <table class="tright">
                <tbody>
                    <tr>
                        <td>Invoice No.</td>
                        <td>:</td>
                        <td><b>{{value['resultset_value']['sinvno']}}</b></td>
                    </tr>
                    <tr>
                        <td>Bill Issue Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['sinvdate']}}</td>
                    </tr>
                    <tr>
                        <td>BS Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docbs']}}</td>
                    </tr>
                    <tr>
                        <td>Transaction Date</td>
                        <td>:</td>
                        <td>{{value['resultset_value']['docdt']}}</td>  
                    </tr>
                    <tr>
                        <td>Print Date & Time</td>
                        <td>:</td>
                        <td>{{ value['printdate'].strftime('%d/%m/%Y') }} {{ value['printdate'].strftime('%H:%M:%S') }}</td>
                    </tr>
                </tbody>
            </table>
            {% if value['resultset_value']['lineitems']|length <11 %}
            <div class="theight">
                <table class="collapse_table">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th>Code</th>
                        <th class="desc">Description</th>
                        <th class="rnum">Qty</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                     {% if (value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none) and (value['resultset_value']['svitems'][0]['itemcodeobj'] is not none) %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                        {%- for i in value['resultset_value']['svitems'] %}
                        <tr>
                           {% if value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                            <td class="snum">{{loop.index + (value['resultset_value']['lineitems']|length)}}</td>
							{% else %}
								<td class="snum">{{loop.index0 + (value['resultset_value']['lineitems']|length)}}</td>
							{% endif %}
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}
                        {% elif value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                        {% elif value['resultset_value']['svitems'][0]['itemcodeobj'] is not none %}
                        {%- for i in value['resultset_value']['svitems'] %}
                        <tr>
                           {% if value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                            <td class="snum">{{loop.index + (value['resultset_value']['lineitems']|length)}}</td>
							{% else %}
								<td class="snum">{{loop.index0 + (value['resultset_value']['lineitems']|length)}}</td>
							{% endif %}
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}
                        {% endif %}
                    </tbody>
                </table>
            </div>
            {% else %} 
            <div class="theight1">
                <table class="collapse_table">
                    <thead class="tabl">
                        <th class="snum">S.No.</th>
                        <th>Code</th>
                        <th class="desc">Description</th>
                        <th class="rnum">Qty</th>
                        <th class="rnum">Rate</th>
                        <th class="rnum">Amount</th>
                    </thead>
                    <tbody>
                        {% if (value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none) and (value['resultset_value']['svitems'][0]['itemcodeobj'] is not none) %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                        {%- for i in value['resultset_value']['svitems'] %}
                        <tr>
                           {% if value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                            <td class="snum">{{loop.index + (value['resultset_value']['lineitems']|length)}}</td>
							{% else %}
								<td class="snum">{{loop.index0 + (value['resultset_value']['lineitems']|length)}}</td>
							{% endif %}
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}
                        {% elif value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                        {%- for i in value['resultset_value']['lineitems'] %}
                            <tr>
                                <td class="snum">{{loop.index}}</td>
                                <td>{{i['itemcode']}}</td>
                                <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                                <td class="rnum">{{i.qty}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                                <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                            </tr>
                        {% endfor -%}
                        {% elif value['resultset_value']['svitems'][0]['itemcodeobj'] is not none %}
                        {%- for i in value['resultset_value']['svitems'] %}
                        <tr>
                           {% if value['resultset_value']['lineitems'][0]['itemcodeobj'] is not none %}
                            <td class="snum">{{loop.index + (value['resultset_value']['lineitems']|length)}}</td>
							{% else %}
								<td class="snum">{{loop.index0 + (value['resultset_value']['lineitems']|length)}}</td>
							{% endif %}
                            <td>{{i['itemcode']}}</td>
                            <td class="desc">{{i['itemcodeobj']['key2']}}</td>
                            <td class="rnum">{{i.qty}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['rate'])}}</td>
                            <td class="rnum">{{\"%.2f\"|format(i['myvalues']['MTLPRICE'])}}</td>
                        </tr>
                        {% endfor -%}
                        {% endif %}
                    </tbody>
                </table>
            </div>
            {% endif %}
            <table class="tleft">
                <tbody>
                    <tr>
                        <td class="num">Amount in Words:</td>
                        <td>{{value['numtoword'].num2words(value['resultset_value']['popricingtotal']['VAL2']*1.00, 
                        lang = 'en_IN', to = 'currency',currency='INR')|replace('paise', 'paisa')|replace('-', ' ')|title}} Only</td>
                    </tr>
                    <tr><td><br><br></td></tr>
                    <tr>
                        <td style="text-align: center;">{{(value['resultset_value']['USR01']['username'])}}</td>
                        <td></td>
                    </tr>
                    <tr>
                        <td class="ltop" style="text-align: center;">Prepared By</td>
                        <td class="ltop" style="text-align: right;">Receiver's Signature</td>
                    </tr>
                </tbody>
            </table>
            <table class="tright" style="border-collapse: collapse;">
                <tbody>
                    <tr>
                        <td class="rnum"><b>Total</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['MTLPRICE']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Discount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        {% if value['resultset_value']['discount'][0] is defined %}
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['discount'][0]['discrate'])}}%</td>
                        {% else %}
                        <td></td>
                        {% endif %}
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['DISCOUNT'])}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Taxable Amount</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot"></td>
                        <td class="foot">{{value['resultset_value']['popricingtotal']['VAL1']}}</td>
                    </tr>
                    <tr>
                        <td class="rnum">Add:VAT</td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{\"%.2f\"|format(value['resultset_value']['popricingtotal']['VATPER'])}}%</td>
                        <td></td>
                        <td></td>
                        <td class="rnum">{{value['resultset_value']['popricingtotal']['VAT']}}</td> 
                    </tr>
                    <tr>
                        <td class="rnum"><b>Net Amount</b></td>
                        <td></td>
                        <td></td>
                        <td></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;"></td>
                        <td class="foot" style="border-bottom: 1px solid black;">{{value['resultset_value']['popricingtotal']['VAL2']}}</td>
                    </tr>
                </tbody>
            </table>
            <div>
                <br><br><br><br><br><br>
                <p class="tright"><b>For  {{value['resultset_value']['CO010']['coname']}}</b></p>
                <p class="tleft">E & OE<br>Goods once sold are not exchangeable or returnable</p>
            </div> 
        </div>
    </body>
</html>""",
    "vrptsum":"""<!DOCTYPE html>
<html lang="en">
    <head>
       <meta charset="UTF-8">
        <style>
            table,tr,th,td{
                font-size: 8px;
                font-family: calibri;
                text-align: left;
            }
            .preinv{
                font-size: 11px;
                font-family: calibri;
            }
            .tabl{
                border: 1px solid black;
                border-right: none;
                border-left: none;
                text-align: center;
            }
            .imag{
                width: 70px;
                height: 85px;
            }
            div.table_items {
                height: 200px !important;
                border: 1px solid #ccc;
            }
            .theight{
                height: 275px;
            }
            .heading{
                font-size: 15px;
                line-height: 0px;
                text-align: left;
                margin-top: 0%;
                padding-top: 0%;
            }
            .collapse_table{
                border-collapse: collapse;
                width: 100%;
                padding:100px;
                margin-top:10px;
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
            .desc{
                padding-right: 150px;
            }
            .tot{
                width: 100%;
                border-bottom: 1px solid black;
                border-top: 1px solid black;
            }
            .footer{
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                color: black;
                border-top: 1px solid black;
                font-size: 11px;
            }
            .head{
                position: fixed;
                display:block;
                left: 0;
                top: 0;
                width: 100%;
                font-size: 15px;
                line-height: 0px;
                color: black;
                z-index: 999;
            }
            .pagebreak {
                clear: both;
                page-break-before: always;
            }
            .breakhead{
                clear: both;
                page-break-before: always;
                line-height: 0px;
                padding-top:3px;
            }
        </style>
    </head>
    <body>
        <header class="breakhead">
        <h2 class="num">{{value['resultset_value']['coidobj']['key2']}}</h2>
        {% if "OU010" in value['resultset_value'] %}
            {% if value['resultset_value']['OU010']['unitname'] is not none %}
                <p class="num">{{value['resultset_value']['OU010']['unitname']}}</p>
            {% endif %}
        {% endif %}
        {% if "OU010" in value['resultset_value'] %}
            {% if value['resultset_value']['OU010']['address'][0]['adrs1'] is not none %}
                <p class="num" style="font-size:9px;">{{value['resultset_value']['OU010']['address'][0]['adrs1']}}</p>
            {% endif %}
        {% endif %}
        <h2 class="num">VAT Number{{value['resultset_value']['vatno']}}</h2>
        <p class="snum" style="font-size:9px;">Phone:{{value['resultset_value']['CO010']['phoneno']}} Email:</p>
        <br>
        <h4 class="snum" style="font-size:12px;">Consolidated VAT Report Summary</h4>
        <h4 class="snum" style="font-size:11px;">Annexure - 5 details</h4>
        <p class="snum" style="font-size:9px;"><b>From</b> {{value['resultset_value']['fromdate']}} <b>to</b> {{value['resultset_value']['todate']}}</p>
        </header>
        <div>
        <table class="collapse_table">
            <thead class="tabl">
                <th>Slno</th>
                <th>Particular</th>
                <th>From</th>
                <th>To</th>
                <th class="rnum">Count</th>
                <th class="rnum">Exemted Sales</th>
                <th class="rnum">VAT Sales</th>
                <th class="rnum">Total Sales</th>
                <th class="rnum">VAT Amount</th>
                <th>From</th>
                <th>To</th>
                <th class="rnum">Count</th>
                <th class="rnum">Sales Return</th>
                <th class="rnum">VAT Return</th>
                <th class="rnum">Net Sales</th>
                <th class="rnum">Net VAT</th>
            </thead>
            <tbody>
                {%- for i in value['resultset_value']['lineitems'] %}
                <tr>
                    <td>{{i['rpsno']}}</td>
                    <td>{{i['rectype']}}</td>
                    <td>{{i['fyear']}}</td>
                    <td>{{i['sinvno']}}</td>
                    <td class="rnum">{{i['custname']}}</td>
                    <td class="rnum">{{i['panno']}}</td>
                    <td class="rnum">{{i['sinvdate']}}</td>
                    <td class="rnum">{{\"%.2f\"|format(i['mtlprice'])}}</td>
                    <td class="rnum">{{\"%.2f\"|format(i['discount'])}}</td>
                    <td>{{\"%.2f\"|format(i['val1'])}}</td>
                    <td>{{\"%.2f\"|format(i['vat'])}}</td>
                    <td class="rnum">{{\"%.2f\"|format(i['val2'])}}</td>
                    <td class="rnum">{{i['syncwithird']}}</td>
                    <td class="rnum">{{i['isprinted']}}</td>
                    <td class="rnum">{{i['isactive']}}</td>
                    <td class="rnum">{{i['printtime']}}</td>                 
                </tr>
                {% endfor -%}
                <tr class="tot">
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td><b>Total</b></td>
                    <td><b></b></td>
                    <td><b></b></td>
                    <td><b></b></td>
                    <td><b></b></td>
                    <td><b></b></td>   
                </tr>
                </tbody>
        </table>
        </div>                             
        <div>
            <p style="font-size:11px; font-family:calibri;" class="tleft">Printed User:{{(value['resultset_value']['loginempid'])}}<span style="margin-left: 6cm;"></span>Page : {{(value['resultset_value']['pageno'])}} <span style="margin-left: 6cm;"></span>{{ value['printdate'].strftime('%d/%m/%Y') }} {{ value['printdate'].strftime('%H:%M:%S') }}</p>
            <br>
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
from operator import itemgetter
import datetime
class C_validation:
    def M_payments(value):
        try:
            value['d3']=datetime.datetime.now().microsecond//1000
            if value.get('payment') is None:
                value['ERPERRMSG']='Key Error'
                value['d4']=datetime.datetime.now().microsecond//1000
                return value
            for i in value['payment']:
                print(i['aprvdamt'],i['amt'])
                if i['amt']>i['aprvdamt']:
                    value['ERPERRMSG']='Value is greater than approval amount'
                    return value
            #a=sum(list(map(itemgetter(['amt']),value['searchresults'][0]['getrecord']['payment'])))
            a=sum([i['amt'] for i in value['payment']])
            variation_percentage=(value['popricingtotal']['VAL2']/100)*2
            #if str(value['popricingtotal']['VAL2']-variation_percentage<=a>=value['popricingtotal']['VAL2']+variation_percentage):
            if value['popricingtotal']['VAL2']-variation_percentage<=a and value['popricingtotal']['VAL2']+variation_percentage>a:
                return value
            else:
                value['ERPERRMSG']='Payment variation more than +/- 10'
                return value
            return 'some thing else'
        except Exception as e:
            value["ERPERRMSG"]=str(e)+"C_validation"
            return value
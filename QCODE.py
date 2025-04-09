import qrcode,io
import PIL.Image as Image
import base64



class QRCODEE:
    def codess(jsoninformation):
        if not jsoninformation.get('box_size'): jsoninformation['box_size']=6
        if not jsoninformation.get('fill_color'): jsoninformation['fill_color'] = 'black'
        if not jsoninformation.get('back_color'): jsoninformation['back_color'] = 'white'
        if not jsoninformation.get('format'): jsoninformation['format'] = 'png'
        if not jsoninformation.get('border'): jsoninformation['border'] = 1
        qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_M,box_size=jsoninformation['box_size'],border=jsoninformation['border'],)
        qr.add_data(jsoninformation['data'])
        qr.make(fit=True)
        img = qr.make_image(fill_color=jsoninformation['fill_color'], back_color=jsoninformation['back_color'],format=jsoninformation['format'])
        img_byte_arr = io.BytesIO()
        img.save(img_byte_arr, subsampling=0, quality=100)
        jsoninformation['imge']=str(base64.b64encode(img_byte_arr.getvalue()))
        return jsonify(jsoninformation)
        
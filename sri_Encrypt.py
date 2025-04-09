from cryptography.fernet import Fernet
import datetime
class Encryp:
    def encry_file(self,value):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)
        temp={}
        for i in value:
            self.text_bytes = i['content'].encode('utf-8')
            self.encrypted_text = self.cipher_suite.encrypt(self.text_bytes)
            i['encrypted']=self.encrypted_text
            i['encrypt_key']=self.key
            temp[i['id']]=i
        return temp
        
        
    def decry_file(self,value):
        for i in value:
            self.saved_key = value[i]['key']
            self.cipher_suite = Fernet(self.saved_key)
            self.decrypted_text = self.cipher_suite.decrypt(value[i]['content'])
            value[i]['decrypted_text']=self.decrypted_text.decode('utf-8')
            return value
        
    def save_key(self,value):
        with open('C:\\inetpub\\wwwroot\\testing_iis\\keys\\key.txt','a+') as f:
            for i in value:
                f.write("\n"+value[i]['encrypt_key'].decode('utf-8')+' '+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+' '+value[i]['name'])
            return "\n"+value[i]['encrypt_key'].decode('utf-8')+' '+datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")+' '+value[i]['name']

            
    def fetch_key(self,value):
        self.last_line=''
        with open('C:\\inetpub\\wwwroot\\testing_iis\\keys\\key.txt','r') as f:
            for i in value:
                for line in f:
                    if value[i]['name'] in line:
                        self.last_line=line
                value[i]['key']=self.last_line.split(" ")[0].encode('utf-8')
                f.seek(0,0)
        return value
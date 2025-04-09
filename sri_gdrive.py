from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload,MediaFileUpload
from google.oauth2.service_account import Credentials
import io
import tempfile,json
class gdrive:
    def __init__(self):
        #for security purose i have hardcoded the path of json and scope
        self.SERVICE_ACCOUNT_FILE = 'C:\\inetpub\\wwwroot\\testing_iis\\keys\\testing-service.json'
        self.SCOPES = ['https://www.googleapis.com/auth/drive']
        self.credentials = Credentials.from_service_account_file(self.SERVICE_ACCOUNT_FILE, scopes=self.SCOPES)
        self.drive_service = build('drive', 'v3', credentials=self.credentials)

    def find_file(self,value):
        self.res={}
        self.file_name=value['file_name']
        self.results=[self.drive_service.files().list(q=f"name='{i}'", fields="files(id, name)").execute() for i in self.file_name]
        for i in self.results:
            for j in i.values():
                for k in j:
                    self.res[k['id']]=k
        #print(self.res)
        return self.res


    def read_file_content(self,value):
        self.fh = io.BytesIO()
        for i in value:
            self.read_request = self.drive_service.files().get_media(fileId=i)
            downloader=MediaIoBaseDownload(self.fh, self.read_request).next_chunk()
            self.fh.seek(0)
            value[i]['content']=self.fh.read().decode("utf-8")
        return value

    def file_upload(self,value):
        for i in value:
            with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                temp_file.write(value[i]['encrypted'])
                temp_file_path = temp_file.name
            media = MediaFileUpload(temp_file_path, mimetype='text/plain', resumable=True)
            res=self.drive_service.files().update(fileId=value[i]['id'],media_body=media).execute()
        return json.loads(res)


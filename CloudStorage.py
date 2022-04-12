import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access.token = access_token
        
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        
    f = open(file_from, 'rb')
    dbx.files_upload(f.read(), file_to)
    
    def main():
        access_token = 'sl.BFk0Oj_o_4neAYkRNJqf0axu809NKsVRvdZKTmtc-QOmElTRune5XCN2g1xmw8uDqq3kgZJPojd9K-56qLjCVF7pbgln0qDMxoYY91tCPEtzS8Lv7aJK2ki1x_rezZyxwkT76Z8'    
        transferData = TransferData(access_token)
        
    file_from = input("enter the file path to transfer: -")
    file_to = input("enter the full path to upload to dropbox: -")    
    
    transferData.upload_file(file_from, file_to)
    print("file has been moved!!!")
    
    main()    
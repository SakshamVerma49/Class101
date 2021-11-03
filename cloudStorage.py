import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'n1eOruYs7b8AAAAAAAAAAY8Sna0HqK1c8V09x62pDD2gmonxIHy-O7vss8nS2EUB'
    transferData = TransferData(access_token)
    file_from = input("ENTER THE FILE PATH: ")
    file_to = input("ENTER YOUR FILE DESTINATION: ")

    transferData.upload_file(file_from, file_to)
    print("FILE HAS BEEN SUCCESFULLY MOVED!")

main()
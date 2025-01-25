import qrcode

data = input("Data to be Encoded: ")
file_name = input("Enter File Name: ")
file_path = 'C:/Users/coolb/Documents/small projects/beginner_projects/qr/'+ file_name + ".png"

def qr_generator(file_path, data):
    img = qrcode.make(data)
    img.save(file_path)

qr_generator(file_path, data)

print ("QR Created, Check Your Folder for your QRCode")
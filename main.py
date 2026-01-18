import qrcode
import os
import time

print("****************************")
print("*  Your Go-To QR Generator *")
print("****************************")
time.sleep(0.5)
print("\nLet's make some QR codes!\n")
time.sleep(0.5)

url = input("Enter a URL or text for your QR code: ")
filename = input("Enter a filename (default: qr_code.png): ") or "qr_code.png"

desktop = os.path.join(os.path.expanduser("~"), "Desktop")
folder = os.path.join(desktop, "QR_Codes")
os.makedirs(folder, exist_ok=True)

filepath = os.path.join(folder, filename)


def createCode(url, filepath):
    """Generates a QR code from a URL or text and saves it as PNG"""
    img = qrcode.make(url)
    img.save(filepath)
    print(f"\n✅ QR code saved as '{filepath}'! Scan it and see the magic!\n")


if __name__ == "__main__":
    createCode(url, filepath)
    print("Thanks for using your QR code generator! 🚀")

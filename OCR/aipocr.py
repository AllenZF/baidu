from PIL import ImageGrab
from aip import AipOcr

img = ImageGrab.grabclipboard()
img.save("screen.bmp")

APP_ID ='18190804627'
API_KEY = '5cf2e0288dc0413aaa00a288a032d75c'
SECRET_KEY ='644cc3ceeecd482fa9636f91a244b4a2'
client = AipOcr(APP_ID,API_KEY,SECRET_KEY)
def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        return fp.read()
image =  get_file_content("screen.bmp")
text = client.basicAccurate(image)
result = text["words_result"]
L = [i["words"] for i in result]
print(L)
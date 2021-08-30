from PIL import Image, ImageGrab
import pytesseract
import cv2 as cv
from matplotlib import pyplot as plt

#_____________________Fester Threshold: 150-160____________________________
img = cv.imread('natsu.png',0)
ret,thresh1 = cv.threshold(img,155,255,cv.THRESH_BINARY)
ret,thresh2 = cv.threshold(img,155,255,cv.THRESH_BINARY_INV)
images = [img, thresh1, thresh2]
for i in range(3):
    imgplot = plt.imshow(images[i],'gray')
    plt.show()

# If you don't have tesseract executable in your PATH, include the following:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

# 1: ーー夏真っ盛りの長期休暇。
print("1: ーー夏真っ盛りの長期休暇。")
print(pytesseract.image_to_string(Image.open('natsu.png'), lang='jpn'))
print(pytesseract.image_to_string(images[1], lang='jpn'))
print(pytesseract.image_to_string(images[2], lang='jpn'))

# 2: あなたは、４畳半アパートでひとり暇を持てあましている
print("2: あなたは、４畳半アパートでひとり暇を持てあましている")
print(pytesseract.image_to_string(Image.open('2.png'), lang='jpn'))

# 3: 「あぁ、やっと出たわ～。久しぶり、元気にしてるの～？」
print("3: 「あぁ、やっと出たわ～。久しぶり、元気にしてるの～？」")
print(pytesseract.image_to_string(Image.open('3.png'), lang='jpn'))

# 4: おばさん　「ほら、あの、田舎のおばちゃんよ。　最近合ってないから、忘れちゃったでしょ」
print("4: おばさん　「ほら、あの、田舎のおばちゃんよ。　最近合ってないから、忘れちゃったでしょ」")
print(pytesseract.image_to_string(Image.open('4.png'), lang='jpn'))

# 5: 家はね、ちょっとあなたに頼みたいことあるよね～。姉さん、あなたのお母さんに聞いたら、どうせ暇してるだろ～って聞いてちょうどいいわって！
print("5: おばさん 家はね、ちょっとあなたに頼みたいことあるよね～。姉さん、あなたのお母さんに聞いたら、どうせ暇してるだろ～って聞いてちょうどいいわって！")
print(pytesseract.image_to_string(Image.open('5.png'), lang='jpn'))
#pip install pyqrcode
import pyqrcode
#links para virar qrCodes
str = ["a","b","c"] # array
#str = open(r"C:\Users\USUARIO\Desktop\Lista.txt")

#Caminho a ser salvo
caminho = r"C:\Users\USUARIO\Downloads\ABC"

#contador para enumerar os qrcode
count = 0

for x in str:
    url = pyqrcode.create(x)
    count += 1
    print(count)
    url.eps( caminho+str(count)+".eps", scale = 50) #vai salvar em eps melhor para photoshop
    #url.svg()
    #url.png()
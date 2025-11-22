print("Ben bir hesap makinesiyim. Lütfen bana yapmak istediğin işlemi yaz:")
islem = input("* / + - işlemlerinden birini seç:")
birinci_sayi = input("Lütfen ilk sayıyı girin:")
ikinci_sayi = input("Lütfen ikinci sayıyı girin:")
print("İşleminizin sonucu:")
if islem == "+":
  cevap =  int(birinci_sayi) + int(ikinci_sayi)
  print (cevap)
if islem == "-":
  sonuc = int(birinci_sayi) - int (ikinci_sayi)
  print (sonuc)
if islem == "/":
  bolme = int(birinci_sayi) / int (ikinci_sayi)
  print (bolme)
if islem == "*":
  carpma = int(birinci_sayi) * int (ikinci_sayi)
  print (carpma)
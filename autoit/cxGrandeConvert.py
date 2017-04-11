import csv

infile = "d:/pontual/produtos/peso_medida_site_parcial_2017_04_11csv.csv"
outfile = "C:/Users/Heitor/Desktop/install Autoit/Scripts/cxGrande_20170411.au3"

with open(infile) as csvfile, open(outfile, 'w') as autoitfile:
    print("""; cx Grande
; fill in produtos' cx grande data
; generate line-by-line in another language

Func fillInCxGrande($cod, $peso, $dim1, $dim2, $dim3)
   WinActivate("Produto")
   ; Send codigo
   Send("{F3}")
   Send($cod)
   Send("{ENTER}")
   
   Sleep(1200)
   
   ; Double click Peso
   MouseClick("left", 63, 350, 2, 0)
   Send($peso)
   Sleep(300)

   ; Click cx grande
   MouseClick("left", 726, 387, 1, 0)
   
   ; Click Medida #1
   MouseClick("left", 376, 456, 1, 0)
   Send($dim1)

   ; Click Medida #2
   MouseClick("left", 475, 456, 1, 0)
   Send($dim2)
   
   ; Click Medida #3
   MouseClick("left", 575, 456, 1, 0)
   Send($dim3)
   Sleep(300)
   
   ; Click Save
   MouseClick("left", 72, 64, 1, 0)
   Sleep(3000)
EndFunc

""", file=autoitfile)

    reader = csv.reader(csvfile, delimiter=",", quotechar='"')
    # ct = 0
    for row in reader:
        # if ct > 15:
        #    break
            
        # ct += 1
        
        codigo, peso, medidas = row
        peso = peso.replace("kg", "").strip()
        medidas = medidas.replace("cm", "").strip()
        medidas_parts = list(map(str.strip, medidas.lower().split("x")))
        print(medidas_parts)
        dim1 = medidas_parts[0]
        dim2 = medidas_parts[1]
        dim3 = medidas_parts[2]
        
        print('fillInCxGrande("{}", "{}", "{}", "{}", "{}")'.format(codigo, peso, dim1, dim2, dim3), file=autoitfile)

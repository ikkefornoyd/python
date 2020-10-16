harf_lis = {"a":"n","b":"o","c":"p","d":"q","e":"r",
            "f":"s","g":"t","h":"u","i":"v","j":"w",
            "k":"x","l":"y","m":"z"}



a = "acem daha"
cevir_rot = list()
for i in a:
    cevir_rot.append(i)
print(cevir_rot)
metin = ""
for q in range(len(a)):
    a = harf_lis(cevir_rot[q])
    metin += a
print(metin)
import function


if __name__ == "__main__":
    print(function.yazdir())
    aranacak = input("Question: ")
    aranacak = aranacak.split(" ")
    url_al = "+".join(aranacak)

    link = function.url_aldir(url_al)
    r = function.baglan(link)

    soup = function.getHtml(r)
    liste = function.getQuestions(soup)

    alin1 = function.title(soup)
    metn = function.secim_yaptir(alin1)
    secim = int(input(metn))
    secim = int(secim)
    if secim <=len(liste):
        print(len(function.answers(liste[secim-1])))

    else:
        print(f"1-{len(liste)}'e kadar bir sayı girmelisin.")
    
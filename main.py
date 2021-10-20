def Citire_Numere():
    '''
    Citeste n numere intregi
    '''
    lista = []
    numar = int(input("Dati marimea sirului: "))
    for index in range(0, numar):
        Numere = int(input("Dati un nr: "))
        lista.append(int(Numere))
    return lista

def Gasire_Numar_de_la_poz(l, numar, poz):
    '''
    Verifica daca un numar exista in lista data de la pozitia poz pana la final
    :param l: lista de numere intregi
    :param numar: numarul care trebuie gasit
    :param poz: pozitia de la care cautam numarul in lista data
    :return: True daca gasit numarul de la pozitia poz si Fals in caz contrar
    '''
    conf = -1
    for index in range(poz, len(l)):
        if numar == l[index]:
            conf = index
    if conf != -1:
        return True
    else:
        return False
def Suma_Numere_Pare(l):
    '''
    Face suma numerelor pare intregi din lista
    :param l: lista de nr. intregi
    :return: Returneaza suma numerelor pare
    '''
    suma = 0
    for index in l:
        if index % 2 == 0:
            suma = suma + index
    return suma
def test_Suma_Numere_Pare():
    '''
    Functia de test pentru funtia Suma_Numere_Pare
    :return:
    '''
    assert Suma_Numere_Pare([2, 3, 12, 5, 9]) == 14
    assert Suma_Numere_Pare([2, 3, 14, 5]) == 16
    assert Suma_Numere_Pare([4, 5, 6, 7]) == 10
def Afisare_Pare(l):
    '''
    Afiseaza numerele pare din lista o singura data
    :param l: lista de nr intregi
    :return: Lista cu numere pare
    '''
    lista_noua = []
    for index in l:
        if index not in lista_noua and index % 2 == 0:
            lista_noua.append(index)
    return lista_noua
def test_Afisare_Pare():
    '''
    Functia de test petru functia Afisare_Pare
    :return:
    '''
    assert Afisare_Pare([23, 12, 3, 52, 12]) == [12, 52]
    assert Afisare_Pare([2, 12, 3, 52]) == [2, 12, 52]
    assert Afisare_Pare([4, 6, 5]) == [4, 6]
def Inlocuire_lista_cu_Tuplu(l):
    '''
    Inlocuieste fiecare numar din lista cu doi termeni a caror suma dau numar respectiv
    :param l: lista de numere intregi
    :return: lista de tuple-uri
    '''
    suma = 0
    lista_noua = []
    gasit = False
    for index in range(len(l)):
        gasit = False
        if gasit == False:
            for y in range(len(l)):
                for z in range(y + 1, len(l)):
                    if index != y and index != z and y != z:
                        if l[index] == l[y] + l[z]:
                            lista_noua.append((l[y], l[z]))
                            gasit = True
        if gasit == False:
            lista_noua.append(l[index])
    return lista_noua
def test_Inlocuire_lista_cu_Tuplu():
    '''
    Funtia de test pentru funtia Inlocuire_lista_cu_Tuplu
    :return:
    '''
    assert Inlocuire_lista_cu_Tuplu([4, 8, 6, 3, 2, 1]) == [(3, 1), (6, 2), (4, 2), (2, 1), 2, 1]
    assert Inlocuire_lista_cu_Tuplu([2, 32, 122, 12, 1456]) == [2, 32, 122, 12, 1456]
def optiune():
    print("Alege optinea:")
    print("1. Citirea liste")
    print("2. Gasirea elementului de la o pozitie pana la final")
    print("3. Suma numerelor intregi pare din lista")
    print("4. Afisare numere pare")
    print("5. Inlocuirea tabloului cu un tuplu")
    print("6. Refresh")
    print("7. Close")
def test_Gasire_Numar_de_la_poz():
    '''
    Functia de test pentru functia Gasire_Numar_de_la_poz
    :return:
    '''
    assert Gasire_Numar_de_la_poz([2, 32, 122, 12, 1456], 12, 3) is True
    assert Gasire_Numar_de_la_poz([2, 32, 122, 12, 1456], 12, 4) is False
def main():
    test_Gasire_Numar_de_la_poz()
    test_Afisare_Pare()
    test_Suma_Numere_Pare()
    test_Inlocuire_lista_cu_Tuplu()
    while True:
        optiune()
        opt = int(input("Introduceti optiunea dumneavoastra: "))
        if opt == 1:
            l = Citire_Numere()
            print(l)
        elif opt == 2:
            nr = int(input("Introduceti un nr: "))
            poz = int(input("Introduceti o pozitie: "))
            if Gasire_Numar_de_la_poz(l, nr, poz) is True:
                print("DA")
            else:
                print("NU")
        elif opt == 3:
            print(Suma_Numere_Pare(l))
        elif opt == 4:
            print(Afisare_Pare(l))
        elif opt == 5:
            print(Inlocuire_lista_cu_Tuplu(l))
        elif opt == 6:
            main()
        elif opt == 7:
            break
        else:
            print("Optiunea aleasa nu exista")
if __name__ == '__main__':
    main()
import math
import csv
import re

class Hotel:
    def __init__(self, nom, codi_hotel, carrer, numero, codi_barri, codi_postal, telefon, latitud, longitud, estrelles):
        if not isinstance(numero, int) and numero <= 0:
            raise TypeError("numero ha de ser un valor enter positiu")

        if not isinstance(codi_barri, int) or codi_barri <= 0:
            raise TypeError("codi_barri ha de ser un valor enter positiu")
        if not isinstance(estrelles, int) or estrelles <= 0:
            raise TypeError("estrelles ha de ser un valor enter positiu")
        if estrelles < 1 or estrelles > 5:
            raise ValueError("estrelles ha de ser un valor entre 1 i 5")
        
        if not isinstance(latitud, float):
            raise TypeError("latitud ha de ser un valor real")
        
        if not isinstance(longitud, float):
            raise TypeError("longitud ha de ser un valor real")
        
        self.nom = nom
        self.codi_hotel = codi_hotel
        self.carrer = carrer
        self.numero = numero
        self.codi_barri = codi_barri
        self.codi_postal = codi_postal
        self.telefon = telefon
        self.latitud = latitud
        self.longitud = longitud
        self.estrelles = estrelles

    def __str__(self):
        return f"{self.nom} ({self.codi_hotel}) {self.carrer},{self.numero} {self.codi_postal} (barri: {self.codi_barri}) {self.telefon} ({self.latitud},{self.longitud}) {self.estrelles} estrelles" 
    
    def __gt__(self, altre_hotel):
        if self.estrelles > altre_hotel.estrelles:
            return True
        return False
    
    def distancia(self, latitud, longitud):
        if not isinstance(latitud, float):
            raise TypeError("latitud ha de ser un valor real")
        
        if not isinstance(longitud, float):
            raise TypeError("longitud ha de ser un valor real")
        
        RADI_TERRA = 6378.137

        lat1 = math.radians(self.latitud)
        lon1 = math.radians(self.longitud)
        lat2 = math.radians(latitud)
        lon2 = math.radians(longitud)

        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distancia = RADI_TERRA * c

        return distancia
#Ex 2:
def codi_in_llista_hotels(llista_hotels, codi_hotel):
    for hotel in llista_hotels:
        if hotel.codi_hotel == codi_hotel:
            return True
    return False
#Ex 3:
def importar_hotels(fitxer, separador):
    llista_hotels = []
    try:
        csv_file = open(fitxer, 'r', encoding='utf-8')
        next(csv_file)  # Salta la primera línia
        for line in csv_file:
            line = line.strip()  #Eliminar salts de línia
            elements = line.split(separador)  #Dividir els camps segons el separador

            codi_i_nom = elements[0]
            match = re.match(r'(.+) - ([A-Z]{2}-[0-9]{6})', codi_i_nom)
            if not match:
                continue
            codi_hotel = match.group(2)
            nom = match.group(1)

            carrer = elements[1]
            numero = int(elements[2])
            codi_barri = int(elements[3])
            codi_postal = elements[4]
            telefon = elements[5]
            latitud = int(elements[6]) / 1000000
            longitud = int(elements[7]) / 1000000
            estrelles = int(elements[8])
            if not codi_in_llista_hotels(llista_hotels, codi_hotel):
                hotel = Hotel(nom, codi_hotel, carrer, numero, codi_barri, codi_postal, telefon, latitud, longitud, estrelles)
                llista_hotels.append(hotel)
    except FileNotFoundError:
        raise FileNotFoundError("fitxer no trobat")

    print("S'han importat correctament", (len(llista_hotels)), "hotels")
    return llista_hotels


#Ex 4:
class Barri ():
    def __init__(self, nom, codi_districte):
        
        if not isinstance(codi_districte, int) or codi_districte<=0:
            raise TypeError("codi_districte ha de ser un valor enter positiu")
        else:
            self.nom = nom
            self.codi_districte = codi_districte
            
           
    
    def __str__ (self):
        return (self.nom+" (districte: "+str(self.codi_districte)+str(")"))
        
#Ex 5:
def importar_barris(fitxer, separador):
    barris = {}
    try:
        with open(fitxer, "r") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=separador)
            next(csv_reader)
            for linia_separada in csv_reader:
                codi_barri = int(linia_separada[0])
                codi_districte = int(linia_separada[1])
                nom = linia_separada[2].strip()
                barris[codi_barri] = Barri(nom, codi_districte)
        print(f"S'han importat correctament {len(barris)} barris")
        return barris
    except FileNotFoundError:
        print(f"Error: el fitxer {fitxer} no s'ha trobat.")
        raise
    except Exception as e:
        print(f"S'ha produït un error: {e}")
        raise


#Ex 6:
class Districte:
    def __init__(self, nom, extensio, poblacio):
        if not isinstance(poblacio, int) or poblacio <= 0:
            raise TypeError("poblacio ha de ser un valor enter positiu")
        
        if not isinstance(extensio, float) or extensio <= 0:
            raise TypeError("extensio ha de ser un valor real positiu")
        
        self.nom = nom
        self.extensio = extensio
        self.poblacio = poblacio
        self.llista_barris = [] 

    def __str__(self):
        if not self.llista_barris:
            barris_str = "N/D"
        else:
            barris_str = ", ".join(self.llista_barris)
        return f"{self.nom} ({self.extensio} kms2, {self.poblacio} habitants) barris: {barris_str}"

    def densitat(self):
        return self.poblacio / self.extensio 
        
#Ex 7:
def importar_districtes(nom_fitxer, separador):
    try:
        with open(nom_fitxer, 'r', encoding='utf-8') as fitxer:
            linies = fitxer.readlines()

        districtes = {}
        for linia in linies[1:]: 
            linia = linia.strip()
            dades = linia.split(separador)
            
            codi_districte = int(dades[0])
            nom = dades[1]
            extensio = float(dades[2])
            poblacio = int(dades[3])

            if codi_districte not in districtes:
                districtes[codi_districte] = Districte(nom, extensio, poblacio)

        print(f"S'han importat correctament {len(districtes)} districtes")
        return districtes

    except FileNotFoundError:
        raise FileNotFoundError("fitxer no trobat")
    except Exception as e:
        raise e
        
#Ex 8:
def omplir_llista_barris (districtes, barris):
    if any(districte.llista_barris for districte in districtes.values()):
        print("El diccionari de districtes ja conté informació dels barris")
    
    else: 
        for codi_districte, districte in districtes.items ():
            noms_barris = [barri.nom for barri in barris.values() if barri.codi_districte == codi_districte]
            districte.llista_barris = noms_barris
            
#Ex 9:
def mostrar_hotels(llista_hotels):
 
    if not llista_hotels: 
        print("No hi ha hotels")
    else:
        for hotel in llista_hotels:
            print(hotel)
            
#PART 2:
#Ex 1:

def ordenar_per_estrelles(llista_hotels):
    hotels_copia = llista_hotels[:]
    hotels_copia.sort(key=lambda hotel: hotel.estrelles)
    return hotels_copia

#Ex 2:

def mostrar_noms_hotels (llista_hotels):
    for hotel in llista_hotels:
        print (hotel.nom, "("+hotel.codi_hotel+")")

#Ex 3:
def buscar_per_nom(llista_hotels, nom_buscar):
    nom_buscar = nom_buscar.lower()
    hotels_trobats = []
    for hotel in llista_hotels:
        if nom_buscar in hotel.nom.lower():
            hotels_trobats.append(hotel)
    return hotels_trobats

#Ex 4:

def buscar_per_estrelles (llista_hotels, estrelles):
    return list(filter(lambda hotel: hotel.estrelles == estrelles, llista_hotels))
#Ex 5:
def buscar_hotels(llista_hotels):
    criteri = input("Introdueix criteri de cerca (1 - per nom, 2 - per estrelles): ")

    if criteri == '1':
        nom_buscar = input("Introdueix el nom de l'hotel a buscar: ").strip()
        hotels_trobats = buscar_per_nom(llista_hotels, nom_buscar)
        if hotels_trobats:
            print(f"S'han trobat {len(hotels_trobats)} hotels amb aquest nom: ")
            mostrar_noms_hotels(hotels_trobats)
        else:
            print("No s'han trobat hotels.")
    elif criteri == '2':
        while True:
            try:
                estrelles = int(input("Introdueix el número d'estrelles a buscar: "))
                if estrelles < 1 or estrelles > 5:
                    print("Error: el número d'estrelles ha de ser un valor entre 1 i 5.")
                else:
                    break
            except ValueError:
                print("Error: el número d'estrelles ha de ser un valor enter.")

        hotels_trobats = buscar_per_estrelles(llista_hotels, estrelles)

        if hotels_trobats:
            print(f"S'han trobat {len(hotels_trobats)} hotels de {estrelles} estrelles: ")
            mostrar_noms_hotels(hotels_trobats)
        else:
            print("No s'han trobat hotels.")
    else:
        print("Error: criteri de cerca no vàlid.")
        

#Ex 6:
    
def hotel_mes_proper (llista_hotels, latitud, longitud):
    if not llista_hotels:
        return None, None
    else: 
        hotel_proper = llista_hotels[0]
        dist_hotel_proper = llista_hotels[0].distancia (latitud, longitud)
        for hotel in llista_hotels:
            if hotel.distancia (latitud, longitud) <dist_hotel_proper:
                hotel_proper = hotel
                dist_hotel_proper = hotel.distancia (latitud, longitud)
    
        return hotel_proper, dist_hotel_proper



#PART 3

#Ex 1:
    
def ordenar_per_nom (llista_hotels):
    return sorted(llista_hotels, key=lambda hotel: hotel.nom.lower())   

#Ex 2:
def carrers_amb_hotels(llista_hotels):
    carrers = set()
    for hotel in llista_hotels:
        carrers.add(hotel.carrer)
    return list(carrers)


#Ex 3:
    
def estrelles_per_barri(llista_hotels, diccionari_barris):
    dic = {}
    for codi_barri, barri in diccionari_barris.items():
        dic[barri.nom] = [0] * 5

    for hotel in llista_hotels:
        if hotel.codi_barri in diccionari_barris:
            barri = diccionari_barris[hotel.codi_barri].nom
            estrelles = hotel.estrelles
            dic[barri][estrelles - 1] += 1

    return dic

#Ex 4:
def densitat_per_districte(llista_hotels, dic_barris, dic_districtes):
    comptadors = {}

    for hotel in llista_hotels:
        codi_barri = hotel.codi_barri

        if codi_barri in dic_barris:
            codi_districte = dic_barris[codi_barri].codi_districte

            if codi_districte not in comptadors:
                comptadors[codi_districte] = 0
            comptadors[codi_districte] += 1

    densitats = {}
    for codi_districte, num_hotels in comptadors.items():
        if codi_districte in dic_districtes:
            area = dic_districtes[codi_districte].extensio
            if area > 0:
                densitats[codi_districte] = num_hotels / area
            else:
                densitats[codi_districte] = 0

    return densitats


#Ex 5:
    
def modificar_telefons (hotel):
    if hotel.telefon [0] != "+":
        hotel.telefon = "+34"+hotel.telefon

#Ex 7:
    
def estrelles_per_districte (llista_hotels, barris, districtes):
    resultat  = {}
    for districtes in districtes.items():
        resultat [districtes.nom] = [0]*5
    for hotel in llista_hotels:
        estrelles = hotel.estrelles
        barri = barris[hotel.barri] 
        districte = districtes [barri.districte]
        resultat [districte] [estrelles -1] +=1
    return resultat

#Ex 9:
    
def mostrar_menu ():
    print()
    print("--- MENÚ PRINCIPAL ---")
    print("1 - Veure hotels")
    print("2 - Veure hotels per estrelles")
    print("3 - Buscar hotels")
    print("4 - Buscar hotel proper")
    print("\n5 - Llistat alfabètic d'hotels \n6 - Carrers amb hotels \n7 - Estadística de barris \n8 - Estadística per districtes \n9 - Internacionalitzar telèfons\nS - Sortir del programa")
    
separador = ';'

try:
    fitxer_hotels = 'hotels.csv'
    fitxer_barris = 'barris.csv'
    fitxer_districtes = 'districtes.csv'

    llista_hotels = importar_hotels(fitxer_hotels, separador)
    diccionari_barris = importar_barris(fitxer_barris, separador)
    diccionari_districtes = importar_districtes(fitxer_districtes, separador)

except FileNotFoundError as e:
    print(f'Error llegint fitxers: {e}')

except Exception as e:
   print(f'Error processant els fitxers: {e}')

else:
    omplir_llista_barris(diccionari_districtes, diccionari_barris)
    while True:
        mostrar_menu()
        op = input("Introdueix la operació a realitzar: ")
        if (op == "1"):
            mostrar_hotels(llista_hotels)
        elif (op == "2"):
            llista_ordenada_estrelles = ordenar_per_estrelles(llista_hotels)
            mostrar_hotels(llista_ordenada_estrelles)
        elif (op == "3"):
            buscar_hotels(llista_hotels)
        elif (op == "4"):
            try:
                latitud = float(input("Introdueix el valor de latitud del punt des d'on vol buscar un hotel proper: "))
                longitud = float(
                    input("Introdueix el valor de longitud del punt des d'on vol buscar un hotel proper: "))
                hotel_proper, distancia_hotel = hotel_mes_proper(llista_hotels, latitud, longitud)
                print(f"L'hotel més proper és el {hotel_proper} a {distancia_hotel} kms")
            except ValueError:
                print("Error: latitud i longitud han de ser valors reals")
        elif (op == "5"):
            llista_hotels_ordenats = ordenar_per_nom(llista_hotels)
            mostrar_hotels(llista_hotels_ordenats)
        elif (op == "6"):
            llista_carrers = carrers_amb_hotels(llista_hotels)
            print("Hi ha " + str(len(llista_carrers)) + " carrers amb algun hotel: " + str(llista_carrers))
        elif (op == "7"):
            estrelles_barris = estrelles_per_barri(llista_hotels, diccionari_barris)
            for nom_barri, llista_estrelles_barri in estrelles_barris.items():
                print("El barri " + str(nom_barri) + " té " + str(
                    llista_estrelles_barri[0]) + " hotels de 1 estrella, " + str(
                    llista_estrelles_barri[1]) + " hotels de 2 estrelles, " + str(
                    llista_estrelles_barri[2]) + " hotels de 3 estrelles, " + str(
                    llista_estrelles_barri[3]) + " hotels de 4 estrelles, " + str(
                    llista_estrelles_barri[4]) + " hotels de 5 estrelles\n")
        elif (op == "8"):
            diccionari_densitats = densitat_per_districte(llista_hotels, diccionari_barris, diccionari_districtes)
            for codi_districte, densitat in diccionari_densitats.items():
                print("Districte " + str(codi_districte) + ": " + str(densitat) + " hotels/km2\n")
        elif (op == "9"):
            modificar_telefons(llista_hotels)
        elif op == 'S' or op == 's':
            print('Sortint del programa')
            break

        else:
            print('Opció no permesa')

finally:
    print ("© Aiman El Yahyaoui Lazaar & Roger Campos Guilera")

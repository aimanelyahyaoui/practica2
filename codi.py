import math

class Hotel:
    def __init__(self, nom, codi_hotel, carrer, numero, codi_barri, codi_postal, telefon, latitud, longitud, estrelles):
        if not isinstance(numero, int) or numero <= 0:
            raise TypeError("numero ha de ser un valor enter positiu")
        
        if not isinstance(codi_barri, int) or numero <= 0:
            raise TypeError("codi_barri ha de ser un valor enter positiu")
        
        if not isinstance(estrelles, int) or not (1 <= estrelles <= 5):
            raise TypeError("estrelles ha de ser un valor enter positiu")
        
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
#ex 2:
def codi_in_llista_hotels (llista_hotels, codi_hotel):
    if codi_hotel in llista_hotels:
        return True
    else: 
        return False
#Ex 3:
def importar_hotels(nom_fitxer, separador: str = ";"):
    llista_hotels = []
    try:
        with open(nom_fitxer, 'r', encoding='utf-8') as fitxer:
            linies = fitxer.readlines()

            for linia in linies[1:]:
                linia = linia.strip()
                dades = linia.split(separador)

                codi, nom = dades[0].split(' - ')
                habitacions = int(dades[1])
                preu = float(dades[2])
                latitud = float(dades[3]) / 1e6
                longitud = float(dades[4]) / 1e6

                if not codi_in_llista_hotels(llista_hotels, codi_hotel):
                    hotel = Hotel(codi, nom, habitacions, preu, latitud, longitud)
                    llista_hotels.append(hotel)
            print(f"S'han importat correctament {len(llista_hotels)} hotels")
            return llista_hotels

    except FileNotFoundError:
        raise FileNotFoundError("fitxer no trobat")

#Ex 4:
    
class Barri ():
    def __init__(self, nom, codi_districte):
        
        if not isinstance(codi_districte, int) or codi_districte<=0:
            raise TypeError("codi_districte ha de ser un valor enter positiu")
        else:
            self.nom = nom
            self.codi_districte = codi_districte
            
           
    
    def __str__ (self):
        return (self.nom+"(districte:"+str(self.codi_districte)+str(")"))
        
#Ex 5:
def importar_barris(nom_fitxer, separador = ';'):
    diccionari_barris = {}

    try:
        with open(nom_fitxer, 'r', encoding='utf-8') as fitxer:
            for linia in fitxer.readlines()[1:]:
                dades = linia.strip().split(separador)
                codi = int(dades[0])
                nom = dades[1]
                poblacio = int(dades[2])
                area = float(dades[3])

                diccionari_barris[codi] = Barri(codi, nom, poblacio, area)
            print(f"S'han importat correctament {len(diccionari_barris)} barris")
            return diccionari_barris
    except FileNotFoundError:
        raise FileNotFoundError("Fitxer no trobat")
        

#Ex 6:

class Districte:
    def __init__ (self, nom, extensio, poblacio):
        if not isinstance(poblacio, int) or poblacio<=0:
            raise TypeError("població ha de ser un valor enter positiu")
        if not isinstance(extensio, float) or extensio<=0:
            raise TypeError("extensio ha de ser un valor enter positiu")
        
        else:
            self.nom = nom
            self.extensio = extensio
            self.poblacio = poblacio
            self.llista_barris = []
            
        
    def __str__ (self):
        if self.llista_barris == []:
            return (self.nom+"("+str(self.extensio)+"kms2,"+str(self.habitants)+"habitants)"+" "+"barris: N/D") 
        else:
            return (self.nom+"("+str(self.extensio)+"kms2,"+str(self.habitants)+"habitants)"+" "+"barris: "+str(self.llista_barris)) 
   
    def densitat (self):
        return (self.poblacio/self.extensio)  
#Ex 7:
def importar_districtes(nom_fitxer, separador = ';'):
    diccionari_districtes = {}

    try:
        with open(nom_fitxer, 'r', encoding='utf-8') as fitxer:
            for linia in fitxer.readlines()[1:]:
                dades = linia.strip().split(separador)
                codi = int(dades[0])
                nom = dades[1]
                poblacio = int(dades[2])
                area = float(dades[3])

                diccionari_districtes[codi] = Districte(codi, nom ,poblacio, area)

        print(f"S'han importat correctament {len(diccionari_districtes)} districtes")
        return diccionari_districtes
    
    except FileNotFoundError:
        raise FileNotFoundError("Fitxer no trobat")
        
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
    if len(llista_hotels) == 0:
        print("No hi ha hotels")
    else:
        for hotel in llista_hotels:
            print(f"Codi: {hotel.codi}, Nom: {hotel.nom}, Habitacions: {hotel.habitacions}, Preu: {hotel.preu}, Latitud: {hotel.latitud}, Longitud: {hotel.longitud}")
            
#Ex 10:

def mostrar_menu ():
    print("\n--- MENÚ PRINCIPAL ---\n1 - Veure hotels\nS - Sortir del programa")

#Ex 11:
    
def main ():
    llista_hotels = []
    diccionari_barris = {}
    diccionari_districtes = {}
    opcio = 1
    try:
        diccionari_barris = importar_barris("hotels.csv")
        diccionari_districtes = importar_districtes("districtes.csv")
        llista_hotels = importar_hotels("hotels.csv")
    except FileNotFoundError:
        raise ("Error llegint fitxers: ")
    except:
        raise ("Error processant els fitxers: ")
    
    else: 
        omplir_llista_barris(diccionari_districtes, diccionari_barris)
        
        while opcio != "S" or opcio!= "s":
            mostrar_menu()
            opcio = input("Introdueix una opcio: ")
            if opcio == 1:
                mostrar_hotels (llista_hotels)
            if opcio == "s" or opcio == "S":
                print("Sortint del programa")
            else: 
                print("Opció no permesa")
    finally:
        raise ("© Aiman El Yayhoui Lazzar & Roger Campos Guilera")
        

#PART 2:
#Ex 1:
def ordenar_per_estrelles(hotels):
    hotels_copia = hotels[:]
    hotels_copia.sort(key=lambda hotel: hotels.estrelles)
    return hotels_copia

#Ex 2:

def mostrar_noms_hotels (llista_hotels):
    for hotel in llista_hotels:
        print (hotel.nom, "("+hotel.codi+")")

#Ex 3:
def buscar_per_nom(hotels, nom_buscar):
    nom_buscar = nom_buscar.lower()
    hotels_trobats = []
    for hotel in hotels:
        if nom_buscar in hotel.nom.lower():
            hotels_trobats.append(hotel)
    return hotels_trobats

#Ex 4:

def buscar_hotels_per_estrelles (llista_hotels, estrelles):
    sortida = []
    for hotel in llista_hotels:
        if hotel.estrelles >= estrelles:
            sortida.append(hotel)
    return sortida
#Ex 5:
def buscar_hotels(hotels):
    criteri = input("Introdueix criteri de cerca (1 - per nom, 2 - per estrelles): ")

    if criteri == '1':
        nom_buscar = input("Introdueix el nom de l'hotel a buscar: ").strip()
        hotels_trobats = buscar_per_nom(hotels, nom_buscar)
        if hotels_trobats:
            print(f"S'han trobat {len(hotels_trobats)} hotels amb aquest nom: ")
            mostrar_noms_hotels(hotels_trobats)
        else:
            print("No s'han trobat hotels.")
    elif criteri == '2':
        while True:
            try:
                estrelles = int(input("Introdueix el número d'estrelles a buscar: "))
                if 1 <= estrelles <= 5:
                    break
                else:
                    print("Error: el número d'estrelles ha de ser un valor enter.")
            except ValueError:
                print("Error: el número d'estrelles ha de ser un valor entre 1 i 5.")
        
        hotels_trobats = buscar_per_estrelles(hotels, estrelles)

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
                dist_hotel_proper = hotel.distacia (latitud, longitud)
    
        return hotel_proper, dist_hotel_proper

#Ex 7:
def mostrar_menu():
    print()
    print("--- MENÚ PRINICIPAL ---")
    print("1 - Veure hotels")
    print("2 - Veure hotels per estrelles")
    print("3 - Buscar hotels")
    print("4 - Buscar hotel proper")
    print("S - Sortir del programa")
    

#! /usr/bin/python3
from nis import match
from os import remove
from bs4 import BeautifulSoup
import requests
import pandas as pd


url = 'https://www.mundodeportivo.com/resultados/baloncesto/nba/clasificacion'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')


def east():

        
        # Equipos este
        allTeams = soup.find_all('a',href='#')
        estTeamsList = list()


        #Añadir nombres de los equipos este a la lista
        cont = 0
        for i in allTeams:
                if cont < 15:
                        estTeamsList.append(i.text)
                else:
                        break
                cont +=1

        # Puntos este
        estStats = soup.find_all('td',class_='tval text-center')
        estStatsList = list()

        #Añadir estadísticas a los equipos del este
        cont = 0
        for i in estStats:
                if cont < 64:
                        estStatsList.append(i.text)
                else:
                        break
                cont +=1



        #Elimino estos string que no me interesan al estar mezclados con las estadísticas

        estStatsList.remove("PJ")
        estStatsList.remove("PG")
        estStatsList.remove("PP")
        estStatsList.remove("%PG")
        

        #Listas estadísticas
        gamesPlayed = list()
        gamesWon = list()
        gamesLost = list()

        cont = 0
        ind = 0

        #Añadimos los partidos jugados a la lista, siguen una orden de 4 en 4 cada estadística, al estar todas apelotonadas
        while cont < 15:
                gamesPlayed.append(estStatsList[ind])
                ind += 4
                cont += 1

        #Añadimos los partidos ganados
        cont = 0
        ind = 1
        while cont < 15:
                gamesWon.append(estStatsList[ind])
                ind += 4
                cont += 1 

        #Añadimos los partidos perdidos
        cont = 0
        ind = 2
        while cont < 15:
                gamesLost.append(estStatsList[ind])
                ind += 4
                cont += 1 

        print("\nCONFERENCIA ESTE")
        df = pd.DataFrame({'EQUIPO':estTeamsList,' PARTIDOS JUGADOS':gamesPlayed,' PARTIDOS GANADOS':gamesWon, 'PARTIDOS PERDIDOS':gamesLost}, index=list(range(1,16)))
        print(df)

def west():

        
        # Equipos este
        allTeams = soup.find_all('a',href='#')
        westTeamsList = list()


        #Añadir nombres de los equipos este a la lista
        cont = 0
        for i in allTeams:
                if cont < 30:
                        westTeamsList.append(i.text)
                else:
                        break
                cont +=1
       
       #Eliminamos los 15 primeros equipos, ya que son del este y queremos a los del oeste
        cont = 0
        remove_east = list()
        while cont < 15:
                remove_east.append(allTeams[cont].text)
                cont += 1

        cont = 0
        while cont < 15:
                westTeamsList.remove(remove_east[cont])
                cont += 1

        # Puntos oeste
        westStats = soup.find_all('td',class_='tval text-center')
        allStatslist = list()
        westStatsList = list()

        for i in westStats:
                if cont < 143:
                        allStatslist.append(i.text)
                else:
                        break
                cont +=1


        #Añadimos solo las estadísticas del oeste, del 64 al 128
        cont = 64
        while cont < 128:
                westStatsList.append(allStatslist[cont])
                cont += 1
       

          #Elimino estos string que no me interesan al estar mezclados con las estadísticas

        westStatsList.remove("PJ")
        westStatsList.remove("PG")
        westStatsList.remove("PP")
        westStatsList.remove("%PG")

         #Listas estadísticas
        gamesPlayed = list()
        gamesWon = list()
        gamesLost = list()

        cont = 0
        ind = 0

        #Añadimos los partidos jugados a la lista, siguen una orden de 4 en 4 cada estadística, al estar todas apelotonadas
        while cont < 15:
                gamesPlayed.append(westStatsList[ind])
                ind += 4
                cont += 1

        #Añadimos los partidos ganados
        cont = 0
        ind = 1
        while cont < 15:
                gamesWon.append(westStatsList[ind])
                ind += 4
                cont += 1 

        #Añadimos los partidos perdidos
        cont = 0
        ind = 2
        while cont < 15:
                gamesLost.append(westStatsList[ind])
                ind += 4
                cont += 1 

        print("\nCONFERENCIA OESTE")
        df = pd.DataFrame({'EQUIPO':westTeamsList,' PARTIDOS JUGADOS':gamesPlayed,' PARTIDOS GANADOS':gamesWon, 'PARTIDOS PERDIDOS':gamesLost}, index=list(range(1,16)))
        print(df)


while True:
        n = input("Si quieres ver la clasificación NBA ESTE, escribe este \
                       \nSi quieres ver la clasificación NBA OESTE, escribe oeste \
                       \nSi desea salir diga salir \n")

        if n.upper() == "ESTE":
                east()
        elif n.upper() == "OESTE":
                west()
        elif n.upper() == "SALIR":
                exit()
        else:
                print("Se ha equivocado de palabra")
        

        
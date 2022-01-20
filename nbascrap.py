#! /usr/bin/python3
from bs4 import BeautifulSoup
import requests
import pandas as pd



def get_ranking_teams():
        url = 'https://www.mundodeportivo.com/resultados/baloncesto/nba/clasificacion'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        all_teams_soup = soup.find_all('a',href='#')
        all_teams_list = list()

        #Añadir los equipos al array
        for i in all_teams_soup:
                all_teams_list.append(i.text)

        return all_teams_list

def get_ranking_stats():
        url = 'https://www.mundodeportivo.com/resultados/baloncesto/nba/clasificacion'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        all_stats_soup = soup.find_all('td',class_='tval text-center')
        all_stats_list = list()

        #Añadir los equipos al array
        for i in all_stats_soup:
                all_stats_list.append(i.text)

        for i in range(8):
                all_stats_list.remove("PJ")
                all_stats_list.remove("PG")
                all_stats_list.remove("PP")
                all_stats_list.remove("%PG")

       
       

        return all_stats_list

def east():
       
        
        # Equipos este, pasamos los 15 primeros equipos
        east_teams_list = get_ranking_teams()[:15]



        # Puntos este, pasamos las 60 primeras estadísticas
        east_stats_list = get_ranking_stats()[:60]
        

        #Listas estadísticas
        games_played = list()
        games_won = list()
        games_lost = list()

        

       

        #Añadimos los partidos jugados a la lista, siguen una orden de 4 en 4 cada estadística, al estar todas apelotonadas
        cont = 0
        ind = 0
        while cont < len(east_teams_list):
                games_played.append(east_stats_list[ind])
                
                ind += 4
                cont += 1
        

        #Añadimos los partidos ganados
        cont = 0
        ind = 1
        while cont < 15:
                games_won.append(east_stats_list[ind])
                ind += 4
                cont += 1 

        #Añadimos los partidos perdidos
        cont = 0
        ind = 2
        while cont < 15:
                games_lost.append(east_stats_list[ind])
                ind += 4
                cont += 1 
       
        print("\nCONFERENCIA ESTE")
        df = pd.DataFrame({'EQUIPO':east_teams_list,' PARTIDOS JUGADOS':games_played, ' PARTIDOS GANADOS':games_won, ' PARTIDOS PERDIDOS':games_lost}, index=list(range(1,16)))
        print(df)
        print(" ")

def west():
       
        
        # Equipos este, pasamos los 15 primeros equipos
        west_teams_list = get_ranking_teams()[15:30]



        # Puntos este, pasamos las 60 primeras estadísticas
        west_stats_list = get_ranking_stats()[60:120]
        

        #Listas estadísticas
        games_played = list()
        games_won = list()
        games_lost = list()

        

       

        #Añadimos los partidos jugados a la lista, siguen una orden de 4 en 4 cada estadística, al estar todas apelotonadas
        cont = 0
        ind = 0
        while cont < len(west_teams_list):
                games_played.append(west_stats_list[ind])
                
                ind += 4
                cont += 1
        

        #Añadimos los partidos ganados
        cont = 0
        ind = 1
        while cont < len(west_teams_list):
                games_won.append(west_stats_list[ind])
                ind += 4
                cont += 1 

        #Añadimos los partidos perdidos
        cont = 0
        ind = 2
        while cont < len(west_teams_list):
                games_lost.append(west_stats_list[ind])
                ind += 4
                cont += 1 
       
        print("\nCONFERENCIA OESTE")
        df = pd.DataFrame({'EQUIPO':west_teams_list, ' PARTIDOS JUGADOS':games_played, ' PARTIDOS GANADOS':games_won, ' PARTIDOS PERDIDOS':games_lost}, index=list(range(1,16)))
        print(df)
        print()

def get_players_list():
        #Función que devolverá una lista con todos los jugadores
        url = 'https://www.mundodeportivo.com/resultados/baloncesto/nba/estadisticas'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        all_players_soup = soup.find_all('td',class_='tname')
        all_players = list()

         #Guardar los nombres en la lista de todos los jugadores
        cont = 0
        for i in all_players_soup:
                if cont < len(all_players_soup):
                        all_players.append(i.text)
                else:
                        break
                cont +=1

        return all_players

def get_players_stats():
        #Función que devolverá una lista con las asistencias de los jugadores
        url = 'https://www.mundodeportivo.com/resultados/baloncesto/nba/estadisticas'
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')

        all_stats_soup = soup.find_all('td',class_='tval text-center')
        all_stats = list()

         #Guardar los nombres en la lista de todos los jugadores
        cont = 0
        for i in all_stats_soup:
                if cont < len(all_stats_soup):
                        all_stats.append(i.text)
                else:
                        break
                cont +=1


        for i in all_stats:
                if i == "TOTAL":
                        all_stats.remove(i)

        return all_stats


def assists():
        
        #Solo guardaremos los 10 primeros, ya que son los pertenecientes a asistencias
        players_list = get_players_list()[:10]
       

        #Guardamos las 10 primeras asistencias
        assists_list = get_players_stats()[:10]
        


        print("\nRANKING ASISTENCIAS")
        df = pd.DataFrame({'JUGADOR':players_list,' TOTAL':assists_list}, index=list(range(1,11)))
        print(df)
        print(" ")



def blocks():
        
        #Solo guardaremos del 10 al 20 ya que son los pertenecientes a tapones
        players_list = get_players_list()[10:20]
       

        #Guardamos los 10  tapones
        blocks_list = get_players_stats()[10:20]
        

        print("\nRANKING TAPONES")
        df = pd.DataFrame({'JUGADOR':players_list,' TOTAL':blocks_list}, index=list(range(1,11)))
        print(df)
        print(" ")



def points():
        
        #Solo guardaremos del 20 al 30 ya que son los pertenecientes a puntos
        players_list = get_players_list()[20:30]
       

        #Guardamos los 10  puntos
        points_list = get_players_stats()[20:30]
        

        print("\nRANKING PUNTOS")
        df = pd.DataFrame({'JUGADOR':players_list,' TOTAL':points_list}, index=list(range(1,11)))
        print(df)
        print(" ")

def triples():
        
        #Solo guardaremos del 30 al 40 ya que son los pertenecientes a triples
        players_list = get_players_list()[30:40]
       

        #Guardamos los 10  Triples
        triples_list = get_players_stats()[30:40]
        
      
        print("\nRANKING TRIPLES")
        df = pd.DataFrame({'JUGADOR':players_list,' TOTAL':triples_list}, index=list(range(1,11)))
        print(df)
        print(" ")

def rebounds():
        
        #Solo guardaremos del 40 al 50 ya que son los pertenecientes a rebotes
        players_list = get_players_list()[40:50]
       

        #Guardamos los 10  rebotes
        rebounds_list = get_players_stats()[40:50]
        
      
        print("\nRANKING REBOTES")
        df = pd.DataFrame({'JUGADOR':players_list,' TOTAL':rebounds_list}, index=list(range(1,11)))
        print(df)
        print(" ")

def rebounds():
        
        #Solo guardaremos del 40 al 50 ya que son los pertenecientes a rebotes
        players_list = get_players_list()[40:50]
       

        #Guardamos los 10  rebotes
        rebounds_list = get_players_stats()[40:50]
        
      
        print("\nRANKING REBOTES")
        df = pd.DataFrame({'JUGADOR':players_list,' TOTAL':rebounds_list}, index=list(range(1,11)))
        print(df)
        print(" ")

def steals():
        
        #Solo guardaremos del 40 al 50 ya que son los pertenecientes a robos
        players_list = get_players_list()[50:60]
       

        #Guardamos los 10  rebotes
        steals_list = get_players_stats()[50:60]
        
      
        print("\nRANKING ROBOS")
        df = pd.DataFrame({'JUGADOR':players_list,' TOTAL':steals_list}, index=list(range(1,11)))
        print(df)
        print(" ")




def stats_menu():
        while True:
                try:
                        n = int(input("1.Asistencias \
                                \n2.Tapones  \
                                \n3.Puntos  \
                                \n4.Triples  \
                                \n5.Rebotes  \
                                \n6.Robos  \
                                \n7.Volver menú principal \n"))

                        if n == 1:
                                assists()
                        elif n == 2:
                                blocks()
                        elif n == 3:
                                points()
                        elif n == 4:
                                triples()
                        elif n == 5:
                                rebounds()
                        elif n == 6:
                                steals()
                        elif n == 7:
                                main()
                        else:
                                print("Se ha equivocado de tecla")

                except ValueError:
                        print("Debes escribir un número")

        

def main():
        while True:
                try:
                        n = int(input("1.Clasificación conferencia este \
                                \n2.Clasificacion conferencia oeste \
                                \n3.Menú estadísticas \
                                \n4.Salir \n"))

                        if n == 1:
                                east()
                        elif n == 2:
                                west()
                        elif n == 3:
                                stats_menu()
                        elif n == 4:
                                exit()
                        else:
                                print("Se ha equivocado de tecla")
                except ValueError:
                        print("Debes escribir un número")
                        main()
        

main()
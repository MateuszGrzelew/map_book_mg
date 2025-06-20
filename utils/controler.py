import requests
from bs4 import BeautifulSoup
import folium
import re

def get_user_info(users_data: list) -> None:
    for user in users_data:
        print(f"Twój znajomy {user['name']} z miejscowości {user['location']} opublikował {user['posts']} postów.")

def add_user(users_data: list) -> None:
    new_name: str = input('Podaj imię nowego znajomego: ')
    new_location: str = input('Podaj lokalizację: ')
    while True:
        try:
            new_posts: int = int(input('Podaj liczbę postów nowego znajomego: '))
            break
        except ValueError:
            print("Podaj poprawną liczbę całkowitą.")
    users_data.append({'name': new_name, 'location': new_location, 'posts': new_posts})

def remove_user(users_data: list) -> None:
    user_name: str = input('Podaj znajomego do usunięcia: ')
    for user in users_data:
        if user['name'] == user_name:
            users_data.remove(user)
            print(f"Usunięto użytkownika {user_name}.")
            return
    print(f"Nie znaleziono użytkownika o imieniu {user_name}.")

def update_user(users_data: list) -> None:
    user_name: str = input('Podaj imię użytkownika do aktualizacji: ')
    for user in users_data:
        if user['name'] == user_name:
            new_name = input('Podaj nowe imię użytkownika: ')
            new_location = input('Podaj nową lokalizację: ')
            while True:
                try:
                    new_posts = int(input('Podaj nową liczbę postów: '))
                    break
                except ValueError:
                    print("Podaj poprawną liczbę całkowitą.")
            user['name'] = new_name
            user['location'] = new_location
            user['posts'] = new_posts
            print(f"Zaktualizowano dane użytkownika {user_name}.")
            return
    print(f"Nie znaleziono użytkownika o imieniu {user_name}.")

def dms_to_decimal(dms_str: str) -> float:

    dms_str = dms_str.strip()
    pattern = r'(\d+)°(\d+)′(\d+)″([NSEW])'
    match = re.match(pattern, dms_str)
    if not match:
        raise ValueError(f"Niepoprawny format DMS: {dms_str}")
    degrees, minutes, seconds, direction = match.groups()
    degrees = float(degrees)
    minutes = float(minutes)
    seconds = float(seconds)

    decimal = degrees + minutes / 60 + seconds / 3600

    if direction in ['S', 'W']:
        decimal = -decimal
    return decimal

def get_coordinates(city: str) -> list | None:
    url = f'https://pl.wikipedia.org/wiki/{city}'
    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        print(f"Nie udało się pobrać strony dla miasta {city}: {e}")
        return None

    response_html = BeautifulSoup(response.text, 'html.parser')
    longitude_elem = response_html.select('.longitude')
    latitude_elem = response_html.select('.latitude')

    if not longitude_elem or not latitude_elem:
        print(f"Nie znaleziono współrzędnych dla miasta {city}")
        return None

    try:
        longitude = dms_to_decimal(longitude_elem[0].text)
        latitude = dms_to_decimal(latitude_elem[0].text)
    except Exception as e:
        print(f"Błąd parsowania współrzędnych dla miasta {city}: {e}")
        return None

    return [latitude, longitude]

def get_map(users_data: list) -> None:
    map = folium.Map(location=(52.23, 21.00), zoom_start=6)
    for user in users_data:
        coordinates = get_coordinates(user['location'])
        if coordinates is None:
            print(f"Pominięto użytkownika {user['name']} - brak współrzędnych.")
            continue
        folium.Marker(
            location=(coordinates[0], coordinates[1]),
            popup=f"Twój znajomy {user['name']} z miejscowości {user['location']} opublikował {user['posts']} postów."
        ).add_to(map)
    map.save('mapa.html')
    print("Mapa została zapisana jako mapa.html")

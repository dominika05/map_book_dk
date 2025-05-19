def get_user_info(users_data:list)->None:
    for user in users_data:
        print(f'Twój znajomy {user["name"]} z miejscowości {user["location"]} opublikował {user["posts"]} postów.')

def add_user(users_data: list) -> None:
    new_name: str = input('podaj imię nowego znajomego: ')
    new_location: str = input('podaj lokalizację: ')
    new_posts: str = input('podaj liczbę postów: ')
    users_data.append({'name': new_name, 'location': new_location, 'posts': new_posts}, )

def remove_user(users_data: list) -> None:
        user_name: str = input('podaj imie znajomego do usuniecia: ')
        for user in users_data:
            if user['name'] == user_name:
                users_data.remove(user)

def update_user(users_data: list) -> None:
    user_name: str = input('podaj imie uzytkownia do aktualizacji: ')
    for user in users_data:
        if user['name'] == user_name:
            user['name']=input('podaj nowe imie uzytkownika')
            user['location']=input('podaj nowa lokalizacje uzytkowanika')
            user['posts']=input('podaj liczbe postow')

def get_coordinates(city_name: str) -> list:
    import requests
    from bs4 import BeautifulSoup
    url = f"https://pl.wikipedia.org/wiki/{city_name}"
    response = requests.get(url).text
    response_html = BeautifulSoup(response, "html.parser")
    longitude = float(response_html.select(".longitude")[1].text.replace(",", "."))
    latitude = float(response_html.select(".latitude")[1].text.replace(",", "."))
    print(longitude)
    print(latitude)
    return [latitude, longitude]

def get_map(users_data: list) -> None:
    import folium
    m = folium.Map(location=(52.23, 21.0), zoom_start=6)
    for user in users_data:
            folium.Marker(location=get_coordinates(user['location']), popup='https://pl.wikipedia.org/wiki').add_to(m)
    m.save("index.html")


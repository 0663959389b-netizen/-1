import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import os
from dotenv import load_dotenv
import random

load_dotenv()
SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET
))

MOOD_GENRES = {
    "Енергійний": "pop",
    "Сумний": "sad",
    "Щасливий": "happy",
    "Спокійний": "chill"
}

HISTORY = {}

FAV_FILE = os.path.join(os.path.dirname(__file__), "favorites.json")


def load_favorites():
    if os.path.exists(FAV_FILE):
        with open(FAV_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_favorites(favorites):
    with open(FAV_FILE, "w", encoding="utf-8") as f:
        json.dump(favorites, f, ensure_ascii=False, indent=2)


def clear_history(chat_id):
    HISTORY[chat_id] = []


def get_spotify_tracks(mood, count=3, chat_id=None):
    genre = MOOD_GENRES.get(mood, "chill")
    results = sp.search(q=f'genre:{genre}', type="track", limit=50)

    used = set(HISTORY.get(chat_id, [])) if chat_id else set()

    # Фільтруємо треки які ще не показували користувачу
    candidates = [tr for tr in results["tracks"]["items"] if tr["id"] not in used]

    # Перемішуємо результати, щоб вибрати випадкові треки
    random.shuffle(candidates)

    tracks = []
    for tr in candidates:
        tracks.append({
            "id": tr["id"],
            "title": tr["name"],
            "artist": tr["artists"][0]["name"],
            "link": tr["external_urls"]["spotify"]
        })
        if len(tracks) == count:
            break

    if chat_id:
        HISTORY.setdefault(chat_id, []).extend(t["id"] for t in tracks)

    return tracks


def add_favorite(chat_id, track_dict):
    favorites = load_favorites()
    key = str(chat_id)
    favorites.setdefault(key, [])
    favorites[key].append(track_dict)
    save_favorites(favorites)


def remove_favorite(chat_id, track_id):
    favorites = load_favorites()
    key = str(chat_id)
    favorites[key] = [t for t in favorites.get(key, []) if t["id"] != track_id]
    save_favorites(favorites)


def get_favorites(chat_id):
    return load_favorites().get(str(chat_id), [])


def main():
    print(get_spotify_tracks("Сумний", 3))
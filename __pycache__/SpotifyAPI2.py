import spotipy
import speech_recognition as sr
from spotipy.oauth2 import SpotifyClientCredentials

# 音声入力を取得する
r = sr.Recognizer()
with sr.Microphone() as source:
    print("何か話してください...")
    audio = r.listen(source)

# 音声をテキストに変換する
try:
    text = r.recognize_google(audio, language='ja-JP')
    print("音声入力：", text)
except sr.UnknownValueError:
    print("音声を認識できませんでした")
except sr.RequestError as e:
    print("音声認識サービスでエラーが発生しました； {0}".format(e))


client_id = '932524c170c94ec29f08e49b3785b873'
client_secret = '60b31c57dec04378af17f4a3d4f59fc6'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

keyword = text

results = sp.search(q=keyword, limit=1, market="JP")
if len(results['tracks']['items']) > 0:
    track = results['tracks']['items'][0]
    print(track['name'])
else:
    print("曲が見つかりませんでした")

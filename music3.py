import speech_recognition as sr
import urllib.parse
import urllib.request
import json
import pyaudio
import os


# 録音する時間（秒）
RECORD_SECONDS = 5

# 録音用の設定
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

# Google Speech Recognition APIキー
API_KEY = "YOUR_API_KEY"

# 録音開始
r = sr.Recognizer()
with sr.Microphone() as source:
    print("曲を再生してください。")
    audio = r.record(source, duration=RECORD_SECONDS)

# Google Speech Recognition APIを使用して音声をテキストに変換
text = r.recognize_google(audio, key=API_KEY, language="ja-JP")
print("認識結果: " + text)

# 曲名を検索して取得
query = urllib.parse.quote(text)
url = "https://itunes.apple.com/search?term=" + query + "&limit=1"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
title = data['results'][0]['trackName']

# 曲名を表示
print("曲名: " + title)

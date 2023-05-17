import speech_recognition as sr
import pyaudio

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


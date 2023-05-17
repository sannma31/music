import speech_recognition as sr
import turtle

# タートルを作成する
t = turtle.Turtle()

# 音声入力を取得する
r = sr.Recognizer()
with sr.Microphone() as source:
    print("何か話してください...")
    audio = r.listen(source)

# 音声をテキストに変換する
try:
    text = r.recognize_google(audio, language='ja-JP')
    print("音声入力：", text)
    # 音声をコマンドに解釈する
    if '左' in text:
        t.left(90)
    elif '右' in text:
        t.right(90)
    elif '前' in text:
        t.forward(50)
    elif '後' in text:
        t.backward(50)
    else:
        print("不明なコマンドです。")
except sr.UnknownValueError:
    print("音声を認識できませんでした")
except sr.RequestError as e:
    print("音声認識サービスでエラーが発生しました； {0}".format(e))

# ウィンドウを開いてタートルを表示する
turtle.done()

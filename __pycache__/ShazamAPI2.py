import sounddevice as sd
import soundfile as sf
import shazamio
from pydub import AudioSegment
import os

class MyShazam(shazamio.Shazam):

    def recognize(self, audio_data, sample_rate):
        return self.recognize_audio(audio_data, sample_rate)

    def recognize_audio(self, audio_data, sample_rate):
        result = self.shazam_request(audio_data, sample_rate)
        return result
    
    def recognize_url(self, url):
        audio_file = AudioSegment.from_file(url)
        audio_file.export("audio.wav", format="wav")
        result = self.recognize_file("audio.wav")
        os.remove("audio.wav")
        return result

    def recognize_file(self, audio_file):
        audio_data, sample_rate = sf.read(audio_file, dtype="int16")
        result = self.recognize(audio_data, sample_rate)
        return result

# Shazam APIの設定
shazam = MyShazam("63a3c56cbbmsh242c4e7e7f4e849p1a76a7jsnab41a9632208")

# マイクの設定
duration = 10  # 録音時間(秒)
fs = 44100  # サンプリング周波数

# 録音
print('Recording started...')
recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()

# 録音ファイルの保存
filename = 'recording.wav'
sf.write(filename, recording, fs)

# 録音ファイルから音声認識
print('Recognizing...')
result = shazam.recognize_file(filename)

# 結果の表示
if result['matches']:
    title = result['matches'][0]['title']
    artist = result['matches'][0]['subtitle']
    print(f'Title: {title}')
    print(f'Artist: {artist}')
else:
    print('No match found.')

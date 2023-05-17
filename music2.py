import librosa
import sounddevice as sd

# 音楽ファイルを読み込む
y, sr = librosa.load('path/to/music_file.mp3')

# 音楽を再生する
sd.play(y, sr)

# 音楽情報を解析する
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
chroma = librosa.feature.chroma_stft(y=y, sr=sr)
mfccs = librosa.feature.mfcc(y=y, sr=sr)

# 解析結果を表示する
print(f"Tempo: {tempo}")
print(f"Beat frames: {beat_frames}")
print(f"Chroma: {chroma}")
print(f"MFCCs: {mfccs}")

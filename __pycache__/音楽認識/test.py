import librosa
import librosa.display
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt

# 1. 音声ファイルの読み込み
filename = 'sample_music.mp3'
y, sr = librosa.load(filename)

# 2. 音声データの前処理
S = librosa.feature.melspectrogram(y, sr=sr, n_mels=128, fmax=8000)
log_S = librosa.power_to_db(S, ref=np.max)

# 3. スペクトル解析による周波数特徴量の抽出
mfcc = librosa.feature.mfcc(S=log_S, n_mfcc=20)

# 4. 機械学習モデルによる音楽ジャンルの分類または曲の識別
model = tf.keras.models.load_model('music_genre_classification_model.h5')
pred = model.predict(mfcc.T)
genre_labels = ['classical', 'country', 'disco', 'hiphop', 'jazz', 'metal', 'pop', 'reggae', 'rock']
predicted_genre = genre_labels[np.argmax(pred)]

# 結果の表示
print('Predicted genre:', predicted_genre)
plt.figure(figsize=(10, 4))
librosa.display.specshow(mfcc, x_axis='time')
plt.colorbar()
plt.title('MFCC')
plt.tight_layout()
plt.show()

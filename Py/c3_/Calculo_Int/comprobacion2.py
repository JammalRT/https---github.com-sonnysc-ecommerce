import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt

y, sr = librosa.load(audio_file)

plt.figure(figsize=(10, 4))
librosa.display.waveshow(y, sr=sr)
plt.title("Forma de Onda del Audio")
plt.xlabel("Tiempo (segundos)")
plt.ylabel("Amplitud")
plt.show()

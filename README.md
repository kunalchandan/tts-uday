# Text to Speech
```
pip install virtualenv

virtualenv venv
source venv/bin/activate

pip install TTS

python tts.py

for i in *.wav; do ffmpeg -i "$i" -f mp3 "${i%}.mp3"; done
```
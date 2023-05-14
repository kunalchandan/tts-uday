# Text to Speech
Instructions
```bash
pip install virtualenv

virtualenv venv
source venv/bin/activate

pip install TTS

python tts.py

for i in *.wav; do ffmpeg -i "$i" -f mp3 "${i%}.mp3"; done

mkdir mp3
mv *.mp3 mp3/

ls -1 Medical_chemistry_p* | awk '$0="file \""$0"\""' | sed "s/\"/'/g" > list1.txt
ffmpeg -f concat -i list1.txt -c copy Medical_chemistry_full.mp3
ls -1 Medical_biology_p* | awk '$0="file \""$0"\""' | sed "s/\"/'/g" > list2.txt
ffmpeg -f concat -i list2.txt -c copy Medical_biology_full.mp3
```

I don't own the IP for the documents `Medical biology.txt` and `Medical chemistry.txt`
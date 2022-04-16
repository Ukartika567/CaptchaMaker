# AudioCaptcha 

from captcha.audio import AudioCaptcha

audio = AudioCaptcha()

audio_captcha = audio.generate('685726')

print(audio.write('685726', 'audiCaptch2.wav'))
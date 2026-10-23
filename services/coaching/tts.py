from io import BytesIO
from gtts import gTTS



from io import BytesIO
from gtts import gTTS


class TextToSpeech:
    def speak(self, text, lang="en"):
        cleaned = (text or "").strip()

        if not cleaned:
            print("TTS Error: Empty text received")
            return None

        try:
            buffer = BytesIO()

            gTTS(text=cleaned, lang=lang).write_to_fp(buffer)

            audio_bytes = buffer.getvalue()

            if not audio_bytes:
                print("TTS Error: Generated audio is empty")
                return None

            print(f"TTS generated {len(audio_bytes)} bytes")
            return audio_bytes

        except Exception as e:
            print(f"TTS Error: {e}")
            return None

    
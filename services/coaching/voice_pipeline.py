
import time
import streamlit as st


class VoicePipeline:
    def __init__(self, llm, tts):
        self.llm = llm
        self.tts = tts
        self.last_spoken_at = 0

    def _find_form_issue(self, exercise, metrics):
        if "issue" in metrics and metrics["issue"]:
            return metrics["issue"]

        if exercise == "Squats":
            depth = metrics.get("depth_status", "")
            back_angle = metrics.get("back_angle", 180)

            if depth == "TOO HIGH":
                return (
                    "Your squat is not deep enough. "
                    "Bend your knees a little more."
                )

            if isinstance(back_angle, (int, float)) and back_angle < 130:
                return (
                    "You are leaning too far forward. "
                    "Keep your chest up."
                )

        elif exercise == "Push-ups":
            alignment = metrics.get("body_alignment", "")
            hip_status = metrics.get("hip_status", "")

            if alignment == "Poor Form":
                return "Keep your body straight during the push-up."

            if hip_status == "SAGGING":
                return "Your hips are sagging. Keep your body straight."

            if hip_status == "PIKED UP":
                return "Lower your hips to maintain a straight body line."

        elif exercise == "Biceps Curls (Dumbbell)":
            swing = metrics.get("swing_status", "")
            shoulder = metrics.get("shoulder_status", "")

            if swing == "SWINGING":
                return "Stop swinging your body. Keep your torso still."

            if shoulder == "ELBOW DRIFTING":
                return "Keep your elbows close to your sides."

        elif exercise == "Shoulder Press":
            back_arch = metrics.get("back_arch_status", "")

            if back_arch == "Excessive Arch":
                return (
                    "You are arching your lower back too much. "
                    "Brace your core."
                )

            if back_arch == "Slight Arch":
                return "Brace your core and keep your back stable."

        elif exercise == "Lunges":
            balance = metrics.get("balance_status", "")

            if balance == "OFF BALANCE":
                return (
                    "You are losing balance. "
                    "Keep your feet about hip-width apart."
                )

        return None

    def process_event(self, event, exercise, metrics):
        issue = self._find_form_issue(exercise, metrics)
        now = time.time()

        major_events = {
            "workout_started",
            "set_completed",
            "workout_completed",
        }

        is_major_event = event in major_events

        if not is_major_event:
            if not issue:
                return None

            if now - self.last_spoken_at < 5:
                return None

        try:
            text = self.llm.give_feedback(event, issue)

            if not text or not text.strip():
                print("VoicePipeline: LLM returned empty feedback.")
                return None

            audio_bytes = self.tts.speak(text)

            if not audio_bytes:
                print("VoicePipeline: TTS returned no audio.")
                return None

            self.last_spoken_at = now

            print(f"VoicePipeline: Generated {len(audio_bytes)} bytes.")

            return audio_bytes, text

        except Exception as e:
            print(f"VoicePipeline error: {e}")
            return None


def autoplay_audio(audio_bytes):
    """Render an audio player in the main Streamlit script."""
    if not audio_bytes:
        st.warning("No audio was generated.")
        return

    st.audio(
        audio_bytes,
        format="audio/mpeg",
        autoplay=False,
    )

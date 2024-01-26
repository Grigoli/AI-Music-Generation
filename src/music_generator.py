import datetime
import wave
import numpy as np
from audiocraft.models import MusicGen

# Initialize the model
model = MusicGen.get_pretrained('facebook/musicgen-small')

# Set generation parameters
model.set_generation_params(duration=16)

# Function to generate and save music
def generate_and_save_tune(prompt):
    results = model.generate([prompt])
    sampling_rate = model.sample_rate

    audio_data = results[0].numpy()
    audio_data = (audio_data * 32767).astype(np.int16)  # Convert to 16-bit PCM

    # Generate a timestamped filename
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"outputs/output_{timestamp}.wav"

    try:
        with wave.open(filename, 'w') as wf:
            wf.setnchannels(1)  # Mono channel
            wf.setsampwidth(2)  # 2 bytes for 16-bit audio
            wf.setframerate(sampling_rate)
            wf.writeframes(audio_data.tobytes())
        print(f"Generated music saved as '{filename}'")
    except Exception as e:
        print(f"Error saving the file: {e}")


prompt = "Upbeat, energetic pop dance track with catchy electronic beats, synth melodies, and a memorable hook suitable for TikTok dance challenges"

# Get user input for the music prompt
# prompt = input('Enter a music prompt (e.g., "classic rock song"): ')


generate_and_save_tune(prompt)
# If you want to play the audio automatically, you will need an external library.

# AI Music Generation Project

## Overview
This Python project utilizes the `audiocraft` library to generate music based on user-defined prompts. The script uses a pre-trained model from `facebookresearch/audiocraft` to generate short audio clips. This tool is particularly useful for creating music pieces such as upbeat, energetic pop dance tracks suitable for platforms like TikTok.

## Features
- Music generation using `audiocraft`'s `MusicGen` model.
- Customizable music prompts for generating different styles.
- Output audio saved in WAV format.

## Requirements
- Python 3.x
- audiocraft
- numpy
- wave

## Installation
1. Ensure that Python 3 is installed on your system.
2. Install the required Python packages:
   ```
   pip install audiocraft numpy wave
   ```

## Usage
1. Initialize the `MusicGen` model and set the desired generation parameters.
2. Call `generate_and_save_tune(prompt)` with a music prompt of your choice. For example, `"Upbeat, energetic pop dance track with catchy electronic beats, synth melodies, and a memorable hook suitable for TikTok dance challenges"`.
3. The generated music will be saved as `output.wav` in the current directory.

### Example:
```python
prompt = "Your music style prompt here"
generate_and_save_tune(prompt)
```

## Customization
You can customize the music generation by changing the `prompt` variable. The script currently sets a default prompt for an upbeat and energetic pop dance track, but this can be modified to any style as per your preference.

## Note
- The current script does not include automatic playback of generated music. For playback, you will need to use an external library or play the `output.wav` file with a standard audio player.
- The generation time and output quality can vary based on the complexity of the prompt and system capabilities.

## License
Please ensure to comply with the licensing terms of `audiocraft` and the `facebookresearch/audiocraft` project. The use of generated music is subject to the terms and conditions of these libraries.

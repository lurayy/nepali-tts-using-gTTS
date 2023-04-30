import torch
import numpy as np
from scipy.io.wavfile import write

# Load the Tacotron 2 model
tacotron2 = torch.hub.load('nvidia/DeepLearningExamples:main',
                           'nvidia_tacotron2')
tacotron2 = tacotron2.to('cpu')
tacotron2.eval()

# Load the WaveGlow model
waveglow = torch.hub.load('nvidia/DeepLearningExamples:main',
                          'nvidia_waveglow')
waveglow = waveglow.to('cpu')
waveglow.eval()

# Set the text to be synthesized
text = "Hello world, I missed you so much."

# Load the TTS utilities
utils = torch.hub.load('nvidia/DeepLearningExamples:main', 'nvidia_tts_utils')

# Prepare the input sequence
sequences, lengths = utils.prepare_input_sequence([text])

# Generate the mel spectrogram with Tacotron 2
with torch.no_grad():
    mel, _, _ = tacotron2.infer(sequences, lengths)

# Synthesize audio with WaveGlow
with torch.no_grad():
    audio = waveglow.infer(mel)

# Convert audio to NumPy array and write to file
audio_numpy = audio[0].data.cpu().numpy()
rate = 22050
write("audio.wav", rate, audio_numpy)

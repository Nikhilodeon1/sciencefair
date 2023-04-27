def transcript():
    import wave
    import pyaudio
    import torch
    import torchaudio
    from playsound import playsound
    torch.random.manual_seed(0)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    from torchaudio.utils import download_asset
    #================================================================
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    seconds = 5.5
    filename = "output.wav"
    plopity = pyaudio.PyAudio()  # Create an interface to PortAudio
    playsound("noise.mp3", block = False)
    stream = plopity.open(format=sample_format, channels=channels, rate=fs, frames_per_buffer=chunk, input=True)
    frames = []  # Initialize array to store frames
    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)
    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    plopity.terminate()
    #idk bruv, im bored
    playsound("noise2.wav", block = False)
    # Save the recorded data as a WAV file
    wf = wave.open('C:\\Users\\nikhi\\Downloads\\Codes\\ScienceFairProject\\{}'.format(filename), 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(plopity.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    #================================================================
    SPEECH_FILE = download_asset("C:\\Users\\nikhi\\Downloads\\Codes\\ScienceFairProject\\output.wav")
    bundle = torchaudio.pipelines.WAV2VEC2_ASR_BASE_960H
    model = bundle.get_model().to(device)
    waveform, sample_rate = torchaudio.load(SPEECH_FILE)
    waveform = waveform.to(device)
    if sample_rate != bundle.sample_rate:
        waveform = torchaudio.functional.resample(waveform, sample_rate, bundle.sample_rate)
    with torch.inference_mode():
        emission, _ = model(waveform)
    class GreedyCTCDecoder(torch.nn.Module):
        def __init__(self, labels, blank=0):
            super().__init__()
            self.labels = labels
            self.blank = blank
        def forward(self, emission: torch.Tensor) -> str:
            indices = torch.argmax(emission, dim=-1)  # [num_seq,]
            indices = torch.unique_consecutive(indices, dim=-1)
            indices = [i for i in indices if i != self.blank]
            return "".join([self.labels[i] for i in indices])
    decoder = GreedyCTCDecoder(labels=bundle.get_labels())
    transcript = decoder(emission[0])
    #transcript = "PLAY|HEAT|WAVES"
    print(transcript)
    return transcript
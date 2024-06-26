import pyaudio

class PyAudioInputStream:
    def __init__(self, sample_rate: int, chunk_size: int):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=sample_rate,
            input=True,
            frames_per_buffer=chunk_size
        )

    def read(self, chunk_size: int):
        try:
            return self.stream.read(chunk_size, exception_on_overflow=False)
        except IOError as e:
            print(f"Error reading audio stream: {e}")
            return None

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()

class PyAudioOutputStream:
    def __init__(self, sample_rate: int):
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=sample_rate,
            output=True
        )

    def write(self, data: bytes):
        self.stream.write(data)

    def close(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()



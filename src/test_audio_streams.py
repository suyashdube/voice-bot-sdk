from voice_bot.audio_stream import PyAudioInputStream, PyAudioOutputStream
import time

def test_audio_streams():
    sample_rate = 16000
    chunk_size = 2048

    input_stream = PyAudioInputStream(sample_rate, chunk_size)
    output_stream = PyAudioOutputStream(sample_rate)

    print("Recording... Speak into the microphone.")
    start_time = time.time()
    while time.time() - start_time < 5:  # Record for 5 seconds
        data = input_stream.read(chunk_size)
        output_stream.write(data)

    print("Finished recording.")
    input_stream.close()
    output_stream.close()

if __name__ == "__main__":
    test_audio_streams()

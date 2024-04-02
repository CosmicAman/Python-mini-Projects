import pyaudio
import wave


FORMAT = pyaudio.paInt16  
CHANNELS = 2             
RATE = 44100            
CHUNK = 1024            
RECORD_SECONDS = 100      
OUTPUT_FILENAME = "output.wav"  


audio = pyaudio.PyAudio()


stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

print("Recording...")

frames = []


for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        try:
            data = stream.read(CHUNK)
            frames.append(data)
        except KeyboardInterrupt:
            print("Recording interrupted.") #ctrl+c to stop recording
            break

print("Finished recording.")


stream.stop_stream()
stream.close()
audio.terminate()


with wave.open(OUTPUT_FILENAME, 'wb') as wf:
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))

print(f"Audio saved to {OUTPUT_FILENAME}")

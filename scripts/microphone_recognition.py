'''
Microphone recognition test script. Repeatedly asks for microphone input and recognizes using the ca-ca model. 
Uses SpeechRecognition module to connect to Sphinx. Sphinx (sphinxbase and pocketsphinx) and pocketsphinx-python module should be installed.
ca-ca directory should be placed under the SpeechRecognition module directory (.../python3.6/site-packages/speech_recognition/pocketsphinx-data)
'''

import _thread
import pyaudio
import wave
import speech_recognition as sr
import os
import sys

WORKING_DIR = 'recorded'

#WAV properties
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024

#other parameters
SEGMENT_END_BUFFER = 0.15

def input_thread(a_list):
	input()
	a_list.append(True)

def record_audio(WAVE_OUTPUT_FILENAME, FORMAT, CHANNELS, RATE, CHUNK, raw_output=False):
	a_list = []
	_thread.start_new_thread(input_thread, (a_list,))

	# start Recording
	audio = pyaudio.PyAudio()
	stream = audio.open(format=FORMAT, channels=CHANNELS, 
						rate=RATE, input=True, frames_per_buffer=CHUNK)
	print("recording...")
	frames = []

	while not a_list:
		data = stream.read(CHUNK)
		frames.append(data)
	print("finished recording")
	# stop Recording
	stream.stop_stream()
	stream.close()
	audio.terminate()

	#Write to file
	if raw_output == False:
		waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
		waveFile.setnchannels(CHANNELS)
		waveFile.setsampwidth(audio.get_sample_size(FORMAT))
		waveFile.setframerate(RATE)
		waveFile.writeframes(b''.join(frames))
		waveFile.close()
	else:
		rawbytes = b''.join(frames)
		with open(RAW_OUTPUT_FILENAME, 'wb') as f:
			f.write(rawbytes)

def run_microphone_recognizer(working_dir_name, recognizer):
	WAVE_OUTPUT_FILENAME = WORKING_DIR + '.wav'
	TXT_OUTPUT_FILENAME = WORKING_DIR + '.lab'

	wav_out = os.path.join(working_dir_name, WAVE_OUTPUT_FILENAME)
	txt_out = os.path.join(working_dir_name, TXT_OUTPUT_FILENAME)

	#record from microphone
	frames = record_audio(wav_out, FORMAT, CHANNELS, RATE, CHUNK)
	 
	# read the entire audio file
	with sr.AudioFile(wav_out) as source:
	     audio = recognizer.record(source)  

	#recognize speech using Sphinx
	try:
		result = r.recognize_sphinx(audio, language="ca-ca")
		return result
	except sr.UnknownValueError:
		print("Sphinx could not understand audio")
	except sr.RequestError as e:
		print("Sphinx error; {0}".format(e))
	except Exception as e:
		print(e)

	return None

def write_to_text(transcription, out_dir, out_file):
	txt_out = os.path.join(out_dir, out_file)
	with open(txt_out, 'w') as f:
		f.write(transcription)

if __name__ == '__main__':
	#load recognition tools
	r = sr.Recognizer()
	TXT_OUTPUT_FILENAME = WORKING_DIR + '.txt'

	if not os.path.exists(WORKING_DIR):
		os.makedirs(WORKING_DIR)

	while True:
		key_input = input("Start recording? ")
		print(key_input)
		if key_input == "n" or key_input=="N":
			sys.exit()
		elif key_input == "y" or key_input=="Y" or key_input=="":
			#run recognition
			mic_transcript = run_microphone_recognizer(WORKING_DIR, r)
			write_to_text(mic_transcript, WORKING_DIR, TXT_OUTPUT_FILENAME)
			print(mic_transcript)

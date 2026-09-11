# Voice Calculator Project

*This project represents a clean learning outcome of Voice Recognition Systems,where the code starts by importing the necessary libraries, 
then defines the functions that handle the logical steps required to transform raw voice input into the final result. Finally,
the main functionality is implemented using a clean while loop.*

## This project depends on understanding the following steps:
1. Recording the voice and saving it in a file with a .wav extension → using libraries such as sounddevice and wavio.
2. STT (Speech-to-Text) is the second step → using Whisper AI model to convert the recorded audio into text.
3. Using the text command obtained from the previous step to execute a specific action →
 this could be used to manage an electronic device, such as in IoT.
4. The operations, such as recording, saving the WAV file, transcribing the file,
 and executing commands, are preferably defined as functions to be called later.

## To run this code, you may need to install the following packages:
1. sounddevice → Used to record audio.
2. wavio → Used to save the recorded audio as a .wav file.
3. openai-whisper → Used to convert the recorded audio into text.
4. re -> Very important to separate the numbers from the text.

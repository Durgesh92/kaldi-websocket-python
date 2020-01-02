#!/usr/bin/python3

from vosk import Model, KaldiRecognizer
import sys
import json

if len(sys.argv) != 3:
    print ("Usage: ./test_local <model_dir> <audio_file>")
    exit(1)

model = Model(sys.argv[1])
rec = KaldiRecognizer(model, 16000.0)

wf = open(sys.argv[2], "rb")
wf.read(44) # skip header

while True:
    data = wf.read(2000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        res = json.loads(rec.Result())
        print (res)
    else:
        res = json.loads(rec.PartialResult())
        print (res)

res = json.loads(rec.FinalResult())
print (res)

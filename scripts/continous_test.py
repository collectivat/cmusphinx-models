#!/usr/bin/python

from os import environ, path

from pocketsphinx import *
from sphinxbase import *

SCRIPTPATH = path.dirname(os.path.realpath(__file__))
BASEDIR = os.path.join(SCRIPTPATH, '..')

config = Decoder.default_config()
config.set_string('-hmm', path.join(BASEDIR, 'ca-es/acoustic-model'))
config.set_string('-lm', path.join(BASEDIR, 'ca-es/language-model.lm.bin'))
config.set_string('-dict', path.join(BASEDIR, 'ca-es/pronounciation-dictionary.dict'))
config.set_string('-logfn', '/dev/null')
decoder = Decoder(config)

stream = open(path.join(BASEDIR, 'scripts/test_wavs/test_ca-es.raw'), 'rb')

in_speech_bf = False
decoder.start_utt()
while True:
    buf = stream.read(1024)
    if buf:
        decoder.process_raw(buf, False, False)
        if decoder.get_in_speech() != in_speech_bf:
            in_speech_bf = decoder.get_in_speech()
            if not in_speech_bf:
                decoder.end_utt()
                print(decoder.hyp().hypstr)
                decoder.start_utt()
    else:
        # the last buffered stream
        print(decoder.hyp().hypstr)
        break
decoder.end_utt()

# -*- coding: utf-8 -*-

import os
from pocketsphinx import AudioFile, get_model_path, get_data_path

def simple_decode(config):
    # simple decode
    audio = AudioFile(**config)
    for phrase in audio:
        print(phrase)

def decode_with_time_stamp(config):
    # with time axis
    fps = config['frate']
    for phrase in AudioFile(**config):
        print('-' * 28)
        print('| %5s |  %3s  |   %5s   |' % ('start', 'end', 'word'))
        print('-' * 29)
        for s in phrase.seg():
            print('| %4ss | %4ss | %9s |' % (s.start_frame / fps,
                                             s.end_frame / fps,
                                             s.word))
        print('-' * 29)

def keyword_spotting(config):
    # keyword spotting
    if not config.get('keyphrase'):
        raise ValueError('no keyphrase given for spotting')
    fps = config['frate']
    config['lm'] = False
    config['kws_threshold'] = 1e-20
    audio = AudioFile(**config)
    for phrase in audio:
        for s in phrase.seg():
            print(s.start_frame / fps,
                  s.end_frame / fps, 
                  s.word)

def keyword_list_spotting(config):
    # uses a file for inputting the keywords
    if not config.get('kws'):
        raise ValueError('no keywords file given for spotting')
    if not os.path.isfile(config['kws']):
        raise IOError('keywords file does not exist %s'%config['kws'])
    fps = config['frate']
    config['lm'] = False
    audio = AudioFile(**config)
    for phrase in audio:
        for s in phrase.seg():
            print(s.start_frame / fps,
                  s.end_frame / fps, 
                  s.word,
                  s.prob)

def grammar_search(config):
    # search via jsgf queries
    # for Java Speech grammar format check https://www.w3.org/TR/jsgf/
    if not config.get('jsgf'):
        raise ValueError('no jsgf file given for grammar search')
    if not os.path.isfile(config['jsgf']):
        raise IOError('grammar file does not exist %s'%config['jsgf'])
    fps = config['frate']
    config['lm'] = False
    config['jsgf'] = 'n.gram'
    config['keyphrase'] = None
    audio = AudioFile(**config)
    for phrase in audio:
        for s in phrase.seg():
            print(s.start_frame / fps,
                  s.end_frame / fps, 
                  s.word)

if __name__ == "__main__":
    base_path = ''
    config = {
        'verbose': False,
        'audio_file': os.path.join(base_path, 'scripts/test_wavs/test_ca-es.wav'),
        'buffer_size': 2048,
        'no_search': False,
        'full_utt': False,
        'keyphrase': False,
        'kws': False,
        'jsgf': False,
        'hmm': os.path.join(base_path, 'ca-es/acoustic-model'),
        'lm': os.path.join(base_path, 'ca-es/language-model.lm.bin'),
        'dict': os.path.join(base_path, 'ca-es/pronounciation-dictionary.dict'),
        'frate': 100 # frames per second (default=100)
    }
    if not os.path.exists(config.get('hmm')):
        raise IOError('no %s directory for acoustic models'%config['hmm'])
    simple_decode(config)
    decode_with_time_stamp(config)
    config['keyphrase'] = 'batalla'
    keyword_spotting(config)
    config['kws'] = os.path.join(base_path, 'scripts/test.kws')
    keyword_list_spotting(config)
    config['jsgf'] = os.path.join(base_path, 'scripts/n.gram')
    grammar_search(config)

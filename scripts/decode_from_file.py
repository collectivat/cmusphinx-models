import os
import speech_recognition as sr

file_path = os.path.dirname(os.path.realpath(__file__))
project_path = os.path.abspath(os.path.join(file_path,'..'))
test_file_ca = os.path.join(file_path,'test_wavs','test_ca-es.wav')

def main(language='ca-es', wav=test_file_ca):
    hmmd, lmd, dictd = get_model_path(language)
    language_tuple = (hmmd, lmd, dictd)

    r = sr.Recognizer()
    with sr.AudioFile(wav) as source:
        audio = r.record(source)

    result = r.recognize_sphinx(audio,language=language_tuple)
    print(result)

def get_model_path(language=None):
    language_path = os.path.join(project_path,language)
    hmm_path = os.path.join(language_path,'acoustic-model')
    lm_file = os.path.join(language_path,'language-model.lm.bin')
    dict_file = os.path.join(language_path,'pronounciation-dictionary.dict')
    for prequisit in [language_path, hmm_path, lm_file, dict_file]:
        if not os.path.exists(prequisit):
            raise IOError('%s does not exits'%prequisit)
    return hmm_path, lm_file, dict_file

if __name__ == '__main__':
    main()

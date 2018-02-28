# CMU Sphinx Models
The repository of acoustic and language models, and the tools to download raw 
data and train them. Currently only for Catalan.

The models are trained with *sphinxtrain 5prealpha*.

## Requirements
For basic setup, one needs to install *PocketSphinx*. For Debian systems:

```
sudo apt-get install pocketsphinx
```

You can also compile directly from the 
[releases](https://cmusphinx.github.io/wiki/download/), or from the source
code in [github](https://github.com/cmusphinx) or 
[sourceforge](https://sourceforge.net/p/cmusphinx/code/HEAD/tree/). The 
installation steps are explained in the official 
[CMU Sphinx tutorials](https://cmusphinx.github.io/wiki/tutorialpocketsphinx/).

The test scripts are tested for Python 3.5.2, and in order for them to run,
`pocketsphinx` and `SpeechRecognition` modules are needed. You can install them
by:
```
pip3 install -r requirements.txt
```

## Catalan
*_WARNING:_* _The current models are here as placeholders. Do not expect 
to be able to use them for practical speech recognition tasks._

All the files necessary for pocketsphinx, i.e. the language model, phonetic 
dictionary and the acoustic models are in `ca-ca` directory. The model files 
are:

```
ca-ca
 ├─ pronounciation.dict       (Phonetic dictionary)
 ├─ language-model.lm.bin     (Language model)
 └─ acoustic-model            (Acoustic model)
    ├─ feat.params
    ├─ mdef
    ├─ means
    ├─ mixture_weights
    ├─ noisdict
    ├─ transition_matrices
    └─ variances
```

In order to test the models, simply execute:
```
$ python script/decode_from_file.py
la seva abraçada havia estat una batalla el clímax una victòria
```

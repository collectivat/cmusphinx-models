# CMU Sphinx Models
The repository of acoustic and language models, and the tools to download raw data and train them. Currently only for Catalan.

The models are trained with *sphinxtrain 5prealpha*.

## git clone

Once you have complete the standard `git clone` you also need `git-lfs`.

The first time you need to:

```
sudo apt-get install git-lfs
git lfs install
```

and then every time:

```
git lfs pull
```

## Requirements
For basic setup, one needs to install *PocketSphinx*. For Debian systems:

```
sudo apt-get install pocketsphinx
```

You can also compile directly from the [releases](https://cmusphinx.github.io/wiki/download/), or from the source code in [github](https://github.com/cmusphinx) or [sourceforge](https://sourceforge.net/p/cmusphinx/code/HEAD/tree/). The installation steps are explained in the official [CMU Sphinx tutorials](https://cmusphinx.github.io/wiki/tutorialpocketsphinx/).

The test scripts are tested for Python 3.5.2, and in order for them to run, `pocketsphinx` and `SpeechRecognition` modules are needed. You can install them by:
```
sudo apt-get install swig
sudo apt-get install libpulse-dev
pip3 install -r requirements.txt
```

## Catalan
### Models

All the files necessary for pocketsphinx, i.e. the language model, phonetic dictionary and the acoustic models are in `ca-es` directory. The model files are:

```
ca-es
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
$ python scripts/decode_from_file.py
la seva abraçada havia estat una batalla el clímax una victòria
```

### Corpus
The 240 hour acoustic corpus can be downloaded from [here](http://laklak.eu/share/tv3_0.3.tar.gz). The installation scripts for training will be coming soon. 

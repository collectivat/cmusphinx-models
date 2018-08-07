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

All the files necessary for pocketsphinx, i.e. the language model, phonetic dictionary and the acoustic models are in `ca-ca` directory. The model files are:

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
$ python scripts/decode_from_file.py
la seva abraçada havia estat una batalla el clímax una victòria
```

### Corpus
It _will be_ possible to download the audio corpus with the transcriptions and run `sphinxtrain`. For that, the script `setup_corpus.sh` is provided. It downloads a tar.gz archive which has the audio corpus with the necessary directory structure for `sphinxtrain`. Extracts it and writes the configuration file.

> **Note:** The `setup_corpus.sh` is not working yet. However the 240 hour acoustic corpus can be downloaded from [here](http://laklak.eu/share/tv3_0.3.tar.gz).

```
$ source scripts/setup_corpus.sh
--2018-03-01 16:51:23--  https://transfer.sh/ZPZ0C/ca-ca-0.1.gpg
Resolving transfer.sh (transfer.sh)... 185.216.24.82
Connecting to transfer.sh (transfer.sh)|185.216.24.82|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 5465467 (5,2M) []
Saving to: ‘ca-ca-0.1.gpg’

(...)

gpg: AES encrypted data
gpg: encrypted with 1 passphrase
PROJECT_PATH is /home/collectivat/scripts/encryption_tests
SPHINX_LIB_PATH is /home/collectivat/scripts/sphinx/5prealpha
filling the config file /home/collectivat/scripts/tests/ca-ca-0.1/etc/sphinx_train.cfg
$ cd ca-ca-0.1
$ sphinxtrain run
```

The tar archive is currently encrypted. In the process, you will be prompted for the pass key by the `setup_corpus.sh`. For the encryption `gpg` version 1.4.20 is used.

The configuration file might need to be modified for the local machine, for example for the number of cores which needs to be used. For details consult the [CMUSphinx tutorials](https://cmusphinx.github.io/wiki/tutorialam/#setting-up-the-training-scripts).

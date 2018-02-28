# CMU Sphinx Models
The repository of acoustic and language models, and the tools to download raw 
data and train them. Currently only for Catalan.

## Catalan
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

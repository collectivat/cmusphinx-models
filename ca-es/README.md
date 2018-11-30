### Corpus and training information

This is the Catalan acoustic models for CMUSphinx decoders. The audio corpus 
consists of 240 hours of recordings from public Catalan television, and 320 
hours of recordings from the Catalan Parliament (Parlament de Catalunya). For 
the training `sphinxtrain` version 5pre-alpha was used.

The acoustic models were trained with 16kHz and mono audios, and trained for
continous speech using 8000 tied states and 32 Gaussian mixture models.

The tests were made with 4 hours of data using `sphinxtrain`'s decode process 
and the final WER (word error rate) is 6,9% for an ideal audio data set with
a language model decoding seen text. For details more details please consult 
Külebi, Öktem 2018, which outlines the preparation of the TV3Parla corpus. The
training details of the current version are identical to the ones explained in 
the paper.
<https://www.isca-speech.org/archive/IberSPEECH_2018/abstracts/IberS18_P1-2_Kulebi.html>

### Revision log

* _0.4:_ Using 240 hours of TV3Parla plus 320 hours of ParlamentParla corpus
* _0.3:_ Using 240 hours of audio with improved language models
* _0.2:_ Using 100 hours of uncleaned corpus
* _0.1:_ Initial experimental commit

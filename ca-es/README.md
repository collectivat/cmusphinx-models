### Corpus and training information

This is the Catalan acoustic models for CMUSphinx decoders. The audio corpus 
consists of 240 hours of recordings from public Catalan television. For the 
training `sphinxtrain` version 5pre-alpha was used. 

The acoustic models were trained with 16kHz and mono audios, and trained for
continous speech using 6000 tied states and 32 Gaussian mixture models.

The tests were made with 4 hours of data using `sphinxtrain`'s decode process 
and the final WER (word error rate) is 11,68% for an ideal audio data set. 
Currently the models are the pre-release version, i.e. not ready to be used 
in practical applications. 

### Revision log

* _0.3:_ Using 240 hours of audio with improved language models
* _0.2:_ Using 100 hours of uncleaned corpus
* _0.1:_ Initial experimental commit

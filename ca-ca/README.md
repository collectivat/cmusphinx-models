### Corpus and training information

This is the Catalan acoustic models for CMUSphinx decoders. The audio corpus 
consists of 30 hours of recordings from public Catalan television. For the 
training `sphinxtrain` version 5pre-alpha was used. 

The acoustic models were trained with 16kHz and mono audios, and trained for
continous speech. 

The tests were made with 4 hours of data using `sphinxtrain`'s decode process 
and the final WER (word error rate) is 41.5%. Currently the models are the 
pre-release version, i.e. not ready to be used in practical applications. The
main issues for the high error rate is the alignment problems and the unclean
text.

### Revision log

* _0.1:_ Initial experimental commit

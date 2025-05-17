# NLP

- Natural language processing
- Generation
- Speech recognition

## Evolution of NLP

1. Symbolic NLP - manually defined rules on templates
    - if else 
2. Statistical NLP - statistical information associated with "words"
    - parsing into verbs, nouns, etc. 
    - create a parse tree
3. Neural NLP - transformers

## Pre train, fine tune paradigm

Problem - having to pretrain from scratch for every problem
Solution - train on a simple task to learn language generally.
    - then fine tune on specific tasks - quicker
    - no need to learn language priors

Pre training
- cloze task
    - filling in correct word
- predicting next word

## Hallucination

Web is 45TB, models are around 800GB. Data is compressed into the most statistically likely data. 

## Emergent behaviour

From next token prediction, the models are able to reason. 


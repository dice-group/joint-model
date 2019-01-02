# Getting Started

This repository contains the source code and dataset for the paper _'Semantic-based Jointly Learning From Social Media and
 Environmental Data For Disaster Prediction'_ by Hamada Zahera, Mohamed Ahmed Sherif and Axel Ngonga

Our approach predicts the typhoon intensity via a joint learning from social media and environmental data. 


---This repository is still under construction---


### Prerequisites

install the requirements via

```
pip install -r requirements.txt

```
### TED Dataset
We provide the typhoon environmental data and tweets ids into TED Dataset folder. Since Twitter terms do not allow public sharing of tweets, only the tweet ids of the tweets will be provided. To download the full tweets data, please use Twitter API tool such as twarc

```
https://github.com/DocNow/twarc

```
On the other hand, we used the standford sentiment dataset (sentiment140) to train our feature extractor model on labeled tweets. Please download the dataset via the following link
```
http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip
```
### Semantic Enriched Word Embedding ###
We trained a domain specific word embedding model on typhoon tweets and sentiment140 dataset. As discussed in the paper (see section 4.1), we enriched the word embedding model by represented entities in tweets with their semantic vectors from the knowledge graph ([Conceptnet](http://conceptnet.io/)).

ConceptNet represents entities and their relationship as semantic vectors and achieved the state-of-the-art performances into different semantics tasks, more information can be found in the [project website.](https://github.com/commonsense/conceptnet-numberbatch)
### Models
We made available the source code of baselines and proposed models into jupyter notebooks. 

- **Demo_1** explores the performance of baseline model (RNN) and proposed model (LSTM+RNN)
- **Demo_2** explores the performance of baseline model (DNN) and proposed model (LSTM+DNN)
- **Demo_3** explores the impact of semantics embedding in LSTM+RNN model
- **Demo_4** explores the impact of semantics embedding in LSTM+DNN model

To run the above-mentioned demos, we provide a preprocessed dataset (training and testing batches) which have been preprocessed in our experiments.
### Contact

Please contact hamada.zahera@upb.de in case you have any questions.

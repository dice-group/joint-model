# Getting Started

This repository contains the source code and dataset for "Semantic-based End-to-End Learning for Typhoon Intensity Prediction" 

In this work, we consider social media as a supplementary source of knowledge in addition to environmental data. We propose the combination of semantically-enriched word embedding model to represent entities in tweets with their semantics representations computed with the traditional word2vec. Moreover,we study how social media users interact during typhoons-in termsof volume and sentiments of tweets- and the correlation with typhoon intensity. Based on these insights, we build a joint model that learns from disaster-related tweets and environmental data to improve prediction. 

![alt text](https://www.dropbox.com/s/bvdc485pzd4lebe/JointModel-Extension.png?dl=0)
 
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
- **Demo_5** explores SVM as a baseline from traditional machine learning approaches.
- **Demo_6** explores the performance of SOAT baselines (CNN and BiLSTM) and our proposed approach (BiLSTM+CNN)

To run the above-mentioned demos, we provide a preprocessed dataset which have been preprocessed in our experiments.
### Contact

Please contact hamada.zahera@upb.de in case you have any questions.

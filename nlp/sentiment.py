#!/usr/bin/env python

# Author:   Alexandre Tea <alexandre.qtea@gmail.com>
# File:     /Users/alexandretea/Work/sentiment-analysis/nlp/SentimentAnalyzer.py
# Purpose:  Module containing classes to classify a sentence by sentiment
# Created:  2016-09-11 18:25:44
# Modified: 2016-09-12 12:18:39

import nlp.extractors as extractors
import sys
import nltk
from nltk.tokenize import word_tokenize
from nltk.classify import apply_features

POSITIVE = True
NEGATIVE = False


class TrainingDataExtractor(extractors.BaseExtractor):

    def parse_data(self, line):
        return (line[2:], (line[0] == '1'))


class Classifier:
    """ Classifies a sentence as positive or negative.
        Needs NLTK's punkt module to work.
    """

    def __init__(self, extractor, valid_score=0.6):
        self.extractor = extractor
        self.word_features = nltk.FreqDist()
        self.training_dataset = None
        self.classifier = None
        self.valid_score = valid_score
        self.classifier = None

    @staticmethod
    def tokenize(sentence):
        return [x.lower() for x in word_tokenize(sentence) if len(x) > 2]

    def extract_features(self, tokens):
        features = {}
        for feature in self.word_features:
            features[feature] = (feature in tokens)
        return features

    def digest_training_sentence(self, raw_data):
        sentiment = raw_data[1]
        features = Classifier.tokenize(raw_data[0])
        self.word_features += nltk.FreqDist(features)

        if self.training_dataset is None:
            self.training_dataset = apply_features(self.extract_features,
                                                   [(features, sentiment)])
        else:
            self.training_dataset += apply_features(self.extract_features,
                                                    [(features, sentiment)])

    def digest_training_file(self, dataset):
        for raw_data in self.extractor.extract_from_file(dataset):
            self.digest_training_sentence(raw_data)

    def train(self):
        self.classifier = nltk.NaiveBayesClassifier.train(self.training_dataset)

    def classify(self, sentence):
        prob = self.classifier.prob_classify(
            self.extract_features(Classifier.tokenize(sentence))
        )
        if prob.prob(True) > self.valid_score:
            return True
        elif prob.prob(False) > self.valid_score:
            return False
        return None


class Analyzer:

    def __init__(self, training_datasets, extractor=TrainingDataExtractor()):
        sys.setrecursionlimit(50000)
        self.classifier = Classifier(extractor)
        for dataset in training_datasets:
            self.classifier.digest_training_file(dataset)
        self.classifier.train()

    def run_cli(self):
        while True:
            sentence = input("Sentence: ")
            if len(sentence) == 0:
                break
            sentiment = self.classifier.classify(sentence)
            if sentiment is None:
                print("Neutral")
            else:
                print("Positive" if sentiment else "Negative")

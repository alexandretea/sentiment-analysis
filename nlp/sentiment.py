#!/usr/bin/env python

# Author:   Alexandre Tea <alexandre.qtea@gmail.com>
# File:     /Users/alexandretea/Work/sentiment-analysis/nlp/SentimentAnalyzer.py
# Purpose:  TODO (a one-line explanation)
# Created:  2016-09-11 18:25:44
# Modified: 2016-09-11 21:16:04

import nlp.extractors as extractors

POSITIVE = True
NEGATIVE = False


class TrainingDataExtractor(extractors.BaseExtractor):

    def parse_data(self, line):
        return (line[2:], (line[0] == '1'))


class Classifier:

    def __init__(self, extractor):
        self.extractor = extractor

    def train_with_file(self, dataset):
        for raw_data in self.extractor.extract_from_file(dataset):
            print(raw_data)


class Analyzer:

    def __init__(self, training_datasets, extractor=TrainingDataExtractor()):
        self.classifier = Classifier(extractor)
        for dataset in training_datasets:
            self.classifier.train_with_file(dataset)

    def run_cli(self):
        pass

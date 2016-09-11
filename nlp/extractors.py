#!/usr/bin/env python

# Author:   Alexandre Tea <alexandre.qtea@gmail.com>
# File:     /Users/alexandretea/Work/sentiment-analysis/nlp/extractors.py
# Purpose:  TODO (a one-line explanation)
# Created:  2016-09-11 20:44:40
# Modified: 2016-09-11 21:00:50

import utils


class BaseExtractor:

    def parse_data(self, line):
        raise NotImplemented("parse_data")

    def extract_from_file(self, path):
        with open(path, "r") as f:
            is_start = True
            lines = []

            while is_start or len(lines) != 0:
                is_start = False
                lines = utils.read_n_lines(f)
                for line in lines:
                    yield self.parse_data(line)

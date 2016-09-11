#!/usr/bin/env python

# Author:   Alexandre Tea <alexandre.qtea@gmail.com>
# File:     /Users/alexandretea/Work/sentiment-analysis/utils.py
# Purpose:  TODO (a one-line explanation)
# Created:  2016-09-11 20:52:38
# Modified: 2016-09-11 20:59:21

from itertools import islice


def read_n_lines(f, n=15):
    return [x.strip() for x in islice(f, n)]

#!/usr/bin/env python

# Author:   Alexandre Tea <alexandre.qtea@gmail.com>
# File:     /Users/alexandretea/Work/sentiment-analysis/sentiment-analyzer.py
# Purpose:  TODO (a one-line explanation)
# Created:  2016-09-11 18:07:59
# Modified: 2016-09-11 21:38:53

import sys
import argparse
import nltk
import nlp.sentiment as sentiment

__doc__ = """
    Zobb
"""


def run(args):
    analyzer = sentiment.Analyzer(args.training_datasets)
    analyzer.run_cli()


def main():
    nltk.download("punkt")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("training_datasets", type=str, nargs="+",
                        help="path to training data sets")
    args = parser.parse_args(sys.argv[1:])

    run(args)


if __name__ == "__main__":
    main()

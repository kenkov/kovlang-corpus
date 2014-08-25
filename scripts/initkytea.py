#! /usr/bin/env python
# coding:utf-8

from __future__ import division
import csv
#from itertools import islice
import preprocessing
import re


if __name__ == '__main__':
    convert = preprocessing.Twitter()

    retweet_regex = re.compile(r'RT @[A-Za-z0-9_]+:')
    kytea_slash_regex = re.compile(r'[/-|!]')

    regexes = [retweet_regex, kytea_slash_regex]

    with open("../csv/tweets.csv", "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            text = row[5]
            if not any(regex.search(text) for regex in regexes):
                tx = " ".join(convert.execute(text))
                print(tx)

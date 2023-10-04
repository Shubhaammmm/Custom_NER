#!/bin/sh

python3 -m spacy train config.cfg --output ./ --paths.train traindata.spacy --paths.dev ./traindata.spacy
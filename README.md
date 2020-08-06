# cislate

Anonymize text using Google Translate.

Say you want to write an anonymous piece of text, and you're concerned about your writing style giving you away through [stylometry](https://en.wikipedia.org/wiki/Stylometry).

This simple program translates each paragraph of a piece of text through a loop of 2-3 languages and back to English, hopefully removing your stylistic fingerprint while losing only *most* of the meaning.

## Usage

`python cislate.py yourfile.txt`.

It is recommended to manually edit the output for coherence and so that it's not obvious the text was machine-translated, with a light enough touch so as to not reintroduce a stylistic fingerprint. 

## Issues

- Only supports English.
- Unknown if this can actually defeat modern stylometry tools.
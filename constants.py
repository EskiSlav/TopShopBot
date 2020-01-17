import json

PHRASES = {}
with open('data/phrases.json', 'r') as f:
    PHRASES = json.load(f)


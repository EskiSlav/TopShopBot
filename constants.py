import json
from pprint import pprint
LANG_CHOOSE_STATUS = "LANG_CHOOSE"
NORMAL_STATUS = "NORMAL"
CATALOG_STATUS = "CATALOG"
IN_GAME = "IN_GAME"
GAME_REQUEST = "GAMEREQUEST"
LANG = {}

def instansiate_language(lang):
    with open("data/EN.json") as f:
        lang['en'] = json.load(f)

    with open("data/RU.json") as f:
        lang['ru'] = json.load(f)

    with open("data/UA.json") as f:
        lang['ua'] = json.load(f)

instansiate_language(LANG)

if __name__ == '__main__':
    pprint(LANG)


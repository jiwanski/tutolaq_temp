import json
import os
import errno
from unidecode import unidecode

persons = {'1': 'eu', '2': 'tu', '3': 'ele', '4': 'nos', '5': 'vos', '6': 'eles'}


def dump_json(suffix: str, caps: dict, target_dir: str):
    filename = target_dir + "/../output/" + suffix + ".json"
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise
    with open(filename, 'w+', encoding='utf-8') as f:
        json.dump(caps, indent=2, ensure_ascii=False, fp=f)
        f.write("\n")


def dump_conjugation(examples, verb="falar", tense="Presente", person="1"):
    tense = unidecode(tense).lower().replace(" ", "_")
    dump_json(verb + '_' + tense + '_' + persons[person], examples, os.path.dirname(__file__))

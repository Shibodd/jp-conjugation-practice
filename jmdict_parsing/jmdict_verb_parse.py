from dataclasses import dataclass
from jmdict_parsing.xml_parse_elems import parse_xml
import itertools
from japyconjugator.verbs import VerbClass

@dataclass
class Verb:
  verbClass: VerbClass
  kanji: str
  reading: str
  meaning: str

def __make_verb_map():
  ICHIDAN = [ "v1", "v1-s" ]
  GODAN = [ "v5aru", "v5b", "v5g", "v5k", "v5k-s", "v5m", "v5n", "v5r", "v5r-i", "v5s", "v5t", "v5u", "v5u-s", "v5uru" ]
  
  verb_map = {}
  for verb in ICHIDAN:
    verb_map[verb] = VerbClass.Ichidan
  for verb in GODAN:
    verb_map[verb] = VerbClass.Godan

  return verb_map

VERB_MAP = __make_verb_map()

def __filter_verbs(entries):
  for entry in entries:
    # Check that all senses are verbs and share the same verb classes.
    common_pos = None
    for sense in entry.get('sense'):
      pos = set(x for x in sense.get('pos') if x in VERB_MAP)
      
      if len(pos) != 1 or (common_pos is not None and pos != common_pos):
        common_pos = None
        break

      if common_pos is None:
        common_pos = pos

    if common_pos != None:
      yield entry



def __get_most_frequent(l):
  s = sorted(l, key = lambda x: len(x.get('ke_pri', tuple())))
  
  if len(s) > 0:
    return s[0]
  
  return None


def __parse_verbs(verbs):
  for verb in verbs:
    kanji = __get_most_frequent(verb.get('k_ele', tuple()))
    if kanji is None:
      continue
    kanji = kanji['keb'][0]
    
    reading = __get_most_frequent(verb.get('r_ele', tuple()))
    if reading is None:
      continue
    reading = reading['reb'][0]

    meaning = "; ".join(itertools.islice(
      itertools.chain.from_iterable(sense.get('gloss') for sense in verb.get('sense')),
      5
    ))
    
    verb_class = VERB_MAP[ [x for x in verb['sense'][0]['pos'] if x in VERB_MAP] [0] ]
    yield Verb(verb_class, kanji, reading, meaning)

def get_jmdic_verbs(filename):
  return __parse_verbs(__filter_verbs(parse_xml(filename, 'entry', resolve_entities = False)))
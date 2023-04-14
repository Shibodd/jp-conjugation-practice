import pprint
from xml_parse_elems import parse_xml
import pprint

FILENAME = 'JMdict_e'

for entry in parse_xml(FILENAME, "entry", resolve_entities = False):
  if entry["ent_seq"][0] == "1358280":
    pprint.pprint(entry)
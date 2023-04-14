import pprint
from xml_parse_elems import parse_xml

FILENAME = 'JMdict_e'

def handle_entry(entry):
  pprint.pprint(entry)
  pass

parse_xml(FILENAME, "entry", handle_entry, True)
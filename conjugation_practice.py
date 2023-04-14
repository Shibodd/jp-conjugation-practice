if __name__ == "__main__":
  from jmdict_parsing.jmdict_verb_parse import get_jmdic_verbs
  from japverbconj.verb_form_gen import generate_japanese_verb_by_str

  for verb in get_jmdic_verbs('JMdict_e'):
    print(generate_japanese_verb_by_str(verb.kanji, verb.verbClass, "pla", "past", "neg"))
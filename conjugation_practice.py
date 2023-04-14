if __name__ == "__main__":
  from jmdict_parsing.jmdict_verb_parse import get_jmdic_verbs

  for verb in get_jmdic_verbs('JMdict_e'):
    print(verb)
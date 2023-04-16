if __name__ == "__main__":
  import japyconjugator.verbs as japyverb
  
  from jmdict_parsing.jmdict_verb_parse import get_jmdic_verbs
  import random

  FORM = {
    japyverb.VerbForm.Plain: "Plain",
    japyverb.VerbForm.PlainPast: "Plain past",
    japyverb.VerbForm.Polite: "Polite",
    japyverb.VerbForm.PolitePast: "Polite past",
    japyverb.VerbForm.Te: "Te-form"
  }

  POLARITY = {
    japyverb.Polarity.Affirmative: "Affirmative",
    japyverb.Polarity.Negative: "Negative"
  }

  VERB_CLASS = {
    japyverb.VerbClass.Ichidan: "Ichidan",
    japyverb.VerbClass.Godan: "Godan"
  }

  def filter_short_verbs(verbs):
    for verb in verbs:
      if len(verb.kanji) <= 5:
        yield verb
  
  def reverse_furigana(kanji: str, reading: str):
    out = ""

    k_i = 0
    r_i = 0

    while k_i < len(kanji):
      while True:
        k = kanji[k_i]
        i = reading.find(k, r_i)

        if i >= 0:
          out += "　" * (i - r_i) + k
          r_i = i + 1
          k_i += 1
          break
        else:
          out += k
          k_i += 1
          r_i += 1

    return out

  def verb_prompt(verb):
    # Me: Mom, can we have clearscreen?
    # Mom: We have clearscreen at home
    # The clearscreen:
    print("\n" * 50)

    print(VERB_CLASS[verb.verbClass], "verb")
    print(verb.meaning)
    print(reverse_furigana(verb.kanji, verb.reading))
    print(verb.reading)
    
    form = random.choice(list(FORM.keys()))
    polarity = random.choice(list(POLARITY.keys()))

    correct_kanji = japyverb.conjugate_verb(verb.kanji, verb.verbClass, form, polarity)
    correct_reading = japyverb.conjugate_verb(verb.reading, verb.verbClass, form, polarity)

    ans = input(f"\nConjugate into {FORM[form]}, {POLARITY[polarity]}: ")
    
    if ans != correct_kanji and ans != correct_reading:
      print("Nope! The correct conjugation was ", correct_kanji, correct_reading)
      input("Press enter to continue...")

  print("Loading...")
  verbs = list(filter_short_verbs(get_jmdic_verbs('JMdict_e')))
  print("Loaded!")
  
  try:
    while True:
      verb_prompt(random.choice(verbs))
  except KeyboardInterrupt:
    pass
if __name__ == "__main__":
  from japverbconj.verb_form_gen import generate_japanese_verb_by_str
  from japverbconj.constants.enumerated_types import VerbClass, BaseForm, Polarity, Tense
  from jmdict_parsing.jmdict_verb_parse import get_jmdic_verbs
  import random

  FORM = {
    BaseForm.PLAIN: "Plain",
    BaseForm.POLITE: "Polite",
    BaseForm.TE: "Te-form"
  }
  POLARITY = {
    Polarity.POSITIVE: "Positive",
    Polarity.NEGATIVE: "Negative"
  }
  TENSE = { 
    Tense.NONPAST: "Present",
    Tense.PAST: "Past"
  }
  VERB_CLASS = {
    VerbClass.ICHIDAN: "Ichidan",
    VerbClass.GODAN: "Godan"
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
    tense = None if form == BaseForm.TE else random.choice(list(TENSE.keys()))

    correct_kanji = generate_japanese_verb_by_str(
      verb.kanji,
      verb.verbClass.value,
      form.value,
      None if tense is None else tense.value,
      polarity.value
    )
    correct_reading = generate_japanese_verb_by_str(
      verb.reading,
      verb.verbClass.value,
      form.value,
      None if tense is None else tense.value,
      polarity.value
    )
    
    print("")
    ans = None
    print("Tense: ", tense)
    if form != BaseForm.TE:
      ans = input(f"Conjugate into {FORM[form]}, {TENSE[tense]}, {POLARITY[polarity]}:　")
    else:
      ans = input(f"Conjugate into {FORM[form]}, {POLARITY[polarity]}: ")
    
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
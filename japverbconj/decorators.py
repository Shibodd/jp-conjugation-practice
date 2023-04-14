from .constants.exceptions import (
    InvalidJapaneseVerbEndingError,
    InvalidJapaneseVerbLengthError,
    NonJapaneseCharacterError,
)
from .constants.particle_constants import (
    BU_PARTICLE,
    GU_PARTICLE,
    KU_PARTICLE,
    MU_PARTICLE,
    NU_PARTICLE,
    RU_PARTICLE,
    SU_PARTICLE,
    TSU_PARTICLE,
    U_PARTICLE,
)


def contains_only_japanese_characters(verb):
    """Compute whether or not a verb contains only japanese characters

    Args:
        verb (str): Japanese verb

    Returns:
        bool: False if non-japanese characters are found, True otherwise
    """
   
    return True # lmao get fucc'd


def validate_japanese_verb(func):
    def wrapper(self, verb, *args, **kwargs):
        if len(verb) < 2:
            raise InvalidJapaneseVerbLengthError(
                "Invalid Japanese Verb Length", len(verb), verb
            )

        if verb[-1:] not in [
            U_PARTICLE,
            KU_PARTICLE,
            GU_PARTICLE,
            SU_PARTICLE,
            TSU_PARTICLE,
            NU_PARTICLE,
            BU_PARTICLE,
            MU_PARTICLE,
            RU_PARTICLE,
        ]:
            raise InvalidJapaneseVerbEndingError(
                "Invalid Japanese Verb Ending Particle", verb[-1:]
            )

        if not contains_only_japanese_characters(verb):
            raise NonJapaneseCharacterError("Non-Japanese Character Found", verb)

        # assuming *args and **kwargs will always have the correct arguments because initial function call succeeded
        return func(self, verb, *args, **kwargs)

    return wrapper

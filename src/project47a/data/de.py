# Copyright 2023 Henryk Plötz
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import random
from enum import IntFlag, auto

__all__ = ["ADJECTIVES", "NOUNS", "adjektiv_deklinieren", "Flags", "generate_random"]

from typing import Optional


class Flags(IntFlag):
    DEKLINABEL = auto()
    GENUS_M = auto()
    GENUS_F = auto()
    GENUS_N = auto()


_ADJECTIVES_1 = [
    "albern",
    "alt",
    "arg",
    "arm",
    "bange",
    "barsch",
    "bieder",
    "bitter",
    "blank",
    "blass",
    "blau",
    "bleich",
    "blind",
    "blond",
    "bloß",
    "blün",
    "braun",
    "brav",
    "breit",
    "brüsk",
    "bunt",
    "derbe",
    "doppelt",
    "drall",
    "dumpf",
    "dunkel",
    "dünn",
    "dürr",
    "düster",
    "eben",
    "echt",
    "edel",
    "eigen",
    "einzeln",
    "eng",
    "ernst",
    "fade",
    "fahl",
    "falsch",
    "fein",
    "feist",
    "fern",
    "fesch",
    "fest",
    "fett",
    "feucht",
    "finster",
    "firn",
    "flach",
    "flau",
    "flink",
    "flott",
    "forsch",
    "frei",
    "fremd",
    "froh",
    "fromm",
    "früh",
    "früh",
    "ganz",
    "gar",
    "gelb",
    "genau",
    "gerade",
    "gering",
    "geschwind",
    "gesund",
    "glatt",
    "gleich",
    "grau",
    "greise",
    "grell",
    "grimm",
    "grob",
    "groß",
    "grün",
    "gut",
    "hager",
    "halb",
    "harsch",
    "hart",
    "hehr",
    "heikel",
    "heil",
    "heiser",
    "heiter",
    "helle",
    "herb",
    "hintere",
    "hoch",
    "hohl",
    "hold",
    "hübsch",
    "innere",
    "jung",
    "jäh",
    "kahl",
    "kalt",
    "kaputt",
    "karg",
    "keck",
    "kess",
    "kirre",
    "klamm",
    "klar",
    "klein",
    "klug",
    "knapp",
    "krank",
    "krass",
    "kraus",
    "krude",
    "krumm",
    "kurz",
    "kühl",
    "kühn",
    "lahm",
    "lang",
    "lauter",
    "lecker",
    "leer",
    "leicht",
    "leise",
    "letzte",
    "licht",
    "lieb",
    "lila",
    "lind",
    "link",
    "locker",
    "lose",
    "mager",
    "matt",
    "mau",
    "mies",
    "milde",
    "mittlere",
    "morsch",
    "munter",
    "müde",
    "mürbe",
    "nahe",
    "nass",
    "nett",
    "neu",
    "nieder",
    "nächste",
    "obere",
    "offen",
    "orange",
    "plan",
    "platt",
    "plump",
    "prall",
    "prüde",
    "rank",
    "rar",
    "rasch",
    "recht",
    "rege",
    "reich",
    "reif",
    "rein",
    "roh",
    "rosa",
    "rot",
    "rund",
    "rüde",
    "sachte",
    "sanft",
    "satt",
    "sauber",
    "sauer",
    "schal",
    "scharf",
    "scheu",
    "schick",
    "schief",
    "schier",
    "schlaff",
    "schlank",
    "schlapp",
    "schlau",
    "schlecht",
    "schlicht",
    "schlimm",
    "schmal",
    "schmuck",
    "schnell",
    "schnöde",
    "schrill",
    "schroff",
    "schräg",
    "schwach",
    "schwarz",
    "schwer",
    "schwül",
    "schön",
    "schütter",
    "seicht",
    "selten",
    "sicher",
    "spitz",
    "spröde",
    "spät",
    "stark",
    "starr",
    "steif",
    "steil",
    "still",
    "stolz",
    "strack",
    "straff",
    "stramm",
    "streng",
    "stumm",
    "stumpf",
    "stur",
    "süß",
    "tapfer",
    "taub",
    "teuer",
    "tief",
    "toll",
    "traut",
    "treu",
    "trocken",
    "träge",
    "trübe",
    "tumb",
    "unscharf",
    "untere",
    "unwirsch",
    "vage",
    "voll",
    "vordere",
    "wach",
    "wacker",
    "wahr",
    "warm",
    "weh",
    "weich",
    "weise",
    "weit",
    "weiß",
    "welk",
    "welsch",
    "wert",
    "wild",
    "wirr",
    "wirsch",
    "wrack",
    "wund",
    "wüst",
    "zahm",
    "zart ",
    "zähe",
    "äußere",
    "öde",
    "übel",
]

_ADJECTIVES_2 = ["lila", "rosa"]

ADJECTIVES = list(
    (
        {k: Flags.DEKLINABEL for k in _ADJECTIVES_1}
        | {k: Flags(0) for k in _ADJECTIVES_2}
    ).items()
)

NOUNS_M = ["Ort", "Bär", "Tag", "Ozean", "Berg"]
NOUNS_F = ["Wolle", "Tüte", "Lücke"]
NOUNS_N = ["Licht", "Tal", "Wasser"]

NOUN_PREFIXES = ["Sommer", "Winter", "Licht", "Geheim"]

NOUNS = list(
    (
        {k: Flags.GENUS_M for k in NOUNS_M}
        | {k: Flags.GENUS_F for k in NOUNS_F}
        | {k: Flags.GENUS_N for k in NOUNS_N}
    ).items()
)


def adjektiv_deklinieren(
    adjektiv: str, adjektiv_flags: Flags, substantiv_flags: Flags
) -> str:
    if not adjektiv_flags & Flags.DEKLINABEL:
        return adjektiv

    if adjektiv.endswith("el"):
        adjektiv = adjektiv[:-2] + "le"

    if adjektiv.endswith("e"):
        adjektiv = adjektiv[:-1]

    if substantiv_flags & Flags.GENUS_M:
        return adjektiv + "er"
    elif substantiv_flags & Flags.GENUS_F:
        return adjektiv + "e"
    elif substantiv_flags & Flags.GENUS_N:
        return adjektiv + "es"

    return adjektiv


def generate_random(rng: Optional[random.Random] = None) -> str:
    """

    :rtype: object
    """
    rng = rng or random.Random()

    adjektiv = rng.choice(ADJECTIVES)
    prefix = "" if rng.choice([True, False]) else rng.choice(NOUN_PREFIXES)
    substantiv = rng.choice(NOUNS)

    adjektiv_dekliniert = adjektiv_deklinieren(
        *adjektiv, substantiv_flags=substantiv[1]
    )

    return f"{adjektiv_dekliniert} {(prefix + substantiv[0]).title()}"

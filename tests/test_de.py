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

from project47a.data.de import Flags, adjektiv_deklinieren, generate_random


def test_adjektiv_deklinieren_1():
    assert adjektiv_deklinieren("blau", Flags.DEKLINABEL, Flags.GENUS_M) == "blauer"
    assert adjektiv_deklinieren("blau", Flags.DEKLINABEL, Flags.GENUS_F) == "blaue"
    assert adjektiv_deklinieren("blau", Flags.DEKLINABEL, Flags.GENUS_N) == "blaues"

    assert adjektiv_deklinieren("heikel", Flags.DEKLINABEL, Flags.GENUS_M) == "heikler"
    assert adjektiv_deklinieren("heikel", Flags.DEKLINABEL, Flags.GENUS_F) == "heikle"
    assert adjektiv_deklinieren("heikel", Flags.DEKLINABEL, Flags.GENUS_N) == "heikles"

    assert adjektiv_deklinieren("orange", Flags.DEKLINABEL, Flags.GENUS_M) == "oranger"
    assert adjektiv_deklinieren("orange", Flags.DEKLINABEL, Flags.GENUS_F) == "orange"
    assert adjektiv_deklinieren("orange", Flags.DEKLINABEL, Flags.GENUS_N) == "oranges"


def test_generate_random():
    a = generate_random()
    b = generate_random()

    assert a
    assert b
    assert a != b

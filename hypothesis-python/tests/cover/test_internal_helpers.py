# This file is part of Hypothesis, which may be found at
# https://github.com/HypothesisWorks/hypothesis/
#
# Copyright the Hypothesis Authors.
# Individual contributors are listed in AUTHORS.rst and the git log.
#
# This Source Code Form is subject to the terms of the Mozilla Public License,
# v. 2.0. If a copy of the MPL was not distributed with this file, You can
# obtain one at https://mozilla.org/MPL/2.0/.

import pytest

from hypothesis.internal.floats import is_negative


def test_is_negative_gives_good_type_error():
    x = "foo"
    with pytest.raises(TypeError) as e:
        is_negative(x)
    assert repr(x) in e.value.args[0]

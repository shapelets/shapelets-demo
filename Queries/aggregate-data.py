# Copyright (c) 2022 Grumpy Cat Software S.L.
#
# This Source Code is licensed under the MIT 2.0 license.
# the terms can be found in LICENSE.md at the root of
# this project, or at http://mozilla.org/MPL/2.0/.

import shapelets as sh
from shapelets.functions import avg

session = sh.sandbox()

data = session.load_test_data()

session.map((x.Class,avg(x.Sepal_Length)) for x in data)
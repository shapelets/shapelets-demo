# Copyright (c) 2023 Grumpy Cat Software S.L.
#
# This Source Code is licensed under the MIT 2.0 license.
# the terms can be found in LICENSE.md at the root of
# this project, or at http://mozilla.org/MPL/2.0/.

from vega_datasets import data
from shapelets.apps import DataApp
import altair as alt

# Instantiate data app
app = DataApp("Simple scatterplot with tooltips", version=(0,1))

# Get sample data frame
source = data.cars()

# Create altair chart spec
spec = alt.Chart(source).mark_circle(size=60).encode(
    x='Horsepower',
    y='Miles_per_Gallon',
    color='Origin',
    tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
).interactive()

# Create altair chart widget
altair_chart = app.altair_chart(title='Simple scatterplot with tooltips', chart=spec)

# Place widget
app.place(altair_chart)

# Register data app
app.register()
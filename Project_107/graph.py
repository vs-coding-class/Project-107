import pandas as pd
import plotly.express as plex

df = pd.read_csv("scores.csv")
groupings = df.groupby(["student_id", "level"], as_index = False)["attempt"].mean()

fig = plex.scatter(groupings, x = "student_id", y = "level", color = "attempt", size = "attempt")
fig.show()
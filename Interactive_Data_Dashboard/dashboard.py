import pandas as pd
import plotly.express as px

# Load sample dataset
df = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Values": [23, 45, 56, 78]
})

# Create interactive bar chart
fig = px.bar(df, x="Category", y="Values", title="Interactive Dashboard Example")
fig.show()

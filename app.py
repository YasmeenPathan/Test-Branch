from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Dummy data for parking insights
parking_insights = pd.DataFrame({
    'Time': ['2024-07-08 08:00', '2024-07-08 09:00', '2024-07-08 10:00'],
    'Occupied Slots': [5, 10, 7],
    'Available Slots': [15, 10, 13]
})

@app.route('/')
def home():
    return render_template('index.html', insights=parking_insights.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)

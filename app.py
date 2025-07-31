from flask import Flask, render_template

app = Flask(__name__)

# Data for the categories and projects
data = {
    "categories": [
        {
            "name": "Data Science",
            "enabled": True,
            "projects": [
                {
                    "name": "Customer Churn Prediction",
                    "description": "A model to predict customer churn.",
                    "enabled": True,
                    "buttons": [
                        {"name": "Demo", "url": "#", "enabled": True},
                        {"name": "PPT", "url": "#", "enabled": True},
                        {"name": "Download", "url": "#", "enabled": False}
                    ]
                },
                {
                    "name": "Sales Forecasting",
                    "description": "Forecasting future sales using time series analysis.",
                    "enabled": True,
                    "buttons": [
                        {"name": "Demo", "url": "#", "enabled": True},
                        {"name": "PPT", "url": "#", "enabled": True}
                    ]
                }
            ]
        },
        {
            "name": "Web Development",
            "enabled": True,
            "projects": [
                {
                    "name": "E-commerce Website",
                    "description": "A full-featured e-commerce website.",
                    "enabled": True,
                    "buttons": [
                        {"name": "Live Demo", "url": "#", "enabled": True},
                        {"name": "Source Code", "url": "#", "enabled": True}
                    ]
                }
            ]
        },
        {
            "name": "Machine Learning",
            "enabled": False,
            "projects": []
        }
    ]
}

@app.route('/')
def index():
    return render_template('index.html', categories=data['categories'])

if __name__ == '__main__':
    app.run(debug=True)

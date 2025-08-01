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
                    "description": "A sophisticated model that leverages machine learning to predict customer churn with high accuracy, enabling proactive retention strategies.",
                    "enabled": True,
                    "buttons": [
                        {"name": "Live Demo", "url": "#", "enabled": True},
                        {"name": "View PPT", "url": "#", "enabled": True},
                        {"name": "Download Report", "url": "#", "enabled": True},
                        {"name": "Source Code", "url": "#", "enabled": True},
                        {"name": "API Docs", "url": "#", "enabled": False}
                    ]
                },
                {
                    "name": "Sales Forecasting",
                    "description": "Utilizing advanced time series analysis and econometric models to forecast sales with remarkable precision, empowering better business planning.",
                    "enabled": True,
                    "buttons": [
                        {"name": "Dashboard", "url": "#", "enabled": True},
                        {"name": "View PPT", "url": "#", "enabled": True},
                        {"name": "Download Data", "url": "#", "enabled": True},
                        {"name": "Methodology", "url": "#", "enabled": True}
                    ]
                }
            ]
        },
        {
            "name": "Web Development",
            "enabled": True,
            "projects": [
                {
                    "name": "E-commerce Platform",
                    "description": "A feature-rich, scalable, and secure e-commerce platform with a modern, responsive UI and a powerful backend.",
                    "enabled": True,
                    "buttons": [
                        {"name": "Live Demo", "url": "#", "enabled": True},
                        {"name": "Frontend Code", "url": "#", "enabled": True},
                        {"name": "Backend Code", "url": "#", "enabled": True},
                        {"name": "Deployment Guide", "url": "#", "enabled": True},
                        {"name": "Video Walkthrough", "url": "#", "enabled": True}
                    ]
                },
                {
                    "name": "Portfolio Website",
                    "description": "A stunning and interactive portfolio website built with the latest web technologies to showcase projects and skills.",
                    "enabled": True,
                    "buttons": [
                        {"name": "View Site", "url": "#", "enabled": True},
                        {"name": "Source Code", "url": "#", "enabled": True},
                        {"name": "Design Assets", "url": "#", "enabled": True}
                    ]
                }
            ]
        },
        {
            "name": "Machine Learning",
            "enabled": True,
            "projects": [
                {
                    "name": "Image Recognition API",
                    "description": "A powerful API that can recognize and classify objects in images with high accuracy, built with deep learning models.",
                    "enabled": True,
                    "buttons": [
                        {"name": "Try It Live", "url": "#", "enabled": True},
                        {"name": "API Docs", "url": "#", "enabled": True},
                        {"name": "Model Architecture", "url": "#", "enabled": True},
                        {"name": "Training Data", "url": "#", "enabled": True},
                        {"name": "Jupyter Notebook", "url": "#", "enabled": True}
                    ]
                }
            ]
        },
        {
            "name": "Cloud & DevOps",
            "enabled": True,
            "projects": [
                {
                    "name": "CI/CD Pipeline Automation",
                    "description": "A fully automated CI/CD pipeline that builds, tests, and deploys applications to the cloud with a single command.",
                    "enabled": True,
                    "buttons": [
                        {"name": "View Pipeline", "url": "#", "enabled": True},
                        {"name": "YAML Config", "url": "#", "enabled": True},
                        {"name": "Monitoring Dashboard", "url": "#", "enabled": True},
                        {"name": "Security Scan Report", "url": "#", "enabled": True}
                    ]
                }
            ]
        },
        {
            "name": "Cybersecurity",
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

from flask import Flask, jsonify, render_template
import os
from analyzer import analyze_energy_usage
from tips_generator import generate_funny_tip

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../frontend'))

app = Flask(__name__,
            template_folder=os.path.join(BASE_DIR, 'templates'),
            static_folder=os.path.join(BASE_DIR, 'static'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['GET']) 
def analyze():
    analysis = analyze_energy_usage('mock_data.csv')
    tips = []

    for waste in analysis["wastage"]:
        tips.append(generate_funny_tip(waste))

    return jsonify({
        "analysis": analysis["summary"],
        "wastage": analysis["wastage"],
        "funny_tips": tips
    })

if __name__ == '__main__':
    app.run(debug=True)

import os
import csv
from datetime import datetime
from flask import Flask, render_template_string, jsonify
from pyngrok import ngrok

app = Flask(__name__, static_url_path='/static')


html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <title>Be My Valentine?</title>
    <style>
        body { text-align: center; font-family: sans-serif; background-color: #ffe6e6; margin: 0; padding: 20px; display: flex; flex-direction: column; justify-content: center; align-items: center; min-height: 100vh; overflow-x: hidden; }
        h1 { color: #ff4d4d; font-size: 2.5rem; }
        img { max-width: 80%; border-radius: 20px; box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
        .btn-container { margin-top: 30px; position: relative; width: 100%; max-width: 400px; height: 100px; }
        button { padding: 15px 30px; font-size: 1.2rem; cursor: pointer; border-radius: 50px; border: none; font-weight: bold; }
        #yes-btn { background-color: #ff4d4d; color: white; }
        #no-btn { background-color: #ffffff; color: #ff4d4d; position: absolute; left: 55%; border: 2px solid #ff4d4d; }
    </style>
</head>
<body>
    <h1>Will you be my Valentine? ❤️</h1>
    <img src="/static/US.jpg" alt="Our Photo">
    
    <div class="btn-container">
        <button id="yes-btn" onclick="handleYesClick()">YES</button>
        <button id="no-btn" onmouseover="moveButton()" onclick="moveButton()" ontouchstart="moveButton()">NO</button>
    </div>

    <script>
        function moveButton() {
            const width = window.innerWidth - 100;
            const height = window.innerHeight - 100;
            const newX = Math.random() * width;
            const newY = Math.random() * height;
            const btn = document.getElementById('no-btn');
            btn.style.position = 'fixed'; 
            btn.style.left = newX + 'px';
            btn.style.top = newY + 'px';
        }

        function handleYesClick() {
            alert('THANK YOU SO MUCH, I LOVE YOU ❤️! 🌹✨');
            // This tells the Python backend to create the CSV file
            fetch('/accept-valentine', { method: 'POST' })
            .then(response => {
                if(response.ok) { document.body.style.backgroundColor = '#ffb3b3'; }
            });
        }
    </script>
</body>
</html>
"""


@app.route('/')
def home():
    return render_template_string(html_template)

@app.route('/accept-valentine', methods=['POST'])
def accept_valentine():
    try:
        with open('responses.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([timestamp, "YES! SHE said YES!"])
        print(f"✅ Success! Response logged at {timestamp}")
        return jsonify({"status": "success"}), 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return jsonify({"status": "error"}), 500


if __name__ == '__main__':
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    if not os.path.exists(os.path.join(script_dir, 'static', 'US.jpg')):
        print("⚠️ WARNING: static/US.jpg not found!")

   
    public_url = ngrok.connect(5000).public_url
    print("\n" + "💖 " * 10)
    print(f"URL FOR YOUR VALENTINE: {public_url}")
    print("💖 " * 10 + "\n")
    
   
    app.run(port=5000, debug=False)
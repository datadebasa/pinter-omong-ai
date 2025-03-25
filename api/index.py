from flask import Flask, render_template,request, jsonify
import requests

app = Flask(__name__)
def chatbot(promt):
    url = f'https://open-source-backend.vercel.app/podcast-ai?prompt={promt}'
    response = requests.get(url)
    response = response.json()
    return response
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pinter-omong')
def pinter_omong():
    return render_template('chat.html')

@app.route('/pinter-omong/chat')
def chat():
    promt = request.args.get('prompt')
    response = chatbot(promt)
    response = response['payload']
    
    return jsonify(response)

    

if __name__ == '__main__':
    app.run(port=5000, debug=True)
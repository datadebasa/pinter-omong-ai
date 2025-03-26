from flask import Flask, render_template,request, jsonify
import requests

app = Flask(__name__)
def chatbot(promt, riwayat_chat = ''):
    promt = promt.replace(' ', '%20')
    # url = f'https://open-source-backend.vercel.app/podcast-ai?prompt={promt}'
    url = f'https://open-source-backend.vercel.app//podcast-ai?prompt={promt}dimana%20riwayat%20chat%20:{riwayat_chat}Jangan%20berikan%20informasi%20riwayat%20chat%20jika%20chatnya%20kosong%20 '
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
    riwayat_chat = request.args.get('riwayat')
    response = chatbot(promt, riwayat_chat)
    response = response['payload']
    
    return jsonify(response)

    

if __name__ == '__main__':
    app.run(port=5000, debug=True)
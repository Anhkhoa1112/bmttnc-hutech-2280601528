from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailfenceCipher
from cipher.playfair import PlayfairCipher

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

# Caesar Cipher Routes
@app.route("/caesar")
def caesar():
    return render_template('caesar.html')

@app.route("/encrypt", methods=['POST'])
def caesar_encrypt():
    text = request.form['inputPlainText']
    Key = int(request.form['inputKeyPlain'])
    Caesar = CaesarCipher()
    encrypted_text = Caesar.encrypt_text(text, Key)
    return f"text: {text}<br/>Key: {Key}<br/>encrypted text: {encrypted_text}"

@app.route("/decrypt", methods=['POST'])
def caesar_decrypt():
    text = request.form['inputCipherText']
    Key = int(request.form['inputKeyCipher'])
    Caesar = CaesarCipher()
    decrypted_text = Caesar.decrypt_text(text, Key)
    return f"text: {text}<br/>Key: {Key}<br/>decrypted text: {decrypted_text}"

# Vigenere Cipher Routes
@app.route("/vigenere")
def vigenere():
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    vigenere = VigenereCipher()
    encrypted_text = vigenere.vigenere_encrypt(text, key)
    return f"text: {text}<br/>Key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    vigenere = VigenereCipher()
    decrypted_text = vigenere.vigenere_decrypt(text, key)
    return f"text: {text}<br/>Key: {key}<br/>decrypted text: {decrypted_text}"

# Rail Fence Cipher Routes
@app.route("/railfence")
def railfence():
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    railfence = RailfenceCipher()
    encrypted_text = railfence.rail_fence_encrypt(text, key)
    return f"text: {text}<br/>Key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    railfence = RailfenceCipher()
    decrypted_text = railfence.rail_fence_decrypt(text, key)
    return f"text: {text}<br/>Key: {key}<br/>decrypted text: {decrypted_text}"

# Playfair Cipher Routes
@app.route("/playfair")
def playfair():
    return render_template('playfair.html')

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    playfair = PlayfairCipher()
    matrix = playfair.create_playfair_matrix(key)
    encrypted_text = playfair.playfair_encrypt(text, matrix)
    return f"text: {text}<br/>Key: {key}<br/>encrypted text: {encrypted_text}"

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    playfair = PlayfairCipher()
    matrix = playfair.create_playfair_matrix(key)
    decrypted_text = playfair.playfair_decrypt(text, matrix)
    return f"text: {text}<br/>Key: {key}<br/>decrypted text: {decrypted_text}"

@app.route("/playfair/creatematrix", methods=['POST'])
def playfair_creatematrix():
    key = request.form['inputKeyMatrix']
    playfair = PlayfairCipher()
    matrix = playfair.create_playfair_matrix(key)
    
    # Tạo HTML để hiển thị ma trận
    matrix_html = "<h3>Ma trận Playfair cho khóa: " + key + "</h3>"
    matrix_html += "<table class='table table-bordered' style='width: 300px;'>"
    
    for row in matrix:
        matrix_html += "<tr>"
        for cell in row:
            matrix_html += f"<td style='text-align: center; font-weight: bold;'>{cell}</td>"
        matrix_html += "</tr>"
    
    matrix_html += "</table>"
    matrix_html += "<a href='/playfair' class='btn btn-primary'>Quay lại</a>"
    
    return matrix_html



if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)

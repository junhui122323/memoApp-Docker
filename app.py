from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

notes = []
next_id = 1

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/notes', methods=['GET'])
def get_notes():
    return jsonify(notes)

@app.route('/api/notes', methods=['POST'])
def add_note():
    global next_id
    data = request.get_json()
    text = data.get('text', '').strip()
    if not text:
        return jsonify({'error': 'Note text is required'}), 400
    note = {'id': next_id, 'text': text}
    notes.append(note)
    next_id += 1
    return jsonify(note), 201

@app.route('/api/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    global notes
    notes = [n for n in notes if n['id'] != note_id]
    return '', 204

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

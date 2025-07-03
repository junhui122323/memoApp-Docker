from flask import Flask, jsonify, request, render_template

# Flask 앱 생성
app = Flask(__name__)

# 메모 목록 저장용 전역 변수 (간단히 메모 임시 저장)
notes = []
# 메모에 고유한 ID 부여를 위한 카운터 변수
next_id = 1
# 루트 경로 ("/")에 접속했을 때 HTML 페이지 렌더링
@app.route('/')
def home():
    return render_template('index.html')
# 전체 메모 목록을 JSON 형식으로 반환하는 API
@app.route('/api/notes', methods=['GET'])
def get_notes():
    return jsonify(notes)
# 메모 추가 API (POST 요청)
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
# 메모 삭제 API (DELETE 요청)
@app.route('/api/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    global notes
    notes = [n for n in notes if n['id'] != note_id]
    return '', 204
# Flask 앱 실행 (외부 접속 허용, 포트 5000)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

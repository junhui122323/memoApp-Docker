from flask import Flask, jsonify, request, render_template
import json
import os

# Flask 앱 생성
app = Flask(__name__)

# 메모 데이터를 저장할 JSON 파일 경로
DATA_FILE = 'memo.json'

# 메모를 저장할 리스트와 고유 ID용 카운터
notes = []
next_id = 1

# 서버 시작 시 memo.json에서 데이터 불러오기
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as f:
        try:
            # JSON 파일이 존재하면 메모 목록 불러오기
            notes = json.load(f)
            if notes:
                # 마지막 메모 ID를 기반으로 next_id 초기화
                next_id = max(note['id'] for note in notes) + 1
        except json.JSONDecodeError:
            # JSON 파싱 에러가 날 경우 빈 리스트로 초기화
            notes = []
            next_id = 1

# 메모 리스트를 memo.json에 저장하는 함수
def save_notes():
    with open(DATA_FILE, 'w') as f:
        json.dump(notes, f, ensure_ascii=False, indent=2)

# 메인 페이지 렌더링
@app.route('/')
def home():
    return render_template('index.html')

# 전체 메모 목록을 반환 (GET /api/notes)
@app.route('/api/notes', methods=['GET'])
def get_notes():
    return jsonify(notes)

# 메모 추가 처리 (POST /api/notes)
@app.route('/api/notes', methods=['POST'])
def add_note():
    global next_id
    data = request.get_json()  # 클라이언트에서 보낸 JSON 데이터 받기
    text = data.get('text', '').strip()  # "text" 필드 가져오기
    if not text:
        return jsonify({'error': 'Note text is required'}), 400

    note = {'id': next_id, 'text': text}  # 새 메모 객체 생성
    notes.append(note)                   # 메모 리스트에 추가
    next_id += 1                         # 다음 메모 ID 증가
    save_notes()                         # JSON 파일로 저장
    return jsonify(note), 201            # 생성된 메모 반환

# 메모 삭제 처리 (DELETE /api/notes/<id>)
@app.route('/api/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    global notes
    # 해당 ID가 아닌 메모만 남김 (삭제)
    notes = [n for n in notes if n['id'] != note_id]
    save_notes()  # JSON 파일에 반영
    return '', 204  # 성공 상태만 반환 (내용 없음)

# 앱 실행 (모든 IP 허용, 포트 5000)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

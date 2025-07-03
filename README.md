# 📝 MemoApp-Docker

간단한 메모 작성 Flask 웹앱을 Docker로 컨테이너화한 프로젝트입니다.  
Docker Hub와 Docker Compose 기반 실습을 위해 제작되었으며,  
Flask 백엔드, HTML 프론트, 데이터 파일 저장을 포함합니다.

---

## 📦 주요 기능

- 사용자가 메모를 작성하고 저장 가능
- Dockerfile 기반 컨테이너 이미지 빌드
- Docker Hub에 이미지 푸시 및 pull
- Docker Volume으로 데이터 유지
- 로컬에서 `docker run` 또는 `docker-compose`로 손쉽게 실행

---

## 🐳 Docker Hub 이미지

> https://hub.docker.com/r/junhui122323/memoapp-docker

```bash
docker pull junhui122323/memoapp-docker
docker run -d -p 5000:5000 junhui122323/memoapp-docker
🏗️ 실행 방법
1️⃣ 일반 Docker 사용 시
bash
복사
편집
docker build -t memoapp .
docker run -d -p 5000:5000 memoapp
2️⃣ Docker Compose 사용 시
bash
복사
편집
docker-compose up -d
📁 프로젝트 구조
plaintext
복사
편집
memoApp-Docker/
├── app.py             # Flask 웹 서버
├── templates/
│   └── index.html     # 메모 작성 HTML 폼
├── memo.json          # 메모 데이터 저장 파일 (볼륨 연결 가능)
├── Dockerfile         # 앱 이미지 정의
├── docker-compose.yml # 여러 컨테이너/볼륨 정의 (선택사항)
└── README.md
🗃️ Dockerfile 요약
dockerfile
복사
편집
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install flask
CMD ["python", "app.py"]
💾 Docker Volume 적용 (데이터 유지)
bash
복사
편집
docker run -d -p 5000:5000 \
  -v $(pwd)/memo.json:/app/memo.json \
  memoapp
✍️ To Do
 메모 수정/삭제 기능 추가

 데이터 파일 분리 저장 (유저별 저장)

 SQLite 연동

 CI/CD 자동 배포 (GitHub Actions + Docker Hub)

🧑‍💻 개발자
이름	깃허브
한준희	junhui122323
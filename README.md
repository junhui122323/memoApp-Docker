# MemoApp-Docker

간단한 메모 작성 웹앱을 Flask와 Docker로 구현한 프로젝트입니다.  
Docker 이미지 빌드부터 실행, Docker Hub 푸시까지 포함한 실습용 예제입니다.

---

## 주요 기능

- 메모 작성 및 저장 기능 제공  
- Flask 웹서버 기반 간단 UI  
- Dockerfile로 이미지 빌드 및 컨테이너 실행  
- Docker Hub에 이미지 등록 및 배포  
- Docker Volume으로 데이터 영속성 확보  

---

## 프로젝트 구조

memoApp-Docker/
├── app.py # Flask 앱 메인 파일
├── templates/
│ └── index.html # 메모 작성 페이지 템플릿
├── memo.json # 메모 데이터 저장 파일 (볼륨 마운트용)
├── Dockerfile # Docker 이미지 빌드 정의
├── docker-compose.yml # 선택적, Docker Compose 설정 파일
└── README.md # 프로젝트 설명 문서

yaml
복사
편집

---

## 빠른 시작

### Docker 이미지 빌드 & 실행

```bash
docker build -t memoapp .
docker run -d -p 5000:5000 memoapp
Docker Hub에서 이미지 받아 실행
bash
복사
편집
docker pull junhui122323/memoapp-docker
docker run -d -p 5000:5000 junhui122323/memoapp-docker
Docker Volume으로 데이터 유지
bash
복사
편집
docker run -d -p 5000:5000 -v $(pwd)/memo.json:/app/memo.json memoapp
앞으로 할 일
메모 수정 및 삭제 기능 추가

사용자별 데이터 관리 기능 도입

데이터베이스(SQLite) 연동

CI/CD 자동화 (GitHub Actions 연동)

개발자
한준희 — GitHub/junhui122323

라이선스
MIT License

yaml
복사
편집

---

복사할 때는 위처럼 전체를 그대로 복사하고,  
에디터에서 들여쓰기나 줄바꿈이 이상하면 적절히 고쳐주면 돼!  
필요하면 내가 `.md` 파일로 만들어서 올려줄 수도 있어.

# 공식 Python 3.9 슬림 이미지를 기반 이미지로 사용 (불필요한 패키지 제외한 경량 버전)
FROM python:3.9-slim
# 컨테이너 안에서 작업할 디렉토리 설정
WORKDIR /app
# 로컬의 requirements.txt 파일을 컨테이너로 복사
COPY requirements.txt .
# 의존성 패키지 설치 (캐시 없이 가볍게 설치)
RUN pip install --no-cache-dir -r requirements.txt
# 현재 디렉토리의 모든 파일을 컨테이너의 작업 디렉토리(/app)에 복사
COPY . .
# 외부에서 접근할 포트 5000 오픈 (Flask 기본 포트)
EXPOSE 5000
# 컨테이너 실행 시 기본으로 수행할 명령어 (Flask 앱 실행)
CMD ["python", "app.py"]

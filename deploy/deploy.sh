#디렉토리 이동
cd ..

#가상환경 활성화
source mutsa/bin/activate
cd back

# 코드 업데이트
git pull

# 패키지 설치
pip install -r requirements.txt

# 서버 실행
nohup python3 manage.py runserver 0.0.0.0:8000 &

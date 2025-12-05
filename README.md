# 🧾 Mini Account Book (파이썬 가계부 프로젝트)

## 📌 프로젝트 소개
이 프로젝트는 Python으로 구현한 **콘솔 기반 미니 가계부 프로그램**입니다.
수입/지출을 등록하고, 전체 목록 조회 및 잔액 확인, 항목 검색이 가능합니다.

## 🛠 주요 기능
- 지출/수입 등록
- 전체 내역 조회
- 특정 키워드로 내역 검색
- 총 잔액 계산
- JSON 파일로 데이터 자동 저장

## 📂 폴더 구조
mini-account-book/
 ├── README.md
 ├── app.py
 ├── data/
 │     └── records.json
 └── utils/
       └── storage.py

## ▶ 실행 방법
### 1) Python 설치 (없다면)
- Windows: https://www.python.org/downloads/ 에서 설치
- macOS: 보통 기본 탑재. 없으면 위 링크에서 설치
- Linux: 배포판 패키지 관리자로 설치

### 2) 실행
터미널(또는 명령 프롬프트)에서 아래 명령어 실행:
```
python app.py
```

## 💾 데이터 저장 방식
- `records.json` 파일에 자동 저장
- 프로그램 종료 후에도 데이터 유지

## 👤 개발자
- 깊쁨(Deeppeum)

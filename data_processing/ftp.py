import ftplib
import os
from constants import FtpConstants

ftp_constant = FtpConstants()
# FTP 정보
host = ftp_constant.FTP_HOST
user = ftp_constant.FTP_USER
pw = ftp_constant.FTP_PW
local_dir = ftp_constant.LOCAL_DIRECTORY

# 다운로드할 파일명 "" 안에 다운로드 하고 싶은 파일 확장자 포함해서 작성
FILE_NAME = "다운로드 파일"
local_file_path = os.path.join(local_dir, FILE_NAME)

with ftplib.FTP() as ftp:
    # FTP 접속
    ftp.connect(host=host, port=21)
    ftp.encoding = 'utf-8'  # 인코딩 설정
    ftp.login(user=user, passwd=pw)  # 로그인

    # 해당 디렉터리로 이동 "" 안에 디렉터리 경로 작성
    ftp.cwd("디렉터리 경로")

    # FTP 서버에 존재하는 파일 리스트 확인
    files = ftp.nlst()
    print("FTP 파일 목록:", files)

    # 저장할 로컬 폴더가 없으면 생성
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)

    # 파일이 존재하면 다운로드
    if FILE_NAME in files:
        with open(local_file_path, "wb") as f:
            ftp.retrbinary(f"RETR {FILE_NAME}", f.write)
        print(f"파일 다운로드 완료: {local_file_path}")
    else:
        print(f"파일이 존재하지 않습니다: {FILE_NAME}")

import ftplib
import os
from constants import FtpConstants

ftp_constant = FtpConstants()
# FTP 정보
host = ftp_constant.FTP_HOST
user = ftp_constant.FTP_USER
pw = ftp_constant.FTP_PW
local_dir = ftp_constant.LOCAL_DIRECTORY
# 파일 리스트 먼저 확인 후 원하는 파일 선택
local_file_path = os.path.join(local_dir, "파일 선택")

with ftplib.FTP() as ftp:
    # ftp 접근
    ftp.connect(host=host, port=21)
    # 인코딩
    ftp.encoding = 'utf-8'
    # ftp 로그인
    ftp.login(user=user, passwd=pw)

    # ftp 서버에 존재하는 폴더 및 파일 리스트
    print(ftp.nlst())

    # 해당 경로에 해당 폴더가 없으면 생성하는 로직
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)

    # 파일 다운로드
    with open(local_file_path, "wb") as f:
        # 파일 리스트 읽어 리스트에 있는 파일 선택해서 내려받기
        ftp.retrbinary("파일 선택", f.write)

    print(f"파일 다운로드 완료: ReadMe.txt")
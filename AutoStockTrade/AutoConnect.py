#크레온 api 자동로그인
from pywinauto import application
import time
import os

os.system('taskkill /IM coStarter* /F /T')
os.system('taskkill /IM CpStart* /F /T')
os.system('taskkill /IM DibServer* /F /T')
os.system('wmic process where "name like \'%coStarter%\'" call terminate')
os.system('wmic process where "name like \'%CpStart%\'" call terminate')
os.system('wmic process where "name like \'%DibServer%\'" call terminate')
time.sleep(5)        

app = application.Application()
app.start('C:\CREON\STARTER\coStarter.exe /prj:cp /id:아이디를 적으세요 /pwd:비밀번호를 적으세요 /pwdcert:공인인증서 비밀번호를 적으세요 /autostart') # 크레온 로그인 아이디 / 비밀번호 /공인인증서 비밀번호
time.sleep(60)

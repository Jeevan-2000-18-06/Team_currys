@echo off
cd /d "C:\Users\JeevanSai\OneDrive - Stylosoft LLP\Desktop\pratice.js\pratice.js\Team_Currys"
echo --- [%DATE% %TIME%] Running daily_mail.py --- >> curry_log.txt
C:\Python313\python.exe daily_mail.py >> curry_log.txt 2>&1
echo --- Finished --- >> curry_log.txt

import smtplib
from email.message import EmailMessage
import getpass
password = getpass.getpass('PASSWORD : ')

to_email_list = ['thgml923@naver.com','thgml923@daum.net']



msg = EmailMessage()
msg['Subject'] = '호로롤로로롤'
msg['From'] = 'ab750ab750@gmail.com'
msg['To'] = 'sophiasoheeleem923@gmail.com'
msg.set_content('뀨뀨뀨뀪뀨뀨뀨뀪')

ssafy = smtplib.SMTP_SSL('smtp.naver.com', 465)
ssafy.login('ab750ab750', password)
ssafy.send_message(msg)

print('이메일 전송 완료!')
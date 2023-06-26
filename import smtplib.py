import smtplib

# اطلاعات سرور ایمیل و حساب کاربری خود را وارد کنید
smtp_server = 'smtp.gmail.com'
port = 587
sender_email = 'example@gmail.com'
sender_password = 'password'

# ورود اطلاعات کاربری
session = smtplib.SMTP(smtp_server, port)
session.starttls()
session.login(sender_email, sender_password)

# دریافت نام و ایمیل کاربر
name = input('نام کاربر: ')
recipient_email = input('ایمیل کاربر: ')

# ساخت پیام ایمیل و ارسال
subject = 'پیام شما دریافت شد'
body = f'سلام {name}،\n\nپیام شما با موفقیت دریافت شد.'
message = f'Subject: {subject}\n\n{body}'

session.sendmail(sender_email, recipient_email, message)
print('ایمیل با موفقیت ارسال شد')

# خروج از حساب کاربری و بستن session
session.quit()
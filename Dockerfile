# استفاده از نسخه سبک پایتون
FROM python:3.9-slim

# تنظیم دایرکتوری کاری
WORKDIR /app

# کپی کردن فایل‌ها
COPY . .

# به‌روزرسانی pip و نصب مستقیم وابستگی‌ها (بدون نیاز به requirements.txt)
RUN pip install --upgrade pip
RUN pip install requests pyTelegramBotAPI

# اجرای برنامه
CMD ["python", "chatgbtea.py"]
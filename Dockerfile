# استفاده از نسخه کم‌حجم پایتون به عنوان بیس ایمیج
FROM python:3.9-slim

# تنظیم دایرکتوری کاری
WORKDIR /app

# کپی کردن فایل‌های مورد نیاز
COPY requirements.txt ./
COPY . ./

# نصب وابستگی‌ها
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# اجرای برنامه
CMD ["python", "chatgbtea.py"]
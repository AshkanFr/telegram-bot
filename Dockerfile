# استفاده از تصویر پایه پایتون
FROM python:3.9-slim

# تنظیم دایرکتوری کاری
WORKDIR /app

# کپی کردن فایل‌های مورد نیاز به دایرکتوری کاری
COPY requirements.txt .
COPY chatgbtea.py .

# نصب وابستگی‌ها
RUN pip install --no-cache-dir -r requirements.txt

# فرمان شروع برنامه
CMD ["python", "chatgbtea.py"]

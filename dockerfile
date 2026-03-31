FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
COPY . /app
ENV PYTHONPATH=/app
RUN pip install --no-cache-dir -r requirements.txt
#RUN python manage.py collectstatic --noinput
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "cricketlive.wsgi:application"]

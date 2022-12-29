FROM python:3.7
RUN mkdir /backend
WORKDIR /backend
COPY requirements.txt /backend/requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt
COPY . .
ENV FLASK_APP=/backend/app.py


CMD ["flask", "run", "--host=0.0.0.0"]





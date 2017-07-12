FROM python:3-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN pip install -r test-requirements.txt
RUN pip install -e .
ENV FLASK_APP "s2.app" 
CMD ["flask", "run", "--host", "0.0.0.0"]

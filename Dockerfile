FROM python:3.7
WORKDIR /usr/src/project
COPY . . 
RUN pip3 install --no-cache-dir -r requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:/usr/src/project"
CMD ["python", "./scripts/classify_scores.py"]

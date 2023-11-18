FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./main.py /code/
COPY ./config.py /code/

# 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]


#Instruction for the build and run of the container.
#docker build -t fast_api_demo .
#docker run -p 8000:8000 fast_api_demo
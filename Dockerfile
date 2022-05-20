# FROM python:3

# WORKDIR /code

# ENV PYTHONUNBUFFERED=1
# ENV PYTHONDONTWRITEBYTECODE=1

# COPY requirements.txt /code/
# RUN pip install -r ./requirements.txt
# COPY . /code/

# EXPOSE 8000



# FROM python:3
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1
# WORKDIR /code
# COPY requirements.txt /code/
# RUN pip install -r requirements.txt
# COPY . /code/

# EXPOSE 8000
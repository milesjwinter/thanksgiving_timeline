FROM python:3.8-slim

RUN apt-get update

RUN apt-get install -y --no-install-recommends graphviz

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

# Change the working dir
WORKDIR /proj


# Copy API files
COPY ./timeline ./timeline
COPY ./thanksgiving.py .

# Change to non-root user
RUN groupadd -g 1000 appuser && \
    useradd -r -u 1000 -g appuser appuser
RUN chown -R appuser:appuser /proj

USER appuser

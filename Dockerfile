FROM unit:1.32.0-python3.11
COPY requirements.txt /config/requirements.txt
RUN python3 -m pip install -r /config/requirements.txt
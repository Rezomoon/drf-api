
FROM python:3.11-slim
# From mige k container man gharare roye ch Image sakhteh beshe
# Yani mige k aval yek image amadeh begir baad dastorat ro roaye haman ejra kon!
# python => yani image python ro az ofiical image haye docker dl kon
# 3.11 => version ro moshakhas kardim
# slim => Noe image hastesh , k sabok hastesh va ba paye DEBAIN hastesh , package ezafi nadarad !

ENV PYTHONDONTWRITEBYTECODE=1 
# jelo giri mikone az ejra file haye python bela estedaeh va movaghati(yani file .py k bayad compile beshe va dar __pycache__ yek .pyc sakhteh shavad ro nmizareh anjam shavad !)

# marbote b file system tamiz dashtane
ENV PYTHONUNBUFFERED=1
# Marbote b loggin tamiz 

WORKDIR /app
# dar vaghe dareh dar os linuxi yek file app misaze va oon mishe file aslie ma!

COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
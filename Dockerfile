FROM python:3.6.8-alpine3.8

LABEL MAINTAINER "Johan van der Kuijl <johan.kuijl@alliander.com>"

WORKDIR /usr/src/app

COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt

# RUN pip install -r requirements.txt -i https://nexus.apps.okd.alliander.com/repository/pypi-proxy/simple --trusted-host https://nexus.apps.okd.alliander.com
RUN pip install -r requirements.txt -i https://nexus.apps.ocp-01.prd.ahcaws.com/repository/pypi-proxy/simple
# RUN pip install -r requirements.txt

COPY . .

# the container will be run as this user
#USER appuser

EXPOSE 8080 9090

ENV APPLICATION_NAME        python-nexus-github
ENV APPLICATION_VERSION     1.0.0

CMD ["python","./app.py"]

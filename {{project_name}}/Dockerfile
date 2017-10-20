FROM python:{{python_version}}

ENV TZ 'Asia/Shanghai'

COPY requirements.txt /opt/spider/requirements.txt

RUN pip install -r /opt/spider/requirements.txt

ADD ./ /opt/spider

WORKDIR /opt/spider/{{project_name}}

CMD ["scrapy", "crawl", "{{spider_name}}"]
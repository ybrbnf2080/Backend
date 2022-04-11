FROM python

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["venv\\Script\\activate\n" "cd src\n", "python", "-m", "src/WeGo"]
# Telegram Chatbot

## 사전 설정

- python 3.7

  - 가상환경 설정

    ```bash
    $ python -m venv venv
    $ source vemv/Scripts/activate
    (venv)
    ```

    - 항상 프로젝트 코드를 작성할 때에는 가상환경 활성화 여부를 확인할 것!!

  - pip

    - requests

    - python-decouple

    - flask

    - 현재 상태 기록

      ```bash
      $ pip freeze > requirements.txt
      ```

    - `requirements.txt`내용 설치하기

      ```bash
      $ pip install -r requirements.txt
      ```

- git

  - `.gitignore`

    - `venv/` : 가상환결 설정(Python)
    - `.env` : 환경변수
    - `.vscode` : IDE 설정

    등 프로젝트 소스코드와 무관한 내용들을 설정한다.

- 환경변수

  - API KEY값이나, DB 설정, 혹은 github에 공개되면 안되는 값들
  - 파이썬에서 활용되는 `python-decouple`을 활용하여 `.env`파일로부터 설정된 환경변수를 가져올 수 있음.

## Telegram webhook 설정

사용자가 보내는 메시지를 받아오기 위해서는 Flask 서버와 Telegram의 서버를 웹훅(webhook) 설정을 하여야 한다.

```
https://api.telegram.org/bot{token}/setWebhook?url={url}
```

url을 만들기 위해서는 배포 및 도메인이 필요하지만, `ngrok`이라는 서비스를 통해서 로컬서버에 도메인을 부여할 수 있다.

```bash
$ ngrok http 5000
```
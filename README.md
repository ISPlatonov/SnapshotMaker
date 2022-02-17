# SnapshotMaker

## Зависимости

Для работы необходимо иметь `python3` + `flask`, `ffmpeg` на linux-машине.

Скрипты для установки:

    sudo apt install python3 python3-pip
    pip3 install flask
    sudo apt install ffmpeg

Также используется стандартная коммандная оболочка `bash`.

## Запуск

Запуск API-сервера:

    flask run --host=0.0.0.0

*... потом добавлю файл конфигурации...*

## API

openapi: 3.0.0
info:
    title: "SnapshotMaker"
    version: "0.1"

paths:
    /snapshot/make:
        post:
            description: 'Request to make a snapshot then send to somewhere'
            requestBody:
              content:
                  application/json:
                      schema:
                          type: object
                          properties:
                              addresses_list:
                                  type: array
                                  items:
                                      type: string
                                      required:
                                          - address
                          required:
                              - addresses_list
            responses:
                '200':
                    description: 'Return status of snapshot'
                    content:
                        application/json:
                            schema:
                                type: object
                                properties:
                                    status:
                                        type: string
                                        
                                required:
                                    - status

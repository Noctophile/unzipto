# Copyright (c) 2022 Itz-fork

import os

class Config(object):
    # Mandotory
    APP_ID = int(os.environ.get("21857983"))
    API_HASH = os.environ.get("e469e84c943ce3b8b056eb6a296f2c67")
    BOT_TOKEN = os.environ.get("7994710683:AAEc8wbxnNI06rIh611TyL_1CXcLmR4igTY")
    LOGS_CHANNEL = int(os.environ.get("-1002164681451"))
    BOT_OWNER = int(os.environ.get("833465134"))
    MONGODB_URL = os.environ.get("mongodb+srv://dhimanrajat:Y8IAGI0lVrMhjvkU@cluster0.mytkgu6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    GOFILE_TOKEN = os.environ.get("GOFILE_TOKEN")
    # Optional
    MAX_DOWNLOAD_SIZE = int(os.environ.get("MAX_DOWNLOAD_SIZE")) if os.environ.get("MAX_DOWNLOAD_SIZE") else 10737418240
    # Constents
    DOWNLOAD_LOCATION = f"{os.path.dirname(__file__)}/NexaBots"
    TG_MAX_SIZE = 2040108421
    CHUNK_SIZE = 1024 * 6

import os
from os.path import join, dirname, exists
from dotenv import load_dotenv


def read_env(f):
    filename = ".env." + f
    dotenv_path = join(dirname(__file__), filename)
    if exists(dotenv_path):
        load_dotenv(dotenv_path)

    else:
        print("file doesn't exist")
        return


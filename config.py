import os


class Config:
    class Database:
        MOVIES_PATH = os.path.abspath("resources/Data1000Movies.csv")

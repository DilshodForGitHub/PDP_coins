from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')
DB_PORT = env.str("DB_PORT")
DB_USERNAME = env.str("DB_USERNAME")
DB_NAME = env.str("DB_NAME")
DB_PASSWORD = env.str("DB_PASSWORD")
DB_HOST = env.str("DB_HOST")



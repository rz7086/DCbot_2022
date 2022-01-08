import config.config as cfg
from app.bot import AssistentBot


def main():
    
    cfg.LoadConfig()
    token = cfg.get('token')

    AssistentBot().run(token)

if __name__ == '__main__':
    main()

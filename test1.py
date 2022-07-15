from configparser import ConfigParser

cfg = ConfigParser()
cfg.read('config.ini', encoding='utf-8')
print(cfg.get('all_path', 'path').replace('\\', '/'))

from util.funcs import *
from forms.form_master import Application 
from forms.form_premir import PremirGUI

def main():
    config = ConfigParser()
    configFile = r'util\settings.ini'
    try:
        with open(configFile,'r') as file:
            file.close()
    except IOError:
        config['server'] = {
            'host': 'localhost',
            'user': '',
            'password': '',
            'db': '',
            'setor': ''
        }
        with open(configFile, 'w', encoding='UTF-8') as file:
            config.write(file)

    config.read(configFile)
    server_config = dict(config['server'])
    setor = server_config['setor']
    if setor == 'PREMIR':
        PremirGUI()
        
    else:
        Application()

if __name__ == '__main__':
    main()


import os
import sys
import logging
if getattr(sys,'frozen', False): #frozen exe
    PATH = os.path.dirname(sys.argv[0]) + '\\'
    logging.basicConfig(filename= os.path.dirname(sys.argv[0]) + '\concerto.log', level=logging.DEBUG)
else: #not frozen
    PATH = os.path.dirname(os.path.abspath(__file__)) + '\\'
    logging.basicConfig(filename= os.path.dirname(os.path.abspath(__file__)) + '\concerto.log', level=logging.DEBUG)
logging.warning('Concerto: old CWD is %s' % os.getcwd()) 
os.chdir(PATH)
logging.warning('Concerto: new CWD is %s' % os.getcwd())
import configparser
from kivy.config import Config
from kivy.resources import resource_add_path
if hasattr(sys, '_MEIPASS'):
    resource_add_path(os.path.join(sys._MEIPASS))
os.environ["KIVY_AUDIO"] = "sdl2"
# Kivy app configs
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '400')
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'multisamples', 0)
Config.set('kivy', 'desktop', 1)
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')
Config.set('kivy', 'window_icon', 'concertoicon.ico')
Config.set(
    "kivy",
    "default_font",
    [
        "Roboto",
        'data/fonts/Roboto-Regular.ttf', 
        'data/fonts/Roboto-Italic.ttf',
        'data/fonts/Roboto-Bold.ttf', 
        'data/fonts/Roboto-BoldItalic.ttf'
    ],
)
Config.write()
#CCCaster ini default settings
caster_opt = {
        'alertOnConnect' : '3',
        'alertWavFile' : 'SystemDefault',
        'autoCheckUpdates' : '1',
        'defaultRollback' : '4',
        'displayName' : 'Concerto Player',
        'fullCharacterName' : '0',
        'heldStartDuration' : '1.5',
        'highCpuPriority' : '0',
        'lastMainMenuPosition' : '-1',
        'lastOfflineMenuPosition' : '-1',
        'lastUsedPort' : '-1',
        'maxRealDelay' : '254',
        'replayRollbackOn' : '1',
        'updateChannel' : '1',
        'versusWinCount' : '2'
}
if os.path.exists(PATH + 'cccaster\config.ini'):
    clean = []
    with open(PATH + 'cccaster\config.ini') as f:
        for i in f.readlines():
            for x in caster_opt:
                if x in i:
                    clean.append(x)
    for i in clean:
        del caster_opt[i]
    if len(caster_opt) != 0:
        with open(PATH + 'cccaster\config.ini','a') as f:
            for k,v in caster_opt.items():
                f.write('\n%s=%s' % (k,v))
            f.close()
else:
    with open(PATH + 'cccaster\config.ini', 'w') as f:
        for k,v in caster_opt.items():
                f.write('\n%s=%s' % (k,v))
        f.close()
with open(PATH + 'cccaster\config.ini', 'r') as f:
    config_string = f.read()
caster_config = configparser.ConfigParser()
caster_config.read_string('[settings]\n' + config_string)

#Concerto ini default settings
opt = [
        'netplay_port',
        'mute_alerts',
        'mute_bgm',
        'discord'
]
if os.path.exists(PATH + 'concerto.ini'):
    with open(PATH + 'concerto.ini') as f:
        for i in f.readlines():
            for x in opt:
                if x in i:
                    opt.remove(x)
    if len(opt) != 0:
        with open(PATH + 'concerto.ini','a') as f:
            for i in opt:
                f.write('\n%s=0\n' % i)
            f.close()
else:
    with open(PATH + 'concerto.ini', 'w') as f:
        f.write('[settings]')
        for i in opt:
            f.write('\n%s=%s' % (i,'0'))
        f.close()
with open(PATH + 'concerto.ini','r') as f:
    config_string = f.read()
app_config = configparser.ConfigParser()
app_config.read_string(config_string)

LOBBYURL = "https://concerto-mbaacc.herokuapp.com/l"
VERSIONURL = "https://concerto-mbaacc.herokuapp.com/v"
CURRENT_VERSION = '7-23-2021'
__version__ = '0.5'
Version = __version__ # for backware compatibility

from vim import Vim
from app import PyvisdkApp
from options import Options

def new():
    app = PyvisdkApp()
    app.parse()
    app.connect()
    return app.vim

from .base import *

'''
local環境で追加したものリスト
・django-toolbar（デバッグ用）
'''

DEBUG = True

if DEBUG:
    def show_toolbar(request):
        return True

    INSTALLED_APPS += (
        'debug_toolbar',
    )
    MIDDLEWARE += (
        'debug_toolbar.middleware.DebugToolbarMiddleware'
    )
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK' : show_toolbar,
    }
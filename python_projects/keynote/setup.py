from setuptools import setup

APP = ['output.py']
DATA_FILES = []
OPTIONS = {'argv_emulation': True,
    'plist': {
        'CFBundleName': 'Keynote Converter',
        'CFBundleDisplayName': 'Keynote Converter',
        'CFBundleGetInfoString': 'Keynote Converter 1.0',
        'CFBundleVersion': '1.0',
        'CFBundleShortVersionString': '1.0',
        'NSHumanReadbleCopyright': 'Copyright (c) 2022 Dan McCollum'

    }}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
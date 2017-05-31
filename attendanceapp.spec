# -*- mode: python -*-

block_cipher = None


a = Analysis(['attendanceapp.py'],
             pathex=['C:\\Users\\mohan\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\site-packages\\PyQt5\\Qt\\bin', 'C:\\Users\\mohan\\Developer\\pyqt5\\attendanceapp\\pyqt5'],
             binaries=[],
             datas=[('attendanceapp2.qml', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='attendanceapp',
          debug=True,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='attendanceapp')

REM pip install https://github.com/pyinstaller/pyinstaller/archive/develop.zip
rm -rf build
rm -rf dist
py -3 -m PyInstaller --onedir --paths C:\Users\mohan\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\PyQt5\Qt\bin attendanceapp.spec
cp -r C:\Users\mohan\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\PyQt5\Qt\qml\Qt dist\attendanceapp
cp -r C:\Users\mohan\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\PyQt5\Qt\qml\QtQuick dist\attendanceapp
cp -r C:\Users\mohan\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\PyQt5\Qt\qml\QtQuick.2 dist\attendanceapp
cp C:\Users\mohan\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\PyQt5\Qt\bin\Qt5Quick.dll dist\attendanceapp
cp C:\Users\mohan\AppData\Local\Programs\Python\Python36-32\Lib\site-packages\PyQt5\Qt\bin\Qt5QuickControls.dll dist\attendanceapp
#! python3

import sys
from PyQt5.QtCore import QUrl, QObject, pyqtSlot, QAbstractListModel, QModelIndex, Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtQml import QQmlApplicationEngine, qmlRegisterType
from PyQt5.QtGui import QGuiApplication, QIcon


class MeetingList(QAbstractListModel):

    def __init__(self, parent=None):
        QAbstractListModel.__init__(self, parent)
        self.data = ["January 2018", "February 2018", "March 2018"]

    def data(self, index, role):
        return self.data[index.row()]

    def rowCount(self, index):
        return len(self.data)

    def roleNames(self):
        return {Qt.DisplayRole: b"name"}


data = MeetingList()


sys_argv = sys.argv
sys_argv += ["-style", "Material"]
app = QGuiApplication(sys_argv)
app.setWindowIcon(QIcon('icon.png'))
app.setApplicationDisplayName('Attendance App')
qmlRegisterType(MeetingList, "MeetingList", 1, 0, "MeetingList")

engine = QQmlApplicationEngine()
context = engine.rootContext()
engine.rootContext().setContextProperty('meetings', data)
engine.load('attendanceapp2.qml')
#window = engine.rootObjects()[0]
# window.show()
sys.exit(app.exec_())

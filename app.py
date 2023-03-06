import sys

from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import *

from PyQt5.QtGui import *

from PyQt5.QtWidgets import *

from PyQt5.QtWebKit import *

from PyQt5.QtWebKitWidgets import *

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

app = QApplication(sys.argv)

app.setApplicationName('RammerHead Browser')

web = QWebView()

web.load(QUrl("https://browser.rammerhead.org"))

web.show()

sys.exit(app.exec_())

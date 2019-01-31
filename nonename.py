import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QPushButton
from PyQt5 import QtGui
from PyQt5.QtCore import *
import time
from pygame import mixer
from PyQt5.QtCore import Qt

mixer.init()
import sys

mixer.music.load('song.mp3')


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.write)
        self.timer2 = QTimer(self)
        self.timer2.timeout.connect(self.move_dat)
        self.timer3 = QTimer(self)
        self.timer3.timeout.connect(self.move_b)
        self.title_timer = QTimer(self)
        self.title_timer.timeout.connect(self.move_titles)
        self.init_mus()
        self.initUI()

    def init_mus(self):
        mixer.music.play(-1)

    def write(self):
        if self.n < len(self.talks[self.q]):
            if self.d > 40 and self.talks[self.q][self.n] == ' ':
                self.label_dia.setText(self.label_dia.text() + '\n')
                self.d = 0
            else:
                self.label_dia.setText(self.label_dia.text() + self.talks[self.q][self.n])
                self.d += 1
            self.n += 1
        else:
            self.timer.stop()

    def initUI(self):
        self.speed = 10
        self.setWindowTitle('Det')
        self.q = -1
        self.k = False
        self.inventory = []
        self.setGeometry(50, 50, 1920, 720)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.w = True
        self.talks = ["Вы ведь Генри, да?",
                      "",
                      "Да, это я.",
                      "Прекрасно! Вы пришли как раз вовремя! Я уже собирался уходить.",
                      "Но мне сказали что вы сначала проведете инструктаж..",
                      "Ох, извиняюсь, но мне срочно нужно бежать.",
                      "Осмотритесь пока здесь, а я приеду как только смогу.",
                      "Договорились? Ну и славно!",
                      ""]

        self.talks2 = ["Вы ведь Генри, да?",
                       "",
                       "Нет, это не я.",
                       "Не время розыгрышей, Генри!",
                       "Ладно, уж и пошутить нельзя.",
                       "Ну раз вы такой юморной, развлеките себя сами, а мне уже нужно бежать.",
                       "Осмотритесь пока здесь, но ничего не трогайте!",
                       "Договорились? Ну и славно!",
                       ""]

        self.talks3 = ["Вы ведь Генри, да?",
                       "",
                       "Ну а вы кто?",
                       "Я детектив Гордон из местного отдела расследований, ваш напарник, а вы мистер..?",
                       "Генри Дюваль, из Цоркшира.",
                       "А, наша любимая столица! Странно что вы уехали, но впрочем это ваше дело.",
                       "Мне нужно бежать, так что можете пока осмотреться здесь, Мистер Генри Дюваль.",
                       "Договорились? Ну и славно!",
                       ""]

        self.talks4 = ["Вы ведь Генри, да?",
                       "",
                       "Какая прекрасная погода сегодня, не находите?",
                       "Если честно, я был бы рад если бы вы представились.",
                       "Генри Дюваль, неважно откуда.",
                       "О, вот вы то мне и нужны.",
                       "Не посидите пока здесь? Мне нужно отлучиться на час.",
                       "Договорились? Ну и славно!",
                       ""]

        self.characters = ["Детектив Гордон",
                           "Я",
                           "Детектив Гордон",
                           "Я",
                           "Детектив Гордон",
                           "Детектив Гордон",
                           "Детектив Гордон",
                           ""]
        self.dialogs = ['Что? Так это была проверка?',
                        "Ну извини, нужно же было как то понять с кем я буду работать.",
                        "Серьезно? Вы знаете что такое собеседование?",
                        "В любом случае, ты принят. Поздравляю!",
                        "Ну спасибо.",
                        "Кстати, готов ехать на новое дело?",
                        "Прямо сейчас?",
                        "Да. Произошло убийство в особняке Гаспаччо.",
                        "Так что мы выезжаем прямо сейчас.",
                        "Время не ждет, садись в машину!"]
        self.r = -1
        self.characters2 = ["Я",
                            "Детектив Гордон",
                            "Я",
                            "Детектив Гордон",
                            "Я",
                            "Детектив Гордон",
                            "Я",
                            "Детектив Гордон",
                            "Детектив Гордон",
                            "Детектив Гордон"]

        self.label_room = QLabel(self)
        pix = QtGui.QPixmap("room1.jpg")
        self.label_room.setPixmap(pix)
        self.label_room.move(0, 180)

        self.stol2 = QLabel(self)
        pix = QtGui.QPixmap("stol2.jpg")
        self.stol2.setPixmap(pix)
        self.stol2.move(742, 301 + 180)
        self.stol2.setVisible(False)

        self.wr5 = QLabel(self)
        self.wr5.setWindowFlags(Qt.FramelessWindowHint)
        self.wr5.setAttribute(Qt.WA_TranslucentBackground)
        movie = QtGui.QMovie('kotey.gif')
        self.wr5.setMovie(movie)
        movie.start()
        self.wr5.adjustSize()
        self.wr5.move(923, 510)

        self.label = QLabel(self)
        pixmap = QtGui.QPixmap('dat.png')
        self.label.setPixmap(pixmap)
        self.label.move(800, 135 + 180)

        self.shcaf = QLabel(self)
        pix = QtGui.QPixmap("shcaf.jpg")
        self.shcaf.setPixmap(pix)
        self.shcaf.move(57, 289)
        self.shcaf.setVisible(False)

        self.dver1 = QLabel(self)
        pix = QtGui.QPixmap("dver1.jpg")
        self.dver1.setPixmap(pix)
        self.dver1.move(1690, 180)
        self.dver1.setVisible(False)

        self.label_room2 = QLabel(self)
        pix = QtGui.QPixmap("stol1.png")
        self.label_room2.setPixmap(pix)
        self.label_room2.setVisible(False)

        self.stol3 = QLabel(self)
        pix = QtGui.QPixmap("stol3.png")
        self.stol3.setPixmap(pix)
        self.stol3.move(397, 103)
        self.stol3.setVisible(False)

        self.yas = QLabel(self)
        pix = QtGui.QPixmap("yaz1.jpg")
        self.yas.setPixmap(pix)
        self.yas.move(0, -10)
        self.yas.setVisible(False)

        self.key_1 = QLabel(self)
        pix = QtGui.QPixmap("key1.png")
        self.key_1.setPixmap(pix)
        self.key_1.move(700, 490)
        self.key_1.setVisible(False)

        pix = QtGui.QPixmap("black.png")
        self.label_b = QLabel(self)
        self.label_b.setPixmap(pix)
        self.label_b.move(1920, 0)

        self.yfpfhljlbr = QLabel(self)
        pix = QtGui.QPixmap("original.png")
        self.yfpfhljlbr.setPixmap(pix)
        self.yfpfhljlbr.setVisible(False)

        self.strelka = QLabel(self)
        pix = QtGui.QPixmap("razvorot.png")
        self.strelka.setPixmap(pix)
        self.strelka.move(20, 800 + 180)
        self.strelka.setVisible(False)

        self.strelka2 = QLabel(self)
        pix = QtGui.QPixmap("razvorot.png")
        self.strelka2.setPixmap(pix)
        self.strelka2.move(20, 800 + 180)
        self.strelka2.setVisible(False)

        self.strelka3 = QLabel(self)
        pix = QtGui.QPixmap("razvorot.png")
        self.strelka3.setPixmap(pix)
        self.strelka3.move(20, 800 + 180)
        self.strelka3.setVisible(False)

        '''
        self.choose = QLabel(self)
        pix = QtGui.QPixmap("choose.png")
        self.choose.setPixmap(pix)
        self.choose.move(1830, 184 + 180)
        # self.chose.setVisible(False)

        self.inv2 = QLabel(self)
        pix = QtGui.QPixmap("inv.png")
        self.inv2.setPixmap(pix)
        self.inv2.move(1838, 290 + 180)
        # self.inv.setVisible(False)

        self.inv3 = QLabel(self)
        pix = QtGui.QPixmap("inv.png")
        self.inv3.setPixmap(pix)
        self.inv3.move(1838, 390 + 180)
        # self.inv.setVisible(False)

        self.inv4 = QLabel(self)
        pix = QtGui.QPixmap("inv.png")
        self.inv4.setPixmap(pix)
        self.inv4.move(1838, 490 + 180)
        # self.inv.setVisible(False)

        self.inv5 = QLabel(self)
        pix = QtGui.QPixmap("inv.png")
        self.inv5.setPixmap(pix)
        self.inv5.move(1838, 590 + 180)
        # self.inv.setVisible(False)
        '''

        self.menu = QLabel(self)
        pix = QtGui.QPixmap("menu.png")
        self.menu.setPixmap(pix)
        self.menu.move(1800, 10 + 180)
        self.menu.setVisible(False)

        self.menu_label_1 = QLabel(self)
        self.menu_label_1.setText("Осмотреться в комнате.                                                             ")
        self.menu_label_1.setFont(QtGui.QFont("Calibri", 13, QtGui.QFont.Bold))
        self.menu_label_1.setStyleSheet("QLabel { color: white}")
        self.menu_label_1.move(1570, 80 + 180)
        self.menu_label_1.setVisible(False)

        self.menu_label_2 = QLabel(self)
        self.menu_label_2.setText("Прогуляться после осмотра.                                                         ")
        self.menu_label_2.setFont(QtGui.QFont("Calibri", 13, QtGui.QFont.Bold))
        self.menu_label_2.setStyleSheet("QLabel { color: white}")
        self.menu_label_2.move(1570, 140 + 180)
        self.menu_label_2.setVisible(False)

        self.wr = QLabel(self)
        self.wr.setWindowFlags(Qt.FramelessWindowHint)
        self.wr.setAttribute(Qt.WA_TranslucentBackground)
        movie = QtGui.QMovie('fire.gif')
        self.wr.setMovie(movie)
        movie.start()
        self.wr.adjustSize()
        self.wr.move(150, 472)

        self.wr2 = QLabel(self)
        self.wr2.setWindowFlags(Qt.FramelessWindowHint)
        self.wr2.setAttribute(Qt.WA_TranslucentBackground)
        movie = QtGui.QMovie('fire.gif')
        self.wr2.setMovie(movie)
        movie.start()
        self.wr2.adjustSize()
        self.wr2.move(223, 548)

        self.wr3 = QLabel(self)
        self.wr3.setWindowFlags(Qt.FramelessWindowHint)
        self.wr3.setAttribute(Qt.WA_TranslucentBackground)
        movie = QtGui.QMovie('fire.gif')
        self.wr3.setMovie(movie)
        movie.start()
        self.wr3.adjustSize()
        self.wr3.move(1085, 600)

        self.wr4 = QLabel(self)
        self.wr4.setWindowFlags(Qt.FramelessWindowHint)
        self.wr4.setAttribute(Qt.WA_TranslucentBackground)
        movie = QtGui.QMovie('fire.gif')
        self.wr4.setMovie(movie)
        movie.start()
        self.wr4.adjustSize()
        self.wr4.move(1048, 621)
        self.wr4.setVisible(False)

        self.car = QLabel(self)
        pix = QtGui.QPixmap("street.jpg")
        self.car.setPixmap(pix)
        self.car.setVisible(False)

        self.label_dialog = QLabel(self)
        pix_dia = QtGui.QPixmap("dialogue.png")
        self.label_dialog.setPixmap(pix_dia)
        self.label_dialog.move(200, 550 + 180)

        self.label_dia = QLabel(self)
        self.label_dia.resize(1000, 80)
        self.label_dia.setText("О вы уже здесь, Генри!                       "
                               "                                            "
                               "                                                       ")
        self.label_dia.move(500, 620 + 180)
        self.label_dia.setFont(QtGui.QFont("Times", 13, QtGui.QFont.Bold))
        self.label_dial = QLabel(self)
        self.label_dial.setText("Детектив Гордон")
        self.label_dial.move(550, 565 + 180)
        self.label_dial.setFont(QtGui.QFont("Times", 13, QtGui.QFont.Bold))
        self.label_dial.setStyleSheet("QLabel { color: brown}")

        self.main_l1 = QLabel(self)
        pix = QtGui.QPixmap("good.png")
        self.main_l1.setPixmap(pix)
        self.main_l1.move(900, 610 + 180)

        self.main_l2 = QLabel(self)
        pix = QtGui.QPixmap("deny.png")
        self.main_l2.setPixmap(pix)
        self.main_l2.move(1000, 610 + 180)

        self.main_l3 = QLabel(self)
        pix = QtGui.QPixmap("aim.png")
        self.main_l3.setPixmap(pix)
        self.main_l3.move(1100, 610 + 180)

        self.main_l4 = QLabel(self)
        pix = QtGui.QPixmap("spy.png")
        self.main_l4.setPixmap(pix)
        self.main_l4.move(1200, 610 + 180)

        self.main_l5 = QLabel(self)
        pix = QtGui.QPixmap("smile.png")
        self.main_l5.setPixmap(pix)
        self.main_l5.move(1300, 610 + 180)

        self.main_l6 = QLabel(self)
        pix = QtGui.QPixmap("list.png")
        self.main_l6.setPixmap(pix)
        self.main_l6.move(1400, 610 + 180)

        self.main_l7 = QLabel(self)
        pix = QtGui.QPixmap("end.png")
        self.main_l7.setPixmap(pix)
        self.main_l7.move(1500, 610 + 180)

        self.arrow_right = QLabel(self)
        pixmap = QtGui.QPixmap('arrow_right.png')
        self.main_l5.setVisible(False)
        self.main_l6.setVisible(False)
        self.arrow_right.setPixmap(pixmap)
        self.arrow_right.move(1550, 660 + 180)

        self.arrow_right2 = QLabel(self)
        pixmap = QtGui.QPixmap('arrow_right.png')
        self.arrow_right2.setPixmap(pixmap)
        self.arrow_right2.move(1550, 660 + 180)
        self.arrow_right2.setVisible(False)

        self.arrow_right3 = QLabel(self)
        pixmap = QtGui.QPixmap('arrow_right.png')
        self.arrow_right3.setPixmap(pixmap)
        self.arrow_right3.move(1550, 80)
        self.arrow_right3.setVisible(False)

        self.car2 = QLabel(self)
        pixmap = QtGui.QPixmap('street2.jpg')
        self.car2.setPixmap(pixmap)
        self.car2.move(507, 760)
        self.car2.setVisible(False)

        self.wr6 = QLabel(self)
        self.wr6.setWindowFlags(Qt.FramelessWindowHint)
        self.wr6.setAttribute(Qt.WA_TranslucentBackground)
        movie = QtGui.QMovie('nplox.gif')
        self.wr6.setMovie(movie)
        movie.start()
        self.wr6.adjustSize()
        self.wr6.move(723, 0)
        self.wr6.setVisible(False)

        self.wr7 = QLabel(self)
        self.wr7.setWindowFlags(Qt.FramelessWindowHint)
        self.wr7.setAttribute(Qt.WA_TranslucentBackground)
        movie = QtGui.QMovie('y4.gif')
        self.wr7.setMovie(movie)
        movie.start()
        self.wr7.adjustSize()
        self.wr7.move(123, 0)
        self.wr7.setVisible(False)

        self.wr8 = QLabel(self)
        self.wr8.setWindowFlags(Qt.FramelessWindowHint)
        self.wr8.setAttribute(Qt.WA_TranslucentBackground)
        movie = QtGui.QMovie('shark.gif')
        self.wr8.setMovie(movie)
        movie.start()
        self.wr8.adjustSize()
        self.wr8.move(1523, 0)
        self.wr8.setVisible(False)

        self.main_l1.setVisible(False)
        self.main_l2.setVisible(False)
        self.main_l3.setVisible(False)
        self.main_l4.setVisible(False)
        self.main_l7.setVisible(False)

        '''
        self.inv = QLabel(self)в
        pix = QtGui.QPixmap("inv.png")
        self.inv.setPixmap(pix)
        self.inv.move(1838, 190 + 180)
        self.inv.setVisible(False)
        self.inv2.setVisible(False)
        self.inv3.setVisible(False)
        self.inv4.setVisible(False)
        self.inv5.setVisible(False)
        self.choose.setVisible(False)
        '''

        self.main_l1.mousePressEvent = self.getPos2
        self.main_l2.mousePressEvent = self.getPos3
        self.main_l3.mousePressEvent = self.getPos4
        self.main_l4.mousePressEvent = self.getPos5
        self.arrow_right.mousePressEvent = self.getPos
        self.arrow_right2.mousePressEvent = self.getPos20
        self.menu.mousePressEvent = self.getPos6
        '''
        self.inv.mousePressEvent = self.getPos7
        self.inv2.mousePressEvent = self.getPos8
        self.inv3.mousePressEvent = self.getPos9
        self.inv4.mousePressEvent = self.getPos10
        self.inv5.mousePressEvent = self.getPos11
        '''
        self.stol2.mousePressEvent = self.start_b
        self.stol3.mousePressEvent = self.getPos13
        self.strelka.mousePressEvent = self.getPos14
        self.strelka2.mousePressEvent = self.getPos15
        self.key_1.mousePressEvent = self.getPos16
        self.shcaf.mousePressEvent = self.getPos17
        self.strelka3.mousePressEvent = self.getPos18
        self.arrow_right3.mousePressEvent = self.getPos21
        self.dver1.mousePressEvent = self.getPos19
        self.car2.mousePressEvent = self.getPos22

        self.showFullScreen()

    def start_b(self, event):
        self.timer3.start(1)

    def move_b(self):
        self.label_b.move(self.label_b.x() - 30, self.label_b.y())
        if self.label_b.x() == 0:
            self.getPos12()
        if self.label_b.x() < -1920:
            self.label_b.move(1920, 0)
            self.timer3.stop()

    def next_text(self):
        if self.q == 0:
            self.main_l1.setVisible(True)
            self.main_l2.setVisible(True)
            self.main_l3.setVisible(True)
            self.main_l4.setVisible(True)
            self.arrow_right.setVisible(False)
        if self.q < 8 and self.q != 0:
            self.label_dial.setText(self.characters[self.q])
            self.n = 0
            self.d = 0
            self.label_dia.setText('')
            self.timer.start(10)
        if self.q == 7:
            self.wr5.setVisible(True)
            self.menu.setVisible(True)
            self.shcaf.setVisible(True)
            # тут нужно сделать эффект ухода
            self.label.clear()
            self.label.setPixmap(QtGui.QPixmap('dat2.png'))
            self.timer2.start(10)
        if self.q == 7:
            self.arrow_right.setVisible(False)
            self.label_dialog.setVisible(False)
        self.q = self.q + 1

    def after_move(self):
        if self.q == 7:
            self.stol2.setVisible(True)

    def move_dat(self):
        self.label.move(self.label.x() + self.speed, self.label.y())
        if self.label.x() > 1000:
            self.wr4.setVisible(True)
        if self.label.x() > 2000:
            self.after_move()
            self.label = QLabel(self)
            pixmap = QtGui.QPixmap('dat.png')
            self.label.setPixmap(pixmap)
            self.timer2.stop()
            self.stol2.setVisible(True)
            self.dver1.setVisible(True)

    def getPos(self, event):
        self.next_text()

    def getPos2(self, event):
        self.main_l1.setVisible(False)
        self.main_l2.setVisible(False)
        self.main_l3.setVisible(False)
        self.main_l4.setVisible(False)
        self.arrow_right.setVisible(True)
        self.next_text()

    def getPos3(self, event):
        self.main_l1.setVisible(False)
        self.main_l2.setVisible(False)
        self.main_l3.setVisible(False)
        self.main_l4.setVisible(False)
        self.arrow_right.setVisible(True)
        self.talks = self.talks2
        self.next_text()

    def getPos4(self, event):
        self.main_l1.setVisible(False)
        self.main_l2.setVisible(False)
        self.main_l3.setVisible(False)
        self.main_l4.setVisible(False)
        self.arrow_right.setVisible(True)
        self.talks = self.talks3
        self.next_text()

    def getPos5(self, event):
        self.main_l1.setVisible(False)
        self.main_l2.setVisible(False)
        self.main_l3.setVisible(False)
        self.main_l4.setVisible(False)
        self.arrow_right.setVisible(True)
        self.talks = self.talks4
        self.next_text()

    def getPos6(self, event):
        self.menu_label_1.setVisible(self.w)
        self.menu_label_2.setVisible(self.w)
        if self.w is True:
            self.w = False
        else:
            self.w = True

    '''
    def getPos7(self, event):
        self.choose.move(1830, 184 + 180)

    def getPos8(self, event):
        self.choose.move(1830, 284 + 180)

    def getPos9(self, event):
        self.choose.move(1830, 384 + 180)

    def getPos10(self, event):
        self.choose.move(1830, 484 + 180)

    def getPos11(self, event):
        self.choose.move(1830, 584 + 180)
    '''

    def getPos12(self):
        self.stol2.setVisible(False)
        self.label_room.setVisible(False)
        self.label_room2.setVisible(True)
        self.strelka.setVisible(True)
        self.stol3.setVisible(True)
        self.label_dia.setVisible(True)
        self.label_dial.setVisible(True)
        self.label_dialog.setVisible(True)
        self.label_dia.setText("Старинный стол. Открыт только первый ящик.")
        self.label_dial.setText("Я")
        self.menu.move(1800, 10)
        self.wr3.setVisible(False)
        self.wr2.setVisible(False)
        self.wr.setVisible(False)
        self.wr4.setVisible(False)
        self.menu_label_1.move(1570, 80)
        self.menu_label_2.move(1570, 140)

    def getPos13(self, event):
        self.stol3.setVisible(False)
        self.strelka2.setVisible(True)
        self.label_room.setVisible(False)
        self.label_room2.setVisible(False)
        self.yas.setVisible(True)
        if self.key_1 not in self.inventory:
            self.label_dia.setVisible(True)
            self.label_dial.setVisible(True)
            self.label_dialog.setVisible(True)
            self.label_dia.setText("Здесь какой-то ключ.")
            self.label_dial.setText("Я")
            self.key_1.setVisible(True)
        else:
            self.label_dia.setVisible(False)
            self.label_dial.setVisible(False)
            self.label_dialog.setVisible(False)

    def getPos14(self, event):
        self.yas.setVisible(False)
        self.stol3.setVisible(False)
        self.stol2.setVisible(True)
        self.label_room2.setVisible(False)
        self.label_room.setVisible(True)
        self.strelka.setVisible(False)
        self.wr3.setVisible(True)
        self.wr2.setVisible(True)
        self.wr.setVisible(True)
        self.wr4.setVisible(True)
        self.label_dia.setVisible(False)
        self.label_dial.setVisible(False)
        self.label_dialog.setVisible(False)
        self.menu.move(1800, 10 + 180)
        self.menu_label_1.move(1570, 80 + 180)
        self.menu_label_2.move(1570, 140 + 180)

    def getPos15(self, event):
        self.yas.setVisible(False)
        self.stol2.setVisible(True)
        self.label_room2.setVisible(True)
        self.stol3.setVisible(True)
        self.strelka2.setVisible(False)
        self.strelka.setVisible(True)
        self.label_dia.setVisible(False)
        self.label_dial.setVisible(False)
        self.label_dialog.setVisible(False)
        self.key_1.setVisible(False)

    def getPos16(self, event):
        self.key_1.setVisible(False)
        self.inventory.append(self.key_1)

    def getPos17(self, event):
        self.shcaf.setVisible(False)
        self.label_room.setVisible(False)
        self.stol2.setVisible(False)
        self.yfpfhljlbr.setVisible(True)
        self.label_dia.setVisible(True)
        self.label_dial.setVisible(True)
        self.label_dialog.setVisible(True)
        self.label_dia.setText("Впечатляющая библиотека! Но в целом ничего интересного.")
        self.label_dial.setText("Я")
        self.menu.move(1800, 10)
        self.menu_label_2.move(1550, 70)
        self.menu_label_1.move(1550, 140)
        self.strelka3.setVisible(True)
        self.wr3.setVisible(False)
        self.wr2.setVisible(False)
        self.wr.setVisible(False)
        self.wr4.setVisible(False)

    def getPos18(self, event):
        self.shcaf.setVisible(True)
        self.label_room.setVisible(True)
        self.label_dia.setVisible(True)
        self.label_dial.setVisible(True)
        self.stol2.setVisible(True)
        self.yfpfhljlbr.setVisible(False)
        self.label_dia.setVisible(False)
        self.label_dial.setVisible(False)
        self.label_dialog.setVisible(False)
        self.menu.move(1800, 10 + 180)
        self.menu_label_2.move(1600, 70 + 180)
        self.menu_label_1.move(1600, 140 + 180)
        self.strelka3.setVisible(False)
        self.wr3.setVisible(True)
        self.wr2.setVisible(True)
        self.wr.setVisible(True)
        self.wr4.setVisible(True)

    def getPos19(self, event):
        if self.key_1 in self.inventory:
            self.strelka3.setVisible(False)
            self.wr3.setVisible(False)
            self.wr2.setVisible(False)
            self.wr.setVisible(False)
            self.wr4.setVisible(False)
            self.label_room.setVisible(False)
            self.label_dial.setVisible(True)
            self.label_dia.setVisible(True)
            self.label_dialog.setVisible(True)
            self.label_dia.setText("3 минуты, 43 секунды. Неплохо. Но можно было лучше.")
            self.label_dial.setText("Детектив Гордон")
            self.stol2.setVisible(False)
            self.label_room.setVisible(False)
            self.wr5.setVisible(False)
            self.shcaf.setVisible(False)
            self.car.setVisible(True)
            self.dver1.setVisible(False)
            self.label.setVisible(True)
            self.label_dialog.move(200, -190 + 180)
            self.label_dia.move(300, -130 + 180)
            self.label_dial.move(500, -175 + 180)
            self.label.move(800, 600)
            self.arrow_right3.setVisible(True)
        else:
            self.label_dia.setVisible(True)
            self.label_dial.setVisible(True)
            self.label_dialog.setVisible(True)
            self.label_dia.setText("Закрытая дверь. Стоп, меня закрыли!? Зачем!?")
            self.label_dial.setText("Я")
            self.arrow_right2.setVisible(True)

    def getPos20(self, event):
        self.arrow_right2.setVisible(False)
        self.label_dia.setVisible(False)
        self.label_dial.setVisible(False)
        self.label_dialog.setVisible(False)

    def getPos21(self, event):
        if self.r < 9:
            self.r = self.r + 1
            self.label_dia.setText('')
            self.talks = self.dialogs
            self.label_dial.setText(self.characters2[self.r])
            self.n = 0
            self.d = 0
            self.q = self.r
            self.timer.start(10)
        if self.r == 9:
            self.arrow_right3.setVisible(False)
            self.label.setVisible(False)
            self.car2.setVisible(True)

    def getPos22(self, event):
        self.arrow_right3.setVisible(False)
        self.car2.setVisible(False)
        self.titles()
        self.wr6.setVisible(True)
        self.wr7.setVisible(True)
        self.wr8.setVisible(True)
        mixer.music.load('give.mp3')
        mixer.music.play(-1)

    def titles(self):
        self.game_developers = ['               ТИТРЫ',

                                '       ПРОГРАММИСТЫ\n        назаров никита\n        рашкин никита',

                                '            ВСЕ РОЛИ\n       были взяты из\n      головы рашкина',

                                '                 КП\n             из труе',

                                '           АНИМАЦИЯ\n        рашкин никита\n        назаров никита\n            интернет)',

                                '         СЦЕНАРИСТЫ\n        рашкин никита\n        назаров никита',

                                '        ПРОДОЛЖЕНИЕ\n     будет с шансом 50%',
                                '    Вероятно у вас нет\n рук и ног чтобы убежать\n    или выключить комп,\n так что сочувствуем вам.',

                                '       СДЕЛАНО ПО ЗАКАЗУ\n       Олега Геннадьевича\n      (нам не платили)\n       но если честно\n даже мы бы не платили за это',

                                '        ПРОИЗВОДСТВО\n      FLEX INTERTAINMENT', ]

        self.label_dial.setVisible(False)
        self.label_dia.setVisible(False)
        self.label_dialog.setVisible(False)
        self.car.setVisible(False)
        self.label.setVisible(False)
        self.menu.setVisible(False)

        self.titles_red = QLabel(self)
        self.titles_red.resize(1900, 10000)
        self.titles_red.move(500, -2000)
        self.titles_red.setFont(QtGui.QFont("Times", 30, QtGui.QFont.Bold))
        self.titles_red.setStyleSheet("QLabel { color: red}")

        self.titles_label = QLabel(self)
        self.titles_label.resize(1900, 10000)
        self.titles_label.move(500, -2000)
        self.titles_label.setFont(QtGui.QFont("Times", 30, QtGui.QFont.Bold))
        self.titles_label.setStyleSheet("QLabel { color: white}")
        for i in self.game_developers:
            self.titles_label.setText(self.titles_label.text() + '\n\n\n\n' + i)
            self.titles_red.setText(self.titles_red.text() + '\n\n\n\n' + i)
        self.deltax = 0
        self.deltay = 0
        self.plusx = -0.1
        self.titles_red.show()
        self.titles_label.show()
        self.title_timer.start(10)

    def move_titles(self):
        self.titles_red.move(self.titles_red.x() + self.deltax, self.titles_red.y() - 1 + self.deltay)
        self.titles_label.move(self.titles_label.x(), self.titles_label.y() - 1)
        self.deltax = round(self.deltax + self.plusx, 2)
        if self.deltax <= -0.5:
            self.plusx = 0.1
        elif self.deltax >= 1.4:
            self.plusx = -0.1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

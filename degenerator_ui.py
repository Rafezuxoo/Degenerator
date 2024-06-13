# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'degenrator_ui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QFrame, QGroupBox, QHBoxLayout,
                               QLabel, QLineEdit, QPushButton,
                               QRadioButton, QSizePolicy, QSpacerItem, QTextBrowser,
                               QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(801, 912)
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"backgound-color:blue")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font1 = QFont()
        font1.setFamilies([u"Comic Sans MS"])
        font1.setPointSize(12)
        self.centralwidget.setFont(font1)
        self.centralwidget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop: 1 rgba(155, 79, 165, 255));")
        self.name_layer = QFrame(self.centralwidget)
        self.name_layer.setObjectName(u"name_layer")
        self.name_layer.setGeometry(QRect(0, 0, 801, 51))
        self.name_layer.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout = QHBoxLayout(self.name_layer)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.name_enter_label = QLabel(self.name_layer)
        self.name_enter_label.setObjectName(u"name_enter_label")
        self.name_enter_label.setFont(font1)
        self.name_enter_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;\n"
"")

        self.horizontalLayout.addWidget(self.name_enter_label)

        self.name_lineEdit = QLineEdit(self.name_layer)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setFont(font1)
        self.name_lineEdit.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout.addWidget(self.name_lineEdit)

        self.generate_pushButton = QPushButton(self.name_layer)
        self.generate_pushButton.setObjectName(u"generate_pushButton")
        font2 = QFont()
        font2.setFamilies([u"Comic Sans MS"])
        font2.setPointSize(11)
        self.generate_pushButton.setFont(font2)
        self.generate_pushButton.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")

        self.horizontalLayout.addWidget(self.generate_pushButton)

        self.save_as_txt_pushButton = QPushButton(self.name_layer)
        self.save_as_txt_pushButton.setObjectName(u"save_as_txt_pushButton")
        self.save_as_txt_pushButton.setFont(font2)
        self.save_as_txt_pushButton.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")

        self.horizontalLayout.addWidget(self.save_as_txt_pushButton)

        self.save_as_png_pushButton = QPushButton(self.name_layer)
        self.save_as_png_pushButton.setObjectName(u"save_as_png_pushButton")
        self.save_as_png_pushButton.setFont(font2)
        self.save_as_png_pushButton.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")

        self.horizontalLayout.addWidget(self.save_as_png_pushButton)

        self.base_info = QFrame(self.centralwidget)
        self.base_info.setObjectName(u"base_info")
        self.base_info.setGeometry(QRect(0, 50, 521, 661))
        self.base_info.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.verticalLayout = QVBoxLayout(self.base_info)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.name_and_level = QGroupBox(self.base_info)
        self.name_and_level.setObjectName(u"name_and_level")
        self.name_and_level.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(self.name_and_level)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.name_label = QLabel(self.name_and_level)
        self.name_label.setObjectName(u"name_label")
        self.name_label.setFont(font1)
        self.name_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_2.addWidget(self.name_label)

        self.name_textBrowser = QTextBrowser(self.name_and_level)
        self.name_textBrowser.setObjectName(u"name_textBrowser")
        self.name_textBrowser.setEnabled(True)
        self.name_textBrowser.setFont(font1)
        self.name_textBrowser.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_2.addWidget(self.name_textBrowser)

        self.level_label = QLabel(self.name_and_level)
        self.level_label.setObjectName(u"level_label")
        self.level_label.setFont(font1)
        self.level_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_2.addWidget(self.level_label)

        self.level_textBrowser = QTextBrowser(self.name_and_level)
        self.level_textBrowser.setObjectName(u"level_textBrowser")
        self.level_textBrowser.setEnabled(True)
        self.level_textBrowser.setFont(font1)
        self.level_textBrowser.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_2.addWidget(self.level_textBrowser)


        self.verticalLayout.addWidget(self.name_and_level)

        self.race_and_class = QGroupBox(self.base_info)
        self.race_and_class.setObjectName(u"race_and_class")
        self.race_and_class.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.race_and_class)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.race_label = QLabel(self.race_and_class)
        self.race_label.setObjectName(u"race_label")
        self.race_label.setFont(font1)
        self.race_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_3.addWidget(self.race_label)

        self.race_textBrowser = QTextBrowser(self.race_and_class)
        self.race_textBrowser.setObjectName(u"race_textBrowser")
        self.race_textBrowser.setEnabled(True)
        self.race_textBrowser.setFont(font1)
        self.race_textBrowser.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_3.addWidget(self.race_textBrowser)

        self.class_label = QLabel(self.race_and_class)
        self.class_label.setObjectName(u"class_label")
        self.class_label.setFont(font1)
        self.class_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_3.addWidget(self.class_label)

        self.class_textBrowser = QTextBrowser(self.race_and_class)
        self.class_textBrowser.setObjectName(u"class_textBrowser")
        self.class_textBrowser.setEnabled(True)
        self.class_textBrowser.setFont(font1)
        self.class_textBrowser.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_3.addWidget(self.class_textBrowser)


        self.verticalLayout.addWidget(self.race_and_class)

        self.background_and_alignment = QGroupBox(self.base_info)
        self.background_and_alignment.setObjectName(u"background_and_alignment")
        self.background_and_alignment.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_4 = QHBoxLayout(self.background_and_alignment)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.background_lable = QLabel(self.background_and_alignment)
        self.background_lable.setObjectName(u"background_lable")
        self.background_lable.setFont(font1)
        self.background_lable.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_4.addWidget(self.background_lable)

        self.background_textBrowser = QTextBrowser(self.background_and_alignment)
        self.background_textBrowser.setObjectName(u"background_textBrowser")
        self.background_textBrowser.setEnabled(True)
        self.background_textBrowser.setFont(font1)
        self.background_textBrowser.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_4.addWidget(self.background_textBrowser)

        self.alignment_label = QLabel(self.background_and_alignment)
        self.alignment_label.setObjectName(u"alignment_label")
        self.alignment_label.setFont(font1)
        self.alignment_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_4.addWidget(self.alignment_label)

        self.alignment_textBrowser = QTextBrowser(self.background_and_alignment)
        self.alignment_textBrowser.setObjectName(u"alignment_textBrowser")
        self.alignment_textBrowser.setEnabled(True)
        self.alignment_textBrowser.setFont(font1)
        self.alignment_textBrowser.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_4.addWidget(self.alignment_textBrowser)


        self.verticalLayout.addWidget(self.background_and_alignment)

        self.hit_dice_and_hits = QGroupBox(self.base_info)
        self.hit_dice_and_hits.setObjectName(u"hit_dice_and_hits")
        self.hit_dice_and_hits.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_5 = QHBoxLayout(self.hit_dice_and_hits)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.hit_dice_label = QLabel(self.hit_dice_and_hits)
        self.hit_dice_label.setObjectName(u"hit_dice_label")
        self.hit_dice_label.setFont(font1)
        self.hit_dice_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_5.addWidget(self.hit_dice_label)

        self.hit_dice_textBrowser = QTextBrowser(self.hit_dice_and_hits)
        self.hit_dice_textBrowser.setObjectName(u"hit_dice_textBrowser")
        self.hit_dice_textBrowser.setEnabled(True)
        self.hit_dice_textBrowser.setFont(font1)
        self.hit_dice_textBrowser.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_5.addWidget(self.hit_dice_textBrowser)

        self.hits_label = QLabel(self.hit_dice_and_hits)
        self.hits_label.setObjectName(u"hits_label")
        self.hits_label.setFont(font1)
        self.hits_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_5.addWidget(self.hits_label)

        self.hits_textBrowser = QTextBrowser(self.hit_dice_and_hits)
        self.hits_textBrowser.setObjectName(u"hits_textBrowser")
        self.hits_textBrowser.setEnabled(True)
        self.hits_textBrowser.setFont(font1)
        self.hits_textBrowser.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_5.addWidget(self.hits_textBrowser)


        self.verticalLayout.addWidget(self.hit_dice_and_hits)

        self.proficiency_bonus_and_size = QGroupBox(self.base_info)
        self.proficiency_bonus_and_size.setObjectName(u"proficiency_bonus_and_size")
        self.proficiency_bonus_and_size.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_18 = QHBoxLayout(self.proficiency_bonus_and_size)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.proficiency_bonus_label = QLabel(self.proficiency_bonus_and_size)
        self.proficiency_bonus_label.setObjectName(u"proficiency_bonus_label")
        self.proficiency_bonus_label.setFont(font1)
        self.proficiency_bonus_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_18.addWidget(self.proficiency_bonus_label)

        self.proficiency_bonus_textBrowser = QTextBrowser(self.proficiency_bonus_and_size)
        self.proficiency_bonus_textBrowser.setObjectName(u"proficiency_bonus_textBrowser")
        self.proficiency_bonus_textBrowser.setEnabled(True)
        self.proficiency_bonus_textBrowser.setFont(font1)
        self.proficiency_bonus_textBrowser.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_18.addWidget(self.proficiency_bonus_textBrowser)

        self.size_label = QLabel(self.proficiency_bonus_and_size)
        self.size_label.setObjectName(u"size_label")
        self.size_label.setFont(font1)
        self.size_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_18.addWidget(self.size_label)

        self.size_textBrowser = QTextBrowser(self.proficiency_bonus_and_size)
        self.size_textBrowser.setObjectName(u"size_textBrowser")
        self.size_textBrowser.setEnabled(True)
        self.size_textBrowser.setFont(font1)
        self.size_textBrowser.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_18.addWidget(self.size_textBrowser)


        self.verticalLayout.addWidget(self.proficiency_bonus_and_size)

        self.name_and_base_spell_mod = QGroupBox(self.base_info)
        self.name_and_base_spell_mod.setObjectName(u"name_and_base_spell_mod")
        self.name_and_base_spell_mod.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_6 = QHBoxLayout(self.name_and_base_spell_mod)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.speed_label = QLabel(self.name_and_base_spell_mod)
        self.speed_label.setObjectName(u"speed_label")
        self.speed_label.setFont(font1)
        self.speed_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_6.addWidget(self.speed_label)

        self.speed_textBrowser = QTextBrowser(self.name_and_base_spell_mod)
        self.speed_textBrowser.setObjectName(u"speed_textBrowser")
        self.speed_textBrowser.setEnabled(True)
        self.speed_textBrowser.setFont(font1)
        self.speed_textBrowser.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_6.addWidget(self.speed_textBrowser)

        self.base_spell_mod_label = QLabel(self.name_and_base_spell_mod)
        self.base_spell_mod_label.setObjectName(u"base_spell_mod_label")
        self.base_spell_mod_label.setFont(font1)
        self.base_spell_mod_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_6.addWidget(self.base_spell_mod_label)

        self.base_spell_mod_textBrowser = QTextBrowser(self.name_and_base_spell_mod)
        self.base_spell_mod_textBrowser.setObjectName(u"base_spell_mod_textBrowser")
        self.base_spell_mod_textBrowser.setEnabled(True)
        self.base_spell_mod_textBrowser.setFont(font1)
        self.base_spell_mod_textBrowser.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_6.addWidget(self.base_spell_mod_textBrowser)


        self.verticalLayout.addWidget(self.name_and_base_spell_mod)

        self.proficient_dif_and_magic_attack_mod = QGroupBox(self.base_info)
        self.proficient_dif_and_magic_attack_mod.setObjectName(u"proficient_dif_and_magic_attack_mod")
        self.proficient_dif_and_magic_attack_mod.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_7 = QHBoxLayout(self.proficient_dif_and_magic_attack_mod)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.proficient_dif_label = QLabel(self.proficient_dif_and_magic_attack_mod)
        self.proficient_dif_label.setObjectName(u"proficient_dif_label")
        self.proficient_dif_label.setFont(font1)
        self.proficient_dif_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_7.addWidget(self.proficient_dif_label)

        self.proficient_dif_textBrowser = QTextBrowser(self.proficient_dif_and_magic_attack_mod)
        self.proficient_dif_textBrowser.setObjectName(u"proficient_dif_textBrowser")
        self.proficient_dif_textBrowser.setEnabled(True)
        self.proficient_dif_textBrowser.setFont(font1)
        self.proficient_dif_textBrowser.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_7.addWidget(self.proficient_dif_textBrowser)

        self.magic_attack_mod_label = QLabel(self.proficient_dif_and_magic_attack_mod)
        self.magic_attack_mod_label.setObjectName(u"magic_attack_mod_label")
        self.magic_attack_mod_label.setFont(font1)
        self.magic_attack_mod_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_7.addWidget(self.magic_attack_mod_label)

        self.magic_attack_mod_textBrowser = QTextBrowser(self.proficient_dif_and_magic_attack_mod)
        self.magic_attack_mod_textBrowser.setObjectName(u"magic_attack_mod_textBrowser")
        self.magic_attack_mod_textBrowser.setEnabled(True)
        self.magic_attack_mod_textBrowser.setFont(font1)
        self.magic_attack_mod_textBrowser.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_7.addWidget(self.magic_attack_mod_textBrowser)


        self.verticalLayout.addWidget(self.proficient_dif_and_magic_attack_mod)

        self.description_for_har = QLabel(self.base_info)
        self.description_for_har.setObjectName(u"description_for_har")
        self.description_for_har.setFont(font1)
        self.description_for_har.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;\n"
"")

        self.verticalLayout.addWidget(self.description_for_har)

        self.strength = QGroupBox(self.base_info)
        self.strength.setObjectName(u"strength")
        self.strength.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_8 = QHBoxLayout(self.strength)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.strength_label = QLabel(self.strength)
        self.strength_label.setObjectName(u"strength_label")
        self.strength_label.setFont(font1)
        self.strength_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_8.addWidget(self.strength_label)

        self.strength_value_textBrowser = QTextBrowser(self.strength)
        self.strength_value_textBrowser.setObjectName(u"strength_value_textBrowser")
        self.strength_value_textBrowser.setEnabled(True)
        self.strength_value_textBrowser.setFont(font1)
        self.strength_value_textBrowser.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_8.addWidget(self.strength_value_textBrowser)

        self.strength_mod_textBrowser = QTextBrowser(self.strength)
        self.strength_mod_textBrowser.setObjectName(u"strength_mod_textBrowser")
        self.strength_mod_textBrowser.setEnabled(True)
        self.strength_mod_textBrowser.setFont(font1)
        self.strength_mod_textBrowser.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_8.addWidget(self.strength_mod_textBrowser)

        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.strength_radioButton = QRadioButton(self.strength)
        self.strength_radioButton.setObjectName(u"strength_radioButton")
        self.strength_radioButton.setEnabled(True)
        self.strength_radioButton.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_8.addWidget(self.strength_radioButton)


        self.verticalLayout.addWidget(self.strength)

        self.dexterity = QGroupBox(self.base_info)
        self.dexterity.setObjectName(u"dexterity")
        self.dexterity.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_9 = QHBoxLayout(self.dexterity)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.dexterity_label = QLabel(self.dexterity)
        self.dexterity_label.setObjectName(u"dexterity_label")
        self.dexterity_label.setFont(font1)
        self.dexterity_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_9.addWidget(self.dexterity_label)

        self.dexterity_value_textBrowser = QTextBrowser(self.dexterity)
        self.dexterity_value_textBrowser.setObjectName(u"dexterity_value_textBrowser")
        self.dexterity_value_textBrowser.setEnabled(True)
        self.dexterity_value_textBrowser.setFont(font1)
        self.dexterity_value_textBrowser.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_9.addWidget(self.dexterity_value_textBrowser)

        self.dexterity_mod_textBrowser = QTextBrowser(self.dexterity)
        self.dexterity_mod_textBrowser.setObjectName(u"dexterity_mod_textBrowser")
        self.dexterity_mod_textBrowser.setEnabled(True)
        self.dexterity_mod_textBrowser.setFont(font1)
        self.dexterity_mod_textBrowser.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_9.addWidget(self.dexterity_mod_textBrowser)

        self.horizontalSpacer_2 = QSpacerItem(200, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_2)

        self.dexterity_radioButton = QRadioButton(self.dexterity)
        self.dexterity_radioButton.setObjectName(u"dexterity_radioButton")
        self.dexterity_radioButton.setEnabled(True)
        self.dexterity_radioButton.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_9.addWidget(self.dexterity_radioButton)


        self.verticalLayout.addWidget(self.dexterity)

        self.constitution = QGroupBox(self.base_info)
        self.constitution.setObjectName(u"constitution")
        self.constitution.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_13 = QHBoxLayout(self.constitution)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.constitution_label = QLabel(self.constitution)
        self.constitution_label.setObjectName(u"constitution_label")
        self.constitution_label.setFont(font1)
        self.constitution_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_13.addWidget(self.constitution_label)

        self.constitution_value_textBrowser = QTextBrowser(self.constitution)
        self.constitution_value_textBrowser.setObjectName(u"constitution_value_textBrowser")
        self.constitution_value_textBrowser.setEnabled(True)
        self.constitution_value_textBrowser.setFont(font1)
        self.constitution_value_textBrowser.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_13.addWidget(self.constitution_value_textBrowser)

        self.constitution_mod_textBrowser = QTextBrowser(self.constitution)
        self.constitution_mod_textBrowser.setObjectName(u"constitution_mod_textBrowser")
        self.constitution_mod_textBrowser.setEnabled(True)
        self.constitution_mod_textBrowser.setFont(font1)
        self.constitution_mod_textBrowser.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_13.addWidget(self.constitution_mod_textBrowser)

        self.horizontalSpacer_3 = QSpacerItem(200, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_3)

        self.constitution_radioButton = QRadioButton(self.constitution)
        self.constitution_radioButton.setObjectName(u"constitution_radioButton")
        self.constitution_radioButton.setEnabled(True)
        self.constitution_radioButton.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_13.addWidget(self.constitution_radioButton)


        self.verticalLayout.addWidget(self.constitution)

        self.intelligence = QGroupBox(self.base_info)
        self.intelligence.setObjectName(u"intelligence")
        self.intelligence.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_12 = QHBoxLayout(self.intelligence)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.intelligence_label = QLabel(self.intelligence)
        self.intelligence_label.setObjectName(u"intelligence_label")
        self.intelligence_label.setFont(font1)
        self.intelligence_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_12.addWidget(self.intelligence_label)

        self.intelligence_value_textBrowser = QTextBrowser(self.intelligence)
        self.intelligence_value_textBrowser.setObjectName(u"intelligence_value_textBrowser")
        self.intelligence_value_textBrowser.setEnabled(True)
        self.intelligence_value_textBrowser.setFont(font1)
        self.intelligence_value_textBrowser.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_12.addWidget(self.intelligence_value_textBrowser)

        self.intelligence_mod_textBrowser = QTextBrowser(self.intelligence)
        self.intelligence_mod_textBrowser.setObjectName(u"intelligence_mod_textBrowser")
        self.intelligence_mod_textBrowser.setEnabled(True)
        self.intelligence_mod_textBrowser.setFont(font1)
        self.intelligence_mod_textBrowser.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_12.addWidget(self.intelligence_mod_textBrowser)

        self.horizontalSpacer_4 = QSpacerItem(200, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_4)

        self.intelligence_radioButton = QRadioButton(self.intelligence)
        self.intelligence_radioButton.setObjectName(u"intelligence_radioButton")
        self.intelligence_radioButton.setEnabled(True)
        self.intelligence_radioButton.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_12.addWidget(self.intelligence_radioButton)


        self.verticalLayout.addWidget(self.intelligence)

        self.wisdom = QGroupBox(self.base_info)
        self.wisdom.setObjectName(u"wisdom")
        self.wisdom.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_11 = QHBoxLayout(self.wisdom)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.wisdom_label = QLabel(self.wisdom)
        self.wisdom_label.setObjectName(u"wisdom_label")
        self.wisdom_label.setFont(font1)
        self.wisdom_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_11.addWidget(self.wisdom_label)

        self.wisdom_value_textBrowser = QTextBrowser(self.wisdom)
        self.wisdom_value_textBrowser.setObjectName(u"wisdom_value_textBrowser")
        self.wisdom_value_textBrowser.setEnabled(True)
        self.wisdom_value_textBrowser.setFont(font1)
        self.wisdom_value_textBrowser.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_11.addWidget(self.wisdom_value_textBrowser)

        self.wisdom_mod_textBrowser = QTextBrowser(self.wisdom)
        self.wisdom_mod_textBrowser.setObjectName(u"wisdom_mod_textBrowser")
        self.wisdom_mod_textBrowser.setEnabled(True)
        self.wisdom_mod_textBrowser.setFont(font1)
        self.wisdom_mod_textBrowser.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_11.addWidget(self.wisdom_mod_textBrowser)

        self.horizontalSpacer_5 = QSpacerItem(200, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_5)

        self.wisdom_radioButton = QRadioButton(self.wisdom)
        self.wisdom_radioButton.setObjectName(u"wisdom_radioButton")
        self.wisdom_radioButton.setEnabled(True)
        self.wisdom_radioButton.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_11.addWidget(self.wisdom_radioButton)


        self.verticalLayout.addWidget(self.wisdom)

        self.charisma = QGroupBox(self.base_info)
        self.charisma.setObjectName(u"charisma")
        self.charisma.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_10 = QHBoxLayout(self.charisma)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.charisma_label = QLabel(self.charisma)
        self.charisma_label.setObjectName(u"charisma_label")
        self.charisma_label.setFont(font1)
        self.charisma_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_10.addWidget(self.charisma_label)

        self.charisma_value_textBrowser = QTextBrowser(self.charisma)
        self.charisma_value_textBrowser.setObjectName(u"charisma_value_textBrowser")
        self.charisma_value_textBrowser.setEnabled(True)
        self.charisma_value_textBrowser.setFont(font1)
        self.charisma_value_textBrowser.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_10.addWidget(self.charisma_value_textBrowser)

        self.charisma_mod_textBrowser = QTextBrowser(self.charisma)
        self.charisma_mod_textBrowser.setObjectName(u"charisma_mod_textBrowser")
        self.charisma_mod_textBrowser.setEnabled(True)
        self.charisma_mod_textBrowser.setFont(font1)
        self.charisma_mod_textBrowser.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_10.addWidget(self.charisma_mod_textBrowser)

        self.horizontalSpacer_6 = QSpacerItem(200, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)

        self.charisma_radioButton = QRadioButton(self.charisma)
        self.charisma_radioButton.setObjectName(u"charisma_radioButton")
        self.charisma_radioButton.setEnabled(True)
        self.charisma_radioButton.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_10.addWidget(self.charisma_radioButton)


        self.verticalLayout.addWidget(self.charisma)

        self.skills = QGroupBox(self.centralwidget)
        self.skills.setObjectName(u"skills")
        self.skills.setGeometry(QRect(520, 50, 281, 861))
        self.skills.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.skills)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.athletics = QGroupBox(self.skills)
        self.athletics.setObjectName(u"athletics")
        self.athletics.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_14 = QHBoxLayout(self.athletics)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.athletics_label = QLabel(self.athletics)
        self.athletics_label.setObjectName(u"athletics_label")
        self.athletics_label.setFont(font1)
        self.athletics_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_14.addWidget(self.athletics_label)

        self.athletics_radioButton = QRadioButton(self.athletics)
        self.athletics_radioButton.setObjectName(u"athletics_radioButton")
        self.athletics_radioButton.setEnabled(True)
        self.athletics_radioButton.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_14.addWidget(self.athletics_radioButton)


        self.verticalLayout_3.addWidget(self.athletics)

        self.intimidation_strength = QGroupBox(self.skills)
        self.intimidation_strength.setObjectName(u"intimidation_strength")
        self.intimidation_strength.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_15 = QHBoxLayout(self.intimidation_strength)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.intimidation_strength_label = QLabel(self.intimidation_strength)
        self.intimidation_strength_label.setObjectName(u"intimidation_strength_label")
        self.intimidation_strength_label.setFont(font1)
        self.intimidation_strength_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_15.addWidget(self.intimidation_strength_label)

        self.intimidation_strength_radioButton = QRadioButton(self.intimidation_strength)
        self.intimidation_strength_radioButton.setObjectName(u"intimidation_strength_radioButton")
        self.intimidation_strength_radioButton.setEnabled(True)
        self.intimidation_strength_radioButton.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_15.addWidget(self.intimidation_strength_radioButton)


        self.verticalLayout_3.addWidget(self.intimidation_strength)

        self.acrobatics = QGroupBox(self.skills)
        self.acrobatics.setObjectName(u"acrobatics")
        self.acrobatics.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_16 = QHBoxLayout(self.acrobatics)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.acrobatics_label = QLabel(self.acrobatics)
        self.acrobatics_label.setObjectName(u"acrobatics_label")
        self.acrobatics_label.setFont(font1)
        self.acrobatics_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_16.addWidget(self.acrobatics_label)

        self.acrobatics_radioButton = QRadioButton(self.acrobatics)
        self.acrobatics_radioButton.setObjectName(u"acrobatics_radioButton")
        self.acrobatics_radioButton.setEnabled(True)
        self.acrobatics_radioButton.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_16.addWidget(self.acrobatics_radioButton)


        self.verticalLayout_3.addWidget(self.acrobatics)

        self.sleight_of_hand = QGroupBox(self.skills)
        self.sleight_of_hand.setObjectName(u"sleight_of_hand")
        self.sleight_of_hand.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_17 = QHBoxLayout(self.sleight_of_hand)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.sleight_of_hand_label = QLabel(self.sleight_of_hand)
        self.sleight_of_hand_label.setObjectName(u"sleight_of_hand_label")
        self.sleight_of_hand_label.setFont(font1)
        self.sleight_of_hand_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_17.addWidget(self.sleight_of_hand_label)

        self.sleight_of_hand_radioButton = QRadioButton(self.sleight_of_hand)
        self.sleight_of_hand_radioButton.setObjectName(u"sleight_of_hand_radioButton")
        self.sleight_of_hand_radioButton.setEnabled(True)
        self.sleight_of_hand_radioButton.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_17.addWidget(self.sleight_of_hand_radioButton)


        self.verticalLayout_3.addWidget(self.sleight_of_hand)

        self.stealth = QGroupBox(self.skills)
        self.stealth.setObjectName(u"stealth")
        self.stealth.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_34 = QHBoxLayout(self.stealth)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.stealth_label = QLabel(self.stealth)
        self.stealth_label.setObjectName(u"stealth_label")
        self.stealth_label.setFont(font1)
        self.stealth_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_34.addWidget(self.stealth_label)

        self.stealth_radioButton = QRadioButton(self.stealth)
        self.stealth_radioButton.setObjectName(u"stealth_radioButton")
        self.stealth_radioButton.setEnabled(True)
        self.stealth_radioButton.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_34.addWidget(self.stealth_radioButton)


        self.verticalLayout_3.addWidget(self.stealth)

        self.arcana = QGroupBox(self.skills)
        self.arcana.setObjectName(u"arcana")
        self.arcana.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_19 = QHBoxLayout(self.arcana)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.arcana_label = QLabel(self.arcana)
        self.arcana_label.setObjectName(u"arcana_label")
        self.arcana_label.setFont(font1)
        self.arcana_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_19.addWidget(self.arcana_label)

        self.arcana_radioButton = QRadioButton(self.arcana)
        self.arcana_radioButton.setObjectName(u"arcana_radioButton")
        self.arcana_radioButton.setEnabled(True)
        self.arcana_radioButton.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_19.addWidget(self.arcana_radioButton)


        self.verticalLayout_3.addWidget(self.arcana)

        self.history = QGroupBox(self.skills)
        self.history.setObjectName(u"history")
        self.history.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_20 = QHBoxLayout(self.history)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.history_label = QLabel(self.history)
        self.history_label.setObjectName(u"history_label")
        self.history_label.setFont(font1)
        self.history_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_20.addWidget(self.history_label)

        self.history_radioButton = QRadioButton(self.history)
        self.history_radioButton.setObjectName(u"history_radioButton")
        self.history_radioButton.setEnabled(True)
        self.history_radioButton.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_20.addWidget(self.history_radioButton)


        self.verticalLayout_3.addWidget(self.history)

        self.investigation = QGroupBox(self.skills)
        self.investigation.setObjectName(u"investigation")
        self.investigation.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_21 = QHBoxLayout(self.investigation)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.investigation_label = QLabel(self.investigation)
        self.investigation_label.setObjectName(u"investigation_label")
        self.investigation_label.setFont(font1)
        self.investigation_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_21.addWidget(self.investigation_label)

        self.investigation_radioButton = QRadioButton(self.investigation)
        self.investigation_radioButton.setObjectName(u"investigation_radioButton")
        self.investigation_radioButton.setEnabled(True)
        self.investigation_radioButton.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_21.addWidget(self.investigation_radioButton)


        self.verticalLayout_3.addWidget(self.investigation)

        self.nature = QGroupBox(self.skills)
        self.nature.setObjectName(u"nature")
        self.nature.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_22 = QHBoxLayout(self.nature)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.nature_label = QLabel(self.nature)
        self.nature_label.setObjectName(u"nature_label")
        self.nature_label.setFont(font1)
        self.nature_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_22.addWidget(self.nature_label)

        self.nature_radioButton = QRadioButton(self.nature)
        self.nature_radioButton.setObjectName(u"nature_radioButton")
        self.nature_radioButton.setEnabled(True)
        self.nature_radioButton.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_22.addWidget(self.nature_radioButton)


        self.verticalLayout_3.addWidget(self.nature)

        self.religion = QGroupBox(self.skills)
        self.religion.setObjectName(u"religion")
        self.religion.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_23 = QHBoxLayout(self.religion)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.religion_label = QLabel(self.religion)
        self.religion_label.setObjectName(u"religion_label")
        self.religion_label.setFont(font1)
        self.religion_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_23.addWidget(self.religion_label)

        self.religion_radioButton = QRadioButton(self.religion)
        self.religion_radioButton.setObjectName(u"religion_radioButton")
        self.religion_radioButton.setEnabled(True)
        self.religion_radioButton.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_23.addWidget(self.religion_radioButton)


        self.verticalLayout_3.addWidget(self.religion)

        self.animal_handling = QGroupBox(self.skills)
        self.animal_handling.setObjectName(u"animal_handling")
        self.animal_handling.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_24 = QHBoxLayout(self.animal_handling)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.animal_handling_label = QLabel(self.animal_handling)
        self.animal_handling_label.setObjectName(u"animal_handling_label")
        self.animal_handling_label.setFont(font1)
        self.animal_handling_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_24.addWidget(self.animal_handling_label)

        self.animal_handling_radioButton = QRadioButton(self.animal_handling)
        self.animal_handling_radioButton.setObjectName(u"animal_handling_radioButton")
        self.animal_handling_radioButton.setEnabled(True)
        self.animal_handling_radioButton.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_24.addWidget(self.animal_handling_radioButton)


        self.verticalLayout_3.addWidget(self.animal_handling)

        self.insight = QGroupBox(self.skills)
        self.insight.setObjectName(u"insight")
        self.insight.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_25 = QHBoxLayout(self.insight)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.insight_label = QLabel(self.insight)
        self.insight_label.setObjectName(u"insight_label")
        self.insight_label.setFont(font1)
        self.insight_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_25.addWidget(self.insight_label)

        self.insight_radioButton = QRadioButton(self.insight)
        self.insight_radioButton.setObjectName(u"insight_radioButton")
        self.insight_radioButton.setEnabled(True)
        self.insight_radioButton.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_25.addWidget(self.insight_radioButton)


        self.verticalLayout_3.addWidget(self.insight)

        self.medicine = QGroupBox(self.skills)
        self.medicine.setObjectName(u"medicine")
        self.medicine.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_26 = QHBoxLayout(self.medicine)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.medicine_label = QLabel(self.medicine)
        self.medicine_label.setObjectName(u"medicine_label")
        self.medicine_label.setFont(font1)
        self.medicine_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_26.addWidget(self.medicine_label)

        self.medicine_radioButton = QRadioButton(self.medicine)
        self.medicine_radioButton.setObjectName(u"medicine_radioButton")
        self.medicine_radioButton.setEnabled(True)
        self.medicine_radioButton.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_26.addWidget(self.medicine_radioButton)


        self.verticalLayout_3.addWidget(self.medicine)

        self.perception = QGroupBox(self.skills)
        self.perception.setObjectName(u"perception")
        self.perception.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_27 = QHBoxLayout(self.perception)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.perception_label = QLabel(self.perception)
        self.perception_label.setObjectName(u"perception_label")
        self.perception_label.setFont(font1)
        self.perception_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_27.addWidget(self.perception_label)

        self.perception_radioButton = QRadioButton(self.perception)
        self.perception_radioButton.setObjectName(u"perception_radioButton")
        self.perception_radioButton.setEnabled(True)
        self.perception_radioButton.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_27.addWidget(self.perception_radioButton)


        self.verticalLayout_3.addWidget(self.perception)

        self.survival = QGroupBox(self.skills)
        self.survival.setObjectName(u"survival")
        self.survival.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_28 = QHBoxLayout(self.survival)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.survival_label = QLabel(self.survival)
        self.survival_label.setObjectName(u"survival_label")
        self.survival_label.setFont(font1)
        self.survival_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_28.addWidget(self.survival_label)

        self.survival_radioButton = QRadioButton(self.survival)
        self.survival_radioButton.setObjectName(u"survival_radioButton")
        self.survival_radioButton.setEnabled(True)
        self.survival_radioButton.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_28.addWidget(self.survival_radioButton)


        self.verticalLayout_3.addWidget(self.survival)

        self.deception = QGroupBox(self.skills)
        self.deception.setObjectName(u"deception")
        self.deception.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_29 = QHBoxLayout(self.deception)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.deception_label = QLabel(self.deception)
        self.deception_label.setObjectName(u"deception_label")
        self.deception_label.setFont(font1)
        self.deception_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_29.addWidget(self.deception_label)

        self.deception_radioButton = QRadioButton(self.deception)
        self.deception_radioButton.setObjectName(u"deception_radioButton")
        self.deception_radioButton.setEnabled(True)
        self.deception_radioButton.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_29.addWidget(self.deception_radioButton)


        self.verticalLayout_3.addWidget(self.deception)

        self.intimidation_charisma = QGroupBox(self.skills)
        self.intimidation_charisma.setObjectName(u"intimidation_charisma")
        self.intimidation_charisma.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_30 = QHBoxLayout(self.intimidation_charisma)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.intimidation_charisma_label = QLabel(self.intimidation_charisma)
        self.intimidation_charisma_label.setObjectName(u"intimidation_charisma_label")
        self.intimidation_charisma_label.setFont(font1)
        self.intimidation_charisma_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_30.addWidget(self.intimidation_charisma_label)

        self.intimidation_charisma_radioButton = QRadioButton(self.intimidation_charisma)
        self.intimidation_charisma_radioButton.setObjectName(u"intimidation_charisma_radioButton")
        self.intimidation_charisma_radioButton.setEnabled(True)
        self.intimidation_charisma_radioButton.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_30.addWidget(self.intimidation_charisma_radioButton)


        self.verticalLayout_3.addWidget(self.intimidation_charisma)

        self.performance = QGroupBox(self.skills)
        self.performance.setObjectName(u"performance")
        self.performance.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_31 = QHBoxLayout(self.performance)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.performance_label = QLabel(self.performance)
        self.performance_label.setObjectName(u"performance_label")
        self.performance_label.setFont(font1)
        self.performance_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_31.addWidget(self.performance_label)

        self.performance_radioButton = QRadioButton(self.performance)
        self.performance_radioButton.setObjectName(u"performance_radioButton")
        self.performance_radioButton.setEnabled(True)
        self.performance_radioButton.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_31.addWidget(self.performance_radioButton)


        self.verticalLayout_3.addWidget(self.performance)

        self.persuasion = QGroupBox(self.skills)
        self.persuasion.setObjectName(u"persuasion")
        self.persuasion.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.horizontalLayout_32 = QHBoxLayout(self.persuasion)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.persuasion_label = QLabel(self.persuasion)
        self.persuasion_label.setObjectName(u"persuasion_label")
        self.persuasion_label.setFont(font1)
        self.persuasion_label.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_32.addWidget(self.persuasion_label)

        self.persuasion_radioButton = QRadioButton(self.persuasion)
        self.persuasion_radioButton.setObjectName(u"persuasion_radioButton")
        self.persuasion_radioButton.setEnabled(True)
        self.persuasion_radioButton.setStyleSheet(u"color: white;\n"
"background-color: none;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.horizontalLayout_32.addWidget(self.persuasion_radioButton)


        self.verticalLayout_3.addWidget(self.persuasion)

        self.inventory = QGroupBox(self.centralwidget)
        self.inventory.setObjectName(u"inventory")
        self.inventory.setGeometry(QRect(0, 710, 521, 201))
        self.inventory.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.inventory)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.inventory_text = QTextBrowser(self.inventory)
        self.inventory_text.setObjectName(u"inventory_text")
        self.inventory_text.setEnabled(True)
        self.inventory_text.setFont(font1)
        self.inventory_text.setStyleSheet(u"color: white;\n"
"border: none;\n"
"font-weigth: bold;\n"
"font-size: 12pt;")

        self.verticalLayout_4.addWidget(self.inventory_text)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Degenerator", None))
        self.name_enter_label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f \u043f\u0435\u0440\u0441\u043e\u043d\u0430\u0436\u0430:", None))
        self.generate_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0434\u0435\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.save_as_txt_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0442\u0435\u043a\u0441\u0442", None))
        self.save_as_png_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0441\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u043f\u043d\u0433", None))
        self.name_label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043c\u044f:", None))
        self.name_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Comic Sans MS'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.level_label.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0440\u043e\u0432\u0435\u043d\u044c:", None))
        self.race_label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0441\u0430:", None))
        self.race_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Comic Sans MS'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.class_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0430\u0441\u0441:", None))
        self.background_lable.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0435\u0434\u044b\u0441\u0442\u043e\u0440\u0438\u044f:", None))
        self.background_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Comic Sans MS'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.alignment_label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u0440\u043e\u0432\u043e\u0437\u0437\u0440\u0435\u043d\u0438\u0435:", None))
        self.alignment_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Comic Sans MS'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.hit_dice_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u0441\u0442\u044c \u0445\u0438\u0442\u043e\u0432:", None))
        self.hit_dice_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Comic Sans MS'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.hits_label.setText(QCoreApplication.translate("MainWindow", u"\u0425\u0438\u0442\u044b:", None))
        self.proficiency_bonus_label.setText(QCoreApplication.translate("MainWindow", u"\u0411\u043e\u043d\u0443\u0441 \u043c\u0430\u0441\u0442\u0435\u0440\u0441\u0442\u0430:", None))
        self.proficiency_bonus_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Comic Sans MS'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.size_label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0437\u043c\u0435\u0440:", None))
        self.speed_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c:", None))
        self.speed_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Comic Sans MS'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.base_spell_mod_label.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0437\u043e\u0432\u0430\u044f \u0445-\u043a\u0430 \u0437\u0430\u043a\u043b\u0438\u043d\u0430\u043d\u0438\u0439:", None))
        self.proficient_dif_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043b. \u0421\u043f\u0430\u0441\u0431\u0440\u043e\u0441\u043a\u0430:", None))
        self.proficient_dif_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Comic Sans MS'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.magic_attack_mod_label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0433. \u0411\u043e\u043d. \u0410\u0442\u0430\u043a\u0438:", None))
        self.description_for_har.setText(QCoreApplication.translate("MainWindow", u"\u0425\u0430\u0440\u0430\u043a\u0442\u0435\u0440\u0438\u0441\u0442\u0438\u043a\u0438:        \u0437\u043d\u0430\u0447\u0438\u043d\u0435        \u043c\u043e\u0434\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440     \u0441\u043f\u0430\u0441\u0431\u043e\u0440\u043e\u0441\u043e\u043a", None))
        self.strength_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043b\u0430:                ", None))
        self.strength_value_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Comic Sans MS'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.strength_radioButton.setText("")
        self.dexterity_label.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0432\u043a\u043e\u0441\u0442\u044c:         ", None))
        self.dexterity_value_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Comic Sans MS'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.dexterity_radioButton.setText("")
        self.constitution_label.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u043b\u043e\u0441\u043b\u043e\u0436\u0435\u043d\u0438\u0435:", None))
        self.constitution_value_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Comic Sans MS'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.constitution_radioButton.setText("")
        self.intelligence_label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0442\u0435\u043b\u043b\u0435\u043a\u0442:        ", None))
        self.intelligence_value_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Comic Sans MS'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.intelligence_radioButton.setText("")
        self.wisdom_label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0443\u0434\u0440\u043e\u0441\u0442\u044c:       ", None))
        self.wisdom_value_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Comic Sans MS'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.wisdom_radioButton.setText("")
        self.charisma_label.setText(QCoreApplication.translate("MainWindow", u"\u0425\u0430\u0440\u0438\u0437\u043c\u0430:         ", None))
        self.charisma_value_textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Comic Sans MS'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.charisma_radioButton.setText("")
        self.athletics_label.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0442\u043b\u0435\u043a\u0442\u0438\u043a\u0430:                                                            ", None))
        self.athletics_radioButton.setText("")
        self.intimidation_strength_label.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0433\u0438\u0432\u0430\u043d\u0438\u0435 \u0441\u0438\u043b\u043e\u0439:                                      ", None))
        self.intimidation_strength_radioButton.setText("")
        self.acrobatics_label.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0440\u043e\u0431\u0430\u0442\u0438\u043a\u0430:                                         ", None))
        self.acrobatics_radioButton.setText("")
        self.sleight_of_hand_label.setText(QCoreApplication.translate("MainWindow", u"\u041b\u043e\u0432\u043a\u043e\u0441\u0442\u044c \u0440\u0443\u043a:                                             ", None))
        self.sleight_of_hand_radioButton.setText("")
        self.stealth_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043a\u0440\u044b\u0442\u043d\u043e\u0441\u0442\u044c:                                       ", None))
        self.stealth_radioButton.setText("")
        self.arcana_label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u0433\u0438\u044f:                                           ", None))
        self.arcana_radioButton.setText("")
        self.history_label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0442\u043e\u0440\u0438\u044f:                                       ", None))
        self.history_radioButton.setText("")
        self.investigation_label.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043d\u0430\u043b\u0438\u0437:                                      ", None))
        self.investigation_radioButton.setText("")
        self.nature_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0440\u043e\u0434\u0430:                                      ", None))
        self.nature_radioButton.setText("")
        self.religion_label.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0435\u043b\u0438\u0433\u0438\u044f:                                  ", None))
        self.religion_radioButton.setText("")
        self.animal_handling_label.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0445\u043e\u0434 \u0437\u0430 \u0416\u0438\u0432\u043e\u0442\u043d\u044b\u043c\u0438:                                                        ", None))
        self.animal_handling_radioButton.setText("")
        self.insight_label.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u043d\u0438\u0446\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c:                            ", None))
        self.insight_radioButton.setText("")
        self.medicine_label.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0435\u0434\u0438\u0446\u0438\u043d\u0430:                                ", None))
        self.medicine_radioButton.setText("")
        self.perception_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0438\u043c\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c:                            ", None))
        self.perception_radioButton.setText("")
        self.survival_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0436\u0438\u0432\u0430\u043d\u0438\u0435:                              ", None))
        self.survival_radioButton.setText("")
        self.deception_label.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043c\u0430\u043d:                                                             ", None))
        self.deception_radioButton.setText("")
        self.intimidation_charisma_label.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043f\u0443\u0433\u0438\u0432\u0430\u043d\u0438\u0435:                                  ", None))
        self.intimidation_charisma_radioButton.setText("")
        self.performance_label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0441\u0442\u0443\u043f\u043b\u0435\u043d\u0438\u0435:                                 ", None))
        self.performance_radioButton.setText("")
        self.persuasion_label.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0431\u0435\u0436\u0434\u0435\u043d\u0438\u0435:                                    ", None))
        self.persuasion_radioButton.setText("")
        self.inventory_text.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Comic Sans MS'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi


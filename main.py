from random import shuffle
from sys import argv, exit

from PySide6.QtWidgets import QApplication, QMainWindow

from character_class import charecter
from Image_creator import generate_char_list, translate_to_ru
from degenerator_ui import Ui_MainWindow


class interface(QMainWindow):
    def __init__(self):
        super(interface, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(803, 910)

        self.generate()
        self.ui.generate_pushButton.clicked.connect(self.generate)
        self.ui.save_as_txt_pushButton.clicked.connect(self.save_as_txt)
        self.ui.save_as_png_pushButton.clicked.connect(self.save_as_png)
    def generate(self):
        self.char = charecter(self.ui.name_lineEdit.text())

        self.ui.name_textBrowser.setText(self.char.name)
        self.ui.level_textBrowser.setText(str(self.char.level))
        self.ui.race_textBrowser.setText(self.char.race)
        self.ui.class_textBrowser.setText(self.char.clas)
        self.ui.background_textBrowser.setText(self.char.background)
        self.ui.alignment_textBrowser.setText(self.char.alignment)
        self.ui.hit_dice_textBrowser.setText(str(self.char.hit_dice))
        self.ui.hits_textBrowser.setText(str(self.char.hits))
        self.ui.proficiency_bonus_textBrowser.setText(str(self.char.proficiency_bonus))
        self.ui.size_textBrowser.setText(str(self.char.size))
        self.ui.speed_textBrowser.setText(str(self.char.speed))
        self.ui.base_spell_mod_textBrowser.setText(translate_to_ru(self.char.base_spell_mod))
        self.ui.proficient_dif_textBrowser.setText(str(self.char.proficient_dif))
        self.ui.magic_attack_mod_textBrowser.setText(str(self.char.magic_attack_mod))

        self.ui.strength_value_textBrowser.setText(str(self.char.har['strength']['value']))
        self.ui.strength_mod_textBrowser.setText(str(self.char.har['strength']['mod']))
        self.ui.strength_radioButton.setChecked(self.char.har['strength']['proficient'])

        self.ui.dexterity_value_textBrowser.setText(str(self.char.har['dexterity']['value']))
        self.ui.dexterity_mod_textBrowser.setText(str(self.char.har['dexterity']['mod']))
        self.ui.dexterity_radioButton.setChecked(self.char.har['dexterity']['proficient'])

        self.ui.constitution_value_textBrowser.setText(str(self.char.har['constitution']['value']))
        self.ui.constitution_mod_textBrowser.setText(str(self.char.har['constitution']['mod']))
        self.ui.constitution_radioButton.setChecked(self.char.har['constitution']['proficient'])

        self.ui.intelligence_value_textBrowser.setText(str(self.char.har['intelligence']['value']))
        self.ui.intelligence_mod_textBrowser.setText(str(self.char.har['intelligence']['mod']))
        self.ui.intelligence_radioButton.setChecked(self.char.har['intelligence']['proficient'])

        self.ui.wisdom_value_textBrowser.setText(str(self.char.har['wisdom']['value']))
        self.ui.wisdom_mod_textBrowser.setText(str(self.char.har['wisdom']['mod']))
        self.ui.wisdom_radioButton.setChecked(self.char.har['wisdom']['proficient'])

        self.ui.charisma_value_textBrowser.setText(str(self.char.har['charisma']['value']))
        self.ui.charisma_mod_textBrowser.setText(str(self.char.har['charisma']['mod']))
        self.ui.charisma_radioButton.setChecked(self.char.har['charisma']['proficient'])

        self.ui.athletics_radioButton.setChecked(self.char.har['strength']['skills']['athletics'])
        self.ui.intimidation_strength_radioButton.setChecked(self.char.har['strength']['skills']['intimidation_strength'])
        self.ui.acrobatics_radioButton.setChecked(self.char.har['dexterity']['skills']['acrobatics'])
        self.ui.sleight_of_hand_radioButton.setChecked(self.char.har['dexterity']['skills']['sleight_of_hand'])
        self.ui.stealth_radioButton.setChecked(self.char.har['dexterity']['skills']['stealth'])
        self.ui.arcana_radioButton.setChecked(self.char.har['intelligence']['skills']['arcana'])
        self.ui.history_radioButton.setChecked(self.char.har['intelligence']['skills']['history'])
        self.ui.investigation_radioButton.setChecked(self.char.har['intelligence']['skills']['investigation'])
        self.ui.nature_radioButton.setChecked(self.char.har['intelligence']['skills']['nature'])
        self.ui.religion_radioButton.setChecked(self.char.har['intelligence']['skills']['religion'])
        self.ui.animal_handling_radioButton.setChecked(self.char.har['wisdom']['skills']['animal_handling'])
        self.ui.insight_radioButton.setChecked(self.char.har['wisdom']['skills']['insight'])
        self.ui.medicine_radioButton.setChecked(self.char.har['wisdom']['skills']['medicine'])
        self.ui.perception_radioButton.setChecked(self.char.har['wisdom']['skills']['perception'])
        self.ui.survival_radioButton.setChecked(self.char.har['wisdom']['skills']['survival'])
        self.ui.deception_radioButton.setChecked(self.char.har['charisma']['skills']['deception'])
        self.ui.intimidation_charisma_radioButton.setChecked(self.char.har['charisma']['skills']['intimidation_charisma'])
        self.ui.performance_radioButton.setChecked(self.char.har['charisma']['skills']['performance'])
        self.ui.persuasion_radioButton.setChecked(self.char.har['charisma']['skills']['persuasion'])

        self.ui.inventory_text.setText(f'Языки: {', '.join(self.char.lagnuages)}\n\n'
                                       f'Экипировка: {', '.join(self.char.equipment)}\n\n'
                                       f'Владение:\n'
                                       f'  -Оружие: {', '.join(self.char.using['оружие'])}\n'
                                       f'  -Доспехи: {', '.join(self.char.using['доспехи'])}\n'
                                       f'  -Инструменты: {', '.join(self.char.using['инструменты'])}\n\n'
                                       f'Черта характера: {self.char.personality_trait}\n\n'
                                       f'Идеал: {self.char.ideal}\n\n'
                                       f'Привязанность: {self.char.bond}\n\n'
                                       f'Слабость: {self.char.flaw}')

    def save_as_txt(self):
        text = (f"Имя: {self.char.name} Уровень: {self.char.level}\n\n"
                f"Бонус мастерства: {self.char.proficiency_bonus}\n\n"
                f"Расса: {self.char.race} Класса: {self.char.clas}\n\n"
                f"Предыстория: {self.char.background}\n"
                f"  -Черта характера: {self.char.personality_trait}\n"
                f"  -Идеал: {self.char.ideal}\n"
                f"  -Привязанность: {self.char.bond}\n"
                f"  -Слабость: {self.char.flaw}\n\n"
                f"Характеристики:\n"
                f"     -Сила: {self.char.har['strength']}\n"
                f"     -Ловскость: {self.char.har['dexterity']}\n"
                f"     -Телосложение: {self.char.har['constitution']}\n"
                f"     -Интеллект: {self.char.har['intelligence']}\n"
                f"     -Мудрость: {self.char.har['wisdom']}\n"
                f"     -Харизма: {self.char.har['charisma']}\n\n"
                f"Базовая харктеристика заклинаний: {self.char.base_spell_mod}\n"
                f"Сл Спасброска: {self.char.proficient_dif}  Маг. Бон. Атаки: {self.char.magic_attack_mod}\n\n"
                f"Языки: {self.char.lagnuages}\n\n"
                f"Снаряжение: {self.char.equipment}\n\n"
                f"Владение: {self.char.using}")
        file_name = list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        shuffle(file_name)
        file = open('./chars/texts/'+''.join(file_name) + '.txt', 'x', encoding='utf8')
        file.write(text)
        file.close()

    def save_as_png(self):
        file_name = list('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
        shuffle(file_name)

        generate_char_list(self.char, ''.join(file_name))



if __name__ == "__main__":
    app = QApplication(argv)
    window = interface()
    window.show()

    exit(app.exec())
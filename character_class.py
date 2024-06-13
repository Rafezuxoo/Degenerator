from json import load
from os import listdir
from random import randint, shuffle, choice


class charecter:
    def __init__(self, name='', level=1):
        # открываем файлы json
        try:
            with open('./races/' + choice(listdir('races')), encoding='utf8') as file:
                self.race_file = load(file)
        except:
            self.race_file = {
        'race_name': '<NOT_FOUND>',
        'names': {
            'm': ['<NOT_FOUND>', '<NOT_FOUND>'],
            'f': ['<NOT_FOUND>', '<NOT_FOUND>']
        },
        'surnames': ['<NOT_FOUND>', '<NOT_FOUND>'],
        "nicks": ["<NOT_FOUND>", "<NOT_FOUND>"],
        'har': {
            "strength": 0,
            "dexterity": 0,
            "constitution": 0,
            "intelligence": 0,
            "wisdom": 0,
            "charisma": 0
        },
        'size': '<NOT_FOUND>',
        'speed': '<NOT_FOUND>',
        'languages': ['<NOT_FOUND>', '<NOT_FOUND>'],
        'features': {
            '<NOT_FOUND>': '<NOT_FOUND>',
            '<NOT_FOUND>1': '<NOT_FOUND>'
        }
    }

        try:
            with open('./classes/' + choice(listdir('classes')), encoding='utf8') as file:
                self.class_file = load(file)
        except:
            self.class_file = {
        "class_name": "<NOT_FOUND>",
        'hit_dice': 0,
        'proficient': ['', ''],
        'skills': ['', ''],
        'using': {
            '<NOT_FOUND>': ['<NOT_FOUND>']
        },
        'equipment': [
            '<NOT_FOUND>'
        ],
        'base_spell_mod': '',
        'abilities': {
            '1': {
                '<NOT_FOUND>': '<NOT_FOUND>'
            }
        }
    }

        try:
            with open('./backgrounds/' + choice(listdir('backgrounds')), encoding='utf8') as file:
                self.background_file = load(file)
        except:
            self.background_file = {
        "background_name": "<NOT_FOUND>",
        "ability": {
            "<NOT_FOUND>": "<NOT_FOUND>"
        },
        "skills": [
            "<NOT_FOUND>"
        ],
        "using": {
            "<NOT_FOUND>": [
                "<NOT_FOUND>"
            ]
        },
        "equipment": [
            "<NOT_FOUND>",
            "<NOT_FOUND>"
        ],
        "personality_trait": [
            "<NOT_FOUND>",
            "<NOT_FOUND>"
        ],
        "ideal": [
            "<NOT_FOUND>(любой)",
            "<NOT_FOUND>(любой)"
        ],
        "bond": [
            "<NOT_FOUND>",
            "<NOT_FOUND>"
        ],
        "flaw": [
            "<NOT_FOUND>",
            "<NOT_FOUND>"
        ],
        "do_roll": False,
        "roll": {
            "roll_name": "<NOT_FOUND>",
            "roll_vars": [
                "<NOT_FOUND>"
            ]
        }
    }

        try:
            with open('languages.json', encoding='utf8') as file:
                self.lagnuage_file = load(file)
        except:
            self.lagnuage_file = ['общий', 'драконий', 'дварфийский', 'инфернальный',
                                  'гномий', 'эльфийсий', 'полуросликов', "орочий"]

        # присваеваем занчения используя файлы
        self.race = self.race_file['race_name']
        self.clas = self.class_file['class_name']
        self.equipment = [choice(i) if type(i) == type(['1']) else i for i in self.class_file['equipment']] + \
                         self.background_file['equipment']
        self.level = level
        self.har = {
        'strength': {
            'value': 0,
            'mod': 0,
            'proficient': False,
            'skills': {
                'athletics': False,
                'intimidation_strength': False
            }
        },
        'dexterity': {
            'value': 0,
            'mod': 0,
            'proficient': False,
            'skills': {
                'acrobatics': False,
                'sleight_of_hand': False,
                'stealth': False
            }
        },
        'constitution': {
            'value': 0,
            'mod': 0,
            'proficient': False,
            'skills': {'': ''}
        },
        'intelligence': {
            'value': 0,
            'mod': 0,
            'proficient': False,
            'skills': {
                'arcana': False,
                'history': False,
                'investigation': False,  # анализ \ расследование
                'nature': False,
                'religion': False
            }
        },
        'wisdom': {
            'value': 0,
            'mod': 0,
            'proficient': False,
            'skills': {
                'animal_handling': False,
                'insight': False,  # проницательность
                'medicine': False,
                'perception': False,  # вопсприятие
                'survival': False
            }
        },
        'charisma': {
            'value': 0,
            'mod': 0,
            'proficient': False,
            'skills': {
                'deception': False,  # обман
                'intimidation_charisma': False,
                'performance': False,
                'persuasion': False  # убеждение
            }
        }
    }
        self.size = self.race_file['size']
        self.speed = self.race_file['speed']

        # из предыстории
        self.background = self.background_file['background_name']
        self.personality_trait = choice(self.background_file['personality_trait'])
        self.ideal = choice(self.background_file['ideal'])
        self.bond = choice(self.background_file['bond'])
        self.flaw = choice(self.background_file['flaw'])
        if self.background_file['do_roll']:
            self.spec_roll = {
                self.background_file['roll']['roll_name']: choice(self.background_file['roll']['roll_vars'])
            }
        else:
            self.spec_roll = {
                "": ""
            }

        self.using = dict()
        self.using.update(self.class_file['using'])
        self.using.update(self.background_file['using'])
        for i in self.using.keys():
            self.using[i] = set(self.using[i])

        self.abilities = []
        self.abilities += self.race_file["features"]
        self.abilities += self.background_file["ability"].keys()
        for i in range(self.level):
            try:
                self.abilities += self.class_file["abilities"][str(i + 1)]
            except:
                pass


        self.gender = choice(['m', 'f'])


        self.name = name
        if self.name == '':
            self.name = (choice(self.race_file['names'][self.gender]) + ' '
                         + choice(self.race_file['surnames']) + " "
                         + choice(self.race_file['nicks']))
        alignments = ["Законный Добрый", "Нейтральный Добрый", "Хаотичный Добрый",
                      "Законный Нейтральный", "Абсолютно Нейтральный", "Хаотичный Нейтральный",
                      "Законный Злой", "Нейтральный Злой", "Хаотичный Злой"]
        while True:
            self.alignment = choice(alignments)
            # print(self.background, self.ideal)
            try:
                if (self.ideal[self.ideal.index('(') + 1:self.ideal.index(')')] in self.alignment
                or self.ideal[self.ideal.index('(') + 1:self.ideal.index(')')] == 'Любой'
                or self.ideal[self.ideal.index('(') + 1:self.ideal.index(')')] == 'Любое'):
                    break
                else:
                    alignments.remove(self.alignment)
            except:
                break

        if 'random' not in self.race_file['languages']:
            self.lagnuages = self.race_file['languages']
        else:
            for i in self.race_file['languages']:
                try:
                    self.lagnuage_file.remove(i)
                except:
                    pass
            self.lagnuages = self.race_file['languages']
            self.lagnuages[self.lagnuages.index('random')] = choice(self.lagnuage_file)

        self.proficiency_bonus = 2
        if self.level / 4 > round(self.level / 4, 0):
            self.proficiency_bonus += level // 4
        else:
            self.proficiency_bonus += int(round(level / 4, 0) - 1)

        # self.money = {
        #     'copper' : 0,
        #     'silver' : 0,
        #     'electrum' : 0,
        #     'gold' : 0,
        #     'platinum' : 0
        # }

        skills = self.class_file['skills']
        for i in self.background_file['skills']:
            try:
                skills.remove(i)
            except:
                pass
        shuffle(skills)
        if self.class_file['class_name'] == 'Бард':
            skills = skills[:3] + self.background_file['skills']
        else:
            skills = skills[:2] + self.background_file['skills']
        if 'intimidation' in skills:
            skills[skills.index('intimidation')] = choice(['intimidation_strength', 'intimidation_charisma'])

        # присвоение статов
        for i in self.har.keys():
            dice_try = []
            for _ in range(4):
                dice_try.append(randint(1, 6))
            dice_try.remove(min(dice_try))
            self.har[i]['value'] = sum(dice_try) + self.race_file['har'][i]
            self.har[i]['mod'] = (self.har[i]['value'] - 10) // 2
            if i in self.class_file["proficient"]:
                self.har[i]['proficient'] = True
            for j in self.har[i]['skills'].keys():
                if j in skills:
                    skills.remove(j)
                    self.har[i]['skills'][j] = True

        # расчёт характеристик связанных с заклинаниями
        self.base_spell_mod = self.class_file['base_spell_mod']
        if self.class_file['base_spell_mod'] != '':
            self.proficient_dif = int(self.har[self.base_spell_mod]['mod']) + 8 + int(self.proficiency_bonus)
            self.magic_attack_mod = int(self.har[self.base_spell_mod]['mod']) + int(self.proficiency_bonus)
        else:
            self.proficient_dif = 0
            self.magic_attack_mod = 0

        self.hit_dice = self.class_file['hit_dice']
        self.hits = self.hit_dice + self.har['constitution']['mod']

    def get_stats(self):
        print(
            f'Имя: {self.name}\n'
            f'Уровень: {self.level}\n'
            f'Расса: {self.race}\n'
            f'Класс: {self.clas}\n'
            f'Предыстория: {self.background}\n'
            f'Размер: {self.size}\n'
            f'Скорость: {self.speed}\n'
            f'Кость хитов: {self.hit_dice} Хиты: {self.hits}\n'
            f'Бонус мастерства: {self.proficiency_bonus}\n'
            f'Характеристики:\n'
            f'Сила: {self.har['strength']['value']} ({self.har['strength']['mod']}) Ловскость: '
            f'{self.har['dexterity']['value']} ({self.har['dexterity']['mod']})\n'
            f'Телосложение: {self.har['constitution']['value']} ({self.har['constitution']['mod']}) Интеллект: '
            f'{self.har['intelligence']['value']} ({self.har['intelligence']['mod']})\n'
            f'Мудрость: {self.har['wisdom']['value']} ({self.har['wisdom']['mod']}) Харизма: '
            f'{self.har['charisma']['value']} ({self.har['charisma']['mod']})\n'
            f'Языки: {self.lagnuages}\n'
            f'Мировозрение: {self.alignment}\n'
            f'Экипировка: {self.equipment}\n'
            f'Умения: {self.abilities}\n'
            f'Базовая характеристика заклинаний: {self.base_spell_mod} Магический бонус атаки: {self.magic_attack_mod} '
            f'Сложность спасброска: {self.proficient_dif}\n'
            f'{self.using}\n'
            f'---'
        )


if __name__ == '__main__':
    own_char = charecter()
    own_char.get_stats()
    print(own_char.har)

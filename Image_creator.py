import sys
from PIL import Image, ImageDraw, ImageFont
from character_class import charecter

def plus_or_mice(n: int) -> str:
    if n <= 0:
        return str(n)
    return '+'+str(n)

def make_proficients(b:bool, index: int, draw: ImageDraw):
    if b and index!=4 and index!=3:
        draw.polygon([146, 325+index*100, 140, 331+index*100, 146, 336+index*100, 152, 331+index*100], (0, 0, 0))
    elif b and index==3:
        draw.polygon([146, 622, 140, 628, 146, 633, 152, 628], (0, 0, 0))
    elif b and index == 4:
        draw.polygon([146, 721, 140, 727, 146, 732, 152, 727], (0, 0, 0))
def make_skills(b:bool, index: int, index1: int, draw: ImageDraw):
    if b and index!=3 and index!=4:
        draw.ellipse([141, 345 + index * 100 + index1*15, 151, 355 + index * 100 + index1 * 15], (0, 0, 0))
    elif b and index == 3:
        draw.ellipse([141, 641 + index1*14, 151, 651+index1*14], (0, 0, 0))
    elif b and index == 4:
        draw.ellipse([141, 740 + index1*14, 151, 750 + index1*14], (0, 0, 0))

def translate_to_ru(word: str)->str:
    word = word.replace('wisdom', "мудрость")
    word = word.replace('charisma', 'харизма')
    word = word.replace('intelligence', "интеллект")
    return word

def generate_char_list(char: charecter, name : str = 'char1', path: str = './chars/pngs/'):
    with Image.open("char_list_pattern.png") as img:
        font = ImageFont.truetype('arial.ttf', 16)
        black = (0, 0, 0)

        draw = ImageDraw.Draw(img)
        #верхняя часть
        draw.text((38, 90), char.name, black, font=ImageFont.truetype("arial.ttf", 18))
        draw.text((300, 60), f'{char.clas} {char.level}', black, font = font)
        draw.text((440, 60), char.background, black, font = font)
        draw.text((300, 100), char.race, black, font=font)
        draw.text((420, 100), char.alignment, black, font=font)

        #над статами
        draw.text((55, 190), '+' + str(char.proficiency_bonus), black, font=font)

        #статы
        for index, value in enumerate(char.har.keys()):
            draw.text((70, 325+index*100), str(char.har[value]['value']), black, font=font)
            draw.text((70, 360+index*100), plus_or_mice(char.har[value]['mod']), black, font = font)
            make_proficients(char.har[value]['proficient'], index, draw)
            for index1, value1 in enumerate(char.har[value]['skills'].keys()):
                make_skills(char.har[value]['skills'][value1], index, index1, draw)


        #хиты и скорость
        draw.text((620, 200), str(char.speed), black, font=font)
        draw.text((600, 300), '1к'+str(char.hit_dice), black, font=font)
        draw.text((375, 300), str(char.hits), black, font=font)
        draw.text((475, 300), str(char.hits), black, font=font)

        #по заклинаниям
        draw.text((440, 765), translate_to_ru(char.base_spell_mod), black, font=font)
        if char.base_spell_mod != '':
            draw.text((475, 820), str(char.proficient_dif), black, font=font)
            draw.text((475, 875), str(char.magic_attack_mod), black, font=font)

        #прочее
        if len(', '.join(char.equipment)) < 47:
            draw.text((40, 950), f'Языки: {', '.join(char.lagnuages)};\nЭкипировка: {', '.join(char.equipment)}', black, font=font)
        else:
            string_equipment = list(', '.join(char.equipment))
            string_equipment.insert(47, '\n')
            for i in range(2, len(string_equipment)//47+1):
                string_equipment.insert(i*55, '\n')
            draw.text((40, 950), f'Языки: {", ".join(char.lagnuages)};\nЭкипировка: {"".join(string_equipment)}', black, font=font)

        img.save(path+name+'.png')
        img.show()

if __name__ == "__main__":
    char = charecter()
    generate_char_list(char)

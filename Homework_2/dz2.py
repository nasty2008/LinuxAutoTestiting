# Задание №1:
# Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования с путями (x).
# Установить пакет для расчёта crc32
# sudo apt install libarchive-zip-perl
# Доработать проект, добавив тест команды расчёта хеша (h).
# Проверить, что хеш совпадает с рассчитанным командой crc32.

import dz1
import crc32

folder_in = '/home/user/tst'
folder_out = '/home/user/out'


def test_1_find_text_in_command():
    # семинар
    assert dz1.find_text_in_command(f'cd {folder_in}; 7z a {folder_out}/arh1','Everything is Ok'), 'test1 FAIL'


def test_2_find_text_in_command():
    #  проверяющими команды вывода списка файлов (l) и разархивирования с путями (x).
    assert dz1.find_text_in_command(f'ls {folder_out}','arh1.7z'), 'test2 FAIL'


def test_3_find_text_in_command():
    #  тест команды расчёта хеша (h). Проверить, что хеш совпадает с рассчитанным командой crc32.
    temp = crc32.crc32(f'{folder_out}/arh1.7z').lower()
    assert dz1.find_text_in_command(f'crc32 {folder_out}/arh1.7z',temp), 'test3 FAIL'

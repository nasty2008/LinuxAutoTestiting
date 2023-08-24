import subprocess


def checkout(cmd, text):
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    print(result.stdout)

    if text in result.stdout and result.returncode == 0:
        return True
    else:
        return False


folder_in = '/home/user/tst'
folder_out = '/home/user/out'
print(checkout('cd /home/user/tst; 7z a /home/user/arh1', 'Everything is Ok'))


def test_step1():
    assert checkout(f'cd {folder_in}; 7z a {folder_out}/arh1', 'Everything is Ok'), 'test1 FAIL'


def test_step2():
    assert checkout(f'cd {folder_in}; 7z u {folder_out}/arh1', 'Everything is Ok'), 'test2 FAIL'


def test_step3():
    assert checkout(f'cd {folder_in}; 7z d {folder_out}/arh1', 'Everything is Ok'), 'test3 FAIL'

# Добавить в проект тесты, проверяющие работу команд
# d (удаление из архива) и u (обновление архива). Вынести
# в отдельные переменные пути к папкам с файлами, с архивом
# и с распакованными файлами. Выполнить тесты с ключом -v.
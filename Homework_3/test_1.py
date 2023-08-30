from task import find_text_in_command
import crc
import yaml

with open('config.yaml') as file:
    data = yaml.safe_load(file)

class Test_Positive:
    def test_1_find_text_in_command(self, make_folders, make_files, print_time):
        assert find_text_in_command(f'cd {data["folderin"]}; '
                                    f''f'7z a -t{data["typearch"]} '
                                    f'{data["folderout"]}/{data["filename"]}',
                                    'Everything is Ok'), 'Test1 FAIL'

    def test_2_find_text_in_command(self, print_time):
        assert find_text_in_command(f'ls {data["folderout"]}',
                                    f'{data["filename"]}'), 'Test2 FAIL'

    def test_3_find_text_in_command(self, clear_folders, print_time):
        assert find_text_in_command(f'crc32 {data["folderout"]}/*',
                                    crc.crc32(f'{data["folderout"]}/{data["filename"]}.{data["typearch"]}').lower()), \
            'Test3 FAIL'
import pytest
from task import find_text_in_command, getout
import yaml
import random
import string
from datetime import datetime

with open('config.yaml') as file:
    data = yaml.safe_load(file)

@pytest.fixture()
def make_folders():
    return find_text_in_command(f'mkdir {data["folderin"]} {data["folderout"]}', "")

@pytest.fixture()
def clear_folders():
    yield
    find_text_in_command(f'rm -rf {data["folderin"]} {data["folderout"]}', "")

@pytest.fixture()
def make_files():
    for i in range(data["count"]):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        find_text_in_command("cd {}; dd if=/dev/urandom of={} bs={} count=1 iflag=fullblock".format(data["folderin"], filename, data["bs"]), "")

@pytest.fixture(autouse=True)
def print_time():
    print("Start: {}".format(datetime.now().strftime("%H:%M:%S.%f")))
    yield
    print("\nFinish: {}".format(datetime.now().strftime("%H:%M:%S.%f")))

@pytest.fixture(autouse=True)
def stat():
    yield
    stat = getout("cat /proc/loadavg")
    find_text_in_command("echo 'time: {} count:{} size: {} load: {}'>> stat.txt".format(datetime.now().strftime("%H:%M:%S.%f"), data["count"], data["bs"], stat), "")
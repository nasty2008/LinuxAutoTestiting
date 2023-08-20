import subprocess
import sys
def find_text_in_out_command(command, text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding="utf-8")
    result_out = result.stdout
    if text in result_out:
        print('TRUE')
    else:
        print('FAIL')


if __name__ == '__main__':
    try:
        arguments = sys.argv
        command = arguments[1]
        text = arguments[2]
        find_text_in_out_command(command, text)
    except:
        find_text_in_out_command('cat /etc/os-release', 'jammy')
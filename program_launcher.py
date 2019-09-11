import subprocess


def launch(program):
    subprocess.Popen(program, shell=True)
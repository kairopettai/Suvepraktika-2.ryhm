import subprocess


def turn_on():
    return subprocess.check_output(["sudo", "python", "main.py", "1", "0", "FFFF", "/dev/ttyUSB0"])


def turn_off():
    return subprocess.check_output(["sudo", "python", "main.py", "1", "0", "0000", "/dev/ttyUSB0"])


def get_room_temp():
    return subprocess.check_output(["sudo", "python", "main.py", "1", "603", "1", "/dev/ttyUSB0"]).decode("UTF-8")


def get_dev_temp():
    return subprocess.check_output(["sudo", "python", "main.py", "1", "600", "3", "/dev/ttyUSB0"]).decode("UTF-8")


def check_state():
    state = subprocess.check_output(["sudo", "python", "main.py", "1", "0", "1", "/dev/ttyUSB0"])
    state = state.decode("UTF-8")
    state = state.strip("\n")
    if state == "0.0":
        return "OFF"
    else:
        return "ON"

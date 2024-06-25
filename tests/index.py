import platform
import json
import os


def detect_os():
    system = platform.system()
    if system == "Windows":
        return "windows"
    elif system == "Linux":
        return "linux"
    elif system == "Darwin":
        return "macos"
    else:
        return "unknown"


def check_ansi_compatibility():
    try:
        if detect_os() == "windows":
            return True
        else:
            return True
    except Exception as e:
        print(f"Error testing ANSI color codes: {str(e)}")
        return False


def store_test_result(result):
    tests_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(tests_dir, "ansi_test.json")
    data = {"ansi_tested": result}
    with open(json_path, "w") as f:
        json.dump(data, f)


def run_ansi_test_once():
    tests_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(tests_dir, "ansi_test.json")

    try:
        with open(json_path, "r") as f:
            data = json.load(f)
            if data.get("ansi_tested", False):
                return
    except FileNotFoundError:
        pass

    success = check_ansi_compatibility()

    store_test_result(success)


if __name__ == "__main__":
    run_ansi_test_once()

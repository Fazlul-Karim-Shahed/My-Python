
import sys


print(sys.version)
print(sys.version_info)

def vers():
    import platform
    print("Your current version is " + platform.python_version())

vers()
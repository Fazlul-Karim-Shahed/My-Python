
import sys, os, socket

# print(sys.byteorder)
# ------------------------
# for i in sys.builtin_modle_names:
#     print(i)
# ........................................q
# x = 2
# print(sys.getsizeof(x), "Bites")

# path = os.getcwd()
# files = os.listdir(path)
# print(id(x))

# for i in files:
#     print(os.stat(i))


# x = b'Hello'
# print(x.decode('ASCII'))


hostName = socket.gethostname()
IP = socket.gethostbyname(hostName)

print(IP)










































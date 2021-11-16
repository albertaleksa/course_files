from webformyself_course import my_libs
import sys

print(__name__)

print(my_libs.get_count('hello', 'l'))
print(my_libs.get_len('hello'))

print(sorted(sys.modules.keys()))

print(*sys.path, sep="\n")


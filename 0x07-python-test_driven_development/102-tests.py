<<<<<<< HEAD
#!/usr/bin/python3

=======
>>>>>>> 855a08f1d3ce28cb797137cc9521ea5082ec3822
import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_string.argtypes = [ctypes.py_object]
s = "The spoon does not exist"
lib.print_python_string(s)
s = "ложка не существует"
lib.print_python_string(s)
s = "La cuillère n'existe pas"
lib.print_python_string(s)
<<<<<<< HEAD
s = "勺孨"
=======
s = "勺子不存在"
>>>>>>> 855a08f1d3ce28cb797137cc9521ea5082ec3822
lib.print_python_string(s)
s = "숟가락은 존재하지 않는다."
lib.print_python_string(s)
s = "スプーンは存在しない"
lib.print_python_string(s)
s = b"The spoon does not exist"
lib.print_python_string(s)

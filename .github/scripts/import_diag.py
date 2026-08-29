import sys, importlib, importlib.util
print('PYTHONPATH:', sys.path)
print('Fun_With_Dev_Flask spec:', importlib.util.find_spec('Fun_With_Dev_Flask'))
print('fun_with_dev_python_shared spec:', importlib.util.find_spec('fun_with_dev_python_shared'))
try:
    import Fun_With_Dev_Flask
    print('Fun_With_Dev_Flask __file__=', Fun_With_Dev_Flask.__file__)
except Exception as e:
    print('Fun_With_Dev_Flask import error:', e)
try:
    import fun_with_dev_python_shared
    print('fun_with_dev_python_shared __file__=', fun_with_dev_python_shared.__file__)
except Exception as e:
    print('fun_with_dev_python_shared import error:', e)

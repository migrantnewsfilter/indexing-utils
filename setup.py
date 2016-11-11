import os
import setuptools

module_path = os.path.join(os.path.dirname(__file__), 'utils.py')

setuptools.setup(
    name="indexing-utils",
    version='0.0.1',
    url="https://github.com/migrantnewsfilter/indexing-utils",

    py_modules=['indexing-utils'],
    zip_safe=False,

    install_requires=[]
)

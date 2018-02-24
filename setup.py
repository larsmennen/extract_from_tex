from setuptools import setup

setup(
    name='extract_from_tex',
    version='0.1',
    py_modules=['extract_from_tex'],
    include_package_data=True,
    python_required='>=3.5',
    install_requires=[
        'click',
    ],
    entry_points='''
        [console_scripts]
        extract_from_tex=extract_from_tex:cli
    ''',
)
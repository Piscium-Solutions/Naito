from setuptools import setup, find_packages

setup(
    name='my_naito_app',
    version='0.0.1',
    description='A custom Frappe app',
    author='Your Name',
    author_email='your_email@example.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[]
)

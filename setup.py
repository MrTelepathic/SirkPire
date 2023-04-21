from setuptools import setup, find_packages

setup(
    name = 'SirkPire',
    version = '1.0',
    author='Mr Telepathic',
    author_email = 'shahrokhenhedam@gmail.com',
    description = 'This is a powerful library for building self robots in Rubika',
    keywords = ['rubika', 'rubino', 'pyrubi', 'pyrubika', 'rubika bot', 'rubika library', 'rubx', 'rubika-bot', 'rubika-lib', 'bot', 'self bot', 'rubika.ir'],
    long_description = open("README.md", encoding="utf-8").read(),
    python_requires="~=3.7",
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/MrTelepathic/SirkPire',
    packages = find_packages(),
    install_requires = ['pycryptodome', 'websocket-client', 'requests', 'aiohttp', 'urllib3', 'pillow', 'mutagen', 'tinytag'],
    classifiers = [
    	"Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
    ]
)
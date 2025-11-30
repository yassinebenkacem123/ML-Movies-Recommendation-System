from setuptools import setup
AUTHOR_NAME = "YASSINE AYOUB"
SRC_REPO = "src"
LIST_OF_REQUIREMENTS = ["streamlit"]
setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_NAME,
    packages=[SRC_REPO],
    author_email="yassinebenkacem12@gmail.com",
    description="A simple app for movie recommendations",
    long_description="This is a simple movie recommendation system built using Streamlit.",
    long_description_content_type="text/markdown",
    install_requires=LIST_OF_REQUIREMENTS,
    python_requires='>=3.7',
)
from setuptools import find_packages, setup
import pathlib

here = pathlib.Path(__file__).parent.resolve()

with open(f"{here}/README.md", "r") as readme_file:
    long_description = readme_file.read()

setup(
    name="spark_etl",
    version="0.0.1",
    author="Sanjeet Shukla",
    author_email="sanjeet.shukla089@gmail.com",
    packages=find_packages(exclude=["test"]),
    description="A pyspark boilerplate with Object Oriented Design",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SanjeetShukla01/pyspark_framework",
    license='CC BY-NC 4.0',
    python_requires='>=3.7',
    include_package_data=False,
    entry_points={
        "console_scripts": [
            "app=app:app",
        ],
    },
    package_data={".":["*.py"]},
    test_suite='tests',
    project_urls={
        "Bug Reports": "https://github.com/SanjeetShukla01/pyspark_framework/issues",
        "Funding": "https://donate.pypi.org",
        "Say Thanks!": "https://saythanks.io/my_project",
        "Source": "https://github.com/SanjeetShukla01/pyspark_framework/"
    }
)

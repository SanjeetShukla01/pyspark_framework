#!/bin/bash
'''
Package pyspark etl application and python dependencies into a `pyspark_etl_job.zip` folder
'''
ZIP_FILE="pyspark_pipeline.zip"
mkdir distribution_package
# activate your virtual environment (if applicable)
source venv/bin/activate
# generate requirements.txt file
pip freeze > requirements.txt
# deactivate your virtual environment (if applicable)
deactivate

pip3 -q install -r requirements.txt -t distribution_package
rm -r requirements.txt
cp -r {setup.py,src} distribution_package
cd distribution_package
version=$(echo `python3 setup.py --version` | sed s/_/-/g)
python3 setup.py sdist --format=zip
unzip -q "dist/$ZIP_FILE-$version.zip"
cd "$ZIP_FILE-$version"
# Small hack so that main package (datajob) can be added to python path
touch __init__.py
zip -q -r "../../$ZIP_FILE.zip" *
cd ../../
rm -r distribution_package






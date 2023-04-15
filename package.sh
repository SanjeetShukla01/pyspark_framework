#!/bin/bash
source respect.sh
# Package pyspark etl application and its python dependencies into a `pyspark_etl_job.zip` folder

zip_file="to_upload"
mkdir $zip_file target
cp README.md $zip_file/

respect.message.green "==============================================================="
respect.message.yellow "========== Creating a directory 'distribution_pacakge' ========"
respect.message.green "==============================================================="

respect.message "Activate your virtual environment (if applicable)"
source venv/bin/activate
respect.message "Generate requirements.txt file"
pip freeze > requirements.txt
respect.message "Deactivate your virtual environment (if applicable)"
deactivate

pip3 -q install -r requirements.txt -t $zip_file
cp -r {setup.py,src} $zip_file
cd $zip_file || exit

respect.message.green "==============================================================="
respect.message.yellow "=================  Inside Distribution Package ================"
respect.message.green "==============================================================="

version=$(echo `python3 setup.py --version` | sed s/_/-/g)
echo "$version"
python3 setup.py sdist --format=zip
pwd
unzip -q "dist/spark_etl-$version.zip"
cd "spark_etl-$version" || exit
# Small hack so that main package (src) can be added to python path
touch __init__.py
zip -q -r "../../target/spark_etl.zip" *
cd ../../
rm -r $zip_file
pwd







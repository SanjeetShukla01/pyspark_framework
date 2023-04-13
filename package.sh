#!/bin/bash
source respect.sh

echo ""
respect.window.title "This is the window title"
echo ""
respect.message "Normal message"
respect.message.red "Red message"
respect.message.yellow "Yellow message"
respect.message.blue "Blue message"
respect.message.green "Green message"
echo ""
respect.message.error "Error"
respect.message.warning "Warning"
respect.message.info "Info"
respect.message.success "Success"
respect.title "Title"

itWillFail() {
    return 1
}

itWillSucceed() {
    return 0
}

respect.process "Process fail\t\t" "itWillFail"
respect.process "Process success\t" "itWillSucceed"

respect.prepend.process "\vPrepend proccess fail" "itWillFail"
respect.prepend.process "Prepend proccess success" "itWillSucceed"

echo ""

respect.label "Label 1" "Value 1"
respect.label "Label 2" "Value 2"
respect.label "Label 3" "Value 3"

echo ""
respect.label.ln "Label line 1" "Value 1"
respect.label.ln "\tLabel line 2" "Value 2"
respect.label.ln "\tLabel line 3" "Value 3"

echo ""



:'
Package pyspark etl application and its python dependencies into a `pyspark_etl_job.zip` folder
'
ZIP_FILE="distribution_package"
mkdir distribution_package
respect.message.green "==============================================================="
respect.message.yellow "========== Creating a directory 'distribution_pacakge' ========"
respect.message.green "==============================================================="
respect.message "Activate your virtual environment (if applicable)"
source venv/bin/activate
respect.message "Generate requirements.txt file"
pip freeze > requirements.txt
respect.message "Deactivate your virtual environment (if applicable)"
deactivate

pip3 -q install -r requirements.txt -t distribution_package
#rm -r requirements.txt
cp -r {setup.py,src} distribution_package
cd distribution_package
respect.message.green "==============================================================="
respect.message.yellow "=================  Inside Distribution Package ================"
respect.message.green "==============================================================="
#version=$(echo `python3 setup.py --version` | sed s/_/-/g)
#echo version
#python3 setup.py sdist --format=zip
#unzip -q "dist/$ZIP_FILE-$version.zip"
#cd "$ZIP_FILE-$version"
# Small hack so that main package (datajob) can be added to python path
#touch __init__.py
#zip -q -r "../../$ZIP_FILE.zip" *
#cd ../../
#rm -r distribution_package






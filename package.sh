#!/bin/bash

# Set the name of the zip file to be created
ZIP_FILE="my_pyspark_pipeline.zip"

# Set the name of the directory containing the Python code
PROJECT_DIR="pipeline_code_directory"

# Navigate to the directory containing the Python code
cd "PROJECT_DIR" || exit

# Create a zip file containing the Python code
zip -r "$ZIP_FILE" .

# Move the zip file to the parent directory
mv "$ZIP_FILE" ..

# Navigate back to the parent directory
cd ..

echo "Successfully packaged Python code into $ZIP_FILE!"

# Run using `./script_name.sh` in terminal






#!/bin/bash

# Create test directories and sample BMP files for testing
mkdir -p test_source
mkdir -p test_output

# Create 20 sample BMP files (empty files with .bmp extension)
for i in $(seq 1 20); do
    touch "test_source/image_${i}.bmp"
done

# Run the data splitter script
python3 data_splitter.py --source test_source --output test_output

# Check results
echo "Checking results..."
echo "Files in train directory: $(ls test_output/train | wc -l)"
echo "Files in validation directory: $(ls test_output/validation | wc -l)"
echo "Files in test directory: $(ls test_output/test | wc -l)"

# Clean up test files
# Uncomment the following line to clean up after testing
# rm -rf test_source test_output

# Data-Splitting-Code-for-.bmp-Images

A Python tool for splitting image datasets into training, validation, and test sets with customizable ratios.

## Features

- Split image datasets into train, validation, and test sets with specified ratios
- Random selection to ensure unbiased data distribution
- Copy files to separate output directories (preserves original files)
- Support for any image format (default: .bmp)
- Command-line interface for easy integration into workflows

## Requirements

- Python 3.6 or higher
- Standard Python libraries (no additional dependencies required):
  - os
  - shutil
  - random
  - glob
  - argparse

## Usage

```bash
python data_splitter.py --source SOURCE_DIRECTORY --output OUTPUT_DIRECTORY
```

### Parameters

- `--source`: Source directory containing images (required)
- `--output`: Output directory for split datasets (required)
- `--train`: Ratio for training set (default: 0.6487)
- `--val`: Ratio for validation set (default: 0.1562)
- `--test`: Ratio for test set (default: 0.1951)
- `--ext`: File extension filter (default: .bmp)

## How It Works

1. The script scans the source directory for all files with the specified extension
2. Files are randomly shuffled to ensure unbiased selection
3. Based on the provided ratios, files are distributed into train, validation, and test sets
4. Files are copied to their respective output directories (train, validation, test)
5. A summary of the split is displayed upon completion

## Notes

- The script normalizes ratios if they don't sum to 1.0
- Actual ratios may slightly differ from specified values due to rounding to whole numbers
- The script ensures all images are used by distributing any remaining images

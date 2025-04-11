import os
import shutil
import random
import glob
import argparse

def split_data(source_dir, output_dir, train_ratio=0.6487, val_ratio=0.1562, test_ratio=0.1951, file_ext='.bmp'):
    """
    Split image data into train, validation, and test sets with specified ratios.
    
    Args:
        source_dir (str): Directory containing the source images
        output_dir (str): Directory where train, validation, and test folders will be created
        train_ratio (float): Ratio of images for training set (default: 0.6487)
        val_ratio (float): Ratio of images for validation set (default: 0.1562)
        test_ratio (float): Ratio of images for test set (default: 0.1951)
        file_ext (str): File extension to filter (default: '.bmp')
    """
    # Normalize ratios if they don't sum to 1
    total = train_ratio + val_ratio + test_ratio
    if abs(total - 1.0) > 0.001:  # Allow small floating point error
        train_ratio /= total
        val_ratio /= total
        test_ratio /= total
        print(f"Ratios normalized to sum to 1.0: Train={train_ratio:.4f}, Val={val_ratio:.4f}, Test={test_ratio:.4f}")
    
    # Create output directories
    train_dir = os.path.join(output_dir, 'train')
    val_dir = os.path.join(output_dir, 'validation')
    test_dir = os.path.join(output_dir, 'test')
    
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)
    
    # Get all image files with the specified extension
    image_files = glob.glob(os.path.join(source_dir, f'*{file_ext}'))
    
    if not image_files:
        print(f"No {file_ext} files found in {source_dir}")
        return
    
    # Shuffle the files randomly
    random.shuffle(image_files)
    
    # Calculate the number of images for each set
    total_images = len(image_files)
    train_count = int(total_images * train_ratio)
    val_count = int(total_images * val_ratio)
    # test_count will be the remainder to ensure all images are used
    
    print(f"Total images found: {total_images}")
    print(f"Train set: {train_count} images ({train_count/total_images:.4f})")
    print(f"Validation set: {val_count} images ({val_count/total_images:.4f})")
    print(f"Test set: {total_images - train_count - val_count} images ({(total_images - train_count - val_count)/total_images:.4f})")
    
    # Split the data
    train_files = image_files[:train_count]
    val_files = image_files[train_count:train_count + val_count]
    test_files = image_files[train_count + val_count:]
    
    # Copy files to respective directories
    for file in train_files:
        dest = os.path.join(train_dir, os.path.basename(file))
        shutil.copy2(file, dest)
    
    for file in val_files:
        dest = os.path.join(val_dir, os.path.basename(file))
        shutil.copy2(file, dest)
    
    for file in test_files:
        dest = os.path.join(test_dir, os.path.basename(file))
        shutil.copy2(file, dest)
    
    print("\nData splitting completed successfully!")
    print(f"Train set: {len(train_files)} images")
    print(f"Validation set: {len(val_files)} images")
    print(f"Test set: {len(test_files)} images")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split image data into train, validation, and test sets.')
    parser.add_argument('--source', type=str, required=True, help='Source directory containing images')
    parser.add_argument('--output', type=str, required=True, help='Output directory for split datasets')
    parser.add_argument('--train', type=float, default=0.6487, help='Ratio for training set (default: 0.6487)')
    parser.add_argument('--val', type=float, default=0.1562, help='Ratio for validation set (default: 0.1562)')
    parser.add_argument('--test', type=float, default=0.1951, help='Ratio for test set (default: 0.1951)')
    parser.add_argument('--ext', type=str, default='.bmp', help='File extension to filter (default: .bmp)')
    
    args = parser.parse_args()
    
    split_data(args.source, args.output, args.train, args.val, args.test, args.ext)

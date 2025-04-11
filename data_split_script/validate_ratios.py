import math

# Total number of images
total_images = 974

# Desired ratios
train_ratio = 0.6487
val_ratio = 0.1562
test_ratio = 0.1951

# Calculate exact counts
train_exact = total_images * train_ratio
val_exact = total_images * val_ratio
test_exact = total_images * test_ratio

# Calculate integer counts
train_count = math.floor(train_exact)
val_count = math.floor(val_exact)
test_count = math.floor(test_exact)

# Distribute remaining images
remaining = total_images - (train_count + val_count + test_count)
# Distribute based on fractional parts
fractions = [(train_exact - train_count, 'train'), 
             (val_exact - val_count, 'val'), 
             (test_exact - test_count, 'test')]
fractions.sort(reverse=True)

# Distribute remaining images to sets with largest fractional parts
for i in range(remaining):
    if fractions[i % 3][1] == 'train':
        train_count += 1
    elif fractions[i % 3][1] == 'val':
        val_count += 1
    else:
        test_count += 1

# Calculate actual ratios
actual_train_ratio = train_count / total_images
actual_val_ratio = val_count / total_images
actual_test_ratio = test_count / total_images

print(f"Total images: {total_images}")
print(f"Desired ratios - Train: {train_ratio:.4f}, Val: {val_ratio:.4f}, Test: {test_ratio:.4f}")
print(f"Actual counts - Train: {train_count}, Val: {val_count}, Test: {test_count}")
print(f"Actual ratios - Train: {actual_train_ratio:.4f}, Val: {actual_val_ratio:.4f}, Test: {actual_test_ratio:.4f}")
print(f"Sum of counts: {train_count + val_count + test_count}")
print(f"Sum of ratios: {actual_train_ratio + actual_val_ratio + actual_test_ratio:.4f}")

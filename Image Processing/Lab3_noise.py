from PIL import Image, ImageFilter

def read_bmp_image(file_path):
    # Open BMP image
    img = Image.open(file_path)
    return img

def apply_mean_filter(image):
    # Apply mean filter to remove noise
    mean_filtered_img = image.filter(ImageFilter.MinFilter(3))
    return mean_filtered_img

def apply_median_filter(image):
    # Apply median filter to remove noise
    median_filtered_img = image.filter(ImageFilter.MedianFilter(size=5))
    return median_filtered_img

def main():
    # 1. Read BMP image content into a memory array
    bmp_file_path = "pic/lab3-2.bmp"
    original_image = read_bmp_image(bmp_file_path)

    # 2. Apply mean filter to remove noise
    mean_filtered_image = apply_mean_filter(original_image)
    mean_filtered_image.save("result/lab3_mean_filtered_image.bmp")

    # 3. Apply median filter to remove noise
    median_filtered_image = apply_median_filter(original_image)
    median_filtered_image.save("result/lab3_median_filtered_image2.bmp")

    print("Image processing completed.")

if __name__ == "__main__":
    main()

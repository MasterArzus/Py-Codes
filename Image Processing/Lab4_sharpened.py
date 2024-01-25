from PIL import Image, ImageFilter
import numpy as np

def read_bmp_image(file_path):
    # Open BMP image
    img = Image.open(file_path)
    return img


def laplacian_filter(image):
    # Convert image to grayscale
    grayscale_img = image.convert("L")

    # Convert image to NumPy array
    img_array = np.array(grayscale_img)

    # Define Laplacian filter kernel
    laplacian_kernel = np.array([[0, 1, 0],
                                 [1, -4, 1],
                                 [0, 1, 0]])

    laplacian_kernel2 = np.array([[1, 1, 1],
                                 [1, -8, 1],
                                 [1, 1, 1]])

    # Perform convolution with Laplacian kernel
    filtered_img_array = np.zeros_like(img_array, dtype=np.int32)

    for i in range(1, img_array.shape[0] - 1):
        for j in range(1, img_array.shape[1] - 1):
            filtered_img_array[i, j] = np.sum(img_array[i - 1:i + 2, j - 1:j + 2] * laplacian_kernel)

    # Normalize the result to ensure values are in the valid pixel range
    filtered_img_array = np.clip(filtered_img_array, 0, 255).astype(np.uint8)

    # Convert back to PIL Image
    new_img= Image.fromarray(img_array+filtered_img_array)
    filtered_img = Image.fromarray(filtered_img_array)
    new_img.save('lab4_laplacian_sharpened_image+8.bmp')

    return filtered_img

def apply_laplacian_sharpening(image):
    # Apply Laplacian filter to sharpen the image
    laplacian_sharpened_img = image.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
    return laplacian_sharpened_img

def main():
    # 1. Read BMP image content into a memory array
    bmp_file_path = "pic/lab4.bmp"
    original_image = read_bmp_image(bmp_file_path)

    # 2. Apply Laplacian sharpening to the image
    laplacian_sharpened_image = apply_laplacian_sharpening(original_image)
    # laplacian_sharpened_image.save("lab4_laplacian_sharpened_image.bmp")

    laplacian_filter(original_image)


    # 3. Compare the sharpened image with the original image
    # comparison_image = ImageOps.concat([original_image, laplacian_sharpened_image], padding=10)
    # comparison_image.save("lab4_comparison_image.bmp")

    print("Image processing completed.")

if __name__ == "__main__":
    main()

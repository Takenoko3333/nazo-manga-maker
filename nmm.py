import sys
import os
import random
from PIL import Image
from datetime import datetime

# --- config start ---
input_folder = 'inputs'
output_folder = 'outputs'
input_extensions = ('png', 'jpg', 'jpeg', 'webp', 'bmp', 'gif')  # Supported formats: 'png', 'jpg', 'jpeg', 'webp', 'bmp', 'gif'
output_count = 3
output_name = 'output'
output_format = 'jpg'  # Supported formats: 'png', 'jpg', 'jpeg', 'webp', 'bmp', 'gif'
quality = 85  # Applies to jpg (jpeg) or webp
crop_type = 'top-left'  # Supported crop types: 'none', 'center', 'top-left', 'bottom-right', 'random'
grid_type = '2x4'  # Supported grid types: '1x4', '2x2', '2x3', '2x4'
# --- config end ---

def get_image_files(folder_path):
    return [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.lower().split('.')[-1] in input_extensions]

def center_crop(image):
    width, height = image.size
    new_edge_length = min(width, height)
    left = (width - new_edge_length) // 2
    top = (height - new_edge_length) // 2
    right = (width + new_edge_length) // 2
    bottom = (height + new_edge_length) // 2
    return image.crop((left, top, right, bottom))

def top_left_crop(image):
    width, height = image.size
    new_edge_length = min(width, height)
    if width > height:
        return image.crop((0, 0, new_edge_length, height))
    else:
        return image.crop((0, 0, width, new_edge_length))

def bottom_right_crop(image):
    width, height = image.size
    new_edge_length = min(width, height)
    if width > height:
        return image.crop((width - new_edge_length, 0, width, height))
    else:
        return image.crop((0, height - new_edge_length, width, height))

def random_crop(image):
    width, height = image.size
    new_edge_length = min(width, height)
    left = random.randint(0, width - new_edge_length)
    top = random.randint(0, height - new_edge_length)
    right = left + new_edge_length
    bottom = top + new_edge_length
    return image.crop((left, top, right, bottom))

def crop_image(image, crop_type):
    if crop_type == 'center':
        return center_crop(image)
    elif crop_type == 'random':
        return random_crop(image)
    elif crop_type == 'top-left':
        return top_left_crop(image)
    elif crop_type == 'bottom-right':
        return bottom_right_crop(image)
    elif crop_type == 'none':
        return image
    else:
        return image  # Default to none if an unsupported crop type is specified

def create_image_grid(image_files, grid_size=(2, 3), output_size=(1024, 1536), output_path='output.png', output_format='png', quality=85, crop_type='none'):
    images = [Image.open(img).convert("RGB") for img in image_files]

    # Crop images based on the specified crop type
    images = [crop_image(img, crop_type) for img in images]

    # Calculate the size of each individual image in the grid
    cell_width = output_size[0] // grid_size[0]
    cell_height = output_size[1] // grid_size[1]
    cell_size = (cell_width, cell_height)

    # If there are less images than the grid requires, add white images to make up the difference
    while len(images) < (grid_size[0] * grid_size[1]):
        images.append(Image.new('RGB', cell_size, (255, 255, 255)))

    # Resize images to fit into the grid cells
    resized_images = [img.resize(cell_size, Image.ANTIALIAS) for img in images]

    # Create a new blank image with the specified output size
    grid_image = Image.new('RGB', output_size)

    # Paste the images into the grid
    for index, img in enumerate(resized_images):
        row = index // grid_size[0]
        col = index % grid_size[0]
        grid_image.paste(img, (col * cell_width, row * cell_height))

    # Save the final image
    if output_format in ['jpg', 'jpeg', 'webp']:
        if output_format == 'jpg': output_format = 'jpeg'
        grid_image.save(output_path, format=output_format.upper(), quality=quality)
    else:
        grid_image.save(output_path, format=output_format.upper())
    print(f"Image grid saved as {output_path}")

# Main function
def main(output_count=3, output_name='output', output_format='jpg', quality=85, crop_type='top-left', grid_type='2x3'):
    # Ensure the output directory exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Validate output count
    try:
        output_count = int(output_count)
    except ValueError:
        print(f"Warning: Invalid output_count '{output_count}'. Defaulting to 3.")
        output_count = 3

    # Validate output format
    valid_output_formats = {'png', 'jpg', 'jpeg', 'webp', 'bmp', 'gif'}
    if output_format.lower() not in valid_output_formats:
        print(f"Warning: Unsupported output format '{output_format}'. Defaulting to 'jpg'.")
        output_format = 'jpg'

    # Validate quality
    try:
        quality = int(quality)
    except ValueError:
        print(f"Warning: Invalid quality '{quality}'. Defaulting to 85.")
        quality = 85
    if not (0 <= quality <= 100):
        print(f"Warning: Invalid quality '{quality}'. Defaulting to 85.")
        quality = 85

    # Validate crop type
    valid_crop_types = {'none', 'center', 'top-left', 'bottom-right', 'random'}
    if crop_type.lower() not in valid_crop_types:
        print(f"Warning: Unsupported crop type '{crop_type}'. Defaulting to 'top-left'.")
        crop_type = 'top-left'

    # Validate grid type and set grid size and output size
    grid_settings = {
        '1x4': {'grid_size': (1, 4), 'output_size': (512, 2048)},
        '2x2': {'grid_size': (2, 2), 'output_size': (1024, 1024)},
        '2x3': {'grid_size': (2, 3), 'output_size': (1024, 1536)},
        '2x4': {'grid_size': (2, 4), 'output_size': (1024, 2048)}
    }
    if grid_type not in grid_settings:
        print(f"Warning: Unsupported grid type '{grid_type}'. Defaulting to '2x3'.")
        grid_type = '2x3'
    grid_size = grid_settings[grid_type]['grid_size']
    output_size = grid_settings[grid_type]['output_size']

    image_files = get_image_files(input_folder)

    if len(image_files) < (grid_size[0] * grid_size[1]):
        print("Not enough images in the folder to create a grid. Adding white images to fill the grid.")

    for i in range(output_count):
        selected_images = random.sample(image_files, min(len(image_files), grid_size[0] * grid_size[1]))
        timestamp = datetime.now().strftime('%Y%m%d-%H%M%S')
        output_path = os.path.join(output_folder, f'{timestamp}-{output_name}-{i+1:05d}.{output_format.lower()}')
        create_image_grid(selected_images, grid_size=grid_size, output_size=output_size, output_path=output_path, output_format=output_format.lower(), quality=quality, crop_type=crop_type)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        output_count = sys.argv[1]

    if len(sys.argv) >= 3:
        output_name = sys.argv[2]

    if len(sys.argv) >= 4:
        output_format = sys.argv[3]

    if len(sys.argv) >= 5:
        quality = sys.argv[4]

    if len(sys.argv) >= 6:
        crop_type = sys.argv[5]

    if len(sys.argv) >= 7:
        grid_type = sys.argv[6]

    main(output_count, output_name, output_format, quality, crop_type, grid_type)

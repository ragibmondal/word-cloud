import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
from PIL import Image

def generate_word_cloud(text_file, mask_image, output_file=None):
    """
    Generate a word cloud from a text file using a custom mask image.
    
    Parameters:
    - text_file (str): Path to the input text file
    - mask_image (str): Path to the mask image
    - output_file (str, optional): Path to save the output image
    """
    # Read the text file
    try:
        with open(text_file, 'r', encoding='utf-8') as file:
            text = file.read()
    except IOError as e:
        print(f"Error reading text file: {e}")
        return

    # Read the mask image
    try:
        python_mask = np.array(Image.open(mask_image))
    except IOError as e:
        print(f"Error reading mask image: {e}")
        return

    # Create a set of custom stopwords (optional)
    custom_stopwords = set(STOPWORDS)
    # Uncomment and modify the line below to add more stopwords
    # custom_stopwords.update(['additional', 'stopwords', 'here'])

    # Generate the word cloud
    wc = WordCloud(
        stopwords=custom_stopwords,
        mask=python_mask,
        background_color="black",
        contour_width=3,
        contour_color='white',
        min_font_size=4,
        max_font_size=150,
        max_words=100000,
        colormap='viridis'  # Changed from 'rainbow' to a more consistent colormap
    ).generate(text)

    # Create the plot
    plt.figure(figsize=(10, 10), facecolor=None)
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad=0)

    # Save or show the plot
    if output_file:
        plt.savefig(output_file, bbox_inches='tight', pad_inches=0)
        print(f"Word cloud saved to {output_file}")
    else:
        plt.show()

# Example usage
if __name__ == "__main__":
    # Replace these with your actual file paths
    text_file = 'name.txt'
    mask_image = 'image.png'
    output_file = 'word_cloud_output.png'  # Optional: specify to save the image

    generate_word_cloud(text_file, mask_image, output_file)
def build_comic_layout(images, stories):
    # Combines images and stories into a structured layout
    layout = []
    for img, text in zip(images, stories):
        layout.append({"image_path": img, "text": text})
    return layout

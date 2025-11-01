function changeImage(selectedColor, productId) {
    const mainImage = document.getElementById(productId);
    const allImages = mainImage.getAttribute('data-images').split(',');
    console.log(allImages)

    const matchedImagePath = allImages.find(path => path.trim().toLowerCase().includes(selectedColor.toLowerCase()));
    
    console.log(matchedImagePath)
    if (matchedImagePath) {

        mainImage.src = `${STATIC_IMAGES_URL}${matchedImagePath.trim()}`;
        console.log(mainImage.src);
    } else {
        console.log(`Nem található kép a következő színhez: ${selectedColor}`);
    }
}
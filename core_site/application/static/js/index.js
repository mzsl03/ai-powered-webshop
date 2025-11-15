document.addEventListener("DOMContentLoaded", () => {
    const colorCircles = document.querySelectorAll(".color-circle");

    colorCircles.forEach(circle => {
        circle.addEventListener("click", (e) => {
            e.preventDefault();
            e.stopPropagation();

            const selectedColor = circle.style.backgroundColor;
            const productCard = circle.closest(".product-card");
            const productImage = productCard?.querySelector(".product-image");
            const productLink = productCard?.querySelector(".product-link");

            if (selectedColor && productImage) {
                changeImage(selectedColor, productImage.id);
                if (productLink && circle.href) {
                    productLink.href = circle.href;
                }
            }
        });
    });
});

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

document.addEventListener("DOMContentLoaded", () => {
    const colorCircles = document.querySelectorAll(".color-circle");

    colorCircles.forEach(circle => {
        circle.addEventListener("click", (e) => {
            e.preventDefault();     // ne nyissa meg a termékoldalt
            e.stopPropagation();    // ne menjen tovább az esemény a kártyáig

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

(function resetScrollContainers() {
  const reset = () => {
    const grid = document.querySelector('.product-grid');
    if (grid) {
      grid.scrollTop = 0;
      grid.scrollLeft = 0;
      requestAnimationFrame(() => grid.scrollTo({ top: 0, left: 0, behavior: 'auto' }));
    }
    if ('scrollRestoration' in history) history.scrollRestoration = 'manual';
    window.scrollTo(0, 0);
  };
  document.addEventListener('DOMContentLoaded', reset);
  window.addEventListener('load', reset);
  window.addEventListener('pageshow', e => {
    if (e.persisted || (performance.getEntriesByType('navigation')[0]?.type === 'reload')) reset();
  });
})();


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

document.addEventListener("DOMContentLoaded", () => {
    window.scrollTo(0, 0);
    const body = document.body;
    const scrollLink = document.querySelector(".hero-btn");
    const target = document.getElementById("products");
    const atTop = window.scrollY < window.innerHeight * 0.5;


    if (atTop) {
        body.style.overflow = "hidden";
        window.scrollTo({ top: 0, behavior: "instant" });
    } else {
        body.style.overflow = "auto";
    }

        function smoothScrollTo(targetY, duration = 3000) {
        const startY = window.scrollY;
        const distance = targetY - startY;
        const startTime = performance.now();

        function step(currentTime) {
            const elapsed = currentTime - startTime;
            const progress = Math.min(elapsed / duration, 1);
            const ease = 1 - Math.pow(1 - progress, 3); // cubic ease-out
            window.scrollTo(0, startY + distance * ease);

            if (elapsed < duration) requestAnimationFrame(step);
        }

        requestAnimationFrame(step);
    }

    scrollLink?.addEventListener("click", (e) => {
        e.preventDefault();

        // először fade-out effekt
        const hero = document.querySelector(".hero");
        if (hero) hero.classList.add("fade-out");

        // kis idő múlva engedjük a scrollt
        setTimeout(() => {
            body.style.overflow = "auto";

            // és görgetünk le
            if (target) {
                target.scrollIntoView({behavior: "smooth", block: "start"});
            }
        }, 600); // ennyi idő alatt elhalványul a hero
    });
});

document.addEventListener("scroll", () => {
    const cards = document.querySelectorAll(".product-card");
    const scrollY = window.scrollY;

    cards.forEach((card, i) => {
        const rect = card.getBoundingClientRect();
        const depth = (i % 3) * 0.15 + 0.35;
        const offset = (scrollY - rect.top * depth) * 0.03;

        if (rect.top < window.innerHeight && rect.bottom > 0) {
            card.style.transform = `translateY(${offset}px) scale(1)`;
            card.style.opacity = 1;
        }
    });
});
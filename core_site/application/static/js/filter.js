// Add this to your index.js or create a new filters.js file

console.log('Custom dropdown script loaded');

document.addEventListener('DOMContentLoaded', function() {
  console.log('DOM loaded, initializing dropdown');

  const select = document.getElementById('cat');
  console.log('Select element found:', select);

  if (!select) {
    console.error('Select element with id "cat" not found!');
    return;
  }

  // Get the currently selected index (preserve URL parameter selection)
  const currentIndex = select.selectedIndex >= 0 ? select.selectedIndex : 0;
  console.log('Current selected index:', currentIndex);

  // Create custom dropdown wrapper
  const wrapper = document.createElement('div');
  wrapper.className = 'custom-select-wrapper';

  const customSelect = document.createElement('div');
  customSelect.className = 'custom-select';

  const selectedOption = document.createElement('div');
  selectedOption.className = 'custom-select-trigger';
  selectedOption.textContent = select.options[currentIndex].text;

  const optionsList = document.createElement('div');
  optionsList.className = 'custom-options';

  // Create custom options
  Array.from(select.options).forEach((option, index) => {
    const customOption = document.createElement('div');
    customOption.className = 'custom-option';
    if (index === currentIndex) {
      customOption.classList.add('selected');
    }
    customOption.textContent = option.text;
    customOption.dataset.value = option.value;

    customOption.addEventListener('click', function(e) {
      console.log('Option clicked:', option.text);
      e.stopPropagation();

      // Update native select
      select.selectedIndex = index;
      select.value = option.value;

      // Update custom dropdown
      selectedOption.textContent = option.text;

      // Update selected state
      optionsList.querySelectorAll('.custom-option').forEach(opt => {
        opt.classList.remove('selected');
      });
      customOption.classList.add('selected');

      // Close dropdown
      customSelect.classList.remove('open');
    });

    optionsList.appendChild(customOption);
  });

  customSelect.appendChild(selectedOption);
  customSelect.appendChild(optionsList);
  wrapper.appendChild(customSelect);

  // Hide native select and insert custom dropdown
  select.style.display = 'none';
  select.parentNode.insertBefore(wrapper, select);

  console.log('Custom dropdown created');

  // Toggle dropdown
  selectedOption.addEventListener('click', function(e) {
    console.log('Trigger clicked');
    e.stopPropagation();
    e.preventDefault();

    const isOpen = customSelect.classList.contains('open');

    // Close all dropdowns first
    document.querySelectorAll('.custom-select').forEach(dropdown => {
      dropdown.classList.remove('open');
    });

    // Toggle this dropdown
    if (!isOpen) {
      customSelect.classList.add('open');
      console.log('Dropdown opened');
    } else {
      console.log('Dropdown closed');
    }
  });

  // Close dropdown when clicking outside
  document.addEventListener('click', function(e) {
    if (!customSelect.contains(e.target)) {
      customSelect.classList.remove('open');
    }
  });

  console.log('Event listeners attached');
});

const grid = document.querySelector(".product-grid");

if (grid) {
  grid.addEventListener("scroll", () => {
    const cards = grid.querySelectorAll(".product-card");
    const scrollTop = grid.scrollTop;
    const gridHeight = grid.clientHeight;

    cards.forEach((card, i) => {
      const rect = card.getBoundingClientRect();
      const depth = (i % 3) * 0.15 + 0.4;


    });
  });
}
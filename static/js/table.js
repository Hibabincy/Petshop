const rows = document.querySelectorAll('.eael-data-table tbody tr');
    let isOdd = true; // Track odd/even state
    rows.forEach((row) => {
        if (row.querySelector('.heading-tage')) {
            // Reset odd/even when encountering a heading row
            isOdd = true;
        } else {
            // Apply odd/even styling
            row.style.backgroundColor = isOdd ? '#FFFFFF' : '#F3F3F3';
            isOdd = !isOdd; // Toggle odd/even
        }
    });






document.addEventListener('DOMContentLoaded', function () {
    const menuItems = document.querySelectorAll('.menus li');
    const table = document.querySelector('.eael-data-table');
    const rows = table.querySelectorAll('tr');

    // Function to reset hidden columns
    function resetColumns() {
        rows.forEach(row => {
            row.querySelectorAll('th, td').forEach(cell => {
                cell.classList.remove('hidden-column');
            });
        });
    }

    // Function to hide columns based on index
    function hideColumns(index) {
        resetColumns(); // Clear previous hidden columns

        rows.forEach(row => {
            const cells = row.querySelectorAll('th, td');
            if (index === 0) { // Basic Clicked
                cells[2]?.classList.add('hidden-column'); // Professional
                cells[3]?.classList.add('hidden-column'); // Enterprise
            } else if (index === 1) { // Professional Clicked
                cells[1]?.classList.add('hidden-column'); // Basic
                cells[3]?.classList.add('hidden-column'); // Enterprise
            } else if (index === 2) { // Enterprise Clicked
                cells[1]?.classList.add('hidden-column'); // Basic
                cells[2]?.classList.add('hidden-column'); // Professional
            }
        });
    }

    // Function to handle responsive behavior
    function handleResponsiveView() {
        if (window.innerWidth <= 1024) {
            // Trigger first <li> (Basic) automatically
            menuItems[0].classList.add('active'); // Optional: Add active class for styling
            hideColumns(0);
        } else {
            // Default view (reset all columns)
            resetColumns();
        }
    }

    // Add click listeners to menu items
    menuItems.forEach((menuItem, index) => {
        menuItem.addEventListener('click', function () {
          menuItems.forEach(item => item.classList.remove('active')); // Remove active from all
          menuItem.classList.add('active'); // Add active to clicked one
          hideColumns(index);
        });
    });
    // Initial check on page load
    handleResponsiveView();
    // Add event listener for window resize
    window.addEventListener('resize', handleResponsiveView);
});



document.querySelectorAll('.menus li').forEach((item) => {
    item.addEventListener('click', () => {
        item.scrollIntoView({
          behavior: 'smooth', // Smooth scrolling
          inline: 'center',   // Horizontal scrolling
          block: 'nearest',   // Prevent unnecessary vertical scrolling
        });
    });
});



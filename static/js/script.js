document.addEventListener('DOMContentLoaded', () => {
    // Add a class to the body once the page is loaded
    document.body.classList.add('loaded');

    // Add event listeners to the category titles for filtering
    const categoryTitles = document.querySelectorAll('h2');
    categoryTitles.forEach(title => {
        title.addEventListener('click', () => {
            const category = title.parentElement;
            category.classList.toggle('collapsed');
        });
    });

    // Add a subtle animation to the cards on mouseover
    const cards = document.querySelectorAll('.card');
    cards.forEach(card => {
        card.addEventListener('mousemove', e => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;

            const rotateX = (y / rect.height - 0.5) * -20;
            const rotateY = (x / rect.width - 0.5) * 20;

            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0)';
        });
    });
});

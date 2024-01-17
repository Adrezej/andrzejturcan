window.addEventListener('scroll', function() {
    let header = document.querySelector('h1');
    if (header) {
        let scrolled = window.scrollY;
        header.style.transform = 'translateY(' + scrolled * 0.3 + 'px)';
    }
});

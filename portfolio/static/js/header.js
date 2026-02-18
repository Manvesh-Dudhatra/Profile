document.addEventListener("DOMContentLoaded", function () {
    const current = window.location.pathname;
    document.querySelectorAll(".menu-item").forEach(link => {
        if (link.getAttribute("href") === current) {
            link.classList.add("border-b-2", "border-blue-700");
        }
    });
});
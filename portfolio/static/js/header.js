let items = document.querySelectorAll(".menu-item")

items.forEach(item => {
    item.addEventListener('click', function () {
        items.forEach(item => {
            item.classList.remove("border-b-3","border-blue-700")
        })
        this.classList.add("border-b-3","border-blue-700")
    })
})
// offcanvasを制御
const sw = window.screen.width
let myOffcanvas = document.getElementById('offcanvasDarkNavbar')
let serchArea = document.getElementById('filter-open-col')

if (768 <= sw) {
    myOffcanvas.classList.add("show");
    if (serchArea) {
        serchArea.classList.add("show");
    }
}

let mainId = document.getElementById('main')
myOffcanvas.addEventListener('show.bs.offcanvas', () => {
    mainId.classList.add("main-padding-left")
})

myOffcanvas.addEventListener('hide.bs.offcanvas', () => {
    mainId.classList.remove("main-padding-left")
})

myOffcanvas.addEventListener('shown.bs.offcanvas', () => {
    
})

myOffcanvas.addEventListener('hidden.bs.offcanvass', () => {

})
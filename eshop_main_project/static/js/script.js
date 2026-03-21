const navLinks = document.getElementById('nav-links')
const menuBtn = document.getElementById('menu-btn')
const menuIcon= document.getElementById('menu-icon')
const link = document.querySelectorAll('.link')

setTimeout( () => {
    document.querySelectorAll('.alert').forEach( message => {
        message.style.display = 'none'
    })
} , 5000)

menuBtn.addEventListener('click' , () => {
    navLinks.classList.toggle('show');

    const isOpen = navLinks.classList.contains('show')
    menuIcon.setAttribute('class' , isOpen? 'ri-close-line' : 'ri-menu-line')
});

link.forEach( el => {
    el.addEventListener('click' , () => {
        navLinks.classList.remove('show')
        menuIcon.setAttribute('class' , 'ri-menu-line ')
    })
})



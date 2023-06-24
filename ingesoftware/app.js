let carrito = [];
let total = 0;

function agregarAlCarrito(producto, precio) {
    carrito.push({ producto, precio });
    total += precio;
    actualizarCarrito();
}

function actualizarCarrito() {
    const listaCarrito = document.getElementById('listaCarrito');
    const totalCarrito = document.getElementById('totalCarrito');
    
    listaCarrito.innerHTML = '';
    
    carrito.forEach(item => {
    const li = document.createElement('li');
    li.textContent = `${item.producto} - $${item.precio.toFixed(2)}`;
    listaCarrito.appendChild(li);
    });
    
    totalCarrito.textContent = `$${total.toFixed(2)}`;
}

function vaciarCarrito() {
    carrito = [];
    total = 0;
    actualizarCarrito();
}

const carousel = document.querySelector('.carousel');
const carouselInner = document.querySelector('.carousel-inner');
const carouselItems = document.querySelectorAll('.carousel-item');

let currentIndex = 0;
const slideWidth = carousel.clientWidth;

function prevSlide() {
    currentIndex = (currentIndex - 1 + carouselItems.length) % carouselItems.length;
    updateSlidePosition();
}

function nextSlide() {
    currentIndex = (currentIndex + 1) % carouselItems.length;
    updateSlidePosition();
}

function updateSlidePosition() {
    const newPosition = -currentIndex * slideWidth;
    carouselInner.style.transform = `translateX(${newPosition}px)`;
}

window.addEventListener("scroll",function(){
    var header = document.querySelector("header");
    header.classList.toggle("abajo",window.scrollY>0);
}
)

const nombre = document.getElementById("name")
const pass = document.getElementById("pass")
const mail = document.getElementById("mail")
const form = document.getElementById("form")
const parr = document.getElementById("warnings")

form.addEventListener("submit", e=>{
    e.preventDefault()
    let warnings = ""
    let entrar = false
    let regexmail = pattern="[A-Za-z0-9!?-]{8,12}"
    parr.innerHTML =""
    if(nombre.Value.length <6){
        warnings += 'El nombre debe tener al menos 6 caracteres'
        entrar = true
    }
    if(regexmail.test(mail.Value) == false){
        warnings += 'El correo no es valido'
        entrar = true
    }
    if(pass.Value.length <6){
        warnings += 'La contraseña debe tener al menos 6 caracteres'
        entrar = true
    }
    if(entrar){
        parr.innerHTML = warnings
    }else{
        parr.innerHTML = "Registrado"
    }
})
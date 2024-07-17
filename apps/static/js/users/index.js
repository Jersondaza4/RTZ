//funciones Javascript que van a interactuar con los templates de usuarios
// $ es una instancia de Jquery
document.addEventListener("DOMContentLoaded", function() {
    const carouselItems = document.querySelectorAll(".data-carousel-item");
    let currentIndex = 0;
    const intervalTime = 5000; // Cambiar cada 5 segundos

    // Función para mostrar el elemento actual y ocultar los demás
    function showCurrentItem() {
        carouselItems.forEach((item, index) => {
            if (index === currentIndex) {
                item.classList.remove("hidden");
            } else {
                item.classList.add("hidden");
            }
        });
    }

    // Función para mostrar el siguiente elemento
    function showNextItem() {
        currentIndex = (currentIndex + 1) % carouselItems.length;
        showCurrentItem();
    }

    // Función para avanzar al siguiente elemento cada intervalo de tiempo
    function autoChangeItem() {
        setInterval(() => {
            showNextItem();
        }, intervalTime);
    }

    // Llamar a la función para cambiar automáticamente los elementos
    autoChangeItem();
});


function userList(){
    $.ajax({
        ulr: "/user/list-user", //debe ir con el / del inicio, sino lo duplica
        type: "get",
        dataType: "json",
        success: function(response){// que pasa si se obtiene una respuesta correcta del back
           //Se puede usar datatable, libreria de JS para usar con AJAX
           console.log(response);
        },
        error: function(error){
            console.log(error);
        }
    });
}

$(document).ready(function(){
    userList();
});
$(document).ready(function () {
    // Agrega el evento de doble clic a cada elemento h2 dentro del contenedor
    $('.container h2').dblclick(function () {
        // Cambia el color de texto del elemento h2 al que se le dio doble clic
        $(this).css('color', '#DC3545');
    });
});

$(document).ready(function(){
    // Agrega el evento de doble clic al contenedor
    $('.container').dblclick(function(){
        // Encuentra el h3 dentro del contenedor actual y cambia su color de fondo
        $(this).find('h3').css('background-color', '#DC3545');
    });
});

var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl)
});

$(document).ready(function(){
    // Seleccionamos el botón por su ID y agregamos un evento de clic
    $("#enviarCorreo").click(function(){
        // Mostramos una alerta cuando se hace clic en el botón
        alert("El correo fue enviado correctamente...");
    });
});

$(document).ready(function(){
    // Agrega un controlador de eventos al hacer clic en los títulos de las cartas
    $('.card-title').click(function(){
        // Encuentra el párrafo (contenido de la carta) correspondiente a este título
        var paragraph = $(this).closest('.card').find('.card-body p');
        // Alterna la visibilidad del párrafo
        paragraph.toggle();
    });
});


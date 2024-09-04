document.addEventListener('DOMContentLoaded', function() {
    const campoBusqueda = document.getElementById('campoBusqueda');
    const estaciones = Array.from(document.querySelectorAll('.estacion'));

    campoBusqueda.addEventListener('keyup', () => {
        const texto = campoBusqueda.value.toLowerCase();
        estaciones.forEach(estacion => {
            const razonSocial = estacion.querySelector('h3').textContent.toLowerCase();
            if (razonSocial.includes(texto)) {
                estacion.style.display = '';
            } else {
                estacion.style.display = 'none';
            }
        });
    });
});

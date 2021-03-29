function carregar () {
    var msg = document.getElementById('msg')
    var img = document.getElementById('imagem')
    var data = new Date()
    var hora = data.getHours()
    //var hora = 2
    msg.innerHTML = `Agora são ${hora} horas.`
    if ( hora >=0 && hora < 12) {
        // Bom dia!
        img.src = 'fotomanha.png'
        document.body.style.background = '#f0c55d'
    } else if ( hora >=12 && hora < 18) {
        // Boa tarde!
        img.src = 'fototarde.png'
        document.body.style.background = '#e94c00'
    } else {
        // Boa noite!
        img.src = 'fotonoite.png'
        document.body.style.background = '#1c353c'
    }
}

let aberto = false;
const sidebar = document.getElementById('sidebar');

let sidebarWidth = '275px'
const abrirmenu = () => {
    if (aberto){                
        aberto = false;
        sidebar.style.left = `-${sidebarWidth}`;
        
    } else {                
        sidebar.style.left = '0';
        aberto = true;
    }
}

const footer = document.getElementsByClassName('footer')[0]
function verificaSide() {
    if (window.innerWidth >= 720) {
        sidebar.style.left = '0';
        aberto = true;
    } else {
        aberto = false;
        sidebar.style.left = `-${sidebarWidth}`;
    }
}

//aumentar e diminuir a fonte
function fonte(e) {
    var elemento = $(".acessibilidade");
    var fonte = elemento.css('font-size');
    cont = 0;

    if (e == 'a') {
        elemento.css("fontSize", parseInt(fonte) + 1);
        console.log('aumentou');

    } else if (e == 'd') {
        elemento.css("fontSize", parseInt(fonte) - 1);
        console.log('diminuiu');
    } else if (e == 'r') {
        elemento.css("fontSize", parseInt(fonte) == 1 + 'em');
        console.log('restaurou');
    }
}

//auto contraste
(function () {
    var Contrast = {
        storage: 'contrastState',
        cssClass: 'contrast',
        currentState: null,
        check: checkContrast,
        getState: getContrastState,
        setState: setContrastState,
        toogle: toogleContrast,
        updateView: updateViewContrast
    };

    window.toggleContrast = function () { Contrast.toogle(); };

    Contrast.check();

    function checkContrast() {
        this.updateView();
    }

    function getContrastState() {
        return localStorage.getItem(this.storage) === 'true';
    }

    function setContrastState(state) {
        localStorage.setItem(this.storage, '' + state);
        this.currentState = state;
        this.updateView();
    }

    function updateViewContrast() {
        var body = document.body;

        if (this.currentState === null)
            this.currentState = this.getState();

        if (this.currentState)
            body.classList.add(this.cssClass);
        else
            body.classList.remove(this.cssClass);
    }

    function toogleContrast() {
        this.setState(!this.currentState);
    }
})();
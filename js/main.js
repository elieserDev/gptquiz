var valueTheme = ''
var menu = document.querySelector('.menu-start');
var titleThemeChoice = document.querySelector('.theme-title-quiz');

function pressStart() {
    let theme = document.querySelector('#theme');
    let valueTheme = theme.value;
    localStorage.setItem('theme', valueTheme);
    getQuestion(valueTheme);
    menu.innerHTML = 'Carregando...';
    titleThemeChoice.style.display = 'none';
    theme.style.display = 'none';
}

function getQuestion(theme) {
    payload = {
        "token": "xxxxxxx",
        "msg": theme
    }

    $.ajax({
        type: "POST",
        url: "http://127.0.0.1:5000/quiz",
        data: JSON.stringify(payload),
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        success,
        error
    });
}

function success(data) {
    localStorage.setItem('question', data.pergunta);
    localStorage.setItem('a', data.A);
    localStorage.setItem('b', data.B);
    localStorage.setItem('c', data.C);
    localStorage.setItem('d', data.D);
    localStorage.setItem('e', data.E);
    localStorage.setItem('answer', data.resposta);
    window.location.pathname = "game/quiz.html"
}

function error(data) { if (data.status >= 400) window.location.reload() }

document.querySelector('#start').addEventListener('click', pressStart)
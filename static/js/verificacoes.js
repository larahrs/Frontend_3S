// var nome = prompt("como voce chama?")
//
//
// if (nome == null) {
//     alert("recarregue a pagina")
// } else {
//     let correto = confirm("voce se chama " + nome + "?")
//
//
//     if (correto) {
//         alert(nome + " bem vindo ao site de cursos")
//     } else {
//         alert("recarregue a pagina")
//     }
// }

function limpaInputsLogin() {
    const inputEmail = document.getElementById('input-email')
    const inputSenha = document.getElementById('input-senha')

    imputEmail.value = ''
    imputSenha.value = ''
}

document.addEventListener("DOMContentLoaded", function () {
    const formLogin = document.getElementById('form-login')


    formLogin.addEventListener("submit", function (event) {
        // pegar os dois inuputs do formulario
        const inputEmail = document.getElementById('input-email')
        const inputSenha = document.getElementById('input-senha')


        let temErro = false


        // verificar se os inputs estao vazios
        if (inputEmail.value === '') {
            inputEmail.classList.add('is-invalid')
            temErro = true
        } else {
            inputEmail.classList.remove('is-invalid')
        }


        if (inputSenha.value === '') {
            inputSenha.classList.add('is-invalid')
            temErro = true
        } else {
            inputSenha.classList.remove('is-invalid')
        }


        if (temErro) {
            // evita de enviar o formulario
            event.preventDefault()
            alert("preencha todos os campos")
        }


    })


    const formCadastro = document.getElementById('form-cadastro')



        const inputNome = document.getElementById('input-nome')
        const inputDataNascimento = document.getElementById('input-data-nascimento')
        const inputEmail2 = document.getElementById('input-email')
        const inputSenha2 = document.getElementById('input-senha')
        const inputCpf = document.getElementById('input-cpf')
        const inputCargo = document.getElementById('input-cargo')
        const inputSalario = document.getElementById('input-salario')

        if (inputNome.value === '') {
            inputNome.classList.add('is-invalid')
            temErro = true
        } else {
            inputNome.classList.remove('is-invalid')
        }

        if (inputDataNascimento.value === '') {
            inputDataNascimento.classList.add('is-invalid')
            temErro = true
        } else {
            inputDataNascimento.classList.remove('is-invalid')
        }

        if (inputEmail2.value === '') {
            inputEmail2.classList.add('is-invalid')
            temErro = true
        } else {
            inputEmail2.classList.remove('is-invalid')
        }

        if (inputSenha2.value === '') {
            inputSenha2.classList.add('is-invalid')
            temErro = true
        } else {
            inputSenha2.classList.remove('is-invalid')
        }

        if (inputCpf.value === '') {
            inputCpf.classList.add('is-invalid')
            temErro = true
        } else {
            inputCpf.classList.remove('is-invalid')
        }

        if (inputCargo.value === '') {
            inputCargo.classList.add('is-invalid')
            temErro = true
        } else {
            inputCargo.classList.remove('is-invalid')
        }

        if (inputSalario.value === '') {
            inputSalario.classList.add('is-invalid')
            temErro = true
        } else {
            inputSalario.classList.remove('is-invalid')
        }


        imputEmail.value = ''
        imputSenha.value = ''






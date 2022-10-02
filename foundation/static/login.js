const user_name_field = document.querySelector('.user_name')
const password_field = document.querySelector('.password')
const login_button = document.querySelector('.login')

const hashCode = s =>
    s.split('').reduce((a, b) => {
      a = (a << 5) - a + b.charCodeAt(0);
      return a & a;
    }, 0);

window.addEventListener('pywebviewready', () => {
    login_button.addEventListener('click', () => {
        const username = user_name_field.value
        const password_hash = hashCode(password_field.value)
        pywebview.api.login(username, password_hash)
    })
})
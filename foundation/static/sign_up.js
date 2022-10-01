const user_name_field = document.querySelector('.user_name')
const password1_field = document.querySelector('.password1')
const password2_field = document.querySelector('.password2')
const sign_up_button = document.querySelector('.sign_up')

const hashCode = s =>
    s.split('').reduce((a, b) => {
      a = (a << 5) - a + b.charCodeAt(0);
      return a & a;
    }, 0);


const check_passwords = () => {
    res = true
    if(password1_field.value !== password2_field.value){
        res = false
    }else if(password1_field.value.length < 3){
        res = false
    }
    return res
}


window.addEventListener('pywebviewready', () => {
    sign_up_button.addEventListener('click', () => {
        //! check if password fields are matching if not stay in the page
        //! if password fields are matching than proceed
        
        if(check_passwords()){
            const hashed_password = hashCode(password1_field.value)

            // pywebview.api.console_log(user_name_field.value)
            //! if it exists stay in the page and clear username field
            //! if it does not than create the user
            const res = pywebview.api.add_user(user_name_field.value, hashed_password)
            pywebview.api.console_log(res)
            // pywebview.api.console_log(result)
            //! redirect user to login page
        }
    })
})
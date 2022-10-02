const user_name_field = document.querySelector('.username')
const old_password_field = document.querySelector('.old_password')
const password1_field = document.querySelector('.password1')
const password2_field = document.querySelector('.password2')
const change_password_button = document.querySelector('.change_password')



const check_passwords = () => {
    res = true
    if(password1_field.value !== password2_field.value){
        res = false
    }else if(password1_field.value.length < 3){
        res = false
    }
    return res
}

const hashCode = s =>
    s.split('').reduce((a, b) => {
    a = (a << 5) - a + b.charCodeAt(0);
    return a & a;
    }, 0);

//! fill username_field with the help of the url
username = window.location.pathname.split('/')[2]
user_name_field.innerHTML = `${username}`


window.addEventListener('pywebviewready', () => {
    change_password_button.addEventListener('click', () => {
        //! check if password fields are matching if not stay in the page
        //! if password fields are matching than proceed
        if(check_passwords()){
            

            // pywebview.api.console_log(old_password_field.value)
            // const hashed_password = hashCode(old_password_field.value)
            // const new_password_hash = hashCode(password1_field.value)
            // pywebview.api.console_log(hashed_password)
            // pywebview.api.console_log(hashed_password)
            // pywebview.api.console_log(user_name_field.value)
            //! if it exists stay in the page and clear username field
            //! if it does not than create the user
            pywebview.api.change_password(username, hashCode(old_password_field.value), hashCode(password1_field.value))
            
            // pywebview.api.console_log(result)
            //! redirect user to login page
            // window.location.href = "/login";
        }
    })
})
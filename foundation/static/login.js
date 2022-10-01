window.addEventListener('pywebviewready', () => {
//     //! make the checks for user login happen
//     //! if everything is fine than proceed to user_info page
//     // following function expects user name and a password hash
//     // and return a boolean
//     // pywebview.api.create_user()
//     pywebview.api.create_user()

    document.querySelector('.test_button').addEventListener('click', ()=>{
        pywebview.api.create_user()
    })
})

// window.when_ready = () => {
//     document.querySelector('.test_button').addEventListener('click', ()=>{
//         pywebview.api.create_user()
//     })
// }


//when clicked to test button call create user function to test


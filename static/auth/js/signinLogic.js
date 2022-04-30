var buttonSubmit = document.querySelector('#buttonSubmit')

var usernameInput = document.querySelector('#usernameInput')
var emailInput = document.querySelector('#emailInput')
var passwordInput = document.querySelector('#passwordInput')


buttonSubmit.addEventListener('click', function() {
  var formData = new FormData
  formData.append('username', usernameInput.value)
  formData.append('email', emailInput.value)
  formData.append('password', passwordInput.value)
  formData.append('csrfmiddlewaretoken', TOKEN)

  $.ajax({
    type: 'POST',
    url: '/signin_user',
    data: formData,
    dataType: 'json',
    cache: false,
    contentType: false,
    processData: false,
    success: function(response) {
      console.log(response['status'])
      if (response['status'] == 'success') {
        window.location.replace('/home')
      }
    },
  })
})

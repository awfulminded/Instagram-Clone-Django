var updatePic = document.querySelector('#updatePic')

var picInput = document.querySelector('#picInput')



updatePic.addEventListener('click', function() {
  files = picInput.files[0]
  var formData = new FormData
  formData.append('avatar', files)
  formData.append('csrfmiddlewaretoken', TOKEN)
  console.log(files)

  $.ajax({
    type: 'POST',
    url: '/update_pic',
    data: formData,
    dataType: 'json',
    cache: false,
    contentType: false,
    processData: false,
    success: function(response) {
      console.log(response['status'])
      if (response['status'] == 'success') {
        window.location.reload()
      }

    },
    error: function(response) {
      console.log(response['status'])
    },
  }, )
})

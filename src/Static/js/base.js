function read_image(input) {
    if (input.files && input.files[0]) {
      var reader = new FileReader();
  //    img.style.display = 'block';
      reader.onload = function (e) {
        $('#upload_image').attr('src', e.target.result).width(50).height(50);
      };
  
      reader.readAsDataURL(input.files[0]);
    }
  }
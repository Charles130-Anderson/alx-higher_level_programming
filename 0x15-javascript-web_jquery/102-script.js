$(document).ready(function () {
  $('#btn_translate').click(function () {
    let languageCode = $('#language_code').val();
    let url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode;

    $.get(url, function (data) {
      $('#hello').text(data.hello);
    });
  });
});

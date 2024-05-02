$(document).ready(function () {
  $('#btn_translate').click(fetchTranslation);
  $('#language_code').keypress(function (event) {
    if (event.which == 13) {
      fetchTranslation();
    }
  });

  function fetchTranslation() {
    let languageCode = $('#language_code').val();
    let url = 'https://www.fourtonfish.com/hellosalut/hello/?lang=' + languageCode;

    $.get(url, function (data) {
      $('#hello').text(data.hello);
    });
  }
});

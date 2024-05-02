// Append new item to list on button click
$('div#add_item').click(function () {
    let element = '<li>Item</li>';
    $('ul.my_list').append(element);
});

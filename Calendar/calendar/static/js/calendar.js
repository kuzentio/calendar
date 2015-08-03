
var ShowEvents = function(data){
    $('span#event').html('');
    $.each($.parseJSON(data), function(index, element) {
        $.each(element.fields, function(key, value){
            if (key == 'date'){
                $('span#event').append(value+': ')
            }
            if (key == 'text') {
                $('span#event').append(value+'<br>')
            }
            });
        });
    };

function send_event(){
    var data = $('#send_event').serialize();
    $.ajax({
        type: 'POST',
        url: "/add_event/",
        data: data,
        success: function (result) {
            $('div#errors').html('')
            if (result == 'error') {
                $('div#errors').html('Не все поля формы были заполнены правильно.')
            }
            else {
                $.get('events').done(ShowEvents);
                $('#notification').val('');
                $('input#date').val('');
            }
        }
    })
}

$(document).ready(function(){
    $.get('events').done(ShowEvents);

    setTimeout(function(){$.get('events').done(ShowEvents)}, 5000);

    $('#refresh_events').click(function(){
        $.get('events').done(ShowEvents)
    });
});




$(document).on('click',"#sterge", function() {
   event.stopPropagation();
   alert("wesdf");
});

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

/*
 POSTUL VIETII CINE NAIBA M-A PUS SA-L FAC DOAAMNEE
$(document).ready(function() {
 $("#campuri").on('submit',function(event) {
     $('#campuri').hide();
     $('.to_hide').hide();
     $('#formular_edit').show();
    $.ajax({
        url : "/",
        type : "POST",
        data : { 'id': $('#camp_id').val(),
                'obligatii': $('#camp_obligatii').val(),
                'data_incepere': $('#data_incepere').val(),
                'data_expirare': $('#data_expirare').val(),
                'data_platii': $('#data_plata').val(),
                'data_rap_inter': $('#data_rap_inter').val(),
                'data_rap_act': $('#data_rap_act').val(),
                'data_emitere_factura': $('#data_emitere_factura').val(),
                'tip_copie':$('#camp_tip_copie').val(),
                'mod_trimitere':$('#camp_mod_trimitere').val(),
                'semnat':$('#camp_semnat').val()
        },
        success : function(json) {
            //console.log(json);
           // $('#message').html("<h1>" +json.id + json.obligatii + "</h1>");
        },

        error : function(xhr,errmsg,err) {
            $('#message').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>");
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });
    return false;
   });});

*/

function editare(){
     $('.campuri').hide();
     $('.to_hide').hide();
     $('.edit').hide();
     $('.formular_edit').show();
     $('.revine').show();
     $('.edit_for_real').show();

}

function vizualizare(id){
     $('.campuri').show();
     $('.to_hide').show();
     $('.edit').show();
     $('.formular_edit').hide();
     $('.revine').hide();
     $('.edit_for_real').hide();

}

function convert(str){
    var parti=str.split(' ');
    var str3;
    if(parti[1]==='Ianuarie')
        str3='01';
    else
        if(parti[1]==='Februarie')
        str3='02';
     else
        if(parti[1]==='Martie')
        str3='03';
      else
        if(parti[1]==='Aprilie')
        str3='04';
       else
        if(parti[1]==='Mai')
        str3='05';
       else
        if(parti[1]==='Iunie')
        str3='06';
       else
        if(parti[1]==='Iulie')
        str3='07';
         else
        if(parti[1]==='August')
        str3='08';
          else
        if(parti[1]==='Septembrie')
        str3='09';
           else
        if(parti[1]==='Octombrie')
        str3='10';
            else
        if(parti[1]==='Noiembrie')
        str3='11';
             else
        if(parti[1]==='Decembrie')
        str3='12';

    var str2=parti[2]+'-'+str3+'-'+parti[0];
    return str2;
}
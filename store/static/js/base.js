$(function() {
    var path = location.pathname.substring(1);
    $('ul.nav li a').each(function(){
        var link = $(this).attr('href');
        if (link == "/" + path){
            $(this).parent().addClass('active');
        }
   });
});

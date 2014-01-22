$(window).load(function() {
    $('section.projects').collagePlus({
        'targetHeight': 250,
        'allowPartialLastRow': true,   
    });
    $('.projects img').blurjs({
        source: 'body',
        radius: 7,
    });
    $('.flexslider').flexslider({
        animation: "slide"
    });
});

$(document).ready(function(){
});

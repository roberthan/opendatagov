$(function() {
    var data = {};
    var max_count = 200;
    var min_count = 1;
    $.each(window.words, function(idx, word) {
        data[word] = Math.floor(Math.random()*200) + 1;
    });
    var proto_div = "<div class=\"tagword\"></div>";

    function randOrd(){
        return (Math.round(Math.random())-0.5); 
    }

    function logsize(count, min_count, max_count) {

        // The result should be between 100 an 10000000
        var minv = Math.log(12.0);
        var maxv = Math.log(60.0);

        // calculate adjustment factor
        var scale = (maxv-minv) / (max_count-min_count);

        return Math.exp(minv + scale*(count-min_count));
    }

    var parent_div = $(".tagcloud");
    parent_div.hide();

    var words = [];
    $.each(data, function (word, count) {
        var size = logsize(count, min_count, max_count);
        var new_div = $(proto_div);
        new_div.text(word);
        new_div.css("font-size", size+"px");
        var color = (Math.floor(Math.random()*150)).toString(16);
        if (color.length < 2) {
            color = "0"+color;
        }
        new_div.css("color", "#"+color+color+color);
        new_div.attr("data-color", "#"+color+color+color);
        console.log(word, count, color);
        words.push(new_div);
    });
    words.sort(randOrd);

    $.each(words, function(idx, div) {
        parent_div.append(div);
    });

    parent_div.show();

    $('.tagcloud').masonry({
        itemSelector: '.tagword',
        columnWidth: 10,
        isAnimated: true
    });

    $(".tagcloud").on('mouseenter', '.tagword', function(evt) {
        $(this).css("color", "#ee5555");
    });

    $(".tagcloud").on('mouseleave', '.tagword', function(evt) {
        $(this).css("color", $(this).attr("data-color"));
    });

});
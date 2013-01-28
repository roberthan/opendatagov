var searching = false;

var get_tagcloud = function(query){
    searching = true;
    var fixed_query = $.trim(query);
    fixed_query = fixed_query.replace(" ","-")
    var endpoint = "http://data2.me:5000/tagcloud/" + encodeURIComponent(fixed_query);
    console.log("Query: "+query+" url "+endpoint);
    $.getJSON(endpoint, {}, function(data, success, jqXHR) {
        var min_count = 100000000000;
        var max_count = 0;

        // Get rid of old tags
        $("#tagcloud-1").empty();

        $.each(data, function(idx, item) {
            var value = item.count;
            if (value < min_count) min_count = value;
            if (value > max_count) max_count = value; 
        });
        
        var fontSize = d3.scale.linear().range([10, 72]);
        fontSize = fontSize.domain([min_count, max_count]);

        function draw(w) {
            // FIXME: DEBUG
            console.log(w);

            d3.select("#tagcloud-1").append("svg")
                .attr("width", 800)
                .attr("height", 400)
                .append("g")
                .attr("transform", "translate(400,200)")
                .selectAll("text")
                .data(w)
                .enter().append("text")
                .style("font-size", function(d) { return d.size + "px"; })
                .style("font-family", "Lato")
                // FIXME: Debug?
                .style("fill",function(d){return '#'+Math.floor(Math.random()*16777215).toString(16);})
                .attr("text-anchor", "middle")
                .attr("transform", function(d) {
                    return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
                }).text(function(d){return d.text;})
                .classed("tagword", true);

            $(".tagword").on("click", function(e) {
                var text = $.trim($(this).text());
                $("#search-box").val(text);
                // FIXME add loading animation
                if (searching) {
                    return;
                }
                get_tagcloud(text);
            });

            $(".tagword").hover(function(e) {
                $(this).attr("data-fill", $(this).css("fill"));
                $(this).css("fill", "#e33");
            }, function(e) {
                $(this).css("fill", $(this).attr("data-fill"));
            });
        }

        var layout = d3.layout.cloud()
                .size([800, 400])
                .words(data.map(function(d) {
                    return {text: " "+d._id+" ", size: d.count};
                }))
                .timeInterval(Infinity)
                .font("Impact")
                .text(function(d) { return d.text; })
                .fontSize(function(d) { return fontSize(+d.size) })
                .rotate(function(d) { return 0;}) //~~(Math.random() * 5) * 30 - 60; })
                .on("end", draw)
                .start();
    });

    searching = false;
}

$(function() {
    get_tagcloud("");

    $('#search-box').keypress(function (e) {
        if (searching) {
            return;
        }
        if (e.which == 13) {
            var text = $(this).val();
            console.log("searched for: "+text);
            // FIXME add loading animation
            get_tagcloud(text);
        }
    });
});

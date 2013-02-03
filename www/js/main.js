var searching = false;

var get_tagcloud = function(query){
    searching = true;
    $("#loading-image").show();

    var fixed_query = $.trim(query);
    fixed_query = fixed_query.replace(/ /g,"-")
    var endpoint = "http://data2.me:5000/tagcloud/" + encodeURIComponent(fixed_query);
    
    populate_search(query);

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
        var textColor = d3.scale.category10();
        fontSize = fontSize.domain([min_count, max_count]);

        function draw(w) {
            // FIXME: DEBUG
            

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
                .style("fill",function(d){
                    //console.log(d);
                    return textColor(d.text.toLowerCase());
                })
                .attr("text-anchor", "middle")
                .attr("transform", function(d) {
                    return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
                }).text(function(d){return d.text;})
                .classed("tagword", true);

            $(".tagword").on("click", function(e) {
                var text = $.trim($(this).text());
                var old_val = $.trim($("#search-box").val())

                if (searching) {
                    return;
                }
 
                $("#search-box").val(old_val + " " + text);
                get_tagcloud(old_val +" "+text);
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
                .font("Lato")
                .padding(1)
                .text(function(d) { return d.text; })
                .fontSize(function(d) { return fontSize(+d.size) })
                .rotate(function(d) { return 0;}) //~~(Math.random() * 5) * 30 - 60; })
                .on("end", draw)
                .start();

        $("#loading-image").hide();

    });

    searching = false;
    
}

var proto_div = "<div class=\"search-result\"></div>"

var populate_search = function(query) {
    var fixed_query = $.trim(query);
    fixed_query = fixed_query.replace(/ /g,"-");

    var endpoint = "http://data2.me:5000/keyword/" + encodeURIComponent(fixed_query);

    window.location.hash = fixed_query;
    
    $(".results .results-list").empty();

    if (fixed_query == "") {
        $(".status-results").show();
        $(".results .no-results").show();
        $(".results .loading").hide();
        $(".number-results").text("a lot of");
        $(".data-gov-search").text("");
        return;
    }

    $(".status-results").show();
    $(".results .no-results").hide();
    $(".results .loading").show();

    $.getJSON(endpoint, {}, function(data, success, jqXHR) {
        
        $(".results .loading").hide();
        if (data.results.length == 0) {
            $(".results .no-results").show();
        }
        $(".status-results").hide();
        $(".results .no-results").hide();

        var target_div = $(".results .results-list")

        $.each(data.results, function(idx, d) {
            var new_div = $(proto_div);
            var new_link = $("<a  target=\"_blank\"></a>");
            
            new_link.attr("href",d.url);
            new_link.text(d.name);

            new_div.append(new_link);

            target_div.append(new_div);
        });

        $(".number-results").text(data.meta.count);
        //console.log(query);
        var data_gov_url = "https://explore.data.gov/catalog/raw?sortBy=relevance&q=" + encodeURIComponent(query);

        $(".data-gov-search").attr("href",data_gov_url);
        if (data.meta.count == 0) {
            $(".data-gov-search").text("Maybe data.gov's search is better than ours?");
        } else{
            $(".data-gov-search").text("See more on data.gov.");
        }
    });

}

$(function() {
    if(window.location.hash) {
        get_tagcloud(window.location.hash.replace('#',''));
        $("#search-box").val(window.location.hash.replace('#','').replace(/-/g,' '));
    }
    else{
        get_tagcloud("");
    }

    $('#search-box').keypress(function (e) {
        if (searching) {
            return;
        }
        if (e.which == 13) {
            var text = $(this).val();
            // FIXME add loading animation
            get_tagcloud(text);
        }
    });

    $(".about_btn").on("click", function(e) {
        if ($(".about_container").is(":hidden")) {
            $(".about_container").slideDown();
            $(this).text("(hide)");
        } else {
            $(".about_container").slideUp();
            $(this).text("(learn more)");
        }
        e.preventDefault();
    });
});

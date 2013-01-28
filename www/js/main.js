$(function() {
    var endpoint = "http://data2.me:5000/tagcloud/";
    $.getJSON(endpoint, {}, function(data, success, jqXHR) {
        var min_count = 100000000000;
        var max_count = 0;
        $.each(data, function(idx, item) {
            var value = item.count;
            if (value < min_count) min_count = value;
            if (value > max_count) max_count = value; 
        });
        
        var fontSize = d3.scale.log().range([10, 72]);
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
                .style("font-family", "Impact")
                .attr("text-anchor", "middle")
                .attr("transform", function(d) {
                    return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
                }).text(function(d){return d.text;}).classed("energy", true);
        }

        var layout = d3.layout.cloud()
                .size([800, 400])
                .words(data.map(function(d) {
                    return {text: d._id, size: d.count};
                }))
                .timeInterval(10)
                .text(function(d) { return d.text; })
                .font("Impact")
                .fontSize(function(d) { return fontSize(+d.size) })
                .rotate(function(d) { return 0;}) //~~(Math.random() * 5) * 30 - 60; })
                .padding(1)
                .on("end", draw)
                .start();
    });

});
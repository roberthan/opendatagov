$(function() {
    var data = {};
    var max_count = 200;
    var min_count = 1;
    $.each(window.words, function(idx, word) {
        data[word] = Math.floor(Math.random()*200) + 1;
    });
    
    var fontSize = d3.scale.log().range([10, 100]);
    fontSize = fontSize.domain([min_count, max_count]);

    function draw(w) {
        console.log(w);
        d3.select("#tagcloud-1").append("svg")
            .attr("width", 960)
            .attr("height", 600)
            .append("g")
            .attr("transform", "translate(480,300)")
            .selectAll("text")
            .data(w)
            .enter().append("text")
            .style("font-size", function(d) { return d.size + "px"; })
            .style("font-family", "Impact")
            .style("fill", function(d, i) { return "red"; })
            .attr("text-anchor", "middle")
            .attr("transform", function(d) {
                return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
            }).text(function(d){return d.text;});
    }

    var layout = d3.layout.cloud()
            .size([960, 600])
            .words(window.words.map(function(d) {
                return {text: d, size: data[d]};
            }))
            .timeInterval(10)
            .text(function(d) { return d.text; })
            .font("Impact")
            .fontSize(function(d) { return fontSize(+d.size) })
            .rotate(function(d) { return ~~(Math.random() * 5) * 30 - 60; })
            .padding(1)
            .on("end", draw)
            .start();

});
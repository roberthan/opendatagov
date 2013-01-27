// Setup.
clearResults();
Session.set('searchstate', 'initial')

if (Meteor.is_client) {

  Template.search.results = function () {
    return Session.get('results');
  };

  Template.search.searchstate = function () {
    // 'initial', 'searching', or 'complete'
    return Session.get('searchstate');
  };
  
  Template.search.lastquery = function () {
    return Session.get('lastquery');
  };  
  
  Template.search.events = {
    'click button.searchgo': doSearch,
    'keyup input.searchstring': function(e) {
      if (e.keyIdentifier == 'Enter') doSearch();
    }
  };

  Template.meta.searchstate = function () {
    // 'initial', 'searching', or 'complete'
    return Session.get('searchstate');
  };
  
  Template.meta.results = function () {
    return Session.get('results');
  };
}

// On server startup, create some results if the database is empty.
if (Meteor.is_server) {
  Meteor.startup(function () {
    clearResults();
  });
}

function clearResults() {
  Session.set('results', []);
}

function doSearch() {
  Session.set('searchstate', 'searching');
  var queryString = $('input.searchstring').val().trim();
	var url = 'http://explore.data.gov/api/views/pyv4-fkgv/rows.json?' +
	    'jsonp=?&max_rows=10&search=' + queryString;
	$.getJSON(url, searchCallback);
	Session.set('lastquery', queryString);
}

function searchCallback(result) {
  clearResults();
  var results = [];
  
  // For debugging: output all column names.
  // $.each(result.meta.view.columns, function(index, columnObj) {
  //   console.log(index, columnObj.fieldName);
  // });
  
  $.each(result.data, function(index, rawResult) {
    var result = convertResult(rawResult);
    result.sessionId = Session.get('id');
    results.push(result);
  });
  Session.set('results', results);
  Session.set('searchstate', 'complete');
}

function convertResult(rawResult) {
  var url = rawResult[10][0];
  if (url.indexOf('http') != 0) {
    url = 'http://explore.data.gov/' + url;
  }
  var result = {
    title: rawResult[10][1],
    url: url,
    description: rawResult[11]
  };
  if (rawResult[19]) result.agency = rawResult[19];
  if (rawResult[20]) result.subagency = rawResult[20];
  return result;
}
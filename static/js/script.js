// deal with an "Add Item" button click
$(function() {
  $("#add").on("click", function() {
    var description = $("#todo_input").val();
    $.ajax({
      url: "/add",
      type: "POST",
      data: JSON.stringify({"description": description}),
      contentType: "application/json; charset=utf-8",
      dataType: "json",
      success: reloadList,
      failure: function() { console.log("failure"); }
    });
  });
});

var reloadList = function() {
  var container = $("#task-list");
  container.empty();
  $.get("/list", function(data) {
    $.each(data.items, function (index, value) {
      var checked = "";
      if (value.status) { checked = "checked "; }
      var itemString = '<li class="todo-item" ' + 'id="' + value.id
      + '"><input type="checkbox" value="" ' + checked + '/> '
      + value.description + '<button class="btn btn-default remove-button" '
      + 'id="'  + value.id
      +'"><span class="glyphicon glyphicon-remove"></span></button>' + '</li>';
      var item = $.parseHTML(itemString);
      container.append(item);
    });
  });
};

$(window).load(reloadList);

var deleteItem = function(url, data, callback, type) {
   return  $.ajax({
        url: url,
        type: "DELETE",
        data: data,
        contentType: type
    });
};

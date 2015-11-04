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
      success: function() { console.log("success"); },
      failure: function() { console.log("failure"); }
    });
  });
});

var reloadList = function() {
};

$.delete = function(url, data, callback, type) {
   return  $.ajax({
        url: url,
        type: "DELETE",
        data: data,
        contentType: type
    });
}

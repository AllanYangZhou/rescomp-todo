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

$(function() {
    $("a").on("click", function() {
        var id = $(this).parent().attr("id")
        $.ajax({
            url: "/delete",
            type: "DELETE",
            data: JSON.stringify({"id": id}),
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function() { console.log("success"); },
            failure: function() { console.log("failure"); }
        });
    });
});

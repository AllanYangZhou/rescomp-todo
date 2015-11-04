// deal with an "Add Item" button click
$(function() {
  $("add").on("click", function() {
    var description = $("#todo_input").val();
    $.post("/add", { "description": description },
      function(data) {
        console.log("Success");
      });
  });
});

var reloadList = function() {
};

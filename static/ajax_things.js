// deal with an "Add Item" button click
$(function() {
  $("add").on("click", function() {
    var todo_item = $("#todo_input").val();
    $.get("callback function",
      {"todo_item": todo_item},
      function(data) {
        // do something with the data returned
      })
  })
})

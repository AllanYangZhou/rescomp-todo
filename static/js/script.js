// deal with an "Add Item" button click
$(function() {
  $("add").on("click", function() {
    var description = $("#todo_input").val();
    // $.post("/add", { "description": description },
    //   function(data) {
    //     console.log("Success");
    //   });
    $.ajax({
        url: "/add",
        type: "post",
        dataType: "json",
        success: function (data) {
            console.log("Success");
        },
        data: {"description": description}
    });
  });
});

var reloadList = function() {
};

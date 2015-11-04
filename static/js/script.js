// On page load
$(function (){
    $("#error-box").hide();
    reloadList();
});

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
      timeout: 2000,
      success: function() {
          reloadList();
          clearErrorBox();
          console.log("Successfully added item: " + description);
      },
      error: function(e, msg, type) {
          message = "Failed to add item '"+description+"' - "+msg
          addError(message)
          console.log(message);
      }
    });
  });
});

function addError(msg) {
    $("#error-box").append(msg);
    $("#error-box").show();
}

function clearErrorBox() {
    $("#error-box").hide();
    $("#error-box").html("");
}

function reloadList() {
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
    removeHandler();
  });
}

function deleteItem(url, data, callback, type) {
   return  $.ajax({
        url: url,
        type: "DELETE",
        data: data,
        contentType: type
    });
}

function removeHandler() {
    $(".remove-button").on("click", function() {
        var id = this.id;
        $.ajax({
            url: "/delete",
            type: "DELETE",
            data: JSON.stringify({"id": id}),
            contentType: "application/json; charset=utf-8",
            dataType: "html",
            success: reloadList,
            failure: function() { console.log("failure"); }
        });
    });
}

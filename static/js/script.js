// On page load
$(function (){
    $("#error-box").hide();
    reloadList();
});

//update
function updateItem() {
    $("li").find("input").on("click", function() {
        var id = this.parentNode.id;
        var status = this.checked ? 1 : 0;
        $.ajax({
            url: "/update",
            type: "POST",
            data: JSON.stringify({"id": id, "status": status}),
            contentType: "application/json; charset=utf-8",
            dataType: "html",
            timeout: 2000,
            success: function() {
                reloadList();
                clearErrorBox();
                console.log("Successfully update item: " + id);
            },
            error: function(e, msg, type) {
                message = "Failed to update item '"+id+"' - "+msg
                addError(message)
                console.log(message);
            }
        })
    });
}

// deal with an "Add Item" button click
$(function() {
  $("#add").on("click", function() {
    var description = $("#todo_input").val();
    $.ajax({
      url: "/add",
      type: "POST",
      data: JSON.stringify({"description": description}),
      contentType: "application/json; charset=utf-8",
      dataType: "",
      timeout: 2000,
      success: function() {
          reloadList();
          clearErrorBox();
          console.log("Successfully added item: " + description);
          $("#todo_input").val("");
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
    $.each(data.items, function (index, item) {
      var li = $("<li/>").attr("id", item.id).addClass("todo-item");
      var checkbox = $("<input/>").attr("type", "checkbox");
      var del = $("<button/>").addClass("btn btn-default remove-button");
      var glyph = $("<span/>").addClass("glyphicon glyphicon-remove");
      del.append(glyph);
      var descr = $("<div/>").addClass("description").html(item.description);
      if (item.status) {
        checkbox.attr("checked", "checked");
        descr.css("text-decoration", "line-through");
      }
      li.append(checkbox);
      li.append(descr);
      li.append(del);
      container.append(li);
    });
    removeHandler();
    updateItem();
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
        var id = this.parentNode.id;
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

$(document).bind('keypress', '#add', function(args) {
  if (args.keyCode == 13) {
    $('#add').click();
  }
});

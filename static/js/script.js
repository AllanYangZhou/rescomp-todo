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
            url: "", // PUT ITEM URL HERE
            type: "POST",
            data: "", // REPLACE WITH NECESSARY DATA FOR SERVER
            contentType: "application/json; charset=utf-8",
            dataType: "html",
            timeout: 2000,
            success: function() {
              // WRITE WHAT TO DO WHEN THE REQUEST IS SUCCESSFUL
            },
            error: function(e, msg, type) {
                message = "Failed to update item '"+id+"': "+msg
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
      url: "", // PUT ITEM ADD URL HERE
      type: "POST",
      data: "", // REPLACE WITH NECESSARY DATA FOR SERVER
      contentType: "application/json; charset=utf-8",
      dataType: "",
      timeout: 2000,
      success: function() {
        // WRITE WHAT TO DO WHEN THE REQUEST IS SUCCESSFUL
      },
      error: function(e, msg, type) {
          message = "Failed to add item '"+description+"': "+msg
          addError(message)
          console.log(message);
      }
    });
  });
});

function addError(msg) {
    item = $("<p/>").html(msg);
    $("#error-box").append(item);
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

function removeHandler() {
    $(".remove-button").on("click", function() {
        var id = this.parentNode.id;
        $.ajax({
            url: "", // PUT DELETE URL HERE
            type: "DELETE",
            data: "", // REPLACE WITH NECESSARY DATA FOR SERVER
            contentType: "application/json; charset=utf-8",
            dataType: "html",
            success: function() {
              // WRITE WHAT TO DO IF THE REQUEST IS SUCCESSFUL
            },
            error: function(e, msg, type) {
                message = "Failed to remove item '"+id+"': "+msg
                addError(message)
                console.log(message);
            }
        });
    });
}

$(document).bind('keypress', '#add', function(args) {
  if (args.keyCode == 13) {
    $('#add').click();
  }
});

$(document).ready(function(){
    $('#table').DataTable();
});
$(".edit_student").click(function(){
    var edit_id=$(this).attr("data-id");
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    $.ajax({
        headers: {'X-CSRFToken': csrftoken},
        url: edit_student_url,
        type: "POST",
        data: {
            id: edit_id
        },
        success: function (response) 
        {
            // console.log(result);
            var instance = JSON.parse(response["instance"]);
            var fields = instance[0]["fields"];
            console.log(fields)
            $("#student_id_div").html("<input type='hidden' name='student_id' id='student_id' value='"+edit_id+"'>");
            $("#fullname").val(fields["fullname"]);
            $("#roll_no").val(fields["roll_no"]);
            $("#mobile").val(fields["mobile"]);
            var section_id=fields["section_id"]
            $("#section_id option[value='" + section_id + "']").attr("selected","selected");
            $("#add_student_model").modal("show");
        }
    });

});
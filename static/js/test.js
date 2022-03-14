// function new_post() {
//     alert('실패했습니다!');
// }

// function name_push() {
//     alert('실패했습니다!');
//     let aa = $('#name_load').text()
//     $('#username').val(aa)
//
// }

function create_comment_test(){
    var body = $("#comment").val();
    $.ajax({
        type: "POST",
        url: "/diary_main/createComment/",
        data: {
            board_id: $('#post_id').text(),
            comment_author: $('#c_name').val(),
            comment_content: $('#c_content').val()
        },
        dataType: 'json',
        success: function (response){
            console.log(response.message)
            $("#comment").append()
        }
    })
}


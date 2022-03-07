
function username_check(){

    $('#username').change(function () {
        $('#username').attr("check_result", "fail");
      })

    let username = $("#username").val();

    $.ajax({
        url: '/do_duplicate_check',
        data: {'username': username},
        datatype: 'json',

        success: function (data) {

          // 중복 있음
          if (data['duplicate'] == "fail") {
              alert("이미 존재하는 아이디입니다.")
            return;

          } else { // 중복 없음
            alert("사용 가능한 아이디 입니다.")
            return ;
          }
        }
      });

}
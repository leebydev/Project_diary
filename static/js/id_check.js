
function username_check(){

    let username=$('#username').val()
    console.log(username)

    $.ajax({
        url: 'do_duplicate_check',
        type: 'POST',
        data: { 'username': username },
        datatype: 'json',

        success: function (data) {
            console.log(data['duplicate']);
          // 중복 있음
              if (data['duplicate'] == "fail") {
                  alert("이미 존재하는 아이디입니다.")
                    return false;
              } else { // 중복 없음
                alert("사용 가능한 아이디 입니다.")
                  return;
              }
            },
        error: function(){
            alert('무언가 잘못되었습니다.')
        }
          });

}


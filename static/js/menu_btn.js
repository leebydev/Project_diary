function new_post() {
    document.location.href = '/diary_main/create/'
}
function to_list() {
    document.location.href = '/diary_main/list/'
}

function delete_post() {
    //내가 어떤글을 삭제할지 알아야 함!
    // alert($('#post_id').text())
    let result = confirm("정말 삭제할까요?")
    // confirm 확인을 받기위한 대화창을 띄워줌 (True, False)결과가 떨어짐
    if(result) {
        let queryString = "?post_id=" + $('#post_id').text()
        // "?post_id =6"
        document.location.href = '/diary_main/delete/' + queryString
    }
}

function like_post() {
    let queryString = "?post_id=" + $('#post_id').text()
    document.location.href = '/diary_main/like/' + queryString
}

// 댓글등록하는 AJAX
function create_comment() {
    $.ajax({
        async: true,
        url: "/diary_main/createComment/",
        type: 'GET',
        data: {
            // 댓글에대한 게시글 id, 댓글에대한 작성자, 댓글 내용이 필요
            board_id: $('#post_id').text(),
            comment_author: $('#c_name').val(),
            comment_content: $('#c_content').val()
        },
        dataType: 'json',   // 서버프로그램이 결과로 돌려주는 값은 JSON
        timeout: 3000,
        success: function(result) {
            // 이제 json을통해 데이터를 가져와 화면에 띄워준다.
            // 결과로 오는 result 는 이렇게 생겼고
            //     'c_id': comment.id,
            //     'c_author': comment.c_author,
            //     'c_content': comment.c_content
            // 호면 구성은 이렇게 생김
            // <tr>
            //     <td>{{comment.c_author}}</td>
            //     <td>{{comment.c_content}}</td>
            //     <td>
            //         <button class="btn btn-danger">삭제</button>
            //     </td>
            // </tr>
            // 이거를 수정하자

            let tr = $("<tr></tr>").attr('id','comment_'+ result['c_id']) // tr에 id를 지정해서 삭제시킴
            let autrhor_td = $('<td></td>').text(result['c_author'])
            let content_td = $('<td></td>').text(result['c_content'])
            let btn_td = $('<td></td>')
            // 이 삭제 버튼을 눌렀을 때 삭제 처리를 해야한다.
            let btn = $('<button></button>').text('삭제').addClass('btn btn-danger')
            // btn 이벤트 처리
            btn.on('click',function (){
                // ajax호출해서 서버쪽 댓글 삭제해야함
                $.ajax({
                    // key와 value널어서 삭제해 주자!
                    async: true,
                    url:'/diary_main/commentDelete',
                    type: 'GET',
                    data: {
                        comment_id: result['c_id']
                    },
                    dataType: 'json',
                    timeout: 3000,
                    success: function () {
                        // id를 찾아 지우자
                        $('#comment_'+ result['c_id']).remove()
                        // 이렇게 처리하면 화면에서 지울 수 있다!
                        // 서버쪽에서 처리가 되야지 succes가 처리가 되어 화면이 처리가 될테니
                        // url을 만들러 url.py로 이동하자!
                        // 이경우에 ajax처리를 통해 동적으로 버튼을 추가하여 이미 만들어진 댓글은 삭제 불가!
                        // 즉 새로운 이벤트로 추가된 댓글만 삭제가 됨
                        // 그럼 기존에 있던 댓글은 어떻게 제거하는가?
                    },
                    error: function (){

                    }
                })
            })
            btn_td.append(btn)
            tr.append(autrhor_td)
            tr.append(content_td)
            tr.append(btn_td)
            $('tbody').prepend(tr)
        },
        error: function() {
            alert('먼가 이상해요!')
        }
    })
}


from django.shortcuts import render, redirect, get_object_or_404
from diary_main.models import Board, Comment
from diary_main.forms import BoardForm, BoardDetailForm, BoardUpdateForm
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.http import require_safe

def b_list(request):
    posts = Board.objects.all().order_by('-id')
    context = {
        "posts": posts
    }
    return render(request, 'diary_main/list.html', context)



@require_http_methods(['GET', 'POST'])
def b_create(request):
    # request 방식이 GET인지 POST인지 구분해서 처리
    # 만약 GET 방식이면 빈 입력상자를 출력하고 POST 방식이면
    # 입력된 데이터를 이용해서 Database 처리
    if request.method == 'GET':

        # 새글을 작성할 수 있는 화면을 만들어 클라이언트에게 제공
        # 입력 양식인 ModelForm 객체를 하나 설정
        board_form = BoardForm()

        context = {
            "my_form": board_form
        }

        return render(request, 'diary_main/create.html', context)
    else:
        # POST 방식인 경우에는 이 부분이 수행돼요
        # 클라이언트가 입력상자에 입력한 내용을 가지고 Database 처리를 해요
        board_form = BoardForm(request.POST, request.FILES)  # 클라이언트가 입력한 데이터를 가지고 있는 ModelForm

        if board_form.is_valid():
            board_form.save()
            # BoardForm 안에 있는 데이터를 이용해서 Board class의 객체를 생성
            # 입력받은 값 이외에 테이블의 다른 컬럼의 값을 지정해서 사용하려면
            # new_post = board_form.save(commit=False)  # 실제로 저장되지 않아요. 대신 객체를 리턴해요
            # new_post.b_like_count = 10
            # new_post.save()
            return redirect('diary_main:b_list')


@require_safe
def b_detail(request, board_id):
    # 게시글의 세부내용을 가져와서 화면에 출력해야 해요
    # ModelForm을 이용해서 Database에서 가져온 내용을 화면에 출력

    # 1. board_id를 이용해서 게시글 1개를 가져와야 해요 (객체)
    post = Board.objects.get(pk=board_id)
    # 2. 만들어놓은 BoarDetailForm이라는 ModelForm의 객체를
    #    위에서 만든 Board class의 객체인 post를 이용해서 생성
    board_detail_form = BoardDetailForm(instance=post)
    # 3. 댓글(Comment) 정보도 가져와야 해요
    comments = post.comment_set.all().order_by('-id')

    context = {
        "detail_form": board_detail_form,
        'comments': comments,
        'post': post,
    }

    return render(request, 'diary_main/detail.html', context)




def b_delete(request):
    # QueryString으로 전달된 삭제할 글 번호부터 뽑아요
    post_id = request.GET['post_id']
    post = get_object_or_404(Board, pk=post_id)
    post.delete()

    return redirect('diary_main:b_list')


def b_like(request):
    post_id = request.GET['post_id']
    post = get_object_or_404(Board, pk=post_id)
    post.b_like_count += 1
    board_detail_form = BoardDetailForm(instance=post)
    context = {
        "detail_form": board_detail_form,
        'post': post
    }
    post.save()

    return render(request, 'diary_main/detail.html', context)


def create_comment(request):
    # request 안에 포함된 사용자가 입력한 데이터를 이용해서
    # comment 객체를 생성
    comment = Comment()
    comment.c_author = request.GET['comment_author']
    comment.c_content = request.GET['comment_content']
    comment.board_id = request.GET['board_id']

    comment.save()

    # AJAX로 호출되었기 때문에 그 결과가 JSON으로 나가야해요
    # 따라서 HttpResponse 객체가 아닌 JsonResponce가 나가야 해요
    # JsonResponse(결과 JSON,)
    return JsonResponse({
        'c_id': comment.id,
        'c_author': comment.c_author,
        'c_content': comment.c_content
    },
        json_dumps_params={'ensure_ascii': True})


def comment_delete(request):
    comment = get_object_or_404(Comment, pk=request.GET['comment_id'])
    comment.delete()
    return JsonResponse({}, json_dumps_params={'ensure_ascii': True})


def b_update(request, board_id):
    post = get_object_or_404(Board, pk=board_id)
    if request.method == 'GET':

        board_update_form = BoardUpdateForm(instance=post)

        comments = post.comment_set.all().order_by('-id')

        context = {
            "detail_update_form": board_update_form,
            'comments': comments,
            'post':post
        }

        return render(request, 'diary_main/update.html', context)

    else:
        post.b_title = request.POST['b_title']
        post.b_content = request.POST['b_content']
        post.b_map = request.POST['b_map']
        post.save()
        return redirect('/diary_main/'+ str(post.id)+'/detail/')
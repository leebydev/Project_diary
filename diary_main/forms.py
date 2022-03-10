# ModelForm class를 여기에 작성

# ModelForm class를 만드려면 Django가 제공해주는 기능(class)를
# 이용해야 해요. (class를 상속받아서 작성해야 해요)

from django import forms
from diary_main.models import *



class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        #fields = "__all__"
        fields = ['b_title', 'b_img', 'b_author', 'b_content','b_map']
        #
        labels = {
            'b_title': '글 제목',
            'b_img': '이미지',
            'b_author': '',
            'b_content': '글 내용',
            'b_map': '지도입력'
        }
        #
        widgets = {
            'b_title': forms.TextInput(
                attrs={
                    'class': 'form-control w-50',
                    'placeholder': '제목을 입력하세요!'
                }
            ),
            'b_author': forms.TextInput(
                attrs={
                    'hidden class': 'form-control w-25',
                    # 'placeholder': '작성자를 입력하세요!'
                    'id': 'username'
                }
            ),
            'b_content': forms.Textarea(
                attrs={
                    'class': 'form-control w-75',
                    'placeholder': '글 내용을 입력하세요!',
                    'onblur': 'name_push()'
                }
            ),
            'b_map':forms.TextInput(
                attrs={
                    'placeholder': '주소를 입력하세요!',
                    'id':'map_name',
                    'onblur': 'focus_out()'

                }
            )# Textarea() : 여러 줄짜리 입력상자
        }


class BoardDetailForm(forms.ModelForm):
    class Meta:
        model = Board
        # fields = '__all__'
        fields= ['b_title','b_content','b_author']
        labels = {
                    'b_title': '글 제목',
                    # 'b_img': '이미지',
                    'b_author': '글 작성자',
                    'b_content': '글 내용',
                    # 'b_comment_count': '댓글 개수',
                    # 'b_like_count': '좋아요 개수'
                }

        widgets = {
            'b_title': forms.TextInput(
                attrs={
                    'readonly class': 'form-control-plaintext w-75',
                    'disabled':'readonly'

                }
            ),
            # 'b_img': forms.TextInput(
            #     attrs={
            #         'class': 'form-control w-25'
            #     }
            # ),
            'b_author': forms.TextInput(
                attrs={
                    'readonly class': 'form-control-plaintext w-25',
                    'disabled':'readonly'
                }
            ),
            'b_content': forms.Textarea(
                attrs={
                    'readonly class': 'form-control-plaintext w-100',
                    'disabled':'readonly'
                }
            ),
            # 'b_comment_count': forms.TextInput(
            #     attrs={
            #         'class': 'form-control w-25'
            #     }
            # ),
            # 'b_like_count': forms.TextInput(
            #     attrs={
            #         'class': 'form-control w-25'
            #     }
            # )
        }


class BoardUpdateForm(forms.ModelForm):
    class Meta:
        model = Board
        # fields = '__all__'
        fields= ['b_title','b_content','b_map']
        labels = {
            'b_title': '글 제목',
            # 'b_img': '이미지',
            'b_map':'지도',
            'b_content': '글 내용',
            # 'b_comment_count': '댓글 개수',
            # 'b_like_count': '좋아요 개수'
        }

        widgets = {
            'b_title': forms.TextInput(
                attrs={
                    'class': 'form-control w-75',


                }
            ),
            # 'b_img': forms.TextInput(
            #     attrs={
            #         'class': 'form-control w-25'
            #     }
            # ),
            'b_content': forms.Textarea(
                attrs={
                    'class': 'form-control w-100',

                }
            ),
            # 'b_comment_count': forms.TextInput(
            #     attrs={
            #         'class': 'form-control w-25'
            #     }
            # ),
            # 'b_like_count': forms.TextInput(
            #     attrs={
            #         'class': 'form-control w-25'
            #     }
            # )
            'b_map':forms.TextInput(
                attrs={
                    'class': 'form-control w-100',
                    'id':'map_name',
                    'onblur': 'focus_out()'
                }
            )

        }



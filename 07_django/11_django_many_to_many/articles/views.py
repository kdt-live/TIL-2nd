from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = article.comment_set.all()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@login_required
def delete(request, artilce_pk):
    article = Article.objects.get(pk=artilce_pk)
    if request.user == article.user:
        article.delete()
    return redirect('articles:index')


@login_required
def update(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.user == article.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, instance=article)
            if form.is_valid():
                form.save()
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    else:
        return redirect('articles:index')
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)


@login_required
def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        return redirect('articles:detail', article.pk)
    context = {
        'article': article,
        'comment_form': comment_form,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def comment_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)

    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', article_pk)


def likes(request, article_pk):
    # 좋아요를 누르는 대상 게시글
    article = Article.objects.get(pk=article_pk)

    # 좋아요 관계를 추가 or 삭제
    # case1. 현재 좋아요를 요청하는 유저가 해당 게시글의 좋아요를 누른 유저 목록에 있는지 없는지를 확인
    if request.user in article.like_users.all():
    # case2. 해당 게시글의 좋아요를 누른 유저에서 현재 요청하는 유저의 존재를 조회
    # if article.like_users.filter(pk=request.user.pk).exists():
        # 좋아요 취소
        article.like_users.remove(request.user)
        # request.user.like_articles.remove(article)
    else:
        # 좋아요 추가
        article.like_users.add(request.user)
        # request.user.like_articles.add(article)
    return redirect('articles:index')





    # 한번 누르면 추가, 두번 누르면 삭제 -> 3번쨰부터는??
    # 체크박스? 좋아요를 누를때 체크박스?? -> 하트
    # 게시글에 좋아요를 누른 모든 유저
    article.like_users.all()
    # 지금 좋아요를 요청하는 유저가 저 유저 목록에 있는지 없는지??

    # 목록에 있으면? => 좋아요 취소
    # 목록에 없으면? => 좋아요 추가

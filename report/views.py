from django.shortcuts import render, redirect
from .models import Category, Post, Comment
from .forms import CommentForm
import json
from django.shortcuts import render
from django.conf import settings

def home_view(request):
    posts = list(Post.objects.all())[-3:]
    context={
        'posts_set':posts,
    }
    return render(request, 'home.html', context)

def detail_bom_view(request, slug, pk):
    #get the specific posts
    post = Post.objects.get(slug=slug, pk=pk)
 
    #initial settings
    model_input="DR"
    new_comment=None
    if request.method == 'POST':
        action=request.POST.get('action')
        if action in ['Dryer', 'Front Loader', 'Top Loader']:
            if action=='Dryer':
                model_input="DR"
            elif action=="Front Loader":
                model_input="FL"
            elif action=="Top Loader":
                model_input="TL"
            comment_form = CommentForm()

        elif action == 'Add Comment':
            comment_form = CommentForm(request.POST, instance=post)  # create new instance with required=False
            if comment_form.is_valid():
                name = request.user.username
                body = comment_form.cleaned_data['comment_body']
                new_comment = Comment(post=post, commenter_name=name, comment_body=body)
                new_comment.save()
                #refresh the page and delete the text
                return redirect('detail_bom_url', slug=post.slug, pk=post.pk) 
            else:
                print('form is invalid')   
    else:
        comment_form = CommentForm()    

    #get graph json data
    week_num=post.title
    graph_json_path=settings.STATICFILES_DIRS[0]+'/json/bom-graph.json'
    with open(graph_json_path,'r') as f:
        data=json.load(f)
    selected_graph=data[week_num][model_input]
    graph_column=selected_graph["columns"]
    graph_value=selected_graph["vs BOM"]
    graph_value1=selected_graph["PO Price Change"]
    graph_value2=selected_graph["Substitute Change"]
    graph_value3=selected_graph["PO + Substitute"]

    #get table trend json data
    table_json_path=settings.STATICFILES_DIRS[0]+'/json/bom-table-trend.json'
    with open(table_json_path,'r') as f:
        json_trend=json.load(f)
    trend_json=json_trend[week_num][model_input]

    #get table item json data
    table_json_path=settings.STATICFILES_DIRS[0]+'/json/bom-table-item.json'
    with open(table_json_path,'r') as f:
        json_item=json.load(f)
    item_json=json_item[week_num][model_input]

    context = {
        'post_detail':post,
        'new_comment': new_comment,
        'form_detail':comment_form,
        'detail_graph_column':json.dumps(graph_column),
        'detail_graph_value':json.dumps(graph_value),
        'detail_graph_value1':json.dumps(graph_value1),
        'detail_graph_value2':json.dumps(graph_value2),
        'detail_graph_value3':json.dumps(graph_value3),
        'trend_table_data':trend_json,
        'item_table_data':item_json,
    }
    return render(request, 'detail-bom.html', context)

def detail_cost_view(request, slug, pk):
    #get the specific posts
    post = Post.objects.get(slug=slug, pk=pk)
 
    #initial settings
    model_input="BPA-DR"
    new_comment=None
    if request.method == 'POST':
        action=request.POST.get('action')
        if action in ['BPA-Dryer', 'BPA-Front Loader', 'BPA-Top Loader', 'PAC-Dryer', 'PAC-Front Loader', 'PAC-Top Loader']:
            if action=='BPA-Dryer':
                model_input="BPA-DR"
            elif action=="BPA-Front Loader":
                model_input="BPA-FL"
            elif action=="BPA-Top Loader":
                model_input="BPA-TL"
            elif action=='PAC-Dryer':
                model_input="PAC-DR"
            elif action=="PAC-Front Loader":
                model_input="PAC-FL"
            elif action=="PAC-Top Loader":
                model_input="PAC-TL"
            comment_form = CommentForm()

        elif action == 'Add Comment':
            comment_form = CommentForm(request.POST, instance=post)  # create new instance with required=False
            if comment_form.is_valid():
                name = request.user.username
                body = comment_form.cleaned_data['comment_body']
                new_comment = Comment(post=post, commenter_name=name, comment_body=body)
                new_comment.save()
                #refresh the page and delete the text
                return redirect('detail_cost_url', slug=post.slug, pk=post.pk) 
            else:
                print('form is invalid')   
    else:
        comment_form = CommentForm()  

    
    #get graph json data
    week_num=post.title
    graph_json_path=settings.STATICFILES_DIRS[0]+'/json/cost-graph.json'
    with open(graph_json_path,'r') as f:
        data=json.load(f)
    selected_graph=data[week_num][model_input]
    graph_column=selected_graph["columns"]
    value1_column=selected_graph["value1"]
    value2_column=selected_graph["value2"]

    #get table trend json data
    table_json_path=settings.STATICFILES_DIRS[0]+'/json/cost-table-trend.json'
    with open(table_json_path,'r') as f:
        json_trend=json.load(f)
    trend_json=json_trend[week_num][model_input]

    #get table item json data
    table_json_path=settings.STATICFILES_DIRS[0]+'/json/cost-table-item.json'
    with open(table_json_path,'r') as f:
        json_item=json.load(f)
    item_json=json_item[week_num][model_input]

    context = {
        'post_detail':post,
        'new_comment': new_comment,
        'form_detail':comment_form,
        'graph_column':json.dumps(graph_column),
        'graph_value1':json.dumps(value1_column),
        'graph_value2':json.dumps(value2_column),
        'trend_table_data':trend_json,
        'item_table_data':item_json,
    }

    return render(request, 'detail-cost.html', context)


def category_bom_view(request, slug):
    category=Category.objects.get(slug=slug)

    context={
        'category_pair':category,
    }
    return render(request,'category-bom.html', context)

def category_cost_view(request, slug):
    category=Category.objects.get(slug=slug)

    context={
        'category_pair':category,
    }
    return render(request,'category-cost.html', context)
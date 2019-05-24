from django.shortcuts import render, redirect, HttpResponse
from .models import User, Post
# Create your views here.
def index(request):
    # TODO: check if username is in session
    # if not "username" in request.session:
    # IF NOT: return index.html
    context = {
        "users": User.objects.all()
    }
    return render(request, "main/index.html", context)

    # print(request.session["username"])
    # # IF SO: redirect to dashboard page
    # return redirect("/dashboard")

def show(request, user_id):
    context = {
        # SELECT * FROM users WHERE id = user_id
        "user": User.objects.get(id=user_id)
    }
    return render(request, "main/show.html", context)

def register(request):
    if request.method == "POST":
        # request.POST is like request.form (flask)
        # ready to add a user
        # User.objects.create(field1 = ..., field2 = ...)
        User.objects.create(username=request.POST["username"], email=request.POST["email"], password=request.POST["password"])

        request.session["username"] = request.POST["username"]
        print(request.POST)

    return redirect("/")

def login(request):
    if request.method == "POST":
        request.session["user_id"] = request.POST["user_id"]
        return redirect("/dashboard")

def dashboard(request):
    # is there a "user_id" in session?
    if not "user_id" in request.session:
        return redirect("/")
    user = User.objects.get(id=request.session["user_id"])
    context = {
        "user": user,
        # SELECT * FROM posts...
        "liked_posts": Post.objects.filter(likes__id=user.id),
        "unliked_posts": Post.objects.exclude(likes__id=user.id),
    }
    return render(request, "main/dashboard.html", context)

def like(request, post_id):
    print(post_id)
    # TODO: Query for user in session
    user = User.objects.get(id=request.session["user_id"])
    # TODO: Query for post with post_id
    post = Post.objects.get(id=post_id)

    # adding user to post's likes
    post.likes.add(user)

    return redirect("/dashboard")
    	


def newpost(request):
    if request.method == "POST":
        # create a new post!
        # request.POST["topic"] # is the topic
        # request.POST["content"] # is the content
        # author must be queried, from User, with session["user_id"]
        author = User.objects.get(id=request.session["user_id"]) # is the author id
        Post.objects.create(topic=request.POST["topic"], content=request.POST["content"], author=author)
        return redirect("/dashboard")

def show_post(request, post_id):

    post = Post.objects.get(id=post_id)
    context = {
        "post": post
    }
    return render(request, "main/show_post.html", context)

def logout(request):
    # when we get here
    # remove "username" from session
    request.session.clear()
    return redirect("/")
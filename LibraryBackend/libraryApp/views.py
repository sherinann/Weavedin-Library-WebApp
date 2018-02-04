from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import book
from .models import author_info
from django.shortcuts import redirect

#gives all data about books
def books(request):
    info=book.objects.all()
    author_info1=author_info.objects.all()
    return render(request,'books_all.html',{'info':info,'ainfo':author_info1})

#gives data from the author_info model
def authors(request):
    info = author_info.objects.all()
    return render(request, 'authors_all.html', {'info': info})

#details of author
def author_description(request,id):
    template = loader.get_template('author_desc.html')
    info=author_info.objects.filter(id=id)
    print(info)
    for item in info:
        info_book=book.objects.filter(author=item.name)
        print(info_book)
        return HttpResponse(template.render({'info':info,'info_book':info_book}))

#details of book
def book_description(request,isbn_no):
    template = loader.get_template('book_desc.html')
    info=book.objects.filter(isbn_no=isbn_no)
    return HttpResponse(template.render({'info':info}))

#to add a new book into database
def addBook(request):
    if request.method=="POST":
        name=request.POST['bname']
        author=request.POST['author']
        isbn_no = request.POST['isbnNo']
        description = request.POST['textarea1']
        if book.objects.filter(isbn_no=isbn_no).exists():
            pass
        else:
            new=book(name=name,author=author,isbn_no=isbn_no,description=description)
            new.save()
    return redirect('/')

#to add a new author into database
def addAuthor(request):
    if request.method=="POST":
        name=request.POST['aname']
        age=request.POST['age']
        gender = request.POST['gender']
        pob = request.POST['pob']
        if author_info.objects.filter(name=name).exists():
            pass
        else:
            new=author_info(name=name,age=age,gender=gender,pob=pob)
            new.save()
    return redirect('authors')

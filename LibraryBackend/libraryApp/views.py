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
    info_author=author_info.objects.all().values('name')
    print(info_author)
    return render(request,'books_all.html',{'info':info,'ainfo':info_author})

#gives data from the author_info model
def authors(request):
    info = author_info.objects.all()
    return render(request, 'authors_all.html', {'info': info})

#details of author
def author_description(request,id):
    template = loader.get_template('author_desc.html')
    info=author_info.objects.filter(id=id)
   # print(info)
    for item in info:
        info_book=book.objects.all().filter(author=item.name)
        return HttpResponse(template.render({'info':info,'info_book':info_book}))

#details of book
def book_description(request,isbn_no):
    template = loader.get_template('book_desc.html')
    info=book.objects.filter(isbn_no=isbn_no).values('name','author','description')
    print(info)
    for item in info:
        print(item)
        print(item['author'])
        info_author=author_info.objects.filter(name=item['author']).values('name','id')
        print('hey', info_author)
        return HttpResponse(template.render({'info':info,'info_author':info_author}))

#to add a new book into database
def addBook(request):
    print('in')
    if request.method=="POST":
        name=request.POST['bname']
        author=request.POST.get('author_name')
        print(author)
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

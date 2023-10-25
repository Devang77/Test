from django.shortcuts import render
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
import datetime
from datetime import timedelta
from django.contrib import messages

# Create your views here.
def frontend(request):
    return render(request,'Frontend.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'Booklist.html', {'books': books})

def book_detail(request, pk):
    
    book = Book.objects.get(pk=pk)
    return render(request, 'BookDetails.html', {'book': book})

def member_list(request):
    members = Member.objects.all()
    return render(request, 'MemberList.html', {'members': members})

def member_detail(request, pk):
    member = Member.objects.get(pk=pk)
    return render(request, 'MemberDeatils.html', {'member': member})

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'TransactionList.html', {'transactions': transactions})
def transaction_detail(request, transaction_id):
    transaction = get_object_or_404(Transaction, pk=transaction_id)
    return render(request, 'TransactionDetails.html', {'transaction': transaction})
def issue_book(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id")
        member_id = request.POST.get("member_id")

        # Get the book and member from the database
        book = get_object_or_404(Book, pk=book_id)
        member = get_object_or_404(Member, pk=member_id)

        # Check if the book is available
        if book.stock > 0:
            # Create a transaction and update the book's stock
            issue_date=datetime.date.today()
            ISO__issue_date=str(issue_date)
            days=datetime.timedelta(days=14)
            return_date=issue_date + days
            ISO__return_date=str(return_date)
            transaction = Transaction(book=book, member=member, issue_date=ISO__issue_date,return_date=ISO__return_date)
            transaction.save()
            book.stock -= 1
            book.save()

            messages.success(request, f"Book '{book.title}' has been issued to {member.name}.")
        else:
            messages.error(request, f"Book '{book.title}' is out of stock.")
    else:
        # If it's a GET request, display a form to select a book and a member
        books = Book.objects.filter(stock__gt=0)
        members = Member.objects.all()
        return render(request, 'Issue.html', {'books': books, 'members': members})

    return redirect('book-list') 

import graphene
from django.db.models import Q
from graphene_django import DjangoObjectType

from .models import Book


class BookType(DjangoObjectType): 
    class Meta:
        model = Book
        fields = "__all__"    

class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    book = graphene.Field(BookType, book_id=graphene.Int())
    most_popular = graphene.List(BookType)
    books_by_user = graphene.List(BookType, owned_by=graphene.ID())
    search_books = graphene.List(BookType, query=graphene.String())

    def resolve_all_books(self, info, **kwargs):
        return Book.objects.all()

    def resolve_book(self, info, book_id):
        return Book.objects.get(pk=book_id)

    def resolve_most_popular(self, info, **kwargs):
        return Book.objects.all().order_by('-times_purchased')

    def resolve_books_by_user(self, info, owned_by= None, **kwargs):
       if owned_by:            
            return Book.objects.filter(owned_by__id=owned_by)    

    def resolve_search_books(self, info, query=None, **kwargs):
        if query:
            return Book.objects.filter(Q(title__icontains=query) | Q(author__name__icontains=query)
)


schema = graphene.Schema(query=Query)

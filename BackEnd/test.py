from rest_framework.test import APIRequestFactory
from test import TestCase
from . views import AuthorListCreateView, AuthorRetrieveUpdateDestroyView, BookListCreateView, BookRetrieveUpdateDestroyView
from . models import Author, Book


class ApiTest_Author(TestCase):
    """
        Test if the author APIView is able to manage diferent HTTP methods and cases.
    """
    
    def setUp(self):
        self.factory = APIRequestFactory()
        
        authors_to_add = (
            ['Pablo', 'Neruda', 'Colombia'],
            ['Alinna', 'Schutz', 'Austria'],
            ['Geovanna', 'Prokarovzka', 'Russia'],
            ['Michael', 'Hudson', 'United States of America'],
        )
        
        for author_data in authors_to_add:
            author = Author.objects.create(first_name=author_data[0], last_name=author_data[1], country=author_data[2])
            author.save()
            
    def test_get_list(self):
        """
            Testing if API can get the list of Authors
        """
        
        # Create a mock get request to get list of authors from api endpoint
        request = self.factory.get('/api/author/', format = 'json')
        
        response = AuthorListCreateView.as_view()(request)
        
        self.assertEqual(response.status_code, 200)
        print(f"\n[Done] API Author endpoint can retrieve authors list: {response.data}\n")
    
    def test_post(self):
        """
            Testing POST method for Author
        """
        
        # Create a mock post request to author api endpoint
        request = self.factory.post('/api/author/', {'first_name': 'Juaquin', 'last_name': 'Martinez', 'country': 'Mexico'}, format='json')
        
        response = AuthorListCreateView.as_view()(request)
        
        self.assertEqual(response.status_code, 201)
        print("[Done] New author has been created throught the API endpoint.")
        
        
        
        
class ApiTest_Book(TestCase):
    """
        Test if the book APIView is able to manage diferent HTTP methods and cases.
    """
    
    def setUp(self):
        """
            Testing environment configurations, settings, instances, context, etc.
        """
        
        # Mock Author to test the post method for book endpoint
        self.factory = APIRequestFactory()
        self.first_author = Author.objects.create(first_name="Pancho", last_name="Barraza", country="Peru")
        self.first_author.save()
        
        # Create a few authors to test the books
        authors_to_add = (
            ['Pablo', 'Neruda', 'Colombia'],
            ['Alinna', 'Schutz', 'Austria'],
            ['Geovanna', 'Prokarovzka', 'Russia'],
            ['Michael', 'Hudson', 'United States of America'],
        )
        
        self.saved_authors = []
        
        for author_data in authors_to_add:
            author = Author.objects.create(first_name=author_data[0], last_name=author_data[1], country=author_data[2])
            author.save()
            self.saved_authors.append(author)
        
        # Create a few books to test them
        books_to_add = (
            ['Cats and Cats', self.saved_authors[1], 'Comedy', 'The cats are our friends!', 2022],
            ['The Zenith Sword', self.saved_authors[3], 'Action/Drama', 'The mythical Zenith is not discovered yet...', 2019],
            ['Night on the Vineville Lake', self.saved_authors[0], 'Terror', 'A group of friends are struggled in a farmhouse near this evil lake...', 2007],
            ['Do not forget me', self.saved_authors[2], 'Romance/Drama', 'A russian soldier have to fight for his country, but her girl do not want it and miss him every day', 1995]
        )
        
        for book_data in books_to_add:
            book = Book.objects.create(title=book_data[0], author=book_data[1], genre=book_data[2], synopsis=book_data[3], release_date=book_data[4])
            book.save()
    
    def test_retrieve_book(self):
        """
            Testing GET method to retrieve a specific book from the API endpoint
        """
        
        book_1 = Book.objects.create(title="The Super Bird", author=self.saved_authors[3], genre='Action', synopsis='A bird that can shoot to planes!', release_date=2024)
        book_1.save()
        book_2 = Book.objects.create(title="Metal Gear Solid: Snake", author=self.saved_authors[3], genre='Action', synopsis='A soviet soldier that stealths the confident data from an outpost.', release_date=2016)
        book_2.save()
    
        # Create a mock request to book api endpoint
        request = self.factory.get(f'/api/book/{book_2.pk}', format='json')
        
        response = BookRetrieveUpdateDestroyView.as_view()(request, pk=book_2.pk)
        
        self.assertEqual(response.status_code, 200)
        print(f"\n[Done] Book API endpoint can retrieve specific GET requests: {response.data}\n")
            
    def test_get_list(self):
        """
            Testing GET list method for Book model using API endpoint
        """
        
        # Create a mock request to book api endpoint
        request = self.factory.get('/api/book/', format='json')
        
        response = BookListCreateView.as_view()(request)
        
        self.assertEqual(response.status_code, 200)
        
        print(f"\n[Done] API Book endpoint can retrieve books list: {response.data}\n")
        
    def test_post(self):
        """
            Testing POST method for Book
        """
        
        # Create a mock post request to book api endpoint
        request = self.factory.post('/api/book/', {'title': 'The last book', 'author': self.first_author.id, 'genre': 'Drama', 'synopsis': 'This is the last book on the entire world', 'release_date': 2024}, format='json')
        
        response = BookListCreateView.as_view()(request)
        
        self.assertEqual(response.status_code, 201)
        print("[Done] New book has been created throught the API endpoint.")
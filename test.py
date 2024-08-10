from django.test import TestCase
from BackEnd.models import Book, Author
from django.urls import reverse
from django.contrib.auth.models import User

"""Testing methods and functions to do the Unit Testing for the project units (modules, models, methods, classes, etc)"""

# Models testing.
class ModelTest_Book(TestCase):
    """
    Test Book instances, can be created and saved to Book model, the case an instance does not exist, etc.
    
    Methods:
        setUp(self): Set testing environment, instances, variables, etc., to be tested.
        test_model_can_create(self): Test if a Book model instance can be created.
        test_model_instance_doesnotexist(self): Test if it is possible to raise an exception when a requested instance does not exist in the database model.
    """
    
    def setUp(self):
        """
        Set testing environment, instances, variables, etc., to be tested.
        
        Attributes:
            author_instance (object): The author that will be created and saved as instance from the database "Author" model to be linked as a Book instance foreign key for book.author field. 
            book_instance (object) = The book instance will be created for the "Book" model from database. 
        
        Returns:
            None
        """
        
        author_instance = Author.objects.create(first_name="Paulo", last_name="Cohelo", country="Brazil")
        book_instance = Book.objects.create(title="My testing Book", author=author_instance, genre="Action", synopsis="This is a testing synopsis", release_date=1990)
        
    def test_model_can_create(self):
        """
        Tests if the model instance can be created (Book).
        
        Attributes:
            test_instance (object): The instance that is being tested (Book instance)
            
        Return:
            None
        """
        
        #Comprobes if the instance is equal to the obtained from the model instance.
        test_instance = Book.objects.get(title="My testing Book")
        
        # Fix this issue: TypeError: TestCase.assertEqual() missing 1 required positional argument: 'second'
        self.assertEqual(test_instance.title, "My testing Book")       
        print("[Done] Book model can create instances.")

    def test_model_instance_doesnotexist(self):
        """
        Test if Book model can manage the situation when Book instance does not be be found.
        
        Attributes:
            test_instance (Object): The Book model instance to be tested.
        
        Returns:
            None
        """
        
        #Manage case where the Book instance does not exist and then raise an Exception (model.DoesNotExist).
        with self.assertRaises(Book.DoesNotExist):
            test_instance = Book.objects.get(title="La ultima noche")
        print("[Done] Book instance does not exist.")
        

#Author model testing
class ModelTest_Author(TestCase):
    """
        Testing methods and cases for Author model.
    
        Methods:
            setUp(self): Configurate testing environment, instances, vairiables, etc.
            test_model_can_create(self): Test if Author model can create an instance.
            test_model_can_update(self): Test if Author model can modify data for an instance.
            test_model_can_delete(self): Test if Author model can delete an instance from.
            test_model_instance_doesnotexist(self): Test if Author model can manage the case a requested instance does not exist.
    """
    
    def setUp(self):
        """
            Configurate testing enironment, instances, variables, etc.
            
            Attributes:
                first_author_instance (Object): Author instance to test has been created.
                second_author_instance (Object): Author instance to be modified.
                third_author_instance (Object): Author instance to be deleted.
        
            Returns:
                None
        """
        
        first_author_instance = Author.objects.create(first_name="Paulo", last_name="Cohelo", country="Brazil")
        second_author_instance = Author.objects.create(first_name="Juan", last_name="del Toro", country="Mexico")
        third_author_instance = Author.objects.create(first_name="Karla", last_name="Montoya", country="Mexico")
        
    def test_model_can_create(self):
        """
            Test if Author model can create an instance.
            
            Attributes:
                None
            
            Returns:
                None
        """
        
        # Get instance to check it has been created.
        book_instance = Author.objects.get(first_name="Paulo", last_name="Cohelo")
        
        # Assert if the requested instance has been created and then it exists.
        self.assertEqual(book_instance.complete_name, "Paulo Cohelo")      
        print("[Done] Author model can create instances.")  
        
    def test_model_can_update(self):
        """
            Test if Author model can update data from an instance.
            
            Attributes:
                author_instance (Object): Get existing instance to be modified.
                modified_author_instance (Object): Modified instance.
                
            Returns:
                None
        """
        
        #Modify instance data (first_name)
        author_instance = Author.objects.get(first_name="Juan", last_name="del Toro")
        author_instance.first_name = "Guillermo"
        author_instance.save()
        
        #Get modified instance
        modified_author_instance = Author.objects.get(id=author_instance.id)
        
        self.assertEqual(modified_author_instance.complete_name, "Guillermo del Toro")
        print("[Done] Author model can update instances data.")        
        
    def test_model_can_delete(self):
        """
            Test if an Author model instance can be deleted from the database.
            
            Attributes:
                author_instance (Object): The Author model instance to be created, tested, and deleted.
                
            Returns:
                None
        """
        
        # Get instance from DB to be deleted
        author_instance = Author.objects.get(first_name="Karla", last_name="Montoya", country="Mexico")
        
        # Ensure the instance has been created (Optional, but hightly recomended)
        self.assertTrue(Author.objects.filter(first_name="Karla", last_name="Montoya", country="Mexico").exists())
        
        # Delete the instance
        author_instance.delete()
        
        # Verify that the instance was deleted
        self.assertFalse(Author.objects.filter(first_name="Karla", last_name="Montoya", country="Mexico").exists())
        
        print("[Done] Author model can delete instances.")
        
    def test_model_model_instance_doesnotexist(self):
        """
            Test if the model can manage the case a requested instance does not exist.
            
            Attributes:
                test_instance (Object): Instance that does not exist, but will be tested to comprobe it.
                
            Returns:
                None
        """
        
        # Get a not existing instance and test if model can raise an Exception.
        with self.assertRaises(Author.DoesNotExist):
            test_instance = Author.objects.get(first_name="Lili", last_name="Dayns")
        print("[Done] Author model can manage the case an instance does not exist with an exception.")
        

"""Views testing"""
class ViewTest_home(TestCase):
    """
        Test if 'home' view from FrontEnd.views renders the correct template, context and get the correct status code

        Methods:
            test_redirect_to_login_if_not_authenticated(self): Test if the view redirects to login when user is not authenticated.
            test_view_for_authenticated_user(self): Test if home view render correct context, template and status code is correct when the user is authenticated.
    """
    
    def test_redirect_to_login_if_not_authenticated(self):
        """
            Test if 'home' view redirects unauthenticated users to the login page.
            
            Attributes:
                response (Object): The requested view response
                
            Returns: 
                None
        """
        
        response = self.client.get(reverse('home'))
        
        # Check that the response status code is 302 (redirect)
        self.assertEqual(response.status_code, 302)
        
        # Check that the redirected URL is correct
        self.assertRedirects(response, f"{reverse('login')}?next={reverse('home')}")
        
        print("[Done] The view redirects unauthenticated users to the login page as expected.")
        
    def test_view_for_authenticated_user(self):
        """
            Test if the 'home' view renders the correct template and context for authenticated users.
            
            Attributes:
                response (Object): Response from the requested view
        """
        
        # Create user to log them in
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        
        response = self.client.get(reverse('home'))
        
        # Check that the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Check that the view renders the correct template
        self.assertTemplateUsed(response, 'home.html')
        
        # Check that the context contains the expected variables
        self.assertIn('user', response.context)
        self.assertIn('authors', response.context)
        self.assertIn('books', response.context)
        
        print("[Done] The view renders the correct template and context for authenticated users.")
        
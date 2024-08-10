from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class ViewTest_register(TestCase):
    """
        Test the registration form view to ensure it works as expected
    """
    
    def test_register_view_renders_form(self):
        """
            Test that the registration form is rendered correctly.
        """
        
        response = self.client.get(reverse('register'))
        
        # Check that response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        
        # Check that the form is rendered
        self.assertContains(response, '<form', status_code=200)
        self.assertContains(response, 'name="username"')
        self.assertContains(response, 'name="email"')
        self.assertContains(response, 'name="password"')
        
        print("[Done] The registration form is rendered correctly.")
        
    def test_register_with_valid_data(self):
        """
            Test the valid data submitted through the form creates a new User
        """
        response = self.client.post(reverse('register'), data={
            'username': 'newuser',
            'email': 'newuser@gmail.com',
            'password': 'complexpassword123',
        })
        
        # Check that the form redirects after succesful submission
        self.assertEqual(response.status_code, 302)
        
        # Check that the user has been created
        user_exists = User.objects.filter(username='newuser').exists()
        self.assertTrue(user_exists)
        
        print("[Done] The registration form creates a new user with valid data")
        
    def test_register_with_invalid_data(self):
        """
            Test that invalid data does not create a user and returns the appropiate errors.    
        """
        
        response = self.client.post(reverse('register'), data={
            'username': 'new_user2',
            'email':'juaquin',
            'password': '123securepassword',
        })
        
        # Check that the form does not redirect and stays on the same page
        self.assertEqual(response.status_code, 200)
        
        # Check that no user was created
        user_exists = User.objects.filter(username='new_user2').exists()
        self.assertFalse(user_exists)
        
        # Check that the form contains the appropriate error message.}
        # Fix this with the formulary message: self.assertContains(response, 'Email field is invalid.')
        
        print("[Done] The registration form returns errors with invalid data.")
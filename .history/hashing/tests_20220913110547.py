from urllib import response
from selenium import webdriver
from django.test import TestCase
from .forms import HashForm
import hashlib
from .models import Hash

# browser = webdriver.Chrome()
# browser.get('http://localhost:8000')
        
    
# class FunctionalTestCase(TestCase):
    
#     def setUp(self):
#         self.browser = webdriver.Chrome()
        
    
#     def tearDown(self):
#         self.browser.quit()
        
        
#     def test_there_is_homepage(self):
#         self.browser.get('http://localhost:8000')
#         self.assertIn("Enter hash here", self.browser.page_source)
        
#     def test_hash_of_hello(self):
#         self.browser.get('http://localhost:8000')
#         text = self.browser.find_element_by_id("id_text")
#         text.send_keys("hello")
#         self.browser.find_element_by_name("submit").click()
#         self.assertIn("2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824", self.browser.page_source)
        
        
class UnitTestCase(TestCase):
    
    def test_homepage_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "hashing/home.html")
        
    def test_hash_form(self):
        form = HashForm(data={"text" : "hello"})
        self.assertTrue(form.is_valid())
        
    
    def test_hash_func_works(self):
        text_hash = hashlib.sha256('hello'.encode('utf-8')).hexdigest()
        self.assertEqual('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', text_hash)
        
        
    def test_hash_object(self):
        hash = Hash()
        hash.text = "hello"
        hash.hash = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
        hash.save()
        
        pulled_hash = Hash.objects.get(hash='2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
        
        self.assertEqual(hash.text, pulled_hash.text)
        
    
    def test_viewing_hash(self):
        hash = Hash()
        hash.text = "hello"
        hash.hash = "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
        hash.save()
        response = self.client.get('/hash/2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
        
        self.assertContains(response, "hello")
from django.test import TestCase,Client
from django.urls import reverse
from .models import *
# Create your tests here.

# class TestCustomUser(TestCase):
#      def setUp(self):
#           self.client = Client()
#           self.user_data = {
#                "role":"blogger",
#                "username" : "user",
#                "first_name" :"user",
#                "last_name" :"some",
#                "email" : "user@mail.com",
#                "password1" : 'qwerty@123',
#                "password2":"qwerty@123"
#           }
#      def test_register_user(self):
#           registration_url = reverse('registration') 
#           response = self.client.post(registration_url,self.user_data)
#           self.assertEqual(response.status_code,302)
#           self.assertEqual(CustomUser.objects.first().username,self.user_data['username'])
#           self.assertEqual(CustomUser.objects.all().count(),1)

#      def test_login_user(self):
#           login_url = reverse("login")
#           response = self.client.post(login_url,data={"username":self.user_data['username'],"password":self.user_data["password1"]})    
#           self.assertEqual(response.status_code,200)

#      def test_log_out(self):
#           logout_url = reverse("logout")
#           response = self.client.get(logout_url)
#           self.assertEqual(response.status_code,302)


class TestBlog(TestCase):
     def setUp(self):
          self.client = Client()
          self.client = self.client
          self.blogger = CustomUser.objects.create(
               role="Blogger",
                username = "user",
                first_name = "user",
                last_name = "some",
                email = "user@mail.com",
          )
          self.blogger.set_password("niaje@123")
          self.blogger.save()

     def test_create_blog(self):
          create_blog_url = reverse("createblog")
          self.client.login(username = "user" ,password = "niaje@123")
          response = self.client.post(create_blog_url,data = {
                "Title":"Celibacy works",
                "category":"Lifestyle",
                "Cover_image":"",
                "Content":"try it",
                "Blogger":self.blogger,
                "tags":"celibacy,lifestyle,spermretention"
          })

          self.assertEqual(response.status_code,302)
          self.assertEqual(Blog.objects.first().Content,"try it")
          self.assertEqual(Blog.objects.all().count(),1)
          print("id",Blog.objects.first().Blogger)
     def test_list_blog(self):
          list_blog_url = reverse("blogs")
          response = self.client.get(list_blog_url)

          self.assertEqual(response.status_code,200)

     def test_detail_blog(self):
          detail_blog_url = reverse("blog",kwargs={"pk":1})
          
          response = self.client.get(detail_blog_url)     

          self.assertEqual(response.status_code,302)
     def test_blog_update(self):
          Blog.objects.create( Title="Celibacy works",
                category="Lifestyle",
                Cover_image="",
                Content="try it",
                Blogger=self.blogger,
                tags="celibacy,lifestyle,spermretention")
          self.client.login(username = "user" ,password = "niaje@123")
          blog_update_url = reverse('update',kwargs={"pk":1})
          response = self.client.post(blog_update_url,data={"Content":"Niaje"})

          self.assertEqual(response.status_code,200)     

     def test_blog_delete(self):
          Blog.objects.create( Title="Celibacy works",
                category="Lifestyle",
                Cover_image="",
                Content="try it",
                Blogger=self.blogger,
                tags="celibacy,lifestyle,spermretention")
          delete_blog_url = reverse("delete",kwargs={"pk":"1"})
          self.client.login(username = "user" ,password = "niaje@123")
          response = self.client.delete(delete_blog_url)
          self.assertEqual(response.status_code,302)     

     def test_create_blog_comment(self):
          blog = Blog.objects.create( Title="Celibacy works",
                category="Lifestyle",
                Cover_image="",
                Content="try it",
                Blogger=self.blogger,
                tags="celibacy,lifestyle,spermretention")
          comment_url = reverse("comment",kwargs={"pk":1})
          
 
          data = {
               "content":"nice",
               "blog": blog,
               "user":self.blogger,
          }
          self.client.login(username = "user" ,password = "niaje@123")
          self.client.post(comment_url,data=data)

     def test_list_blog_comments(self):
          blog = Blog.objects.create( Title="Celibacy works",
                category="Lifestyle",
                Cover_image="",
                Content="try it",
                Blogger=self.blogger,
                tags="celibacy,lifestyle,spermretention")
          Comment.objects.create(content="niaje",user=self.blogger,blog=blog)
          list_comment_url = reverse("comments",kwargs={"pk":1})
          self.client.login(username = "user" ,password = "niaje@123")
          response = self.client.get(list_comment_url)

          self.assertEqual(response.status_code,200)
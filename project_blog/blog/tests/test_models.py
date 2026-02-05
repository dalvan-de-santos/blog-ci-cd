from django.test import TestCase
from django.contrib.auth import get_user_model
from blog.models import Blog, Post
from django.core.files.uploadedfile import SimpleUploadedFile

User = get_user_model()


class TestBlogModel(TestCase):

    def setUp(self):
        self.user=User.objects.create_user(
            username='test123',
            password='1234567'
        )

        self.blog=Blog.objects.create(
            name='Meu Blog de Teste',
            description='Descrição do blog',
            tags='django,python,testes',
            user=self.user
        )

    def test_blog_is_created(self):
        """Testa se o blog é criado corretamente"""
        self.assertEqual(Blog.objects.count(), 1)

    
    def test_blog_fields(self):
        """Testa os campos do blog"""
        self.assertEqual(self.blog.name, 'Meu Blog de Teste')
        self.assertEqual(self.blog.description, 'Descrição do blog')
        self.assertEqual(self.blog.tags, 'django,python,testes')
        self.assertEqual(self.blog.user, self.user)

    
    def test_blog_str(self):
        """Testa o método __str__"""
        self.assertEqual(str(self.blog), 'Meu Blog de Teste')



    def test_created_at_is_auto(self):
        """Testa se created_at é criado automaticamente"""
        self.assertIsNotNone(self.blog.created_at)

    def test_updated_at_is_auto(self):
        """Testa se updated_at é criado automaticamente"""
        self.assertIsNotNone(self.blog.updated_at)


    def test_user_related_name(self):
        """Testa o related_name='blogs'"""
        self.assertIn(self.blog, self.user.blogs.all())


class TestPostModel(TestCase):

    def setUp(self):
        self.user=User.objects.create_user(
            username='test123',
            password='1234567'
        )

        self.blog=Blog.objects.create(
            name='Meu Blog de Teste',
            description='Descrição do blog',
            tags='django,python,testes',
            user=self.user
        )

        self.image = SimpleUploadedFile(
            name='image.png',
            content=b'fake image content',
            content_type='image/png'
        )

        self.post=Post.objects.create(
          image=self.image,
          description='sei la',
          tags='python, java',
          blog=self.blog 
        )

    def test_post_is_created(self):
        """Testa se o post é criado corretamente"""
        self.assertEqual(Post.objects.count(), 1)

    
    def test_post_fields(self):
        """Testa os campos do post"""
        self.assertEqual(self.post.description, 'sei la')
        self.assertEqual(self.post.tags, 'python, java')
        self.assertEqual(self.post.blog, self.blog)
        self.assertTrue(self.post.image)

    def test_post_str(self):
        """Testa o método __str__ do Post"""
        self.assertEqual(str(self.post), 'sei la')

    def test_created_at_is_auto(self):
        """Testa se created_at é criado automaticamente"""
        self.assertIsNotNone(self.post.created_at)

    def test_updated_at_is_auto(self):
        """Testa se updated_at é criado automaticamente"""
        self.assertIsNotNone(self.post.updated_at)

    def test_blog_related_name_posts(self):
        """Testa o related_name='posts' no Blog"""
        self.assertIn(self.post, self.blog.posts.all())

    def test_post_delete_when_blog_is_deleted(self):
        """Testa se o post é deletado quando o blog é removido"""
        self.blog.delete()
        self.assertEqual(Post.objects.count(), 0)

        
        
import factory
from product.models import Product
from product.models.category import Category

class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('pystr')
    slug = factory.Faker('pystr')
    description = factory.Faker('text')
    active = factory.Faker([True, False])

    class Meta:
        model = Category

class ProductFactory(factory.django.DjangoModelFactory):
    title = factory.Faker('pystr')
    price = factory.Faker('pyint')
    category = factory.SubFactory(CategoryFactory)

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for category in extracted:
                self.category.add(category)
    class Meta:
        model = Product

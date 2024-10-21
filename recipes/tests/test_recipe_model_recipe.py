from django.core.exceptions import ValidationError

from .test_recipe_base import RecipeTestBase


class RecipeModelTest(RecipeTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def test_recipe_title_raises_error_if_title_has_more_than_65_chars(self):
        self.recipe.title = 'A' * 70

        with self.assertRaises(ValidationError): #Isso obriga que o erro seja levantado
            self.recipe.full_clean()  #A validação ocorre aqui. O que vem a seguir não executa
        
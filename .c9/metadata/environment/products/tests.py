{"filter":false,"title":"tests.py","tooltip":"/products/tests.py","ace":{"folds":[],"scrolltop":78,"scrollleft":0,"selection":{"start":{"row":0,"column":0},"end":{"row":12,"column":53},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"hash":"4809a80f81413f451ad8d33e28eafd93b9156a14","undoManager":{"mark":0,"position":0,"stack":[[{"start":{"row":0,"column":0},"end":{"row":3,"column":0},"action":"remove","lines":["from django.test import TestCase","","# Create your tests here.",""],"id":2},{"start":{"row":0,"column":0},"end":{"row":12,"column":53},"action":"insert","lines":["from django.test import TestCase","from .models import Product","","# Create your tests here.","class ProductTests(TestCase):","    \"\"\"","    Here we'll define the tests that we'll run against our","    Product model","    \"\"\"","","    def test_str(self):","        test_name = Product(name='A product')","        self.assertEqual(str(test_name), 'A product')"]}]]},"timestamp":1567076420814}
from django.test import SimpleTestCase
from django.urls import reverse


class TestAddCanHandleSimpleAddition(SimpleTestCase):
    def test_two_plus_two(self):
        response = self.client.get(
            path=reverse("add"),
            data={
                'num1': '2',
                'num2': '2'
            },
        )
        self.assertEqual(response.context['answer'], 4)

    def test_two_plus_negative_one(self):
        response = self.client.get(
            path=reverse("add"),
            data={
                'num1': '-2',
                'num2': '2'
            },
        )
        self.assertEqual(response.context['answer'], 0)

    def test_zero_plus_zero(self):
        response = self.client.get(
            path=reverse("add"),
            data={
                'num1': '0',
                'num2': '0'
            },
        )
        self.assertEqual(response.context['answer'], 0)

    def test_decimal_plus_decimal(self):
        response = self.client.get(
            path=reverse("add"),
            data={
                'num1': '2.3',
                'num2': '1.2'
            },
        )
        self.assertEqual(response.context['answer'], 3.5)

    def test_negative_plus_negative(self):
        response = self.client.get(
            path=reverse("add"),
            data={
                'num1': '-2',
                'num2': '-2'
            },
        )
        self.assertEqual(response.context['answer'], -4)


class TestAddWithoutNumbers(SimpleTestCase):
    def test_given_non_numeric_input(self):
        response = self.client.get(
            path=reverse("add"),
            data={
                'num1': 'a',
                'num2': 'a'
            },
        )
        self.assertTemplateUsed(response, 'app/add.html')
        self.assertNotIn('answer', response.context)


class TestDoubleCanDoubleRealNumber(SimpleTestCase):
    def test_double_a_number(self):
        response = self.client.get(
            path=reverse('double'), data={
                'num1': '1',
            })
        self.assertEqual(response.context['answer'], 2)


class TestSubtractCanSubtractRealNumbers(SimpleTestCase):
    def test_subtract_a_number(self):
        response = self.client.get(
            path=reverse('subtract'), data={
                'num1': '7',
                'num2': '3'
            })
        self.assertEqual(response.context['answer'], 4)

    def test_subtract_a_negative_number(self):
        response = self.client.get(
            path=reverse('subtract'), data={
                'num1': '7',
                'num2': '-3'
            })
        self.assertEqual(response.context['answer'], 10)

    def test_subtract_a_float(self):
        response = self.client.get(
            path=reverse('subtract'), data={
                'num1': '3.5',
                'num2': '1.3'
            })
        self.assertEqual(response.context['answer'], 2.2)

    def test_subtract_a_zero(self):
        response = self.client.get(
            path=reverse('subtract'), data={
                'num1': '0',
                'num2': '0'
            })
        self.assertEqual(response.context['answer'], 0)


class TestMultiplicationCanMultiplyNumbers(SimpleTestCase):
    def test_multThree_a_number(self):
        response = self.client.get(
            path=reverse('multThree'), data={
                'x': '2',
                'y': '5',
                'z': '2',
            })
        self.assertEqual(response.context['answer'], 20)


class TestEarningsTotalsTheCost(SimpleTestCase):
    def test_earnings(self):
        response = self.client.get(
            path=reverse('earnings'), data={
                'a': '2',
                'b': '5',
                'c': '2',
            })
        self.assertEqual(response.context['answer'], 108)


class TestBoth(SimpleTestCase):
    def test_both(self):
        response = self.client.get(
            path=reverse('both'), data={
                'x': 'true',
                'y': 'false',
            })
        self.assertEqual(response.context['answer'], 'false')

    def test_both_1(self):
        response = self.client.get(
            path=reverse('both'), data={
                'x': 'false',
                'y': 'false',
            })
        self.assertEqual(response.context['answer'], 'false')

    def test_both_2(self):
        response = self.client.get(
            path=reverse('both'), data={
                'x': 'true',
                'y': 'true',
            })
        self.assertEqual(response.context['answer'], 'true')


class TestWalkOrDrive(SimpleTestCase):
    def test_walk_or_drive_both_true(self):
        response = self.client.get(
            path=reverse('walkordrive'),
            data={
                'miles': .25,
                'isNiceWeather': True,
            })
        self.assertEqual(response.context['answer'], 'walk')

    def test_walk_or_drive_both_false(self):
        response = self.client.get(
            path=reverse('walkordrive'),
            data={
                'miles': .27,
                'isNiceWeather': False,
            })
        self.assertEqual(response.context['answer'], 'drive')

    def test_walk_or_drive_one_true(self):
        response = self.client.get(
            path=reverse('walkordrive'),
            data={
                'miles': .25,
                'isNiceWeather': False,
            })
        self.assertEqual(response.context['answer'], 'drive')

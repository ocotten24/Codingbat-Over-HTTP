from django.test import SimpleTestCase


class TestNearHundred(SimpleTestCase):
    def test_near_hundred_1(self):
        response = self.client.get("/warmup-1/near-hundred/93")
        self.assertContains(response, True)

    def test_near_hundred_2(self):
        response = self.client.get("/warmup-1/near-hundred/90")
        self.assertContains(response, True)

    def test_near_hundred_3(self):
        response = self.client.get("/warmup-1/near-hundred/89")
        self.assertContains(response, False)


class TestStringSplosion(SimpleTestCase):
    def test_string_splosion_1(self):
        response = self.client.get("/warmup-2/string-splosion/Code")
        self.assertContains(response, "CCoCodCode")

    def test_string_splosion_2(self):
        response = self.client.get("/warmup-2/string-splosion/abc")
        self.assertContains(response, "aababc")

    def test_string_splosion_3(self):
        response = self.client.get("/warmup-2/string-splosion/ab")
        self.assertContains(response, "aab")


class TestCatDog(SimpleTestCase):
    def test_cat_dog_1(self):
        response = self.client.get("/string-2/cat-dog/catdog")
        self.assertContains(response, True)

    def test_cat_dog_2(self):
        response = self.client.get("/string-2/cat-dog/catcat")
        self.assertContains(response, False)

    def test_cat_dog_3(self):
        response = self.client.get("/string-2/cat-dog/1cat1cadodog")
        self.assertContains(response, True)


class TestLoneSum(SimpleTestCase):
    def test_lone_sum_1(self):
        response = self.client.get("/logic-2/lone-sum/1/2/3")
        self.assertContains(response, 6)

    def test_lone_sum_2(self):
        response = self.client.get("/logic-2/lone-sum/3/2/3")
        self.assertContains(response, 2)

    def test_lone_sum_3(self):
        response = self.client.get("/logic-2/lone-sum/3/3/3")
        self.assertContains(response, 0)

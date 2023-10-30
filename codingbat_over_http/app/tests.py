from django.test import SimpleTestCase


class TestNearHundred(SimpleTestCase):
    def test_near_hundred_within_10(self):
        response = self.client.get("/warmup-1/near-hundred/91")
        self.assertContains(response, True)

    def test_near_hundred_within_10_2(self):
        response = self.client.get("/warmup-1/near-hundred/109")
        self.assertContains(response, True)

    def test_near_hundred_outside_10(self):
        response = self.client.get("/warmup-1/near-hundred/1000")
        self.assertContains(response, False)


class TestStringSplosion(SimpleTestCase):
    def test_string_splosion_hello(self):
        response = self.client.get("/warmup-2/string-splosion/hello")
        self.assertContains(response, "hhehelhellhello")

    def test_string_splosion_empty_string(self):
        response = self.client.get("/warmup-2/string-splosion/testcase")
        self.assertContains(response, "ttetestesttestctestcatestcastestcase")

    def test_string_splosion_single_character(self):
        response = self.client.get("/warmup-2/string-splosion/owen")
        self.assertContains(response, "oowoweowen")


class TestCatDog(SimpleTestCase):
    def test_cat_dog_equal_counts(self):
        response = self.client.get(
            "/string-2/cat-dog/caaaaaaaaaaaaaaaatdooooooogdogdogdog"
        )
        self.assertContains(response, False)

    def test_cat_dog_unequal_counts(self):
        response = self.client.get("/string-2/cat-dog/cattestcasedog")
        self.assertContains(response, True)

    def test_cat_dog_no_cats_or_dogs(self):
        response = self.client.get("/string-2/cat-dog/catdogdogdogdogcatcatcat")
        self.assertContains(response, True)


class TestLoneSum(SimpleTestCase):
    def test_lone_sum_no_repeated_values(self):
        response = self.client.get("/logic-2/lone-sum/1/7/3")
        self.assertContains(response, 11)

    def test_lone_sum_one_repeated_value(self):
        response = self.client.get("/logic-2/lone-sum/3/1/3")
        self.assertContains(response, 1)

    def test_lone_sum_all_repeated_values(self):
        response = self.client.get("/logic-2/lone-sum/3/3/3")
        self.assertContains(response, 0)

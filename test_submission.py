# Unit tests for submission.py

from unittest import TestCase, main

import submission as sub


class PS_04_01(TestCase):
    def test_load_content_returns_a_list(self):
        self.assertIsInstance(
            sub.load_content_section("data/four_words/four_words.content-cmdt"),
            list,
            "The content section should return a list",
        )

    def test_load_content_is_len_three_list(self):
        self.assertEqual(
            len(sub.load_content_section("data/four_words/four_words.content-cmdt")),
            3,
            "`four_words.content-cmdt` has three lines, so the list should have three items",
        )

    def test_load_content_four_words(self):
        self.assertEqual(
            sub.load_content_section("data/four_words/four_words.content-cmdt"),
            [["ab", "cd", "ef"], [], ["gh"]],
            "There should be three tokens on the first line, zero on two, one on three.",
        )

    def test_load_cmdt_simple_returns_length_9_list(self):
        self.assertEqual(
            len(sub.load_content_section("data/simple/simple.content-cmdt")),
            9,
            "`simple.content-cmdt` has 9 lines, so it should return a list of 9 lists",
        )

    def test_load_cmdt_simple_content_first_line_has_two_items(self):
        self.assertEqual(
            sub.load_content_section("data/simple/simple.content-cmdt")[0],
            ["yy", "yU"],
            "The first list in the content section should be ['yy', 'yU]",
        )


class PS_04_02(TestCase):
    def test_load_data_returns_dictionary(self):
        self.assertIsInstance(
            sub.load_data_section("data/four_words/four_words.data-cmdt"),
            dict,
            "The data section should be interpreted as a dictionary",
        )

    def test_load_data_has_length_four(self):
        self.assertEqual(
            len(sub.load_data_section("data/four_words/four_words.data-cmdt")),
            4,
            "Loading the four words should be a length-4 dictionary",
        )

    def test_load_data_four_words(self):
        self.assertDictEqual(
            sub.load_data_section("data/four_words/four_words.data-cmdt"),
            {"ab": "does", "cd": "this", "ef": "work", "gh": "thanks"},
            "The four words should be a dictionary mapping from a token to a word",
        )

    def test_load_simple_cmdt_data_section_yy_maps_to_hello(self):
        self.assertEqual(
            sub.load_data_section("data/simple/simple.data-cmdt")["yy"],
            "hello",
            "In the `simple.data-cmdt` file, the token 'yy' should map to 'hello'",
        )

    def test_load_simple_cmdt_is_dictionary(self):
        self.assertIsInstance(
            sub.load_data_section("data/simple/simple.data-cmdt"),
            dict,
            "Loading the `simple.data-cmdt` should return a dictionary",
        )

    def test_load_simple_cmdt_has_length(self):
        self.assertEqual(
            len(sub.load_data_section("data/simple/simple.data-cmdt")),
            35,
            "`simple.data-cmdt` should be a length-35 dictionary",
        )


class PS_04_03(TestCase):
    def test_load_cmdt_returns_valid_content(self):
        content, _ = sub.load_cmdt("data/four_words/four_words")
        self.assertEqual(
            content,
            [["ab", "cd", "ef"], [], ["gh"]],
            "The 'content' return should be a list returned from 'load_content_section'",
        )

    def test_load_cmdt_returns_valid_data(self):
        _, data = sub.load_cmdt("data/four_words/four_words")
        self.assertEqual(
            data,
            {"ab": "does", "cd": "this", "ef": "work", "gh": "thanks"},
            "The 'data' return should be a list returned from 'load_data_section'",
        )


class PS_04_04(TestCase):
    def test_four_words_cmdt_to_plaintext(self):
        content, data = sub.load_cmdt("data/four_words/four_words")
        self.assertEqual(
            sub.cmdt_to_plaintext(content, data),
            "does this work\n\nthanks",
            "The `four_words` should be converted to plaintext with three words, two newlines, and the word 'thanks'",
        )

    def test_simple_cmdt_to_plaintext(self):
        content, data = sub.load_cmdt("data/simple/simple")
        self.assertIn(
            "only letters a through z exist",
            sub.cmdt_to_plaintext(content, data),
            "The phrase 'only letters a through z exist' should be in the 'simple' plaintext",
        )


class PS_04_05(TestCase):
    def test_build_list_of_recipes(self):
        plaintext = sub.cmdt_to_plaintext(*sub.load_cmdt("data/desserts/desserts"))
        self.assertEqual(
            sub.build_list_of_recipes(plaintext),
            [
                "pie crust recipe",
                "cherry pie recipe",
                "pecan pie",
                "spiced rum pecan pie",
                "sugar creme pie",
                "fruit pie",
                "peach pie",
                "peach pie",
                "peach pie",
                "key lime pie",
            ],
            "build_list_of_recipes should return a list of 10 recipes",
        )


class PS_04_06(TestCase):
    def test_dessert_extraction(self):
        content, data = sub.load_cmdt("data/desserts/desserts")
        plaintext = sub.cmdt_to_plaintext(content, data)
        self.assertIn("pie crust recipe", plaintext)

    def test_dessert_list_of_recipes_extraction(self):
        plaintext = sub.cmdt_to_plaintext(*sub.load_cmdt("data/desserts/desserts"))
        self.assertEqual(
            sub.build_list_of_recipes(plaintext),
            [
                "pie crust recipe",
                "cherry pie recipe",
                "pecan pie",
                "spiced rum pecan pie",
                "sugar creme pie",
                "fruit pie",
                "peach pie",
                "peach pie",
                "peach pie",
                "key lime pie",
            ],
            "build_list_of_recipes should return a list of 10 recipes",
        )


if __name__ == "__main__":
    main()

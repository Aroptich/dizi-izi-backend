import unittest

from core import Core


class TestFurnitureArrangement(unittest.TestCase):
    def setUp(self):
        self.calculator = Core()



    def test_algorithm_activation_1(self):
        self.calculator.algorithm_activation(
            [
                {
                    "north_west": {"x": 4, "y": 10},
                    "north_east": {"x": 7, "y": 10},
                    "south_west": {"x": 4, "y": 9},
                    "south_east": {"x": 7, "y": 9},
                },
                {
                    "north_west": {"x": 14, "y": 0},
                    "north_east": {"x": 12, "y": 0},
                    "south_west": {"x": 14, "y": 4},
                    "south_east": {"x": 12, "y": 4},
                },
            ],
            [{"width": 2, "length": 3},
             {"width": 3, "length": 1}],
            {
                "first_wall": 10,
                "second_wall": 14,
                "third_wall": 10,
                "fourth_wall": 14,
            },
        )

    def test_algorithm_activation_2(self):
        self.calculator.algorithm_activation(
            [
                {
                    "north_west": {"x": 4, "y": 10},
                    "north_east": {"x": 7, "y": 10},
                    "south_west": {"x": 4, "y": 9},
                    "south_east": {"x": 7, "y": 9},
                },
                {
                    "north_west": {"x": 14, "y": 0},
                    "north_east": {"x": 12, "y": 0},
                    "south_west": {"x": 14, "y": 4},
                    "south_east": {"x": 12, "y": 4},
                },
            ],
            [{"width": 4, "length": 6},
             {"width": 3, "length": 2}],
            {
                "first_wall": 10,
                "second_wall": 14,
                "third_wall": 10,
                "fourth_wall": 14,
            },
        )

    def test_algorithm_activation_3(self):
        self.calculator.algorithm_activation(
            [
                {
                    "north_west": {"x": 4, "y": 10},
                    "north_east": {"x": 7, "y": 10},
                    "south_west": {"x": 4, "y": 9},
                    "south_east": {"x": 7, "y": 9},
                },
                {
                    "north_west": {"x": 14, "y": 0},
                    "north_east": {"x": 12, "y": 0},
                    "south_west": {"x": 14, "y": 4},
                    "south_east": {"x": 12, "y": 4},
                },
            ],
            [
                {"width": 1, "length": 1},
                {"width": 2, "length": 1},
                {"width": 1, "length": 1},
                {"width": 3, "length": 1},
            ],
            {
                "first_wall": 10,
                "second_wall": 14,
                "third_wall": 10,
                "fourth_wall": 14,
            },
        )

    def test_algorithm_activation_4(self):
        self.calculator.algorithm_activation(
            [
                {
                    "north_west": {"x": 4, "y": 10},
                    "north_east": {"x": 7, "y": 10},
                    "south_west": {"x": 4, "y": 9},
                    "south_east": {"x": 7, "y": 9},
                },
                {
                    "north_west": {"x": 14, "y": 0},
                    "north_east": {"x": 12, "y": 0},
                    "south_west": {"x": 14, "y": 4},
                    "south_east": {"x": 12, "y": 4},
                },
            ],
            [
                {"width": 4, "length": 1},
                {"width": 1, "length": 6},
                {"width": 3, "length": 3},
                {"width": 1, "length": 1},
            ],
            {
                "first_wall": 10,
                "second_wall": 14,
                "third_wall": 10,
                "fourth_wall": 14,
            },
        )

    def test_algorithm_activation_5(self):
        self.calculator.algorithm_activation(
            [
                {
                    "north_west": {"x": 4, "y": 10},
                    "north_east": {"x": 7, "y": 10},
                    "south_west": {"x": 4, "y": 9},
                    "south_east": {"x": 7, "y": 9},
                },
                {
                    "north_west": {"x": 14, "y": 0},
                    "north_east": {"x": 12, "y": 0},
                    "south_west": {"x": 14, "y": 4},
                    "south_east": {"x": 12, "y": 4},
                },
            ],
            [{"width": 5, "length": 1}],
            {
                "first_wall": 10,
                "second_wall": 14,
                "third_wall": 10,
                "fourth_wall": 14,
            },
        )

    def test_algorithm_activation_6(self):
        self.calculator.algorithm_activation(
            [
                {
                    "north_west": {"x": 0, "y": 250},
                    "north_east": {"x": 0, "y": 750},
                    "south_west": {"x": 500, "y": 250},
                    "south_east": {"x": 500, "y": 750},
                },

            ],
            [{"width": 1800, "length": 2000},
             {"width": 1200, "length": 1200}
             ],
            {
                "first_wall": 10000,
                "second_wall": 12000,
                "third_wall": 10000,
                "fourth_wall": 12000,
            },
        )

    def test_algorithm_activation_7(self):
        """Тест примагничивания к углам 1"""
        self.calculator.algorithm_activation(
            [
                {
                    "north_west": {"x": 0, "y": 3},
                    "north_east": {"x": 0, "y": 7},
                    "south_west": {"x": 1, "y": 3},
                    "south_east": {"x": 1, "y": 7},
                },
                {
                    "north_west": {"x": 14, "y": 7},
                    "north_east": {"x": 14, "y": 3},
                    "south_west": {"x": 13, "y": 7},
                    "south_east": {"x": 13, "y": 3},
                },
            ],
            [
                {"width": 13, "length": 1},
            ],
            {
                "first_wall": 10,
                "second_wall": 14,
                "third_wall": 10,
                "fourth_wall": 14,
            },
        )

    def test_algorithm_activation_8(self):
        """Тест примагничивания к углам 2"""
        self.calculator.algorithm_activation(
            [
                {
                    "north_west": {"x": 0, "y": 1200},
                    "north_east": {"x": 0, "y": 8800},
                    "south_west": {"x": 100, "y": 1200},
                    "south_east": {"x": 100, "y": 8800},
                },
                {
                    "north_west": {"x": 14000, "y": 8800},
                    "north_east": {"x": 14000, "y": 1200},
                    "south_west": {"x": 13800, "y": 8800},
                    "south_east": {"x": 13800, "y": 1200},
                },
            ],
            [
                {"width": 13000, "length": 1000},
            ],
            {
                "first_wall": 10000,
                "second_wall": 14000,
                "third_wall": 10000,
                "fourth_wall": 14000,
            },
        )


    def test_algorithm_activation_9(self):
        """
        Тест примагничивания к углам 3.
        Отмена смещения к углу, если там уже что-то есть.
        """
        self.calculator.algorithm_activation(
            [
                {
                    "north_west": {"x": 0, "y": 500},
                    "north_east": {"x": 0, "y": 9500},
                    "south_west": {"x": 100, "y": 500},
                    "south_east": {"x": 100, "y": 9500},
                },
                {
                    "north_west": {"x": 14000, "y": 9500},
                    "north_east": {"x": 14000, "y": 500},
                    "south_west": {"x": 13900, "y": 9500},
                    "south_east": {"x": 13900, "y": 500},
                },
            ],
            [
                {"width": 13000, "length": 1000},
            ],
            {
                "first_wall": 10000,
                "second_wall": 14000,
                "third_wall": 10000,
                "fourth_wall": 14000,
            },
        )
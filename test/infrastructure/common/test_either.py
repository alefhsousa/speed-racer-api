from infrastructure.common.either import Right, Left


class TestEither:

    def test_should_return_an_right_instance(self):
        either_right = Right('right')
        assert not either_right.is_left
        assert either_right.is_right
        assert 'right' == either_right.value

    def test_should_return_an_left_instance(self):
        either_left = Left('left')
        assert either_left.is_left
        assert not either_left.is_right
        assert 'left' == either_left.value

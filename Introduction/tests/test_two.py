from programs.person import Person
from pytest import fixture, raises


@fixture
def person_zero_initial():
    print("Creating Person with zero initials")
    return Person()


@fixture
def person():
    print("Creating Person")
    return Person(100)


def test_initial_amount(person_zero_initial):
    assert person_zero_initial.amount == 0


def test_initial_amount_two(person):
    assert person.amount == 100


def test_recieve_amount():
    person = Person()
    assert person.amount == 0
    person.recieve_income(100)
    assert person.amount == 100


def test_create_expense(person):
    with raises(Exception):
        person.create_expense(200)
        assert person.amount == 80


def test_save(person):
    person.save()
    assert person.saving == 10
    assert person.amount == 90

    
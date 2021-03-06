import pytest
from faker import Faker
from model_mommy import mommy
from rolepermissions.roles import assign_role


@pytest.fixture
def fake():
    return Faker('pt_BR')


@pytest.fixture
def client_with_user(client, django_user_model, logged_user):
    client.force_login(logged_user)
    return client


@pytest.fixture
def logged_user(django_user_model):
    logged_user = mommy.make(django_user_model)
    return logged_user


@pytest.fixture
def client_with_lead(client, django_user_model, logged_user):
    assign_role(logged_user, 'lead')
    client.force_login(logged_user)
    return client


@pytest.fixture
def client_with_member(client, django_user_model, logged_user):
    assign_role(logged_user, 'member')
    client.force_login(logged_user)
    return client


@pytest.fixture
def client_with_client(client, django_user_model, logged_user):
    assign_role(logged_user, 'client')
    client.force_login(logged_user)
    return client

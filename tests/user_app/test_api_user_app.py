import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from model_bakery import baker

from user_app.models import Profile


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def user_factory():
    def factory(*args, **kwargs):
        return baker.make(User, *args, **kwargs)
    return factory


# Тест получения списка профилей
@pytest.mark.django_db
def test_get_profiles(client, user_factory):
    profiles = user_factory(_quantity=10)

    response = client.get('/api/v1/profiles/')
    data = response.json()

    assert response.status_code == 200
    assert len(data) == len(profiles)


# Тест успешного создания пользователя, профиль создается одновременно
@pytest.mark.django_db
def test_success_create_profiles(client):
    users_count = User.objects.count()

    response = client.post('/auth/users/', data={'username': 'admin', 'password': 'random_random'})
    data = response.json()

    assert response.status_code == 201
    assert data['username'] == 'admin'
    assert User.objects.count() == users_count + 1


# Тест успешного обновления профиля
@pytest.mark.django_db
def test_success_update_profile(client, user_factory):

    profiles = user_factory(_quantity=10)
    count = Profile.objects.count()
    response = client.patch(f'/api/v1/profile/{profiles[0].id}/', data={'country': 'Brazil',
                                                                        'city': 'Rio'})
    data = response.json()

    assert response.status_code == 200
    assert data['country'] == 'Brazil'
    assert data['city'] == 'Rio'
    assert Profile.objects.count() == count


@pytest.mark.django_db
def test_success_delete_profile(client, user_factory):
    profiles = user_factory(_quantity=10)
    profiles_count = Profile.objects.count()

    response = client.delete(f'/api/v1/profile/{profiles[0].id}/')

    assert response.status_code == 204

    assert Profile.objects.count() == profiles_count - 1

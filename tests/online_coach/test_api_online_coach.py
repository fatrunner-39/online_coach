import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from running.models import Report


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def report_factory():
    def factory(*args, **kwargs):
        return baker.make(Report, *args, **kwargs)
    return factory


# Проверка получения списка тренировок
@pytest.mark.django_db
def test_get_reports_list(client, report_factory):
    reports = report_factory(_quantity=10)

    response = client.get('/api/v1/reports/')
    data = response.json()

    assert response.status_code == 200
    assert len(data) == len(reports)


# Тест успешного обновления отчета
@pytest.mark.django_db
def test_success_update_report(client, report_factory):

    reports = report_factory(_quantity=10)
    count = Report.objects.count()
    response = client.patch(f'/api/v1/reports/{reports[0].id}/', data={'text_report': 'Perfect'})
    data = response.json()

    assert response.status_code == 200
    assert data['text_report'] == 'Perfect'
    assert Report.objects.count() == count


# Тест успешного удаления отчета
@pytest.mark.django_db
def test_success_delete_report(client, report_factory):

    reports = report_factory(_quantity=10)
    count = Report.objects.count()
    response = client.delete(f'/api/v1/reports/{reports[0].id}/')

    assert response.status_code == 204
    assert Report.objects.count() == count - 1

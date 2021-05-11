import tempfile
from pathlib import Path

from pytest import fixture
from libcloud.storage.types import Provider
from libcloud.storage.providers import get_driver


@fixture
def libcloud_local(fs):
    key = '/location'
    Path(key).mkdir(parents=True)
    cls = get_driver(Provider.LOCAL)
    driver = cls(key)
    print(f'fixture: tmp dir before yield: {tempfile.gettempdir()} - exists:  {Path(tempfile.gettempdir()).exists()}')
    yield driver
    print(f'fixture: tmp dir after yield: {tempfile.gettempdir()} - exists:  {Path(tempfile.gettempdir()).exists()}')
    # cleanup containers
    for container in driver.iterate_containers():
        driver.delete_container(container)

def test_create_container_ok(libcloud_local):
    libcloud_local.create_container('c1')

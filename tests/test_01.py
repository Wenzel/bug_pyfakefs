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
    yield driver
    # cleanup containers
    for container in driver.iterate_containers():
        driver.delete_container(container)

def test_create_container_ok(libcloud_local):
    libcloud_local.create_container('c1')

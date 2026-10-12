import pytest
from server.Cache import Cache
from common.Request import Request
from common.Payload import Payload
from common.Address import Address
from common.Commands import OK_STATUS, ERROR_STATUS

REQUEST = Request(Payload(123, "List"), Address(("127.0.0.1", 5011)))
REQUEST_WRONG = Request(Payload(124, "List"), Address(("127.0.0.1", 5011)))

FIXTURE_DICT = {
    1: ("Ice Мороженое 10", OK_STATUS),
    2: ("Invalid quantity <test>", ERROR_STATUS),
    123: None
}

initRecordParams = [
    (REQUEST, (None, None)),
    (None, None)
]

setDataByRequest = [
    (REQUEST, "Test", OK_STATUS),
    ("str", None, None),
    (None, None, None),
    (REQUEST, "Test", 1)
]

getDataByRequestParams = [
    (REQUEST, ("Test", OK_STATUS)),
    (REQUEST_WRONG, (None, None)),
    (None, (None, None))
]

removeByRequestParams = [
    (REQUEST, 123),
    (None, 123),
    ("", 123)
]

@pytest.fixture
def cache() -> Cache:
    cache = Cache()
    cache._storage = FIXTURE_DICT

    return cache

class TestCache:
    def test_constructor(self):
        cache = Cache()
        assert cache._storage is not None
        assert len(cache._storage) == 0


    @pytest.mark.parametrize("requestObject, expected_output", initRecordParams)
    def test_init_record(self, requestObject: Request, expected_output, cache: Cache):
        cache.initRecord(requestObject)
        try:
            assert cache._storage[requestObject.getId()] == expected_output
        except:
            assert True


    def test_list_records(self, cache):
        assert cache.listRecords() == FIXTURE_DICT


    @pytest.mark.parametrize("requestObject, data, status", setDataByRequest)
    def test_set_data_by_request(self, requestObject: Request, data, status, cache: Cache):
        cache.setDataByRequest(requestObject, data, status)
        try:
            assert cache._storage[requestObject.getId()] == data
        except:
            assert True


    @pytest.mark.parametrize("requestObject, expected_output", getDataByRequestParams)
    def test_get_data_by_request(self, requestObject: Request, expected_output, cache: Cache):
        assert cache.getDataByRequest(requestObject) == expected_output


    @pytest.mark.parametrize("requestObject, id", removeByRequestParams)
    def test_remove_by_request(self, requestObject: Request, id, cache: Cache):
        cache.removeByRequest(requestObject)
        try:
            cache._storage[id]
            assert False
        except:
            assert True

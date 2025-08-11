from coordinator import run_all_providers

DUMMY_AUDIO = __file__

def test_run_all_providers():
    results = run_all_providers(DUMMY_AUDIO)
    assert isinstance(results, list)
    assert len(results) == 4
    for result in results:
        assert 'provider' in result
        assert 'language' in result
        assert 'status' in result

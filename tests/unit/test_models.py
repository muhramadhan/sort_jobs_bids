import datetime
import app

def test_sort_jobs(data_sort_jobs):
    expected_id = [4,5,7,6,3,1,2]
    app.sort_job(data_sort_jobs)
    for index in range(len(data_sort_jobs)):
        assert data_sort_jobs[index].id == expected_id[index]

def test_sort_bids(data_sort_bids):
    expected_id = [3,2,4,5,1]
    app.sort_bid(data_sort_bids)
    for index in range(len(data_sort_bids)):
        assert data_sort_bids[index].id == expected_id[index]

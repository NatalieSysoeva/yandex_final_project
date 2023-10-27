# Наталья Сысоева, 10-я когорта

import sender_stand_request

def test_get_order_info_by_track():
    track_number = sender_stand_request.get_order_info_by_track()
    assert track_number.status_code == 200


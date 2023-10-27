import data
import configuration
import requests

# Создание заказа
def create_order(order_body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=order_body)

# Получение номера заказа
def get_order_track():
    track_response = create_order(data.order_body)
    return track_response.json()["track"]

# Получение информации о заказе по номеру заказа
def get_order_info_by_track():
    track = get_order_track()
    track_params = {"t": track}
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_INFO_BY_TRACK_PATH, params=track_params)






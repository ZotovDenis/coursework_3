import main.code


def test_all_executed_values():
    assert main.code.all_executed_values([{"id": 736942989, "state": "EXECUTED"}]) == [{
        "id": 736942989, "state": "EXECUTED"}]
    assert main.code.all_executed_values([{"id": 816266176, "state": "CANCELED"}]) == []


def test_sort_date():
    assert main.code.sort_date(
        [{"id": 736942989, "state": "EXECUTED", "date": "2020-01-01"},
         {"id": 816266176, "state": "CANCELED", "date": "2020-01-02"}]) == [
               {"id": 816266176, "state": "CANCELED", "date": "2020-01-02"},
               {"id": 736942989, "state": "EXECUTED", "date": "2020-01-01"}]


def test_transformation_date():
    assert main.code.transformation_date("2019-09-14T00:48:01.081967") == "14.09.2019"
    assert main.code.transformation_date("2018-06-24T00:46:32.422648") == "24.06.2018"
    assert main.code.transformation_date("2018-08-08T16:14:59.936274") == "08.08.2018"


def test_change_date():
    assert main.code.change_date(
        [{"id": 121646999, "state": "CANCELED", "date": "2018-06-08T16:14:59.936274"},
         {"id": 917824439, "state": "EXECUTED", "date": "2019-07-18T12:27:13.355343"}]) == [
               {"id": 121646999, "state": "CANCELED", "date": "08.06.2018"},
               {"id": 917824439, "state": "EXECUTED", "date": "18.07.2019"}]


def test_last_operations():
    assert main.code.last_operations([{"id": 422035015}, {"id": 185048835},
                                      {"id": 280743947}, {"id": 232222017},
                                      {"id": 86608620}, {"id": 902831954}]) == [{"id": 422035015}, {"id": 185048835},
                                                                                {"id": 280743947}, {"id": 232222017},
                                                                                {"id": 86608620}]
    assert main.code.last_operations([{"id": 422035015}, {"id": 185048835},
                                      {"id": 280743947}]) == [{"id": 422035015}, {"id": 185048835}, {"id": 280743947}]


def test_hide_information_from():
    assert main.code.hide_information_from({"description": "Перевод организации",
                                            "from": "Visa Platinum 3530191547567121"}) == \
                                                                                    "Visa Platinum 3530 19** **** 7121"
    assert main.code.hide_information_from({"description": "Перевод организации",
                                            "from": "Счет 17691325653939384901"}) == "Счет 1769 13** **** **** 4901"
    assert main.code.hide_information_from({"description": "Открытие вклада"}) == ""
    assert main.code.hide_information_from({"description": "Перевод с карты на счет",
                                            "from": "MasterCard 8847384717023026"}) == "MasterCard 8847 38** **** 3026"


def test_hide_information_to():
    assert main.code.hide_information_to({"to": "Счет 18889008294666828266"}) == "Счет **8266"
    assert main.code.hide_information_to({"to": "Счет 56363465303962313778"}) == "Счет **3778"

from monitor import check_readings


def test_normal_readings():
    result = check_readings(230, 5, 30)

    assert result == [
        "All readings are within the configured limits"
    ]


def test_high_temperature():
    result = check_readings(230, 5, 85)

    assert "Temperature is outside the configured range" in result


def test_high_voltage():
    result = check_readings(260, 5, 30)

    assert "Voltage is outside the configured range" in result


def test_high_current():
    result = check_readings(230, 12, 30)

    assert "Current is outside the configured range" in result

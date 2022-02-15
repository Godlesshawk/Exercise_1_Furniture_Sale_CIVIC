import pytest
from decimal import Decimal
from datetime import date
from dummy_furniture_sale import calculate_discount

_test_data_valid_input = [
    pytest.param( date( 2022, 1, 1 ), Decimal( "0.01" ), Decimal( "0.00" ), id = "1" ),
    pytest.param( date( 2022,11,25 ), Decimal( "0.01" ), Decimal( "0.00" ), id = "2" ),
    pytest.param( date( 2022,12,27 ), Decimal( "0.01" ), Decimal( "0.00" ), id = "3" ),
    pytest.param( date( 2022,12,31 ), Decimal( "0.01" ), Decimal( "0.00" ), id = "4" ),
    pytest.param( date( 2022,11,28 ), Decimal( "0.01" ), Decimal( "0.05" ), id = "5" ),
    pytest.param( date( 2022,12,23 ), Decimal( "0.01" ), Decimal( "0.05" ), id = "6" ),
    pytest.param( date( 2022,11,26 ), Decimal( "0.01" ), Decimal( "0.10" ), id = "7" ),
    pytest.param( date( 2022,12,24 ), Decimal( "0.01" ), Decimal( "0.10" ), id = "8" ),
    pytest.param( date( 2022, 1, 1 ), Decimal( "99.99" ), Decimal( "0.00" ), id = "9" ),
    pytest.param( date( 2022,11,25 ), Decimal( "99.99" ), Decimal( "0.00" ), id = "10" ),
    pytest.param( date( 2022,12,27 ), Decimal( "99.99" ), Decimal( "0.00" ), id = "11" ),
    pytest.param( date( 2022,12,31 ), Decimal( "99.99" ), Decimal( "0.00" ), id = "12" ),
    pytest.param( date( 2022,11,28 ), Decimal( "99.99" ), Decimal( "0.05" ), id = "13" ),
    pytest.param( date( 2022,12,23 ), Decimal( "99.99" ), Decimal( "0.05" ), id = "14" ),
    pytest.param( date( 2022,11,26 ), Decimal( "99.99" ), Decimal( "0.10" ), id = "15" ),
    pytest.param( date( 2022,12,24 ), Decimal( "99.99" ), Decimal( "0.10" ), id = "16" ),
    pytest.param( date( 2022, 1, 1 ), Decimal( "100.00" ), Decimal( "0.00" ), id = "17" ),
    pytest.param( date( 2022,11,25 ), Decimal( "100.00" ), Decimal( "0.00" ), id = "18" ),
    pytest.param( date( 2022,12,27 ), Decimal( "100.00" ), Decimal( "0.00" ), id = "19" ),
    pytest.param( date( 2022,12,31 ), Decimal( "100.00" ), Decimal( "0.00" ), id = "20" ),
    pytest.param( date( 2022,11,28 ), Decimal( "100.00" ), Decimal( "0.1" ), id = "21" ),
    pytest.param( date( 2022,12,23 ), Decimal( "100.00" ), Decimal( "0.1" ), id = "22" ),
    pytest.param( date( 2022,11,26 ), Decimal( "100.00" ), Decimal( "0.10" ), id = "23" ),
    pytest.param( date( 2022,12,24 ), Decimal( "100.00" ), Decimal( "0.10" ), id = "24" ),
    pytest.param( date( 2022, 1, 1 ), Decimal( "100.01" ), Decimal( "0.00" ), id = "25" ),
    pytest.param( date( 2022,11,25 ), Decimal( "100.01" ), Decimal( "0.00" ), id = "26" ),
    pytest.param( date( 2022,12,27 ), Decimal( "100.01" ), Decimal( "0.00" ), id = "27" ),
    pytest.param( date( 2022,12,31 ), Decimal( "100.01" ), Decimal( "0.00" ), id = "28" ),
    pytest.param( date( 2022,11,28 ), Decimal( "100.01" ), Decimal( "0.1" ), id = "29" ),
    pytest.param( date( 2022,12,23 ), Decimal( "100.01" ), Decimal( "0.1" ), id = "30" ),
    pytest.param( date( 2022,11,26 ), Decimal( "100.01" ), Decimal( "0.10" ), id = "31" ),
    pytest.param( date( 2022,12,24 ), Decimal( "100.01" ), Decimal( "0.10" ), id = "32" ),
    pytest.param( date( 2022, 1, 1 ), Decimal( "499.99" ), Decimal( "0.00" ), id = "33" ),
    pytest.param( date( 2022,11,25 ), Decimal( "499.99" ), Decimal( "0.00" ), id = "34" ),
    pytest.param( date( 2022,12,27 ), Decimal( "499.99" ), Decimal( "0.00" ), id = "35" ),
    pytest.param( date( 2022,12,31 ), Decimal( "499.99" ), Decimal( "0.00" ), id = "36" ),
    pytest.param( date( 2022,11,28 ), Decimal( "499.99" ), Decimal( "0.1" ), id = "37" ),
    pytest.param( date( 2022,12,23 ), Decimal( "499.99" ), Decimal( "0.1" ), id = "38" ),
    pytest.param( date( 2022,11,26 ), Decimal( "499.99" ), Decimal( str( ( 0.10 + 0.10 ) - ( 0.10 * 0.10 ) ) ), id = "39" ),
    pytest.param( date( 2022,12,24 ), Decimal( "499.99" ), Decimal( str( ( 0.10 + 0.10 ) - ( 0.10 * 0.10 ) ) ), id = "40" ),
    pytest.param( date( 2022, 1, 1 ), Decimal( "500.00" ), Decimal( "0.00" ), id = "41" ),
    pytest.param( date( 2022,11,25 ), Decimal( "500.00" ), Decimal( "0.00" ), id = "42" ),
    pytest.param( date( 2022,12,27 ), Decimal( "500.00" ), Decimal( "0.00" ), id = "43" ),
    pytest.param( date( 2022,12,31 ), Decimal( "500.00" ), Decimal( "0.00" ), id = "44" ),
    pytest.param( date( 2022,11,28 ), Decimal( "500.00" ), Decimal( "0.2" ), id = "45" ),
    pytest.param( date( 2022,12,23 ), Decimal( "500.00" ), Decimal( "0.2" ), id = "46" ),
    pytest.param( date( 2022,11,26 ), Decimal( "500.00" ), Decimal( str( ( 0.20 + 0.10 ) - ( 0.20 * 0.10 ) ) ), id = "47"),
    pytest.param( date( 2022,12,24 ), Decimal( "500.00" ), Decimal( str( ( 0.20 + 0.10 ) - ( 0.20 * 0.10 ) ) ), id = "48"),
    pytest.param( date( 2022, 1, 1 ), Decimal( "500.01" ), Decimal( "0.00" ), id = "49" ),
    pytest.param( date( 2022,11,25 ), Decimal( "500.01" ), Decimal( "0.00" ), id = "50" ),
    pytest.param( date( 2022,12,27 ), Decimal( "500.01" ), Decimal( "0.00" ), id = "51" ),
    pytest.param( date( 2022,12,31 ), Decimal( "500.01" ), Decimal( "0.00" ), id = "52" ),
    pytest.param( date( 2022,11,28 ), Decimal( "500.01" ), Decimal( "0.2" ), id = "53" ),
    pytest.param( date( 2022,12,23 ), Decimal( "500.01" ), Decimal( "0.2" ), id = "54" ),
    pytest.param( date( 2022,11,26 ), Decimal( "500.01" ), Decimal( str( ( 0.20 + 0.10 ) - ( 0.20 * 0.10 ) ) ), id = "55"),
    pytest.param( date( 2022,12,24 ), Decimal( "500.01" ), Decimal( str( ( 0.20 + 0.10 ) - ( 0.20 * 0.10 ) ) ), id = "56")
]

@pytest.mark.parametrize( "total,day,expected", _test_data_valid_input )
def test_valid_input( total: Decimal, day: date, expected: Decimal ):

    value = calculate_discount( total, day )

    assert value == expected

_test_data_invalid_input = [
    pytest.param( date( 2022,12,24 ), "a", id = "57" ),
    pytest.param( date( 2022,12,24 ), Decimal( "0.00" ), id = "58" ),
    pytest.param( date( 2022,12,24 ), Decimal( "-0.01" ), id = "59" ),
    pytest.param( date( 2022,12,24 ), Decimal( "-5000.00" ), id = "60" ),
    pytest.param( "a", Decimal( "5.00" ), id = "61" ),
    pytest.param( date( 2022,11,27 ), Decimal( "50.00" ), id = "62" ),
    pytest.param( date( 2022,12,26 ), Decimal( "500.00" ), id = "63" )]

@pytest.mark.parametrize( "total,day", _test_data_invalid_input )
def test_invalid_input( total: Decimal, day: date ):
    with pytest.raises( ValueError ):
        calculate_discount( total, day )
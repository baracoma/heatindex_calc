def celsius(temperature, humidity):
    """
    Based on Wikipedia heat index formula 3
    http://en.wikipedia.org/wiki/Heat_index#Formula
    """
    # Heat Index is calculated in F, so convert to C
    T = (float(temperature) * 9.0/5.0) + 32.0
    R = float(humidity)

    Rsquared = pow(R, 2.0)
    Tsquared = pow(T, 2.0)
    Rcubed = pow(R, 3.0)
    Tcubed = pow(T, 3.0)

    # coefficients for calculation
    c = [None, 16.932, 0.185212, 5.37941, -0.100254, 9.41695 * pow(10.0, -3.0),
    7.28898 * pow(10.0, -3.0), 3.45372 * pow(10.0, -4.0), -8.14971 * pow(10.0, -4.0),
    1.02102 * pow(10.0, -5.0), -3.8646 * pow(10.0, -5.0), 2.91583 * pow(10,-5.0),
    1.42721 * pow(10.0, -6.0), 1.97483 * pow(10.0, -7.0), -2.18429 * pow(10.0, -8.0),
    8.43296 * pow(10.0, -10.0), -4.81975 * pow(10.0 ,-11.0)]

    heat_index = ( c[1] + (c[2]* T) + (c[3]* R) + (c[4]* T * R) +
                    (c[5] * Tsquared) + (c[6] * Rsquared) +
                    (c[7] * Tsquared * R) + (c[8] * T * Rsquared) +
                    (c[9] * Tsquared * Rsquared)  + (c[10] * Tcubed) +
                    (c[11] * Rcubed) + (c[12] * Tcubed * R) +
                    (c[13] * T * Rcubed) + (c[14] * Tcubed * Rsquared)+
                    (c[15] * Tsquared * Rcubed) + (c[16]) * Tcubed * Rcubed)

    # round to one decimal place and return in celsius
    return round(((heat_index - 32.0) * 5.0/9.0), 1)
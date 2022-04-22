## @file stocks_calculator.py
#  @brief stock algorithms
#  @date March 17, 2022


## @brief Calculates the profit gain or loss when a broker is used
#  @param shares A float that represents the amount of shares of a stock
#  @param purchasePrice A float that represents the purchase price of the stock
#  @param sellPrice A float that represents the price the stock was sold at
#  @param buyCommission A float that represents the price of commission the broker
#  charged at purchase
#  @param sellCommission A float that represents the price of commission the broker
#  charged when sold
#  @return The gain or loss on the stock
#  @throws ValueError Throws an exception if inputs are strings
def calcUserGainLossCase1(shares, purchasePrice, sellPrice, buyCommission, sellCommission):
    if(isinstance(shares, str)):
        raise ValueError

    if(isinstance(purchasePrice, str)):
        raise ValueError

    if(isinstance(sellPrice, str)):
        raise ValueError

    if(isinstance(buyCommission, str)):
        raise ValueError

    if(isinstance(sellCommission, str)):
        raise ValueError

    user_gain_loss_1 = ((sellPrice * shares) - sellCommission) - (
        (purchasePrice * shares) + buyCommission)
    return user_gain_loss_1

## @brief Calculates the profit gain or loss when a broker is not used
#  @param shares A float that represents the amount of shares of a stock
#  @param purchasePrice A float that represents the purchase price of the stock
#  @param sellPrice A float that represents the price the stock was sold at
#  @return The gain or loss on the stock
#  @throws ValueError Throws an exception if inputs are strings
def calcUserGainLossCase2(shares, purchasePrice, sellPrice):
    if(isinstance(shares, str)):
        raise ValueError

    if(isinstance(purchasePrice, str)):
        raise ValueError

    if(isinstance(sellPrice, str)):
        raise ValueError
        
    user_gain_loss_2 = (sellPrice * shares) - (
            (purchasePrice * shares))
    return user_gain_loss_2
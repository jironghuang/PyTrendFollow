"""

This file defines the instruments the system has access to.

These may change from time-to-time. If you make reasonable changes, please submit a pull request at https://github.com/chrism2671/PyTrendFollow so we can update it for everybody.

See the defaults in core/instrument.py and extra parameters not shown here.

Schema:

{
    'name': 'corn',                         # Unique shorthand name which we can refer to this instrument by
    'contract_data': ['ib', 'quandl'],      # Data providers we should collect and merge data from 
    'months_traded': [3, 5, 7, 9, 12],      # Months that this contract is available for trading
    'first_contract': 196003,               # First month this contract traded, so we know when to download from (March 1960)
    'backtest_from_contract': 199312,       # Backtest from this month (December 1993)
    'trade_only': [12],                     # Trade only these contract months (December - the 'Z' contract)
    'quandl_symbol': 'C',                   # Symbol on Quandl representing this contract
    'quandl_database': 'CME',               # Database on Quandl providing contract data
    'ib_code': 'ZC',                        # Symbol on Interactive Brokers representing this contract
    'denomination' 'USD',                   # Currency of the contract. Default is 
    'roll_day': -20,                        # Day of month to roll to next contract. If it's negative, it's this day in the previous month. For example, if we are in the December contract, a roll_day of -20 means roll on November 20th.
    'exchange': 'ECBOT',                    # Exchange identifier on Interactive Brokers.
    'point_value': 50,                      # $ move per point move on the futures contract. Usually equal to the contract multiplier.
    'spread': 0.25,                         # Estimated spread, for estimating costs
    'commission': 2.81,                     # Interactive Brokers per contract commission in base currency
},


When setting roll days, we can't let it get to close to the expiry dates. Interactive Brokers require us to be out of a contract well before expiry. The dates for each contract are on this page: https://www.interactivebrokers.co.uk/en/index.php?f=deliveryExerciseActions&p=physical

"""

from core.currency import Currency
from core.spot import Spot

MONTHLY = list(range(1, 13))
QUARTERLY = [3, 6, 9, 12]
ODDS = [1, 3, 5, 7, 9, 11]
EVENS = [2, 4, 6, 8, 10, 12]

instruments_all = {
    ### Soft ###

    'soft': [
        {
            'name': 'arabica',
            'fullname': 'Arabica ICE Coffee C',
            'contract_data': ['quandl'],
            'quandl_database': 'ICE',
            'quandl_data_factor': 100,
            'quandl_symbol': 'KC',
            'first_contract': 197312,
            'months_traded': [3, 5, 7, 9, 12],
            'trade_only': [3, 5, 7, 9, 12],
            'denomination': 'USD',
            'ib_code': 'KC',
            'point_value': 37500,
            'exchange': 'NYBOT',
            'roll_day': -19,
            'spread': 0.0005,
        }, {
            'name': 'cattle',
            'fullname': 'Live Cattle',
            'contract_data': ['ib', 'quandl'],
            'quandl_symbol': 'LC',
            'quandl_database': 'CME',
            'first_contract': 196512,
            'months_traded': EVENS,
            'trade_only': [4, 8, 12],
            'denomination': 'USD',
            'ib_code': 'LE',
            'roll_day': -15,
            'exchange': 'GLOBEX',
            'point_value': 400,
            'spread': 0.025,
        }, {
            'name': 'cocoa',
            'fullname': 'Cocoa (London)',
            'contract_data': ['quandl'],
            'quandl_database': 'LIFFE',
            'quandl_symbol': 'C',
            'first_contract': 199309,
            'months_traded': [3, 9, 12],
            'trade_only': [3, 9, 12],
            'denomination': 'GBP',
            'ib_code': 'C',
            'point_value': 10,
            'exchange': 'ICEEUSOFT',
            'roll_day': 1,
            'spread': 1,
        }, {
            'name': 'cotton',
            'fullname': 'Cotton No 2',
            'contract_data': ['quandl'],
            'quandl_database': 'ICE',
            'quandl_symbol': 'CT',
            'quandl_data_factor': 100,
            'first_contract': 197203,
            'months_traded': [3, 5, 7, 10, 12],
            'trade_only': [12],
            'denomination': 'USD',
            'ib_code': 'CT',
            'point_value': 50000,
            'exchange': 'NYBOT',
            'roll_day': -15,
            'spread': 0.0003,
        }, {
            'name': 'feeder',
            'contract_data': ['ib', 'quandl'],
            'quandl_symbol': 'FC',
            'quandl_database': 'CME',
            'first_contract': 197403,
            'months_traded': [1, 3, 4, 5, 8, 9, 10, 11],
            'trade_only': [1, 3, 4, 5, 8, 9, 10, 11],
            'denomination': 'USD',
            'ib_code':'GF',
            'roll_day':-15,
            'exchange': 'GLOBEX',
            'point_value': 500,
            'spread':0.1,
        }, {
            'name': 'wheat',
            'contract_data': ['ib', 'quandl'],
            'quandl_database': 'CME',
            'quandl_symbol': 'W',
            'first_contract': 195912,
            'months_traded': [3, 5, 7, 9, 12],
            'trade_only': [3, 5, 7, 9, 12],
            'roll_day': -20,
            'ib_code': 'ZW',
            'exchange': 'ECBOT',
            'point_value': 50,
            'spread': 0.25,
            'commission': 2.81,
        }, {
            'name': 'corn',
            'contract_data': ['ib', 'quandl'],
            'months_traded': [3, 5, 7, 9, 12],
            'first_contract': 196003,
            'backtest_from_contract': 199312,
            'trade_only': [12],
            'quandl_symbol': 'C',
            'quandl_database': 'CME',
            'ib_code': 'ZC',
            'roll_day': -20,
            'exchange': 'ECBOT',
            'point_value': 50,
            'spread': 0.25,
            'commission': 2.81,
        }, {
        #Trade the front 2 contracts only
            'name': 'leanhog',
            'contract_data': ['ib', 'quandl'],
            'quandl_database': 'CME',
            'quandl_symbol': 'LN',
            'first_contract': 197002,
            'roll_day': 7,
            'months_traded': [2, 4, 6, 8, 10, 12],
            'trade_only': [2, 4, 6, 8, 10, 12],
            'ib_code': 'HE',
            'exchange': 'GLOBEX',
            'point_value': 400,
            'spread': 0.025,
            'commission': 2.89,
        }, {
            'name': 'oats',
            'contract_data': ['ib', 'quandl'],
            'fullname': 'Oats (CME)',
            'quandl_symbol': 'O',
            'quandl_database': 'CME',
            'first_contract': 197003,
            'months_traded': [3, 5, 7, 9, 12],
            'trade_only': [7, 12],
            'denomination': 'USD',
            'ib_code':'ZO',
            'roll_day':-15,
            'exchange': 'ECBOT',
            'point_value':50,
            'spread':0.25, #guess
        }, {
            'name': 'robusta',
            'contract_data': ['quandl'],
            'fullname': 'Robusta Coffee (LIFFE)',
            'quandl_database': 'LIFFE',
            'quandl_symbol': 'RC',
            'first_contract': 199309,
            'months_traded': ODDS,
            'trade_only': ODDS,
            'denomination': 'USD',
            'ib_code': 'D',
            'point_value': 10,
            'exchange': 'ICEEUSOFT',
            'roll_day': 1,
            'spread': 5,
        }, {
            'name':'soybean',
            'contract_data': ['ib', 'quandl'],
            'quandl_database': 'CME',
            'quandl_symbol': 'S',
            'first_contract': 196208,
            'months_traded': [1, 3, 5, 7, 8, 9, 11],
            'trade_only': [11],
            'roll_day': 5,
            'denomination': 'USD',
            'ib_code': 'ZS',
            'exchange': 'ECBOT',
            'point_value': 50,
            'spread': 0.25,
        }, {
            'name': 'soymeal',
            'fullname': 'Soybean Meal',
            'contract_data': ['ib', 'quandl'],
            'quandl_database': 'CME',
            'quandl_symbol': 'SM',
            'first_contract': 196401,
            'months_traded': [1, 3, 5, 7, 8, 9, 10, 12],
            'trade_only': [7, 12],
            'denomination': 'USD',
            'ib_code': 'ZM',
            'point_value': 100,
            'exchange': 'ECBOT',
            'roll_day': -15,
            'spread': 0.1,
        }, {
            'name': 'soyoil',
            'fullname': 'Soybean Oil',
            'contract_data': ['ib', 'quandl'],
            'quandl_database': 'CME',
            'quandl_symbol': 'BO',
            'first_contract': 196101,
            'months_traded': [1, 3, 5, 7, 8, 9, 10, 12],
            'trade_only': [7, 12],
            'denomination': 'USD',
            'ib_code': 'ZL',
            'point_value': 600,
            'exchange': 'ECBOT',
            'roll_day': -15,
            'spread': 0.01,
        }, {
            'name': 'sugar',
            'fullname': 'White Sugar (ICE)',
            'contract_data': ['quandl'],
            'quandl_database': 'LIFFE',
            'quandl_symbol': 'W',
            'first_contract': 199310,
            'months_traded': [3, 5, 8, 10, 12],
            'trade_only': [3, 5, 8, 10, 12],
            'denomination': 'USD',
            'ib_code': 'W',
            'point_value': 50,
            'exchange': 'ICEEUSOFT',
            'expiration_month': -1,
            'roll_day': 1,
            'spread': 0.2,
        },
    ],


    ### Currencies ###

    'currency': [
        {
            'name': 'mxp',
            'contract_data': ['ib', 'quandl'],
            'quandl_database': 'CME',
            'quandl_symbol': 'MP',
            'first_contract': 199603,
            'trade_only': [3, 6, 9, 12],
            'ib_code': 'MXP',
            'roll_day': 5,
            'exchange': 'GLOBEX',
            'quandl_data_factor': 1000000,
            'point_value': 500000,
            'denomination': 'USD',
            'spread': .00001,
            'spot': Currency('MXNUSD').rate,
            'expiry': 18,
        }, {
            'name': 'aud',
            'contract_data': ['ib', 'quandl'],
            'quandl_database': 'CME',
            'quandl_symbol': 'AD',
            'first_contract': 198703,
            'months_traded': QUARTERLY,
            'trade_only': QUARTERLY,
            'roll_day': 10,
            'denomination': 'USD',
            'ib_code': 'AUD',
            'exchange': 'GLOBEX',
            'point_value': 100000,
            'spread': 0.0001,
            'spot': Currency('AUDUSD').rate,
            'expiry': 18,
        }, {
            'name': 'eur',
            'contract_data': ['ib', 'quandl'],
            'quandl_symbol': 'EC',
            'quandl_database': 'CME',
            'first_contract': 199903,
            'months_traded': [3, 6, 9, 12],
            'trade_only': [3, 6, 9, 12],
            'denomination': 'USD',
            'ib_code':'EUR',
            'roll_day':5,
            'exchange': 'GLOBEX',
            'point_value': 125000,
            'spread':0.00005,
            'spot': Currency('EURUSD').rate,
            'expiry': 18,
        }, {
            'name': 'gbp',
            'contract_data': ['ib', 'quandl'],
            'quandl_database': 'CME',
            'quandl_symbol': 'BP',
            'first_contract': 197509,
            'roll_day': 5,
            'months_traded': [3, 6, 9, 12],
            'trade_only': [3, 6, 9, 12],
            'ib_code': 'GBP',
            'exchange': 'GLOBEX',
            'point_value': 62500,
            'denomination': 'USD',
            'spread': .0001,
            'spot': Currency('GBPUSD').rate,
            'expiry': 18,
        }, {
            'name':'nzd',
            'contract_data': ['ib', 'quandl'],
            'quandl_symbol': 'NE',
            'quandl_database': 'CME',
            'first_contract': 200403,
            'months_traded': [3, 6, 9, 12],
            'trade_only': [3, 6, 9, 12],
            'denomination': 'USD',
            'ib_code':'NZD',
            'roll_day': 8,
            'exchange': 'GLOBEX',
            'point_value': 1E6,
            'spread':0.0001,
            'spot': Currency('NZDUSD').rate,
            'expiry': 18,
        }, {
            'name': 'yen',
            'contract_data': ['ib', 'quandl'],
            'commission': 2.46,
            'quandl_database': 'CME',
            'quandl_symbol': 'JY',
            'first_contract': 197712,
            'months_traded': [3, 6, 9, 12],
            'trade_only': [3, 6, 9, 12],
            'denomination': 'USD',
            'ib_code': 'JPY',
            'exchange': 'GLOBEX',
            'quandl_data_factor': 1000000,
            'point_value': 12500000,
            'spread': .0000005,
            'spot': Currency('JPYUSD').rate,
            'expiry': 18,
        }, {
            'name': 'bitcoin',
            'contract_data': ['ib'],
            'point_value': 1,
            'denomination': 'USD',
            'months_traded': MONTHLY,
            'trade_only': MONTHLY,
            'first_contract': 201801,
            'exchange': 'CFECRYPTO',
            'ib_code': 'GXBT',
            'roll_day': 10,
            'expiry': 14,
           }
    ],


    ### Hard ###

    'hard': [
        {
            'name': 'copper',
            'contract_data': ['ib', 'quandl'],
            'quandl_database': 'CME',
            'quandl_symbol': 'HG',
            'first_contract': 196001,
            'trade_only': [7, 12],
            'months_traded': [1, 3, 5, 7, 9, 10, 12],
            'roll_day': -20,
            'commission': 2.36,
            'spread': 0.0005,
            'ib_code': 'HG',
            'exchange': 'NYMEX',
            'point_value': 25000,
            'denomination': 'USD',
            'expiry': 27,
            'spot': Spot('copper').get,
        }, {
            'name': 'crude',
            'contract_data': ['ib', 'quandl'],
            'quandl_database': 'CME',
            'quandl_symbol': 'CL',
            'first_contract': 198306,
            'trade_only': [12],
            'roll_day': -15,
            'expiration_month': -1,
            'commission': 2.36,
            'spread': 0.01,
            'ib_code': 'CL',
            'exchange': 'NYMEX',
            'point_value': 1000,
            'denomination': 'USD',
        }, {
            'name': 'gas',
            'contract_data': ['ib', 'quandl'],
            'quandl_database': 'CME',
            'quandl_symbol': 'NG',
            'first_contract': 199101,
            'trade_only': [12],
            'spread': 0.001,
            'commission': 2.36,
            'ib_code': 'NG',
            'expiration_month': -1,
            'roll_day': 18,
            'exchange': 'NYMEX',
            'point_value': 10000,
            'denomination': 'USD',
        }, {
            'name': 'gold',
            'contract_data': ['ib', 'quandl'],
            'commission': 2.36,
            'quandl_database': 'CME',
            'quandl_symbol': 'GC',
            'first_contract': 197512,
            'months_traded': [2, 4, 8, 10, 12],
            'trade_only': [12],
            # Cutoff is 30th of the month before (30 Jan for Feb contract)
            'roll_day' : -15,
            'denomination': 'USD',
            'ib_code': 'GC',
            'exchange': 'NYMEX',
            'point_value': 100,
            'spread': 0.10,
            'spot': Spot('gold').get,
            'expiry': 27,
        }, {
            'name': 'pallad',
            'contract_data': ['ib', 'quandl'],
            'quandl_symbol':'PA',
            'quandl_database': 'CME',
            'first_contract':'197703',
            'months_traded': [3,4,5,6,9,12],
            'trade_only': [3,6,9,12],
            'denomination': 'USD',
            'roll_day':-24,
            'ib_code': 'PA',
            'exchange': 'NYMEX',
            'point_value':100,
            'spread':0.50,
            'spot': Spot('pallad').get,
            'expiry': 27,
        }, {
            'name': 'platinum',
            'contract_data': ['ib', 'quandl'],
            'quandl_database': 'CME',
            'quandl_symbol': 'PL',
            'first_contract': 201101,
            'roll_day': -10,
            'months_traded': [1, 2, 3, 4, 7, 10, 12],
            'trade_only': [1, 4, 10],
            'commission': 2.36,
            'spread': 0.1,
            'ib_code': 'PL',
            'exchange': 'NYMEX',
            'point_value': 50,
            'denomination': 'USD',
            'expiry': 27,
            'spot': Spot('platinum').get,
        }, {
            'name': 'silver',
            'fullname': 'Silver',
            'contract_data': ['ib', 'quandl'],
            'quandl_database': 'CME',
            'quandl_symbol': 'SI',
            'first_contract': 196403,
            'months_traded': [1, 3, 5, 7, 9, 12],
            'trade_only': [3, 7, 12],
            'denomination': 'USD',
            'ib_code': 'SI',
            'point_value': 1000,
            'ib_multiplier': 1000,
            'exchange': 'NYMEX',
            'roll_day': -15,
            'spread': 0.005, #GUESS
            'expiry': 27,
            'spot': Spot('silver').get,
        },
    ],


    ### Index ###

    'index': [
        {
            'name': 'aex',
            'fullname': 'Amsterdam Exchange Index',
            'contract_data': ['quandl'],
            'quandl_symbol': 'FTI',
            'quandl_database': 'LIFFE',
            'first_contract': 201310,
            'months_traded': MONTHLY,
            'trade_only': MONTHLY,
            'denomination': 'EUR',
            'ib_code': 'EOE',
            'ib_multiplier': 200,
            'exchange': 'FTA',
            'point_value': 200,
            'roll_day': 12,
            'spread': 0.05,
        }, {
            'name': 'cac',
            'contract_data': ['quandl'],
            'quandl_database': 'LIFFE',
            'quandl_symbol': 'FCE',
            'first_contract': 199903,
            'trade_only': [3, 6, 9, 12],
            'months_traded': [3, 6, 9, 12], #Not true, but others have dodgy data on Quandl
            'roll_day': 1,
            'ib_code': 'CAC40',
            'exchange': 'MONEP',
            'denomination': 'EUR',
            'point_value': 10,
            'ib_multiplier': 10,
            'spread': 0.5,
            'per_contract_cost': 2,
            # 'spot': Index('CAC').close,
            'expiry': 15,
        }, {
            'name': 'dax',
            'fullname': 'DAX Index Future',
            'contract_data': ['quandl'],
            'quandl_database': 'EUREX',
            'quandl_symbol': 'FDAX',
            'first_contract': 199703,
            'months_traded': QUARTERLY,
            'trade_only': QUARTERLY,
            'denomination': 'EUR',
            'ib_code': 'DAX',
            'ib_multiplier': 25,
            'point_value': 25,
            'exchange': 'DTB',
            'roll_day': 1,
            'spread': 1,
            # 'spot': Index('DAX').close,
            'expiry': 15,
        }, {
            'name': 'eurostoxx',
            'contract_data': ['ib', 'quandl'],
            'quandl_symbol': 'FESX',
            'quandl_database': 'EUREX',
            'first_contract': 199809,
            'months_traded': [3, 6, 9, 12],
            'trade_only': [3, 6, 9, 12],
            'denomination': 'EUR',
            'ib_code': 'ESTX50',
            'exchange': 'DTB',
            'point_value': 10,
            'roll_day': 10,
            'spread': 1,
            'spot': Spot('eurostoxx').get
        }, {
            'name': 'ftse',
            'fullname': 'FTSE 100 Index',
            'contract_data': ['quandl'],
            'quandl_database': 'LIFFE',
            'quandl_symbol': 'Z',
            'first_contract': 198406,
            'months_traded': QUARTERLY,
            'trade_only': QUARTERLY,
            'denomination': 'GBP',
            'ib_code': 'Z',
            'point_value': 10,
            'exchange': 'ICEEU',
            'roll_day': 1,
            'spread': 0.5,
            # 'spot': Index('FTSE').close,
            'expiry': 15,
        }, {
            'name': 'hsi',
            'fullname': 'Hang Seng Index',
            'contract_data': ['ib', 'quandl'],
            'quandl_symbol': 'HSI',
            'quandl_database': 'HKEX',
            'quandl_rename_columns': {"Last Traded": 'Settle', "Close": 'Settle'},
            'first_contract': 199709,
            'months_traded': MONTHLY,
            'trade_only': MONTHLY,
            'denomination': 'HKD',
            'ib_code': 'HSI',
            'point_value': 50,
            'commission': 30, #Commission in HKD
            'exchange': 'HKFE',
            'roll_day': 1,
            'spread': 2,
            'expiry': 28,
            'spot': Spot('hsi').get
            # 'spot': Index('HSI').close,
        }, {
            #This is the e-mini version
            'name': 'nasdaq',
            'fullname': 'Nasdaq 100',
            'contract_data': ['ib', 'quandl'],
            'commission': 0.85,
            'quandl_database': 'CME',
            'quandl_symbol': 'NQ',
            'first_contract': 199812,
            'months_traded': [3, 6, 9, 12],
            'trade_only': [3, 6, 9, 12],
            'roll_day': 13,
            'denomination': 'USD',
            'ib_code': 'NQ',
            'exchange': 'GLOBEX',
            'point_value': 20,
            'spread': 0.25,
            # 'spot': Index('IUXX').close,
            'expiry': 15,
        }, {
            'name': 'r2000',
            'fullname': 'Russell 2000 Mini',
            'contract_data': ['quandl'],
            'quandl_database': 'ICE',
            'quandl_symbol': 'TF',
            'first_contract': 200703,
            'months_traded': QUARTERLY,
            'trade_only': QUARTERLY,
            'denomination': 'USD',
            'ib_code': 'TF',
            'point_value': 50,
            'exchange': 'NYBOT',
            'roll_day': 1,
            'spread': 0.1,
            # 'spot': Index('IUX').close,
            'expiry': 15,
        }, {
            'name': 'smi',
            'contract_data': ['ib', 'quandl'],
            'quandl_symbol': 'FSMI',
            'quandl_database': 'EUREX',
            'first_contract': 201309,
            'months_traded': [3, 6, 9, 12],
            'trade_only': [3, 6, 9, 12],
            'denomination': 'CHF',
            'ib_code':'SMI',
            'roll_day': -26, #guess
            'exchange': 'SOFFEX',
            'point_value': 10,
            'spread':2,
            'expiry': 15,
            'spot': Spot('smi').get
            # 'spot': Index('SSMI').close,
        }, {
            'name': 'sp500', #trade the emini version
            'contract_data': ['quandl'],
            'quandl_symbol': 'ES',
            'quandl_database': 'CME',
            'first_contract': 199709,
            'months_traded': [3, 6, 9, 12],
            'trade_only': [3, 6, 9, 12],
            'denomination': 'USD',
            'ib_code': 'ES',
            'exchange': 'GLOBEX',
            'point_value':   50,
            'roll_day': 10,
            'spread': 0.25,
            'expiry': 15,
            # 'spot': Index('INX').close
        },
        {
            'name': 'vix',
            'contract_data': ['ib', 'quandl'],
            'commission': 2.40,
            'quandl_database': 'CBOE',
            'quandl_rename_columns': {"Trade Date": "Date", "Total Volume": "Volume",
                                      # Prevent column duplication after renaming both Close and Settle
                                      "Close": "_Close_"},
            'quandl_symbol': 'VX',
            'first_contract': 200501,
            #Quarterly contracts run for 6 months, other contracts are shorter
            # 'spot': lambda: quandl.get("CBOE/VIX")['VIX Close'],
            # 'expiry': 15,
            'trade_only': [2,5,8,11],
            'rules': ('sell_and_hold',),
            # 'rules': ('ewmac', 'carry_prev',),
            'roll_shift': -91,
            'ib_code': 'VIX',
            'exchange': 'CFE',
            'ib_trading_class': 'VX',
            'ib_multiplier': 1000,
            'point_value': 1000,
            'denomination': 'USD',
            'spread': 0.01,
        }, {
            'name': 'vstoxx',
            'contract_data': ['quandl'],
            'commission': 0.0211,
            'quandl_database': 'EUREX',
            'quandl_symbol': 'FVS',
            'first_contract': 201401,
            'roll_day': 15,
            # 'rules': ('ewmac', 'carry_prev',),
            'rules': ('sell_and_hold',),
            'roll_shift': -61,
            'trade_only': [1, 3, 5, 7, 9, 11],
            'denomination': 'EUR',
            'ib_code': 'V2TX',
            'exchange': 'DTB',
            'point_value': 100,
            'spread':0.05,
        },
    ],

    ### Rate ###

    'rate': [
        {
            'name': 'eurodollar',
            'contract_data': ['ib', 'quandl'],
            'quandl_symbol': 'ED',
            'first_contract': 199603,
            'months_traded': QUARTERLY,
            'trade_only': [12],
            'quandl_database': 'CME',
            'ib_code': 'GE',
            'exchange': 'GLOBEX',
            'point_value': 2500,
            'denomination': 'USD',
            'spread': 0.005,
            'roll_shift': -900,
            'rules': ('ewmac', 'carry_prev'),
            'commission': 2.11,
        }, {
            'name': 'us2',
            'contract_data': ['ib', 'quandl'],
            'quandl_database': 'CME',
            'quandl_symbol': 'TU',
            'first_contract': 199303,
            'roll_day': -20,
            'months_traded': [3, 6, 9, 12],
            'trade_only': [3, 6, 9, 12],
            'spread': 0.0078125,
            'commission': 1.46,
            'ib_code': 'ZT',
            'exchange': 'ECBOT',
            'point_value': 2000,
            'denomination': 'USD',
        }, {
            'name': 'bobl',
            'contract_data': ['quandl'],
            'quandl_database': 'EUREX',
            'quandl_symbol': 'FGBM',
            'first_contract': 199903,
            'roll_day': -25,
            'months_traded': [3, 6, 9, 12],
            'trade_only': [3, 6, 9, 12],
            'denomination': 'EUR',
            'ib_code': 'GBM',
            'point_value': 1000,
            'exchange': 'DTB',
            'spread': 0.01,
            'per_contract_cost': 2,
            'rules': ('ewmac',),
        }, {
            'name': 'bund',
            'contract_data': ['quandl'],
            'quandl_symbol': 'FGBL',
            'quandl_database': 'EUREX',
            'first_contract': 201303,
            'months_traded': [3, 6, 9, 12],
            'trade_only': [3, 6, 9, 12],
            'denomination': 'EUR',
            'ib_code':'GBL',
            'roll_day':-25,
            'exchange': 'DTB',
            'point_value': 1000,
            'spread':0.01,
        }, {
            'name': 'us30',
            'contract_data': ['ib', 'quandl'],
            'quandl_symbol': 'US',
            'quandl_database': 'CME',
            'first_contract': 197712,
            'months_traded': [3, 6, 9, 12],
            'trade_only': [3, 6, 9, 12],
            'denomination': 'USD',
            'ib_code':'ZB',
            'roll_day':-24,
            'exchange': 'ECBOT',
            'point_value':1000,
            'spread':1/32,
        }, {
            'name': 'longbtp',
            'contract_data': ['quandl'],
            'quandl_symbol': 'FBTP',
            'quandl_database': 'EUREX',
            'first_contract': 201303,
            'months_traded': [3, 6, 9, 12],
            'trade_only': [3, 6, 9, 12],
            'denomination': 'EUR',
            'ib_code': 'BTP',
            'exchange': 'DTB',
            'point_value': 1000,
            'roll_day': -25,
            'spread': 0.1,
        }, {
            'name': 'eurooat',
            'contract_data': ['quandl'],
            'fullname': 'French government bond',
            'quandl_symbol': 'FOAT',
            'quandl_database': 'EUREX',
            'first_contract': 201303,
            'months_traded': QUARTERLY,
            'trade_only': QUARTERLY,
            'denomination': 'EUR',
            'ib_code': 'OAT',
            'ib_multiplier': 1000,
            'point_value': 1000,
            'exchange': 'DTB',
            'roll_day': -25,
            'spread': 0.01,
        },
    ],

    #### Bitmex ####
    # 'bitmex': [
    #     {
    #         'name': 'btc',
    #         'contract_data': ['bitmex'],
    #         'bitmex_symbol': 'XBT',
    #         # 'first_contract': 201606,
    #         'first_contract': 201506,
    #         'months_traded': [3, 6, 9, 12],
    #         'trade_only': [3, 6, 9, 12],
    #         'roll_day': 27,
    #         'denomination': 'USD',
    #         'broker': 'bitmex',
    #         'contract_name_format': 'bitmex',
    #         'point_value': 1,
    #         'spread': 0.01,
    #         'rules': ('ewmac'), #  'carry_spot'),
    #         'spot': Currency('BTCUSD').rate,
    #         'maker_fee': -0.025,  # Still to implement
    #         'taker_fee': 0.075,
    #     },
    #     {
    #         'name': 'xbj',
    #         'contract_data': ['bitmex'],
    #         'fullname': 'Bitcoin/Yen',
    #         'bitmex_symbol': 'XBJ',
    #         'first_contract': 201609,
    #         'months_traded': [3, 6, 9, 12],
    #         'trade_only': [3, 6, 9, 12],
    #         'roll_day': 29,
    #         'denomination': 'JPY',
    #         'broker': 'bitmex',
    #         'contract_name_format': 'bitmex',
    #         'point_value': 1,
    #         'spread': 24.5,
    #         'rules': ('ewmac', 'carry_spot'),
    #         'spot': Spot(data_prov='bitmex', symbol='.XBTJPY', col='close').get,
    #     },
    #     {
    #         'name': 'bat',
    #         'contract_data': ['bitmex'],
    #         'bitmex_symbol': 'BAT',
    #         'first_contract': 201706,
    #         'months_traded': [6, 9],
    #         'trade_only': [6, 9],
    #         'roll_day': 29,
    #         'denomination': 'BTC',
    #         'broker': 'bitmex',
    #         'contract_name_format': 'bitmex',
    #         'point_value': 1,
    #         'spread': 3.19e-7,
    #         'rules': ('ewmac', 'carry_spot'),
    #         'spot': Spot(data_prov='bitmex', symbol='.BATXBT', col='close').get,
    #     },
    #     {
    #         'name': 'dash',
    #         'contract_data': ['bitmex'],
    #         'bitmex_symbol': 'DASH',
    #         'first_contract': 201704,
    #         'months_traded': [4, 6, 9],
    #         'trade_only': [4, 6, 9],
    #         'roll_day': 29,
    #         'denomination': 'BTC',
    #         'broker': 'bitmex',
    #         'contract_name_format': 'bitmex',
    #         'point_value': 1,
    #         'spread': 1.0e-4,
    #         'rules': ('ewmac', 'carry_spot'),
    #         'spot': Spot(data_prov='bitmex', symbol='.DASHXBT', col='close').get,
    #     },
    #     {
    #         'name': 'ethereum',
    #         'contract_data': ['bitmex'],
    #         'bitmex_symbol': 'ETH',
    #         'first_contract': 201704,
    #         'months_traded': [4, 6, 9],
    #         'trade_only': [4, 6, 9],
    #         'roll_day': 29,
    #         'denomination': 'BTC',
    #         'broker': 'bitmex',
    #         'contract_name_format': 'bitmex',
    #         'point_value': 1,
    #         'spread': 1.0e-4,
    #         'rules': ('ewmac', 'carry_spot'),
    #         'spot': Spot(data_prov='bitmex', symbol='.ETHXBT', col='close').get,
    #     },
    #     # {
    #     #     'name': 'etc',
    #     #    'contract_data': ['bitmex'],
    #     #     'fullname': 'Etherium Classic',
    #     #     'bitmex_symbol': 'ETC7D',
    #     #     'denomination': 'BTC',
    #     #     'broker': 'bitmex',
    #     #     'contract_name_format': 'bitmex',
    #     #     'point_value': 1,
    #     #     'spread': 1.0e-4,
    #     #     # 'rules': ('ewmac', 'carry_spot'),
    #     #     'rules': ('ewmac',),
    #     # },
    #     {
    #         'name': 'litecoin',
    #         'contract_data': ['bitmex'],
    #         'bitmex_symbol': 'LTC',
    #         'first_contract': 201706,
    #         'months_traded': [6, 9],
    #         'trade_only': [6, 9],
    #         'roll_day': 29,
    #         'denomination': 'BTC',
    #         'broker': 'bitmex',
    #         'contract_name_format': 'bitmex',
    #         'point_value': 1,
    #         'spread': 2.3e-5,
    #         'rules': ('ewmac', 'carry_spot'),
    #         'spot': Spot(data_prov='bitmex', symbol='.LTCXBT', col='close').get,
    #     },
    #     {
    #         'name': 'monero',
    #         'contract_data': ['bitmex'],
    #         'bitmex_symbol': 'XMR',
    #         'first_contract': 201704,
    #         'months_traded': [4, 6, 9],
    #         'trade_only': [4, 6, 9],
    #         'roll_day': 29,
    #         'denomination': 'BTC',
    #         'broker': 'bitmex',
    #         'contract_name_format': 'bitmex',
    #         'point_value': 1,
    #         'spread': 2.7e-5,
    #         'rules': ('ewmac', 'carry_spot'),
    #         'spot': Spot(data_prov='bitmex', symbol='.XMRXBT', col='close').get,
    #     },
    #     {
    #         'name': 'stellar',
    #         'contract_data': ['bitmex'],
    #         'bitmex_symbol': 'STR',
    #         'first_contract': 201706,
    #         'months_traded': [6, 9],
    #         'trade_only': [6, 9],
    #         'roll_day': 29,
    #         'denomination': 'BTC',
    #         'broker': 'bitmex',
    #         'contract_name_format': 'bitmex',
    #         'point_value': 1,
    #         'spread': 2.3e-8,
    #         'rules': ('ewmac', 'carry_spot'),
    #         'spot': Spot(data_prov='bitmex', symbol='.STRXBT', col='close').get,
    #     },
    #     {
    #         'name': 'ripple',
    #         'contract_data': ['bitmex'],
    #         'bitmex_symbol': 'XRP',
    #         'first_contract': 201706,
    #         'months_traded': [6, 9],
    #         'trade_only': [6, 9],
    #         'roll_day': 29,
    #         'denomination': 'BTC',
    #         'broker': 'bitmex',
    #         'contract_name_format': 'bitmex',
    #         'point_value': 1,
    #         'spread': 4.5e-7,
    #         'rules': ('ewmac', 'carry_spot'),
    #         'spot': Spot(data_prov='bitmex', symbol='.XRPXBT', col='close').get,
    #     },
    #     {
    #         'name': 'tezos',
    #         'contract_data': ['bitmex'],
    #         'bitmex_symbol': 'XTZ',
    #         'first_contract': 201712,
    #         'months_traded': [12],
    #         'trade_only': [12],
    #         'roll_day': 29,
    #         'denomination': 'BTC',
    #         'broker': 'bitmex',
    #         'contract_name_format': 'bitmex',
    #         'point_value': 1,
    #         'spread': 0.01,
    #         # 'rules': ('ewmac', 'carry_spot'),
    #         # 'spot': Spot(data_prov='bitmex', symbol='.XTZXBT', col='close').get,
    #         'rules': ('ewmac',),
    #     },
    #     {
    #         'name': 'zcash',
    #         'contract_data': ['bitmex'],
    #         'bitmex_symbol': 'ZEC',
    #         'first_contract': 201612,
    #         'months_traded': [3, 6, 9, 12],
    #         'trade_only': [3, 6, 9, 12],
    #         'roll_day': 29,
    #         'denomination': 'BTC',
    #         'broker': 'bitmex',
    #         'contract_name_format': 'bitmex',
    #         'point_value': 1,
    #         'spread': 0.007,
    #         'rules': ('ewmac', 'carry_spot'),
    #         'spot': Spot(data_prov='bitmex', symbol='.ZECXBT', col='close').get,
    #     },
    # ],
}

# Backward compatibility workaround (flattens instruments_all into a single 1D-list)
instrument_definitions = [entry for group in instruments_all.values() for entry in group]


### Financials

 # {
    #     'name': 'us5',
    #     'quandl_database': 'CME',
    #     'quandl_symbol': 'FV',
    #     'first_contract': 198812,
    #     'roll_day': -20,
    #     'months_traded': [3, 6, 9, 12],
    #     'trade_only': [3, 6, 9, 12],
    #     'spread': 0.0078125, #TO BE CONFIRMED
    #     'commission': 1.51,
    #     'ib_code': 'ZF',
    #     'exchange': 'ECBOT',
    #     'point_value': 1000,
    #     'denomination': 'USD',
    #}
   # {
   #      'name': 'zec',
   #      'quandl_symbol': 'ZEC',
   #      'first_contract': 201703,
   #      'months_traded': [3, 6, 9, 12],
   #      'trade_only': [3, 6, 9, 12],
   #      'roll_day': 27,
   #      'denomination': 'XBT',
   #      'broker': 'bitmex',
   #      'contract_name_format': 'bitmex',
   #      'point_value': 1,
   #      'spread': 0.01,
   #      'rules': ('ewmac',),
   #      # 'spot': core.currency.Currency('XBTUSD').rate,
   #  }, {
   #      'name': 'etc',
   #      'quandl_symbol': 'ETC7D',
   #      # 'first_contract': 201703,
   #      # 'months_traded': [3, 6, 9, 12],
   #      # 'trade_only': [3, 6, 9, 12],
   #      # 'roll_day': 27,
   #      'denomination': 'XBT',
   #      'broker': 'bitmex',
   #      'contract_name_format': 'bitmex',
   #      'point_value': 1,
   #      'spread': 0.01,
   #      'rules': ('ewmac',),
   #  },  {
    #     'name': 'us10',
    #     'quandl_symbol': 'TY',
    #     'quandl_database': 'CME',
    #     'first_contract': 198206,
    #     'months_traded': [3, 6, 9, 12],
    #     'trade_only': [3, 6, 9, 12],
    #     'denomination': 'USD',
    #     'ib_code':'ZN',
    #     'roll_day':-24,
    #     'exchange': 'ECBOT',
    #     'point_value':1000,
    #     'spread':1/64,
    # },{
        # 'name': 'n225',
        # 'fullname': 'Nikkei 225 Index Futures',
        # 'quandl_database': 'OSE',
        # 'quandl_symbol': 'NK225',
        # 'quandl_rename_columns': {'Sett Price': 'Settle'},
        # 'first_contract': 201612,
        # 'months_traded': QUARTERLY,
        # 'trade_only': QUARTERLY,
        # 'denomination': 'JPY',
        # 'ib_code': 'N225',
        # 'point_value': 1000,
        # 'exchange': 'OSE.JPN',
        # 'roll_day': -15,
        # 'spread': 10,

    # }, {
    #     'name': 'dow',
    #     'fullname': 'Dow Jones Industrial Industrial Mini',
    #     'quandl_database': 'CME',
    #     'quandl_symbol': 'DJ',
    #     'first_contract': 201203,
    #     'months_traded': QUARTERLY,
    #     'trade_only': QUARTERLY,
    #     'denomination': 'USD',
    #     'ib_code': 'YM',
    #     'point_value': 5,
    #     'exchange': 'ECBOT',
    #     'roll_day': 1,
    #     'spread': 1,

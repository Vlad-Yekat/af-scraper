from datetime import date
from flask import Flask, jsonify
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    return "Index Page"


@app.route('/<path:dummy>')
def fallback(dummy):
    answer = {
        "termsOfUse": "https://www.pandora_air.com/ie/en/corporate/terms-of-use=AGREED",
        "currency": "SEK",
        "currPrecision": 2,
        "trips": [
            {"origin": "VST", "originName": "Stockholm Västerås", "destination": "ALC", "destinationName": "Alicante",
             "dates": [
                 {"dateOut": "1987-10-15T00:00:00.000", "flights": []},
                 {"dateOut": "1987-10-16T00:00:00.000", "flights": []},
                 {"dateOut": "1987-10-17T00:00:00.000", "flights": []},
                 {"dateOut": "1987-10-18T00:00:00.000", "flights": [
                     {"faresLeft": -1, "flightKey": "FR~7426~ ~~VST~10/18/2019 18:25~ALC~10/18/2019 22:20~~",
                      "infantsLeft": 17,
                      "regularFare": {"fareKey": "JKX7ZWJASBGBR5RQRGWY63SL37O", "fareClass": "C",
                                      "fares": [
                                          {"type": "ADT", "amount": 873.0000, "count": 1, "hasDiscount": False,
                                           "publishedFare": 873.0000,
                                           "mandatorySeatFee": {"vat": 0.0, "amt": 44.0000, "total": 44.0000,
                                                                "totalDiscount": 0.0, "totalWithoutDiscount": 44.0000,
                                                                "code": "SETA", "qty": 1},
                                           "discountInPercent": 0, "hasPromoDiscount": False, "discountAmount": 0.0},
                                          {"type": "CHD", "amount": 873.0000, "count": 1, "hasDiscount": False,
                                           "publishedFare": 873.0000,
                                           "discountInPercent": 0, "hasPromoDiscount": False, "discountAmount": 0.0}
                                      ]},
                      "operatedBy": "", "segments": [
                         {"segmentNr": 0, "origin": "VST", "destination": "ALC", "flightNumber": "FR 7426",
                          "time": ["1987-10-18T18:25:00.000", "1987-10-18T22:20:00.000"],
                          "timeUTC": ["1987-10-18T16:25:00.000Z", "1987-10-18T20:20:00.000Z"],
                          "duration": "03:55"}
                     ],
                      "flightNumber": "FR 7426", "time": ["1987-10-18T18:25:00.000", "1987-10-18T22:20:00.000"],
                      "timeUTC": ["1987-10-18T16:25:00.000Z", "1987-10-18T20:20:00.000Z"], "duration": "03:55"}]
                  },
                 {"dateOut": "1987-10-19T00:00:00.000", "flights": []},
                 {"dateOut": "1987-10-20T00:00:00.000", "flights": []},
                 {"dateOut": "1987-10-21T00:00:00.000", "flights": [
                     {"faresLeft": -1, "flightKey": "FR~7426~ ~~VST~10/21/2019 18:25~ALC~10/21/2019 22:20~~",
                      "infantsLeft": 17,
                      "regularFare": {
                          "fareKey": "JNPYUNBTAD6HMYJRUG2OV6Z22QPBADOO3F2JM4EZOYEDXSASF662CY7URT66CNTVU3JQCQLKOR3RUMY",
                          "fareClass": "A",
                          "fares": [
                              {"type": "ADT", "amount": 696.0000, "count": 1, "hasDiscount": False,
                               "publishedFare": 696.0000,
                               "mandatorySeatFee": {"vat": 0.0, "amt": 44.0000, "total": 44.0000, "totalDiscount": 0.0,
                                                    "totalWithoutDiscount": 44.0000, "code": "SETA", "qty": 1},
                               "discountInPercent": 0, "hasPromoDiscount": False, "discountAmount": 0.0},
                              {"type": "CHD", "amount": 696.0000, "count": 1, "hasDiscount": False,
                               "publishedFare": 696.0000, "discountInPercent": 0,
                               "hasPromoDiscount": False, "discountAmount": 0.0}]}, "operatedBy": "",
                      "segments": [{"segmentNr": 0, "origin": "VST", "destination": "ALC", "flightNumber": "FR 7426",
                                    "time": ["1987-10-21T18:25:00.000", "1987-10-21T22:20:00.000"],
                                    "timeUTC": ["1987-10-21T16:25:00.000Z", "1987-10-21T20:20:00.000Z"],
                                    "duration": "03:55"}], "flightNumber": "FR 7426",
                      "time": ["1987-10-21T18:25:00.000", "1987-10-21T22:20:00.000"],
                      "timeUTC": ["1987-10-21T16:25:00.000Z", "1987-10-21T20:20:00.000Z"], "duration": "03:55"}]}
             ]
             },
            {"origin": "ALC", "originName": "Stockholm Västerås", "destination": "VST", "destinationName": "Alicante",
             "dates": [
                 {"dateOut": "1987-10-15T00:00:00.000", "flights": []},
                 {"dateOut": "1987-10-16T00:00:00.000", "flights": []},
                 {"dateOut": "1987-10-17T00:00:00.000", "flights": []},
                 {"dateOut": "1987-10-18T00:00:00.000",
                  "flights": [
                      {"faresLeft": 5, "flightKey": "FR~7427~ ~~ALC~10/18/2019 14:00~VST~10/18/2019 18:00~~",
                       "infantsLeft": 17, "regularFare": {"fareKey": "EHT4BRIBRCTXPAQJHWWTCEIBCI2",
                                                          "fareClass": "K", "fares": [
                              {"type": "ADT", "amount": 1203.0000, "count": 1, "hasDiscount": False,
                               "publishedFare": 1203.0000,
                               "mandatorySeatFee": {"vat": 0.0, "amt": 44.0000, "total": 44.0000, "totalDiscount": 0.0,
                                                    "totalWithoutDiscount": 44.0000,
                                                    "code": "SETA", "qty": 1}, "discountInPercent": 0,
                               "hasPromoDiscount": False, "discountAmount": 0.0},
                              {"type": "CHD", "amount": 1203.0000, "count": 1, "hasDiscount": False,
                               "publishedFare": 1203.0000, "discountInPercent": 0, "hasPromoDiscount": False,
                               "discountAmount": 0.0}]}, "operatedBy": "", "segments": [
                          {"segmentNr": 0, "origin": "ALC", "destination": "VST", "flightNumber": "FR 7427",
                           "time": ["1987-10-18T14:00:00.000", "1987-10-18T18:00:00.000"],
                           "timeUTC": ["1987-10-18T12:00:00.000Z", "1987-10-18T16:00:00.000Z"], "duration": "04:00"}],
                       "flightNumber": "FR 7427", "time": ["1987-10-18T14:00:00.000", "1987-10-18T18:00:00.000"],
                       "timeUTC": ["1987-10-18T12:00:00.000Z", "1987-10-18T16:00:00.000Z"], "duration": "04:00"}]},
                 {"dateOut": "1987-10-19T00:00:00.000", "flights": []},
                 {"dateOut": "1987-10-20T00:00:00.000", "flights": []},
                 {"dateOut": "1987-10-21T00:00:00.000", "flights": [
                     {"faresLeft": 5, "flightKey": "FR~7427~ ~~ALC~10/21/2019 14:00~VST~10/21/2019 18:00~~",
                      "infantsLeft": 17,
                      "regularFare": {"fareKey": "UKY7EYD23WKCX23UJ3SC", "fareClass": "L", "fares": [
                          {"type": "ADT", "amount": 1623.0000, "count": 1, "hasDiscount": False,
                           "publishedFare": 1623.0000,
                           "mandatorySeatFee": {"vat": 0.0, "amt": 44.0000, "total": 44.0000, "totalDiscount": 0.0,
                                                "totalWithoutDiscount": 44.0000, "code": "SETA", "qty": 1},
                           "discountInPercent": 0, "hasPromoDiscount": False,
                           "discountAmount": 0.0},
                          {"type": "CHD", "amount": 1623.0000, "count": 1, "hasDiscount": False,
                           "publishedFare": 1623.0000, "discountInPercent": 0, "hasPromoDiscount": False,
                           "discountAmount": 0.0}]},
                      "operatedBy": "", "segments": [
                         {"segmentNr": 0, "origin": "ALC", "destination": "VST", "flightNumber": "FR 7427",
                          "time": ["1987-10-21T14:00:00.000", "1987-10-21T18:00:00.000"],
                          "timeUTC": ["1987-10-21T12:00:00.000Z", "1987-10-21T16:00:00.000Z"], "duration": "04:00"}],
                      "flightNumber": "FR 7427", "time": ["1987-10-21T14:00:00.000", "1987-10-21T18:00:00.000"],
                      "timeUTC": ["1987-10-21T12:00:00.000Z", "1987-10-21T16:00:00.000Z"], "duration": "04:00"}]}
             ]
             }
        ],
        "serverTimeUTC": "1987-09-10T05:15:06.601Z"
    }
    return jsonify(answer)


@app.route("/timtbl/3/schedules/AAR/STN/years/2019/months/09")
def show_answer_as_pandora_air_schedule():

    answer = {
        "month": 9,
        "days": [
            {
                "day": 2,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "14:25",
                        "arrivalTime": "15:05",
                    }
                ],
            },
            {
                "day": 3,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "14:30",
                        "arrivalTime": "15:10",
                    }
                ],
            },
            {
                "day": 4,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "14:30",
                        "arrivalTime": "15:10",
                    }
                ],
            },
            {
                "day": 5,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "14:35",
                        "arrivalTime": "15:15",
                    }
                ],
            },
            {
                "day": 6,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "14:30",
                        "arrivalTime": "15:10",
                    }
                ],
            },
            {
                "day": 7,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "17:30",
                        "arrivalTime": "18:10",
                    }
                ],
            },
            {
                "day": 8,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "11:00",
                        "arrivalTime": "11:40",
                    }
                ],
            },
            {
                "day": 9,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "14:25",
                        "arrivalTime": "15:05",
                    }
                ],
            },
            {
                "day": 10,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "14:30",
                        "arrivalTime": "15:10",
                    }
                ],
            },
            {
                "day": 11,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "14:30",
                        "arrivalTime": "15:10",
                    }
                ],
            },
            {
                "day": 12,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "14:35",
                        "arrivalTime": "15:15",
                    }
                ],
            },
            {
                "day": 13,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "14:30",
                        "arrivalTime": "15:10",
                    }
                ],
            },
            {
                "day": 14,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "17:30",
                        "arrivalTime": "18:10",
                    }
                ],
            },
            {
                "day": 15,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "11:00",
                        "arrivalTime": "11:40",
                    }
                ],
            },
            {
                "day": 16,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "14:25",
                        "arrivalTime": "15:05",
                    }
                ],
            },
            {
                "day": 17,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "14:30",
                        "arrivalTime": "15:10",
                    }
                ],
            },
            {
                "day": 18,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "14:30",
                        "arrivalTime": "15:10",
                    }
                ],
            },
            {
                "day": 19,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "14:35",
                        "arrivalTime": "15:15",
                    }
                ],
            },
            {
                "day": 20,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "14:30",
                        "arrivalTime": "15:10",
                    }
                ],
            },
            {
                "day": 21,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "17:30",
                        "arrivalTime": "18:10",
                    }
                ],
            },
            {
                "day": 22,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "11:00",
                        "arrivalTime": "11:40",
                    }
                ],
            },
            {
                "day": 23,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "14:25",
                        "arrivalTime": "15:05",
                    }
                ],
            },
            {
                "day": 24,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "14:30",
                        "arrivalTime": "15:10",
                    }
                ],
            },
            {
                "day": 25,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "14:30",
                        "arrivalTime": "15:10",
                    }
                ],
            },
            {
                "day": 26,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "14:35",
                        "arrivalTime": "15:15",
                    }
                ],
            },
            {
                "day": 27,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "14:30",
                        "arrivalTime": "15:10",
                    }
                ],
            },
            {
                "day": 28,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "17:30",
                        "arrivalTime": "18:10",
                    }
                ],
            },
            {
                "day": 29,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "11:00",
                        "arrivalTime": "11:40",
                    }
                ],
            },
            {
                "day": 30,
                "flights": [
                    {
                        "carrierCode": "FR",
                        "number": "713",
                        "departureTime": "14:25",
                        "arrivalTime": "15:05",
                    }
                ],
            },
        ],
    }
    return jsonify(answer)


@app.route("/v4/en-gb/availability")
def show_answer_as_pandora_air():
    ADT = request.args.get("ADT", None)
    CHD = request.args.get("CHD", None)
    DateOut = request.args.get("DateOut", None)
    Destination = request.args.get("Destination", None)
    FlexDaysOut = request.args.get("FlexDaysOut", None)
    INF = request.args.get("INF", None)
    IncludeConnectingFlights = request.args.get("IncludeConnectingFlights", None)
    Origin = request.args.get("Origin", None)
    RoundTrip = request.args.get("RoundTrip", None)
    TEEN = request.args.get("TEEN", None)
    ToUs = request.args.get("ToUs", None)
    exists = request.args.get("exists", None)
    promoCode = request.args.get("promoCode", None)

    answer = {
        "termsOfUse": "https://www.pandora_air.com/ie/en/corporate/terms-of-use=AGREED",
        "currency": "GBP",
        "currPrecision": 2,
        "trips": [
            {
                "origin": Origin,
                "originName": "London (Stansted)",
                "destination": Destination,
                "destinationName": "Tenerife (South)",
                "dates": [
                    {
                        "dateOut": DateOut,
                        "flights": [
                            {
                                "faresLeft": -1,
                                "flightKey": "FR~8166~ ~~STN~10/31/2019 06:15~TFS~10/31/2019 10:45~~",
                                "infantsLeft": 12,
                                "regularFare": {
                                    "fareKey": "5KUS",
                                    "fareClass": "A",
                                    "fares": [
                                        {
                                            "type": "ADT",
                                            "amount": 53.9900,
                                            "count": 1,
                                            "hasDiscount": False,
                                            "publishedFare": 53.9900,
                                            "mandatorySeatFee": {
                                                "vat": 0.0,
                                                "amt": 5.8800,
                                                "total": 5.8800,
                                                "totalDiscount": 0.0,
                                                "totalWithoutDiscount": 5.8800,
                                                "code": "SETA",
                                                "qty": 1,
                                            },
                                            "discountInPercent": 0,
                                            "hasPromoDiscount": False,
                                            "discountAmount": 0.0,
                                        },
                                        {
                                            "type": "CHD",
                                            "amount": 53.9900,
                                            "count": 1,
                                            "hasDiscount": False,
                                            "publishedFare": 53.9900,
                                            "discountInPercent": 0,
                                            "hasPromoDiscount": False,
                                            "discountAmount": 0.0,
                                        },
                                    ],
                                },
                                "operatedBy": "",
                                "segments": [
                                    {
                                        "segmentNr": 0,
                                        "origin": "STN",
                                        "destination": "TFS",
                                        "flightNumber": "FR 8166",
                                        "time": [
                                            "1987-10-31T06:15:00.000",
                                            "1987-10-31T10:45:00.000",
                                        ],
                                        "timeUTC": [
                                            "1987-10-31T06:15:00.000Z",
                                            "1987-10-31T10:45:00.000Z",
                                        ],
                                        "duration": "04:30",
                                    }
                                ],
                                "flightNumber": "FR 8166",
                                "time": [
                                    "1987-10-31T06:15:00.000",
                                    "1987-10-31T10:45:00.000",
                                ],
                                "timeUTC": [
                                    "1987-10-31T06:15:00.000Z",
                                    "1987-10-31T10:45:00.000Z",
                                ],
                                "duration": "04:30",
                            }
                        ],
                    }
                ],
            }
        ],
        "serverTimeUTC": date.today(),
    }

    return jsonify(answer)


with app.test_request_context():
    pass
    # print(url_for('show_post', post_id=1))
    # print(url_for('static', filename='style.css'))

app.run()

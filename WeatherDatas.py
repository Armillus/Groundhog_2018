#!/usr/bin/env python3

class WeatherDatas:
    def __init__(self, period):
        self.period = period
        self.values = []
        self.aberrations = []
        self.last_temp_perc = 0
        self.switches = 0

# 稍微改造一点点

# 案例: 一个气象站检测各个气象数值, 一个类获取这些数据, 通知给各个需求方, 如当前气象情况台, 气象历史统计台, 天气预报台

class WeatherData(object):
    def __init__(self):
        self.observer_list = []
        self.changed = False
        self.temperature = None
        self.humidity = None
        self.pressure = None

    def register_observer(self, observer):
        self.observer_list.append(observer)

    def remove_observer(self, observer):
        index = self.observer_list.index(observer)
        del(self.observer_list[index])

    def notify_observer(self, **kargs):
        for observer in self.observer_list:
            observer.update(**kargs)

    # 这个是书里提到的东西, 书里说的用处如下
    # 如果温度感应很灵敏, 0.001度变化都能感应到, 那么观察者会频繁收到推送
    # 如果想设置每0.1度变化才推送
    # 通过changed这个flag就可以很轻松做到了
    # 想推送的时候set_changed(), 相当于打开阀门, 不会影响到其他逻辑
    def set_changed(self):
        self.changed = True

    def data_changed(self):
        if self.changed:
            # 观察者获取数据有推拉两种方式
            # 如下是我传空, 他们拉数据的方式
            self.notify_observer()
            # 如下是我主动推送数据的方式
            # self.notify_observer(temperature=self.temperature, humidity=self.humidity, pressure=self.pressure)
            self.changed = False

    def set_data(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.set_changed()
        self.data_changed()

    # getter用于观察者拉数据
    def get_template(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity

    def get_pressure(self):
        return self.pressure

class CurrentWeather(object):
    def __init__(self, weather_data):
        # 由于观察者要拉数据, 所以要保存一份weather_data
        self.weather_data = weather_data
        # 既然有weather_data, 那么注册顺便也在内部做了吧
        self.weather_data.register_observer(self)
        self.temperature = None
        self.humidity = None
        self.pressure = None

    def update(self, **kargs):
        if kargs:
            print('推数据')
            self.temperature = kargs['temperature']
            self.humidity = kargs['humidity']
            self.pressure = kargs['pressure']
        else:
            print('拉数据')
            self.temperature = self.weather_data.get_template()
            self.humidity = self.weather_data.get_humidity()
            self.pressure = self.weather_data.get_pressure()
        self.display()

    def display(self):
        print('当前气象台数据如下:')
        print("温度: %s" % self.temperature)
        print("湿度: %s" % self.humidity)
        print("气压: %s" % self.pressure)

class ForecastWeather(object):
    def __init__(self, weather_data):
        self.weather_data = weather_data
        self.weather_data.register_observer(self)
        self.temperature = None
        self.humidity = None
        self.pressure = None
    
    def update(self, **kargs):
        if kargs:
            print('推数据')
            self.temperature = kargs['temperature']
            self.humidity = kargs['humidity']
            self.pressure = kargs['pressure']
        else:
            print('拉数据')
            self.temperature = self.weather_data.get_template()
            self.humidity = self.weather_data.get_humidity()
            self.pressure = self.weather_data.get_pressure()
        self.display()

    def display(self):
        print('天气预报台数据如下:')
        print("明日温度: %s" % (self.temperature + 1))
        print("明日湿度: %s" % (self.humidity + 0.1))
        print("明日气压: %s" % (self.pressure + 10))

weather_data = WeatherData()

current_weather = CurrentWeather(weather_data)
forecast_weather = ForecastWeather(weather_data)

weather_data.set_data(30, 0.5, 60)
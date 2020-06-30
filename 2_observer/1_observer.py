# 案例: 一个气象站检测各个气象数值, 一个类获取这些数据, 通知给各个需求方, 如当前气象情况台, 气象历史统计台, 天气预报台

class WeatherData(object):
    def __init__(self):
        # 观察者列表
        self.observer_list = []
        self.temperature = None
        self.humidity = None
        self.pressure = None

    # 注册观察者
    def register_observer(self, observer):
        self.observer_list.append(observer)

    # 解绑观察者
    def remove_observer(self, observer):
        index = self.observer_list.index(observer)
        del(self.observer_list[index])

    # 通知观察者
    def notify_observer(self):
        for observer in self.observer_list:
            observer.update(self.temperature, self.humidity, self.pressure)

    # 数据改变时的处理
    def data_changed(self):
        self.notify_observer()

    # 设置新数据
    def set_data(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.data_changed()

class CurrentWeather(object):
    def __init__(self):
        self.temperature = None
        self.humidity = None
        self.pressure = None
    
    # 观察者统一一个接口, 数据变更时, 被观察者统一调用这个接口来通知观察者
    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        # display()放在这里不是最好的
        # 想想MVC, MVVM, 数据和表现是要分开的
        self.display()

    def display(self):
        print('当前气象台数据如下:')
        print("温度: %s" % self.temperature)
        print("湿度: %s" % self.humidity)
        print("气压: %s" % self.pressure)

class ForecastWeather(object):
    def __init__(self):
        self.temperature = None
        self.humidity = None
        self.pressure = None
    
    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        print('天气预报台数据如下:')
        print("明日温度: %s" % (self.temperature + 1))
        print("明日湿度: %s" % (self.humidity + 0.1))
        print("明日气压: %s" % (self.pressure + 10))

current_weather = CurrentWeather()
forecast_weather = ForecastWeather()

weather_data = WeatherData()
weather_data.register_observer(current_weather)
weather_data.register_observer(forecast_weather)
weather_data.set_data(30, 0.5, 60)
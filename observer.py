from abc import ABC, abstractmethod


class AbstractObserver(ABC):

    @abstractmethod
    def update(self, temp: float, humidity: float, pressure: float):
        pass


class AbstractWeatherData(ABC):

    @abstractmethod
    def register_observer(self, observer: AbstractObserver):
        pass

    @abstractmethod
    def remove_observer(self, observer: AbstractObserver):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class AbstractDisplayElement(ABC):

    @abstractmethod
    def display(self):
        pass


class WeatherData(AbstractWeatherData):

    def __init__(self):
        self.temperature = None
        self.humidity = None
        self.pressure = None
        self._observers = list()

    def register_observer(self, observer: AbstractObserver):
        self._observers.append(observer)

    def remove_observer(self, observer: AbstractObserver):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notify_observers()

    def set_measurements(self, temp: float, humidity: float, pressure: float):
        self.temperature = temp
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()


class CurrentConditionsDisplay(AbstractObserver, AbstractDisplayElement):

    def __init__(self, data_source: AbstractWeatherData | None = None):
        if data_source is None:
            data_source = WeatherData()
        self.weather_data = data_source
        self.weather_data.register_observer(self)
        self.temperature = None
        self.humidity = None
        self.pressure = None

    def update(self, temp: float, humidity: float, pressure: float):
        self.temperature = temp
        self.humidity = humidity
        self.pressure = pressure
        self.display()

    def display(self):
        output = (f'Current conditions: \n'
                  f'Temperature: {self.temperature} F\n'
                  f'Humidity: {self.humidity} %\n'
                  f'Pressure: {self.pressure}')
        print(output)


if __name__ == '__main__':
    data_src = WeatherData()
    disp_element = CurrentConditionsDisplay(data_src)
    data_src.set_measurements(80, 65, 30.4)

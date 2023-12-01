from abc import ABC, abstractmethod


class AbstractObserver(ABC):
    """Observer interface."""

    @abstractmethod
    def update(self):
        pass


class AbstractWeatherData(ABC):
    """Subject interface."""

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
            observer.update()

    def get_temperature(self):
        return self.temperature

    def get_humidity(self):
        return self.humidity

    def get_pressure(self):
        return self.pressure

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

    def update(self):
        self.temperature = self.weather_data.get_temperature()
        self.humidity = self.weather_data.get_humidity()
        self.display()

    def display(self):
        output = (f'Current conditions: {self.temperature} F degrees and '
                  f'{self.humidity}% humidity')
        print(output)


class HeatIndexDisplay(AbstractObserver, AbstractDisplayElement):

    def __init__(self, data_source: AbstractWeatherData | None = None):
        if data_source is None:
            data_source = WeatherData()
        self.weather_data = data_source
        self.weather_data.register_observer(self)
        self.t = None
        self.rh = None
        self.heat_index = None

    def update(self):
        self.t = self.weather_data.get_temperature()
        self.rh = self.weather_data.get_humidity()

        self.heat_index = ((16.923 + (0.185212 * self.t) + (5.37941 * self.rh)
                            - (0.100254 * self.t * self.rh) +
                            (0.00941695 * (self.t * self.t)) +
                            (0.00728898 * (self.rh * self.rh)) +
                            (0.000345372 * (self.t * self.t * self.rh)) -
                            (0.000814971 * (self.t * self.rh * self.rh)) +
                            (0.0000102102 * (self.t * self.t * self.rh *
                                             self.rh)) -
                            (0.000038646 * (self.t * self.t * self.t)) +
                            (0.0000291583 * (self.rh * self.rh * self.rh)) +
                            (0.00000142721 * (self.t * self.t * self.t *
                                              self.rh)) +
                            (0.000000197483 * (self.t * self.rh * self.rh *
                                               self.rh)) -
                            (0.0000000218429 * (self.t * self.t * self.t *
                                                self.rh * self.rh)) +
                            0.000000000843296 * (self.t * self.t * self.rh *
                                                 self.rh * self.rh)) -
                           (0.0000000000481975 * (self.t * self.t * self.t *
                                                  self.rh * self.rh *
                                                  self.rh)))

        self.display()

    def display(self):
        print(f'Heat index is {round(self.heat_index, 5)}')


if __name__ == '__main__':
    data_src = WeatherData()
    cur_cond = CurrentConditionsDisplay(data_src)
    heat_ind = HeatIndexDisplay(data_src)
    data_src.set_measurements(80, 65, 32.7)



class Parameters(object):

    def __init__(self):
        _unit_name = None
        _mac_address = None
        _ip_address = None
        _login = None
        _password = None

    @property
    def unit_name(self):
        return self._unit_name

    @unit_name.setter
    def unit_name(self, value):
        self._unit_name = value

    @unit_name.deleter
    def unit_name(self):
        del self._unit_name

    @property
    def mac_address(self):
        return self._mac_address

    @mac_address.setter
    def mac_address(self, value):
        self._mac_address = value

    @mac_address.deleter
    def mac_address(self):
        del self._mac_address

    @property
    def ip_address(self):
        return self._ip_address

    @ip_address.setter
    def ip_address(self, value):
        self._ip_address = value

    @ip_address.deleter
    def ip_address(self):
        del self._ip_address


    @property
    def login(self):
        return self._login

    @login.setter
    def login(self, value):
        self._login = value

    @login.deleter
    def login(self):
        del self._login


    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = value

    @password.deleter
    def password(self):
        del self._password


if __name__ == '__main__':
    p = Parameters()
    p.unit_name = 100
    print('c: ', p.unit_name)
    del p.unit_name
    try:
        print('after del c: ', p.unit_name)
    except AttributeError as ae:
        print("An error occured: ", ae)

